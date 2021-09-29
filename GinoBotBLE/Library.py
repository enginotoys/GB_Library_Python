import GinobotBLE as gb  # Imports Ginobot Library
import asyncio  # Imports asyncio Library for asynchronous calls


async def run():  # Run Function ( Runs what ever program is placed inside)
    # scan function. Important to locate your device and connect to it.
    # With out the scan function you will not be able to controll Ginobot
    await gb.scan()
    await gb.Front_Lights(c)


loop = asyncio.get_event_loop()  # Asynchronous event loop,waits for an await call to happen and executes it
loop.run_until_complete(run()) # This command will run until a function has given an exit state
