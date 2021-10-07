from GinobotBLE import * #Imports all functionalities of ginobot
import GinobotBLE as gb  # Imports Ginobot Library functions
import asyncio  # Imports asyncio Library for asynchronous calls


async def run():  # Run Function ( Runs what ever program is placed inside)
    # scan function. Important to locate your device and connect to it.
    # With out the scan function you will not be able to controll Ginobot
    await gb.scan()
    while True:
        if await gb.Left_Color_sense() == color.RED:
            print("reddddd boy")
        else:
            print("not reddddd boy")

        #await gb.Front_Left_IR(threshold.MEDIUM)
    #while True:
        #await gb.Front_Left_IR()


loop = asyncio.get_event_loop()  # Asynchronous event loop,waits for an await call to happen and executes it
loop.run_until_complete(run()) # This command will run until a function has given an exit state
