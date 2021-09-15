import GinobotBLE as gb
from GinobotBLE import *
import asyncio
import keyboard
from time import sleep


async def run():
    await gb.scan()
    # while True:
    #     await gb.move_forward(Speed.Fast)
    #await gb.move_backwards()
    await gb.Back_Lights()


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
