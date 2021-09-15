import sys
import asyncio
import time
import keyboard
import ast
from enum import Enum
from time import sleep
from bleak import BleakClient
from bleak import discover


# from aioconsole import ainput

class speed(Enum):
    Fast = 100
    Medium = 80
    Slow = 60


class color(Enum):
    red = 255
    green = 255
    blue = 255


read_characteristic = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"
write_characteristic = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"

device_count = 0
Firmware = 0
Hardware = 0

connected = False
payload_write = 35
array_struct = []


def search():
    searching = "Searching"
    count = 0
    for x in range(9):
        sleep(0.3)
        count += 1
        searching = searching + "."
        sys.stdout.write('\r' + searching)
        sys.stdout.flush()
        if count == 3:
            count = 0
            searching = "Searching"


async def scan():
    # Error message
    # await client.write_gatt_char(write_characteristic, who_msg)
    # NameError: name
    # 'client' is not defined
    global devices
    global client
    search()
    devices = await discover()
    for i, device in enumerate(devices):

        if device.name == 'ESP32':
            print("Device found do you with to connect? [y/n]")
            if (input() == 'y'):
                client = BleakClient(device.address)
                await client.connect()
                device_address = client.address
                if (client.is_connected):
                    print("Connection was successful")
                    await who_func()
                    return True
                else:
                    return False


async def who_func():
    who_msg = b'?\n'
    global who_im_i
    global Firmware
    global Hardware
    if BleakClient.is_connected:
        await client.write_gatt_char(write_characteristic, who_msg)
        time.sleep(0.3)
        who_im_i = await client.read_gatt_char(read_characteristic)
    Firmware = who_im_i[3]
    Hardware = who_im_i[4]
    # Make sure this runs until is confirmed


async def empty_array():  # This function builds the start empty array for Ginobot
    # Bug! When a scan fails , the array build function still runs, which means the who func in the array build will fail
    # Make sure that the exception is in a while Loop that ensures connection and gets Firm , and Hardware version

    array_struct.append(hex(ord('W')))
    array_struct.append(hex(ord(':')))

    array_struct.append(hex(ord('0'))), array_struct.append(hex(ord('0'))), array_struct.append(hex(ord('8')))
    array_struct.append(hex(ord('0'))), array_struct.append(hex(ord('\n')))

    for i in range(7, 32):
        array_struct.append(hex(ord(' ')))

    array_struct.append(hex(ord('[')))
    array_struct.append(hex(ord('[')))
    array_struct.append(hex(ord('[')))

    array_struct.append(Firmware)  # pos 35
    array_struct.append(Hardware)  # pos 36

    array_struct.append(hex(int(payload_write & 0x00FF)))
    array_struct.append(hex(int(payload_write & 0xFF00) >> 8))

    array_struct.append(hex(ord('W')))
    array_struct.append(hex(0))  # pos 40

    for i in range(36):
        array_struct.append(hex(0))


async def payload_maker():
    checksum = 0

    for i in range(payload_write):
        checksum += int(array_struct[i + 40], 16)

    array_struct.append(hex(int(checksum) & 0x000000FF))
    array_struct.append(hex((int(checksum) & 0x0000FF00) >> 8))

    array_struct.append(hex(ord(']')))
    array_struct.append(hex(ord(']')))
    array_struct.append(hex(ord(']')))

    print(array_struct)
    for i in range(len(array_struct)):
        array_struct[i] = int(str(array_struct[i]), base=16)

    await client.write_gatt_char(write_characteristic, bytes(array_struct))
    print(array_struct)
    print('Here')
    array_struct.clear()


async def Front_Lights(red, green, blue):
    print("Front Lights input (Red , Green , Blue)")
    await empty_array()
    array_struct[49] = hex(red)
    array_struct[50] = hex(green)
    array_struct[51] = hex(blue)
    await payload_maker()


async def Back_Lights(*argument): # Look for multiple arguments in function
    print('Back Lights input (Red , Green , Blue)')
    col_arr = []
    await empty_array()
    col_arr.append(0)
    col_arr.append(0)
    col_arr.append(0)

    for count, i in enumerate(argument):
        col_arr[count] = i
        print(i)
    array_struct[46] = hex(col_arr[0])
    array_struct[47] = hex(col_arr[1])
    array_struct[48] = hex(col_arr[2])

    await payload_maker()


async def Front_Lights2(red, green, blue):
    print("Front Lights input (Red , Green , Blue)")
    await empty_array()
    print("Red=", end=" ")
    red = int(input())
    print("Green=", end=" ")
    green = int(input())
    print("Blue=", end=" ")
    blue = int(input())
    array_struct[49] = hex(red)
    array_struct[50] = hex(green)
    array_struct[51] = hex(blue)
    await payload_maker()


async def Back_Lights2():
    print('Back Lights input (Red , Green , Blue)')

    print("Red=", end=" ")
    red = int(input())
    print("Green=", end=" ")
    green = int(input())
    print("Blue=", end=" ")
    blue = int(input())
    await empty_array()  # This probably shouldnt be here
    # array_struct[36] = Firmware
    # array_struct[37] = Hardware
    array_struct[46] = hex(red)
    array_struct[47] = hex(green)
    array_struct[48] = hex(blue)
    await payload_maker()


