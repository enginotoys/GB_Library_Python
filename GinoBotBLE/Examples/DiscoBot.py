import asyncio  # Imports asyncio Library for asynchronous calls
from GinoBotBLE.GinobotBLE import *  # Imports all functionalities of ginobot
import GinoBotBLE.GinobotBLE as gb  # Imports Ginobot Library functions
import time  # Make sure time is installed


async def run():  # Run Function ( Runs what ever program is placed inside)
    await gb.scan()  # scan function. Important to locate your device and connect to it.

    while True:
        await gb.Front_Lights(color.RED)
        await gb.Back_Lights(color.PURPLE)
        time.sleep(0.1)
        await gb.Front_Lights(color.PINK)
        await gb.Front_Lights(color.ORANGE)
        time.sleep(0.1)
        await gb.Front_Lights(color.YELLOW)
        await gb.Front_Lights(color.BLUE)
        time.sleep(0.1)
        await gb.Front_Lights(color.GREEN)
        await gb.Front_Lights(color.PINK)
        time.sleep(0.1)
        await gb.Front_Lights(color.RED)
        await gb.Front_Lights(color.PURPLE)
        time.sleep(0.1)
        await gb.Front_Lights(color.ORANGE)
        await gb.Front_Lights(color.BLUE)

loop = asyncio.get_event_loop()  # Asynchronous event loop,waits for an await call to happen and executes it
loop.run_until_complete(run())  # This command will run until a function has given an exit state
