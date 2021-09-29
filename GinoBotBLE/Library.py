import GinobotBLE as gb
from GinobotBLE import *
import asyncio
import keyboard
from time import sleep


async def run():

    await gb.scan()
    await gb.Front_Lights(color.RED)
    #await gb.Front_Lights(color.red, 0 ,0)


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
