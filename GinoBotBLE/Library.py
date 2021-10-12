import asyncio  # Imports asyncio Library for asynchronous calls
from GinoBotBLE.GinobotBLE import * # Imports all functionalities of ginobot
import GinoBotBLE.GinobotBLE as gb  # Imports Ginobot Library functions


async def run():  # Run Function ( Runs what ever program is placed inside)
    await gb.scan()  # scan function. Important to locate your device and connect to it.



loop = asyncio.get_event_loop() # Asynchronous event loop,waits for an await call to happen and executes it
loop.run_until_complete(run())   # This command will run until a function has given an exit state

