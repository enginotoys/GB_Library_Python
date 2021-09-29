from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import sys
import asyncio
from time import sleep
import struct
import time
import pygame
from time import sleep
from bleak import BleakClient
from bleak import discover


# from aioconsole import ainput


class speed():
    fast = 100
    medium = 80
    slow = 60


class color():
    RED = [255, 0, 0]
    GREEN = [0, 255, 0]
    BLUE = [0, 0, 255]
    PURPLE = [128, 0, 128]
    PINK = [255, 0, 255]
    ORANGE = [255, 165, 0]
    YELLOW = [255, 255, 0]


class read_live_data():
    def __init__(self):
        self.data = None
        self.Left_IR_Sensor = None
    async def sensor(self):
        self.read = b'R\n'
        while True:
            await client.write_gatt_char(write_characteristic, self.read)
            sleep(0.05)
            self.data = await client.read_gatt_char(read_characteristic)
            self.Left_IR_Sensor =self.data[11]





read_characteristic = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"
write_characteristic = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"

devices_list = []
devices_add = []
device_count = 0
Found = False
InputsYes = ['Y', 'yes', 'YES', 'y', 'Yes']
InputsNo = ['n', 'N', 'No', 'NO', 'no']
Firmware = 0
Hardware = 0

connected = False
payload_write = 35
array_struct = []

#####Controling Arrays #######
array_struct_gen = []
array_struct_mf = []
array_struct_mb = []
array_struct_mr = []
array_struct_ml = []
array_struct_empty = []
##############################


########Live Data Arrays #####




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
    global devices
    global InputN
    global InputY
    global device_count
    device_count = 0
    InputY = False
    InputN = False
    search()
    devices = await discover()
    for i, device in enumerate(devices):
        if device.name == 'ESP32':
            devices_list.append(device.name + " " + device.address)
            devices_add.append(device.address)
            device_count += 1
    if device_count == 0:
        print('No devices found')
        ins = input("Do you want to rescan? [y/n]")
        if ins in InputsYes or ins in InputY:
            await scan()

        elif ins in InputsNo or ins in InputN:
            print("Exiting")
            quit()
        else:
            ins = input("Invalid Input Enter again:")
            while ins not in InputsYes or ins not in InputsNo:
                ins = input("Invalid input Enter again")
                if ins in InputsYes:
                    InputY = True
                    await scan()
                    break
                elif ins in InputsNo:
                    InputN = True
                    break
                else:
                    continue

    if device_count == 1:
        print()
        print("1 Device found")
        print("| # | Name  |    Mac-Address     |")
        print("|",device_count,"|", devices_list[0][0:5],"| " ,devices_list[0][6:25], "|" )
        print("Choose a device to connect or type 'No' to exit ")
        await connect()


    elif device_count > 1:
        print()
        print(device_count, "Devices found ")
        print("| # | Name  |    Mac-Address     |")
        for i in range(device_count):
            print("|", device_count, "|", str(devices_list[i][0:5]), "| ", devices_list[i][6:25], "|")
        print("Choose a device to connect")
        await connect()


async def connect():
    global client
    while True:
        try:
            var = int(input())
            if var > device_count:
                print("Invalid input")
            else:
                break
        except Exception:
            print("Invalid input")

    client = BleakClient(devices_add[var - 1])
    try:
        await client.connect()
        device_add = client.address
        if client.is_connected:
            print("Connection was successful")
            await who_func()
            return True
    except Exception as e:
        print("Device failed to connect")


async def who_func():
    who_msg = b'?\n'
    global who_im_i
    global Firmware
    global Hardware
    if BleakClient.is_connected:
        print(client)
        try:
            await client.write_gatt_char(write_characteristic, who_msg)
            sleep(0.3)
            who_im_i = await client.read_gatt_char(read_characteristic)
            Firmware = who_im_i[3]
            Hardware = who_im_i[4]
        except Exception:  # Exception is only caused by NameError or Index out of range
            print("Device failed to configure")


async def empty_array():  # This function builds the start empty array for Ginobot

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
    array_struct.clear()