async def Buzzer(freq):
    # 53 , 54
    print("Enter buzzer frequancy")
    await empty_array()
    array_struct[53] = (hex(int(freq) & 0x00FF))
    array_struct[54] = (hex((int(freq) & 0x0000FF00) >> 8))  # Wrong bit shifting seems to work
    print(array_struct[53])
    print((array_struct[54]))
    await payload_maker()


async def move_forward(speed):
    await empty_array()
    array_struct[57] = '0x44'
    array_struct[58] = (hex(0 & 0x00FF))
    array_struct[59] = (hex((0 & 0xFF00) >> 8))
    array_struct[60] = (hex(speed & 0xff00 >> 8))

    array_struct[61] = (hex(0 & 0x00FF))
    array_struct[62] = (hex((0 & 0xFF00) >> 8))
    array_struct[63] = (hex(speed & 0xff00 >> 8))
    await payload_maker()
    # 57 - 63


async def move_backwards(speed):
    await empty_array()
    array_struct[57] = '0x44'
    array_struct[58] = (hex(0 & 0x00FF))
    array_struct[59] = (hex((0 & 0xFF00) >> 8))
    array_struct[60] = (hex(-speed & 0xff00 >> 8))

    array_struct[61] = (hex(0 & 0x00FF))
    array_struct[62] = (hex((0 & 0xFF00) >> 8))
    array_struct[63] = (hex(-speed & 0xff00 >> 8))
    await payload_maker()


async def move_right(speed):
    await empty_array()
    array_struct[57] = '0x44'
    array_struct[58] = (hex(0 & 0x00FF))
    array_struct[59] = (hex((0 & 0xFF00) >> 8))
    array_struct[60] = (hex(speed & 0xff00 >> 8))

    array_struct[61] = (hex(0 & 0x00FF))
    array_struct[62] = (hex((0 & 0xFF00) >> 8))
    array_struct[63] = (hex(0 & 0xff00 >> 8))
    await payload_maker()


async def move_left(speed):
    await empty_array()
    array_struct[57] = '0x44'
    array_struct[58] = (hex(0 & 0x00FF))
    array_struct[59] = (hex((0 & 0xFF00) >> 8))
    array_struct[60] = (hex(0 & 0xff00 >> 8))

    array_struct[61] = (hex(0 & 0x00FF))
    array_struct[62] = (hex((0 & 0xFF00) >> 8))
    array_struct[63] = (hex(speed & 0xff00 >> 8))
    await payload_maker()


########################## TESTS #############################
async def Buzzer2():
    # 53 , 54
    print("Enter buzzer frequancy")
    freq = int(input())
    await empty_array()
    array_struct[53] = (hex(int(freq) & 0x00FF))
    array_struct[54] = (hex((int(freq) & 0x0000FF00) >> 8))  # Wrong bit shifting seems to work
    print(array_struct[53])
    print((array_struct[54]))
    await payload_maker()


async def move_forward2():
    # power = int(input())
    await empty_array()
    speed = 100
    array_struct[57] = '0x44'
    array_struct[58] = (hex(0 & 0x00FF))
    array_struct[59] = (hex((0 & 0xFF00) >> 8))
    array_struct[60] = (hex(speed & 0xff00 >> 8))

    array_struct[61] = (hex(0 & 0x00FF))
    array_struct[62] = (hex((0 & 0xFF00) >> 8))
    array_struct[63] = (hex(speed & 0xff00 >> 8))
    await payload_maker()
    await empty_array()
    time.sleep(0.1)
    array_struct[57] = '0x44'
    array_struct[58] = (hex(0 & 0x00FF))
    array_struct[59] = (hex((0 & 0xFF00) >> 8))
    array_struct[60] = (hex(0 & 0xff00 >> 8))

    array_struct[61] = (hex(0 & 0x00FF))
    array_struct[62] = (hex((0 & 0xFF00) >> 8))
    array_struct[63] = (hex(0 & 0xff00 >> 8))
    await payload_maker()


async def move_forward3():
    await move_forward(100)
    await client.write_gatt_char(write_characteristic, bytes(array_struct))
    array_struct.clear()


async def stop():
    await empty_array()
    array_struct[57] = '0x44'
    array_struct[58] = (hex(0 & 0x00FF))
    array_struct[59] = (hex((0 & 0xFF00) >> 8))
    array_struct[60] = (hex(0 & 0xff00 >> 8))

    array_struct[61] = (hex(0 & 0x00FF))
    array_struct[62] = (hex((0 & 0xFF00) >> 8))
    array_struct[63] = (hex(0 & 0xff00 >> 8))
    await payload_maker()

#
# async def controller():
#     val = True
#     while val:
#         if keyboard.is_pressed('w'):
#             await move_forward3()
#         else:


# async def live_data():
#     read = b'R\n'
#     await BleakClient.write_gatt_char(write_characteristic, bytes(None))
#     time.sleep(0.01)
#     while True:
#         data_set = await BleakClient.read_gatt_char(read_characteristic)

# data_set = int(''.join(map(hex, data_set)).replace('0x', ''), 16)
# print(data_set)
