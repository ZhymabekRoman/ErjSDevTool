import asyncio
from .mitmproxy.script import start_proxy
from loguru import logger
from pycdp import cdp
from pycdp.browser import ChromeLauncher
from pycdp.asyncio import connect_cdp


async def main():
    a = await start_proxy("localhost", 7030)
    # asyncio.create_task(a)


async def main_old():
    logger.debug("Executing browser...")
    chrome = ChromeLauncher(
        binary='/usr/bin/chromium',
        args=['--remote-debugging-port=9222', '--remote-allow-origins="*"', '--incognito', '--proxy-server=localhost:7030']
    )
    await asyncio.get_running_loop().run_in_executor(None, chrome.launch)

    logger.debug("Connecting to Chrome devtool protocol...")
    conn = await connect_cdp('http://localhost:9222')

    logger.debug("Creating target...")
    target_id = await conn.execute(cdp.target.create_target('about:blank'))
    logger.debug(f"Target created! Target id: {target_id}")
    target_session = await conn.connect_session(target_id)
    logger.debug("Enable CDP for target page!")
    await target_session.execute(cdp.page.enable())

    # you may use "async for target_session.listen()" to listen multiple events, here we listen just a single event.
    with target_session.safe_wait_for(cdp.page.DomContentEventFired) as navigation:
        logger.debug("Navigating to translate.google.com")
        await target_session.execute(cdp.page.navigate("https://translate.google.com"))
        await navigation

    logger.debug("Navigating is done, sleep 10 seconds")
    await asyncio.sleep(10)

    input("Press Enter to continue...")

    """
    while True:

        step_into_result = await target_session.execute(cdp.debugger.step_into())
        logger.debug(step_into_result)

        scopes = await target_session.execute(cdp.runtime.sc)

        # await target_session.execute(cdp.runtime.get_properties())
    """

    """
    logger.debug("Enable debugger for target page!")
    await target_session.execute(cdp.debugger.enable())
    logger.debug("Set breakpoint!")
    break_point_script_data = await target_session.execute(cdp.debugger.set_breakpoint_by_url(line_number=0, url=""))
    """

    """
    dom = await target_session.execute(cdp.dom.get_document())
    node = await target_session.execute(cdp.dom.query_selector(dom.node_id, 'p'))
    js_node = await target_session.execute(cdp.dom.resolve_node(node))
    print((await target_session.execute(cdp.runtime.call_function_on('function() {return this.innerText;}', js_node.object_id, return_by_value=True)))[0].value)
    """

    # Closing page/target/browser
    await target_session.execute(cdp.page.close())
    await conn.close()
    await asyncio.get_running_loop().run_in_executor(None, chrome.kill)


asyncio.run(main())