async def payload_gen():
    array_struct_gen.append(hex(ord('W')))
    array_struct_gen.append(hex(ord(':')))

    array_struct_gen.append(hex(ord('0'))), array_struct_gen.append(hex(ord('0'))), array_struct_gen.append(hex(ord('8')))
    array_struct_gen.append(hex(ord('0'))), array_struct_gen.append(hex(ord('\n')))

    for i in range(7, 32):
        array_struct_gen.append(hex(ord(' ')))

    array_struct_gen.append(hex(ord('[')))
    array_struct_gen.append(hex(ord('[')))
    array_struct_gen.append(hex(ord('[')))

    array_struct_gen.append(Firmware)  # pos 35
    array_struct_gen.append(Hardware)  # pos 36

    array_struct_gen.append(hex(int(payload_write & 0x00FF)))
    array_struct_gen.append(hex(int(payload_write & 0xFF00) >> 8))

    array_struct_gen.append(hex(ord('W')))
    array_struct_gen.append(hex(0))  # pos 40

    for i in range(36):
        array_struct_gen.append(hex(0))

    checksummf = 0
    checksummb = 0
    checksummr = 0
    checksumml = 0

    array_struct_mf.extend(array_struct_gen)
    array_struct_ml.extend(array_struct_gen)
    array_struct_mr.extend(array_struct_gen)
    array_struct_mb.extend(array_struct_gen)
    ############################################
    array_struct_mf[57] = '0x44'
    array_struct_mf[58] = (hex(0 & 0x00FF))
    array_struct_mf[59] = (hex((0 & 0xFF00) >> 8))
    array_struct_mf[60] = (hex(100 & 0xff00 >> 8))

    array_struct_mf[61] = (hex(0 & 0x00FF))
    array_struct_mf[62] = (hex((0 & 0xFF00) >> 8))
    array_struct_mf[63] = (hex(100 & 0xff00 >> 8))
    ############################################

    array_struct_mr[57] = '0x44'
    array_struct_mr[58] = (hex(0 & 0x00FF))
    array_struct_mr[59] = (hex((0 & 0xFF00) >> 8))
    array_struct_mr[60] = (hex(100 & 0xff00 >> 8))

    array_struct_mr[61] = (hex(0 & 0x00FF))
    array_struct_mr[62] = (hex((0 & 0xFF00) >> 8))
    array_struct_mr[63] = (hex(-100 & 0xff00 >> 8))

    ############################################
    array_struct_ml[57] = '0x44'
    array_struct_ml[58] = (hex(0 & 0x00FF))
    array_struct_ml[59] = (hex((0 & 0xFF00) >> 8))
    array_struct_ml[60] = (hex(-100 & 0xff00 >> 8))

    array_struct_ml[61] = (hex(0 & 0x00FF))
    array_struct_ml[62] = (hex((0 & 0xFF00) >> 8))
    array_struct_ml[63] = (hex(100 & 0xff00 >> 8))

    ############################################
    array_struct_mb[57] = '0x44'
    array_struct_mb[58] = (hex(0 & 0x00FF))
    array_struct_mb[59] = (hex((0 & 0xFF00) >> 8))
    array_struct_mb[60] = (hex(-100 & 0xff00 >> 8))

    array_struct_mb[61] = (hex(0 & 0x00FF))
    array_struct_mb[62] = (hex((0 & 0xFF00) >> 8))
    array_struct_mb[63] = (hex(-100 & 0xff00 >> 8))
    ############################################
    for i in range(payload_write):
        checksummf += int(array_struct_mf[i + 40], 16)
        checksummr += int(array_struct_mr[i + 40], 16)
        checksumml += int(array_struct_ml[i + 40], 16)
        checksummb += int(array_struct_mb[i + 40], 16)

    array_struct_mf.append(hex(int(checksummf) & 0x000000FF))
    array_struct_mf.append(hex((int(checksummf) & 0x0000FF00) >> 8))

    array_struct_mf.append(hex(ord(']')))
    array_struct_mf.append(hex(ord(']')))
    array_struct_mf.append(hex(ord(']')))
    #########################################################
    array_struct_mr.append(hex(int(checksummr) & 0x000000FF))
    array_struct_mr.append(hex((int(checksummr) & 0x0000FF00) >> 8))

    array_struct_mr.append(hex(ord(']')))
    array_struct_mr.append(hex(ord(']')))
    array_struct_mr.append(hex(ord(']')))
    ###############################################
    array_struct_ml.append(hex(int(checksumml & 0x000000FF)))
    array_struct_ml.append(hex((int(checksumml) & 0x0000FF00) >> 8))

    array_struct_ml.append(hex(ord(']')))
    array_struct_ml.append(hex(ord(']')))
    array_struct_ml.append(hex(ord(']')))
    ################################################
    array_struct_mb.append(hex(int(checksummb) & 0x000000FF))
    array_struct_mb.append(hex((int(checksummb) & 0x0000FF00) >> 8))

    array_struct_mb.append(hex(ord(']')))
    array_struct_mb.append(hex(ord(']')))
    array_struct_mb.append(hex(ord(']')))

    for i in range(len(array_struct_mf)):
        array_struct_mf[i] = int(str(array_struct_mf[i]), base=16)
        array_struct_mr[i] = int(str(array_struct_mr[i]), base=16)
        array_struct_ml[i] = int(str(array_struct_ml[i]), base=16)
        array_struct_mb[i] = int(str(array_struct_mb[i]), base=16)


