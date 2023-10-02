import pyautogui
from aiohttp import web
import asyncio

async def f9_press_func():
    await asyncio.sleep(3)
    while True:
        await asyncio.sleep(0.4)
        print("Press f9...")
        # pyautogui.press('f9')

async def hello(request):
    exit(1)

def main():
    app = web.Application()
    app.add_routes([web.get('/', hello)])
    return app


async def main_async():
    app = main()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 6752)
    await site.start()
    await f9_press_func()

asyncio.run(main_async())

