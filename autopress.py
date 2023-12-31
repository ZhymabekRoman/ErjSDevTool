import pyautogui
from aiohttp import web
import asyncio

pyautogui.FAILSAFE = False

async def f9_press_func():
    await asyncio.sleep(3)
    while True:
        await asyncio.sleep(0.4)
        print("Press f9...")
        pyautogui.press('f9')


async def f9_task_function():
    await asyncio.create_task(f9_press_func())


async def hello(request):
    exit(1)


def main():
    app = web.Application()
    app.add_routes([web.get('/', hello)])
    web.run_app(app, port=6752)

asyncio.run(f9_task_function())
main()