async def payload_empty():
    array_struct_empty.append(hex(ord('W')))
    array_struct_empty.append(hex(ord(':')))

    array_struct_empty.append(hex(ord('0'))), array_struct_empty.append(hex(ord('0'))), array_struct_empty.append(hex(ord('8')))
    array_struct_empty.append(hex(ord('0'))), array_struct_empty.append(hex(ord('\n')))

    for i in range(7, 32):
        array_struct_empty.append(hex(ord(' ')))

    array_struct_empty.append(hex(ord('[')))
    array_struct_empty.append(hex(ord('[')))
    array_struct_empty.append(hex(ord('[')))

    array_struct_empty.append(Firmware)  # pos 35
    array_struct_empty.append(Hardware)  # pos 36

    array_struct_empty.append(hex(int(payload_write & 0x00FF)))
    array_struct_empty.append(hex(int(payload_write & 0xFF00) >> 8))

    array_struct_empty.append(hex(ord('W')))
    array_struct_empty.append(hex(0))  # pos 40

    for i in range(36):
        array_struct_empty.append(hex(0))
    checksum = 0
    for i in range(payload_write):
        checksum += int(array_struct_empty[i + 40], 16)

    array_struct_empty.append(hex(int(checksum) & 0x000000FF))
    array_struct_empty.append(hex((int(checksum) & 0x0000FF00) >> 8))

    array_struct_empty.append(hex(ord(']')))
    array_struct_empty.append(hex(ord(']')))
    array_struct_empty.append(hex(ord(']')))

    print(array_struct_empty)
    for i in range(len(array_struct_empty)):
        array_struct_empty[i] = int(str(array_struct_empty[i]), base=16)


####################### Functionality ##########################

async def Front_Lights(red=None, green=0, blue=0):
    print("Front Lights input (Red , Green , Blue)")
    await empty_array()

    if isinstance(red, list):
        array_struct[49] = hex(red[0])
        array_struct[50] = hex(red[1])
        array_struct[51] = hex(red[2])
    else:
        array_struct[49] = hex(red)
        array_struct[50] = hex(green)
        array_struct[51] = hex(blue)

    await payload_maker()


async def Back_Lights(red=None, green=0, blue=0):
    print("Front Lights input (Red , Green , Blue)")
    await empty_array()

    if isinstance(red, list):
        array_struct[46] = hex(red[0])
        array_struct[47] = hex(red[1])
        array_struct[48] = hex(red[2])
    else:
        array_struct[46] = hex(red)
        array_struct[47] = hex(green)
        array_struct[48] = hex(blue)

    await payload_maker()


