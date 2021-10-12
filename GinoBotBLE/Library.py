from GinobotBLE import *  # Imports all functionalities of ginobot
import GinobotBLE as gb  # Imports Ginobot Library functions
import asyncio  # Imports asyncio Library for asynchronous calls


async def run():  # Run Function ( Runs what ever program is placed inside)
    await gb.scan()  # scan function. Important to locate your device and connect to it.


loop = asyncio.get_event_loop()
loop.run_until_complete(run())  # Asynchronous event loop,waits for an await call to happen and executes it
# This command will run until a function has given an exit state
