import asyncio
from loguru import logger
from mitmproxy import options
from mitmproxy.tools import dump
from .cather import Cather


async def start_proxy(host: str, port: str):
    opts = options.Options(listen_host=host, listen_port=port)

    master = dump.DumpMaster(
        opts,
        with_termlog=False,
        with_dumper=False,
    )
    master.addons.add(Cather())

    logger.debug("Starting mitmproxy...")
    await master.run()
    return master


if __name__ == '__main__':
    asyncio.run(start_proxy())