async def Buzzer(freq):
    # 53 , 54
    # (From 0 -10000)
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


async def stop_movement():
    await empty_array()
    array_struct[57] = '0x44'
    array_struct[58] = (hex(0 & 0x00FF))
    array_struct[59] = (hex((0 & 0xFF00) >> 8))
    array_struct[60] = (hex(0 & 0xff00 >> 8))

    array_struct[61] = (hex(0 & 0x00FF))
    array_struct[62] = (hex((0 & 0xFF00) >> 8))
    array_struct[63] = (hex(0 & 0xff00 >> 8))
    await payload_maker()


########################## TESTS #############################

async def Back_Lights_Test(*args):  # Look for multiple arguments in function
    print('Back Lights input (Red , Green , Blue)')
    col_arr = []
    await empty_array()
    col_arr.append(0)
    col_arr.append(0)
    col_arr.append(0)

    for count, i in enumerate(args):
        col_arr[count] = i
        print(i)
    array_struct[46] = hex(col_arr[0])
    array_struct[47] = hex(col_arr[1])
    array_struct[48] = hex(col_arr[2])

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
    sleep(0.15)
    array_struct[57] = '0x44'
    array_struct[58] = (hex(0 & 0x00FF))
    array_struct[59] = (hex((0 & 0xFF00) >> 8))
    array_struct[60] = (hex(0 & 0xff00 >> 8))

    array_struct[61] = (hex(0 & 0x00FF))
    array_struct[62] = (hex((0 & 0xFF00) >> 8))
    array_struct[63] = (hex(0 & 0xff00 >> 8))
    await payload_maker()


async def move_backwards2():
    await empty_array()
    array_struct[57] = '0x44'
    array_struct[58] = (hex(0 & 0x00FF))
    array_struct[59] = (hex((0 & 0xFF00) >> 8))
    array_struct[60] = (hex(-100 & 0xff00 >> 8))

    array_struct[61] = (hex(0 & 0x00FF))
    array_struct[62] = (hex((0 & 0xFF00) >> 8))
    array_struct[63] = (hex(-100 & 0xff00 >> 8))
    await payload_maker()
    await empty_array()
    sleep(0.15)
    array_struct[57] = '0x44'
    array_struct[58] = (hex(0 & 0x00FF))
    array_struct[59] = (hex((0 & 0xFF00) >> 8))
    array_struct[60] = (hex(0 & 0xff00 >> 8))

    array_struct[61] = (hex(0 & 0x00FF))
    array_struct[62] = (hex((0 & 0xFF00) >> 8))
    array_struct[63] = (hex(0 & 0xff00 >> 8))
    await payload_maker()


async def move_right2():
    await empty_array()
    array_struct[57] = '0x44'
    array_struct[58] = (hex(0 & 0x00FF))
    array_struct[59] = (hex((0 & 0xFF00) >> 8))
    array_struct[60] = (hex(100 & 0xff00 >> 8))

    array_struct[61] = (hex(0 & 0x00FF))
    array_struct[62] = (hex((0 & 0xFF00) >> 8))
    array_struct[63] = (hex(0 & 0xff00 >> 8))
    await payload_maker()
    await empty_array()
    sleep(0.15)
    array_struct[57] = '0x44'
    array_struct[58] = (hex(0 & 0x00FF))
    array_struct[59] = (hex((0 & 0xFF00) >> 8))
    array_struct[60] = (hex(0 & 0xff00 >> 8))

    array_struct[61] = (hex(0 & 0x00FF))
    array_struct[62] = (hex((0 & 0xFF00) >> 8))
    array_struct[63] = (hex(0 & 0xff00 >> 8))
    await payload_maker()


async def move_left2():
    await empty_array()
    array_struct[57] = '0x44'
    array_struct[58] = (hex(0 & 0x00FF))
    array_struct[59] = (hex((0 & 0xFF00) >> 8))
    array_struct[60] = (hex(0 & 0xff00 >> 8))

    array_struct[61] = (hex(0 & 0x00FF))
    array_struct[62] = (hex((0 & 0xFF00) >> 8))
    array_struct[63] = (hex(100 & 0xff00 >> 8))
    await payload_maker()
    await empty_array()
    sleep(0.15)
    array_struct[57] = '0x44'
    array_struct[58] = (hex(0 & 0x00FF))
    array_struct[59] = (hex((0 & 0xFF00) >> 8))
    array_struct[60] = (hex(0 & 0xff00 >> 8))

    array_struct[61] = (hex(0 & 0x00FF))
    array_struct[62] = (hex((0 & 0xFF00) >> 8))
    array_struct[63] = (hex(0 & 0xff00 >> 8))
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


async def read_live_data2():
    read = b'R\n'
    while True:
        await client.write_gatt_char(write_characteristic,read)
        sleep(0.5)
        #bytearray(b'[[[\x01\t=\x00R\x01[d\x1a;@\x1c\xffAl\xffgx\x00\x00\x00\x00\x00\x00\x00\x00\x007\x02\xab\x00\x9f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000u\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00/\x07]]]')
                    #5784404021390297995967854687338395505204618818410782889100534200507419783995774457835664446359544355193215984683490923712504531209856515148434533361814640438277517221018203938141
                    #57844040213902979959678
        live_data = await client.read_gatt_char(read_characteristic)
        print(live_data)
        # for i in b:
        #     print(i)
        print(live_data[0],live_data[1],live_data[2],live_data[3],live_data[4],live_data[5],live_data[6],live_data[7],live_data[8],live_data[9],live_data[10],live_data[11],live_data[12],live_data[13],live_data[14],live_data[15],live_data[16],live_data[17],live_data[18],live_data[19],live_data[20],live_data[21],live_data[22],live_data[23],live_data[24],live_data[25],live_data[26],live_data[27],live_data[28], live_data[29])
        Left_IR_Sensor = live_data[11]
        if Left_IR_Sensor >= 50:
            print("works!!!")
        elif Left_IR_Sensor<10:
            print("NOT WORKS")


async def controller():
    await payload_empty()
    await payload_gen()
    bool_statew = False
    bool_states = False
    count = 0
    bool_state_off = False
    window = pygame.display.set_mode((300, 300))
    clock = pygame.time.Clock()

    rect = pygame.Rect(0, 0, 20, 20)
    rect.center = window.get_rect().center
    while True:

        for event in pygame.event.get():
                state = pygame.key.get_pressed()
                state1 = not pygame.key.get_pressed()
                if state[pygame.K_UP]==1 and state[pygame.K_LEFT] == 0:
                    print("here")
                    await client.write_gatt_char(write_characteristic, bytes(array_struct_mf))
                if state[pygame.K_UP]==0 and state[pygame.K_LEFT] == 1:
                    print("here")
                    await client.write_gatt_char(write_characteristic, bytes(array_struct_ml))
                if state[pygame.K_UP]==1 and state[pygame.K_RIGHT] == 0:
                    print("here")
                    await client.write_gatt_char(write_characteristic, bytes(array_struct_mf))
                if state[pygame.K_UP]==0 and state[pygame.K_RIGHT] == 1:
                    print("here")
                    await client.write_gatt_char(write_characteristic, bytes(array_struct_mr))
                if state[pygame.K_DOWN]==1 and state[pygame.K_LEFT] == 0:
                    print("here")
                    await client.write_gatt_char(write_characteristic, bytes(array_struct_mb))
                if state[pygame.K_DOWN]==0 and state[pygame.K_LEFT] == 1:
                    print("here")
                    await client.write_gatt_char(write_characteristic, bytes(array_struct_ml))
                if state[pygame.K_DOWN]==1 and state[pygame.K_RIGHT] == 0:
                    print("here")
                    await client.write_gatt_char(write_characteristic, bytes(array_struct_mb))
                if state[pygame.K_DOWN]==0 and state[pygame.K_RIGHT] == 1:
                    print("here")
                    await client.write_gatt_char(write_characteristic, bytes(array_struct_mr))
                # if state[pygame.K_RIGHT] and state[pygame.UP] == 0:
                #     print("here")
                #     await client.write_gatt_char(write_characteristic, bytes(array_struct_mr))
                if not state[pygame.K_LEFT] and not state[pygame.K_RIGHT] and not state[pygame.K_UP] and not state[pygame.K_DOWN]:
                    print("key None")
                    await client.write_gatt_char(write_characteristic, bytes(array_struct_empty))

                #
                # if event.key == pygame.K_LEFT:
                #     print("key left")
                #     await client.write_gatt_char(write_characteristic, bytes(array_struct_empty))
                # if event.key == pygame.K_RIGHT:
                #     print("key right")
                #     await client.write_gatt_char(write_characteristic, bytes(array_struct_empty))
                # if event.key == pygame.K_UP:
                #     print("key up")
                #     await client.write_gatt_char(write_characteristic, bytes(array_struct_empty))
                # if event.key == pygame.K_DOWN:
                #     print("key down")
                #     await client.write_gatt_char(write_characteristic, bytes(array_struct_empty))



        #     print("w", end=" ")
        #     await client.write_gatt_char(write_characteristic, bytes(array_struct_mf))
        #     bool_statew = True
        #   #  keyboard.unhook_all()
        # if keyboard.read_key() == 's':
        #     print('s', end=" ")
        #     await client.write_gatt_char(write_characteristic, bytes(array_struct_mb))
        #     bool_statew = True
        # if keyboard.read_key() == 'd':
        #     print('d', end=" ")
        #     await client.write_gatt_char(write_characteristic, bytes(array_struct_mr))
        #     bool_statew = True
        # if not keyboard.is_pressed('w') and bool_statew and not keyboard.is_pressed('s') and bool_statew:
        #     bool_state_off = True
        # if bool_state_off:
        #     await client.write_gatt_char(write_characteristic,bytes(array_struct_empty))
        # if not keyboard.is_pressed('w') and bool_statew and not keyboard.is_pressed('s') and bool_statew and not keyboard.is_pressed('d') and bool_statew:
        #     print("not in")
        #   #  await client.write_gatt_char(write_characteristic, bytes(array_struct_empty))
        #     bool_statew = False

        # if keyboard.read_key() == 's' and not bool_states:
        #     await client.write_gatt_char(write_characteristic, bytes(array_struct_mb))
        #
        #     bool_states = True
        # if not keyboard.is_pressed('s') and bool_states:
        #     await client.write_gatt_char(write_characteristic, bytes(array_struct_empty))
        #     keyboard.press('w')
        #     bool_states = False
        # print("here")
    # When sewnding too many bytes it blocks gino bot and ignores some ifs

    # while True:
    #     bool_state = False
    #     while True:
    #         if keyboard.read_key() == 'w' and not bool_state:
    #             await client.write_gatt_char(write_characteristic, bytes(array_struct_mf))
    #             print("hELLO")
    #             bool_state = False
    #         if keyboard.is_pressed('w') and
    # if keyboard.read_key() =='s' and not bool_state[1]:
    #     await client.write_gatt_char(write_characteristic, bytes(array_struct_mb))
    #     bool_state[1] = True

    # if keyboard.read_key() == 's' and not bool_state:
    #     await s_press()

    # while True:
    #     while keyboard.read_key()=='w' and not bool_state:
    #         await client.write_gatt_char(write_characteristic, bytes(array_struct_mf))
    #         bool_state = True
    #
    #     while keyboard.read_key()=='s' and not bool_state:
    #         await client.write_gatt_char(write_characteristic, bytes(array_struct_mb))
    #         bool_state = True
    # if not keyboard.is_pressed("s") and bool_state: #or not keyboard.is_pressed("s")):
    #     #     bool_state = T rue
    #     #     await client.write_gatt_char(write_characteristic,bytes(array_struct_empty))
    #     #     print("stop")
    #
    #     if not keyboard.is_pressed('w') and bool_state :
    #         bool_state = False
    #         await client.write_gatt_char(write_characteristic, bytes(array_struct_empty))
    #         print("Hello")