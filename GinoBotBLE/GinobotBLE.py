from os import environ
from typing import Union
import sys
from time import sleep
from bleak import BleakClient
from bleak import discover


environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame


class speed:  # Speed standard values
    fast: int = 100
    medium: int = 80
    slow: int = 70


class color:  # Color standard values
    RED = [255, 0, 0]
    GREEN = [0, 255, 0]
    BLUE = [0, 0, 255]
    PURPLE = [128, 0, 128]
    PINK = [255, 0, 255]
    ORANGE = [255, 165, 0]
    YELLOW = [255, 255, 0]


class frequency:  # Frequency standard value
    HIGH: int = 800
    MEDIUM: int = 400
    LOW: int = 200


class threshold:  # Threshold standard values
    HIGH = 0
    MEDIUM = 30
    LOW = 50


### Characteristics ###

read_characteristic = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"
write_characteristic = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"

######################

### Vars and Lists ###
devices_list = []
devices_add = []
device_count = 0
count_delay = 0
count = 0

Found = False
InputsYes = ['Y', 'yes', 'YES', 'y', 'Yes']
InputsNo = ['n', 'N', 'No', 'NO', 'no']
Firmware = 0
Hardware = 0

connected = False
payload_write = 35
array_struct = []

###################

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
    count_delay = 1
    for x in range(9):
        sleep(0.3)
        count_delay += 1
        searching = searching + "."
        sys.stdout.write('\r' + searching)
        sys.stdout.flush()
        if count_delay == 3:
            count_delay = 0
            searching = "Searching"


async def scan(): #Scan for devices
    global devices
    global device_count
    device_count = 0
    search()
    devices = await discover()
    for i, device in enumerate(devices): # Enumarate and assign
        if device.name == 'ESP32':
            devices_list.append(device.name + " " + device.address) # Create a breakable string
            devices_add.append(device.address)
            device_count += 1
    if device_count == 0: # Check for devices again
        print('No devices found')
        ins = input("Do you want to rescan? [y/n]")
        if ins in InputsYes:
            await scan()
            return

        elif ins in InputsNo:
            print("Exiting")
            quit()
        else:
            ins = input("Invalid Input Enter again:")
            while ins not in InputsYes or ins not in InputsNo:
                ins = input("Invalid input Enter again")
                if ins in InputsYes:
                    await scan()
                    break
                elif ins in InputsNo:
                    break
                else:
                    continue


    if device_count == 1:
        print()
        print("1 Device found")
        print("| # | Name  |    Mac-Address     |")
        print("|", device_count, "|", devices_list[0][0:5], "| ", devices_list[0][6:25], "|")
        print("Choose a device to connect")
        await connect()

    elif device_count > 1:
        print()
        print(device_count, "Devices found ")
        print("| # | Name  |    Mac-Address     |")
        for i in range(device_count):
            print("|", i + 1, "|", str(devices_list[i][0:5]), "| ", devices_list[i][6:25], "|")
        print("Choose a device to connect")
        await connect()


async def connect():
    global client
    while True: # Exception for invalid input
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

    except Exception as e:
        print("Device failed to connect")


async def who_func():
    who_msg = b'?\n'
    global who_im_i
    global Firmware
    global Hardware
    if BleakClient.is_connected:
        print("Client name", client)
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

    for i in range(len(array_struct_empty)):
        array_struct_empty[i] = int(str(array_struct_empty[i]), base=16)


####################### Functionality ##########################

async def Front_Lights(red: Union[int, color], green=0, blue=0):
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


async def Back_Lights(red: Union[int, color], green=0, blue=0):
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


async def Buzzer(freq: Union[frequency, int]):
    # 53 , 54
    # (From 0 -10000)
    await empty_array()
    array_struct[53] = (hex(int(freq) & 0x00FF))
    array_struct[54] = (hex((int(freq) & 0x0000FF00) >> 8))  # Wrong bit shifting seems to work
    await payload_maker()


async def move_forward(speed: Union[speed, int]):
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


async def move_backwards(speed: Union[speed, int]):
    await empty_array()
    array_struct[57] = '0x44'
    array_struct[58] = (hex(0 & 0x00FF))
    array_struct[59] = (hex((0 & 0xFF00) >> 8))
    array_struct[60] = (hex(-speed & 0xff00 >> 8))

    array_struct[61] = (hex(0 & 0x00FF))
    array_struct[62] = (hex((0 & 0xFF00) >> 8))
    array_struct[63] = (hex(-speed & 0xff00 >> 8))
    await payload_maker()


async def move_right(speed: Union[speed, int]):
    await empty_array()
    array_struct[57] = '0x44'
    array_struct[58] = (hex(0 & 0x00FF))
    array_struct[59] = (hex((0 & 0xFF00) >> 8))
    array_struct[60] = (hex(speed & 0xff00 >> 8))

    array_struct[61] = (hex(0 & 0x00FF))
    array_struct[62] = (hex((0 & 0xFF00) >> 8))
    array_struct[63] = (hex(0 & 0xff00 >> 8))
    await payload_maker()


async def move_left(speed: Union[speed, int, None]):
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


##################### Live Data #######################


async def Front_Left_IR(thhold: Union[int, threshold]):
    read = b'R\n'
    global count
    if count == 0:
        print("Front Left IR Active ")
        count = 1
    sleep(0.2)
    await client.write_gatt_char(write_characteristic, read)
    sleep(0.05)
    data = await client.read_gatt_char(read_characteristic)
    Left_IR_Sensor = data[10]
    if thhold is None:
        Left_IR_Sensor = data[10]
    elif thhold == threshold.HIGH:
        Left_IR_Sensor = data[10]
    elif thhold == threshold.MEDIUM:
        Left_IR_Sensor = data[10] - threshold.MEDIUM
    elif thhold == threshold.LOW:
        Left_IR_Sensor = data[10] - threshold.LOW
    else:
        Left_IR_Sensor = data[10] - thhold
    return Left_IR_Sensor


async def Front_Right_IR(thhold: Union[int, threshold]):
    read = b'R\n'
    global count
    if count == 0:
        print("Front Right IR Active ")
        count = 1
    sleep(0.2)
    await client.write_gatt_char(write_characteristic, read)
    sleep(0.05)
    data = await client.read_gatt_char(read_characteristic)
    Left_IR_Sensor = data[11]
    if thhold == None:
        Left_IR_Sensor = data[11]
    elif thhold == threshold.HIGH:
        Left_IR_Sensor = data[11]
    elif thhold == threshold.MEDIUM:
        Left_IR_Sensor = data[11] - threshold.MEDIUM
    elif thhold == threshold.LOW:
        Left_IR_Sensor = data[11] - threshold.LOW
    else:
        Left_IR_Sensor = data[11] - thhold
    return Left_IR_Sensor


async def Back_IR(thhold: Union[int, threshold]):
    read = b'R\n'
    global count
    if count == 0:
        print("Front Right IR Active ")
        count = 1
    sleep(0.2)
    await client.write_gatt_char(write_characteristic, read)
    sleep(0.05)
    data = await client.read_gatt_char(read_characteristic)
    Left_IR_Sensor = data[9]
    if thhold is None:
        Left_IR_Sensor = data[9]
    elif thhold == threshold.HIGH:
        Left_IR_Sensor = data[9]
    elif thhold == threshold.MEDIUM:
        Left_IR_Sensor = data[9] - threshold.MEDIUM
    elif thhold == threshold.LOW:
        Left_IR_Sensor = data[9] - threshold.LOW
    else:
        Left_IR_Sensor = data[9] - thhold

    return Left_IR_Sensor


async def Ultrasonic_sense():
    read = b'R\n'
    global count
    if count == 0:
        print("Ultrasonic sensor is Active ")
        count = 1
    sleep(0.2)
    await client.write_gatt_char(write_characteristic, read)
    sleep(0.05)
    data = await client.read_gatt_char(read_characteristic)
    Ultrasonic_Sensor = data[30] +data[31]*256
    value_conversion = (Ultrasonic_Sensor) /10
    return value_conversion


async def Left_Color_sense():
    read = b'R\n'
    global count  # 15-16-17
    if count == 0:
        print("Left color sensor is Active ")
        count = 1
    sleep(0.2)
    await client.write_gatt_char(write_characteristic, read)
    sleep(0.05)
    data = await client.read_gatt_char(read_characteristic)
    Red_comp = data[15]
    Green_comp = data[16]
    Blue_Comp = data[17]
    if Red_comp >= 235 and Green_comp <= 100 and Blue_Comp <= 100:
        return [255, 0, 0]
    elif Red_comp <= 100 and Green_comp >= 235 and Blue_Comp <= 100:
        return [0, 255, 0]
    elif Red_comp <= 100 and Green_comp <= 100 and Blue_Comp >= 255:
        return [0, 0, 255]
    else:
        pass


async def Right_Color_sense():
    read = b'R\n'
    global count  # 15-16-17
    if count == 0:
        print("Right color sensor is Active ")
        count = 1
    sleep(0.2)
    await client.write_gatt_char(write_characteristic, read)
    sleep(0.05)
    data = await client.read_gatt_char(read_characteristic)
    Red_comp = data[15]  # 255
    Green_comp = data[16]
    Blue_Comp = data[17]
    if Red_comp >= 235 and Green_comp <= 100 and Blue_Comp <= 100:
        return [255, 0, 0]
    elif Red_comp <= 100 and Green_comp >= 235 and Blue_Comp <= 100:
        return [0, 255, 0]
    elif Red_comp <= 100 and Green_comp <= 100 and Blue_Comp >= 255:
        return [0, 0, 255]
    else:
        pass


async def controller():
    await payload_empty()
    await payload_gen()
    window = pygame.display.set_mode((500, 500))
    window1 = pygame.Surface((500, 500), pygame.SRCALPHA)

    clock = pygame.time.Clock()
    window_rect = window1.get_rect(midleft=(20, window.get_height() // 2))
    run = True
    while run:
        clock.tick(60)
        # current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            state = pygame.key.get_pressed()

            if state[pygame.K_UP] == 1:
                pygame.draw.polygon(surface=window1, color=(255, 0, 0), points=[(150, 150), (300, 150), (225, 40)])
                await client.write_gatt_char(write_characteristic, bytes(array_struct_mf))

            if state[pygame.K_LEFT] == 1:
                pygame.draw.polygon(surface=window1, color=(255, 0, 0), points=[(100, 170), (100, 310), (10, 240)])
                await client.write_gatt_char(write_characteristic, bytes(array_struct_ml))

            if state[pygame.K_DOWN] == 1:
                pygame.draw.polygon(surface=window1, color=(255, 0, 0), points=[(150, 350), (300, 350), (225, 440)])
                await client.write_gatt_char(write_characteristic, bytes(array_struct_mb))

            if state[pygame.K_RIGHT] == 1:
                pygame.draw.polygon(surface=window1, color=(255, 0, 0), points=[(350, 170), (350, 310), (450, 240)])
                await client.write_gatt_char(write_characteristic, bytes(array_struct_mr))

            if not state[pygame.K_LEFT] and not state[pygame.K_RIGHT] and not state[pygame.K_UP] and not state[pygame.K_DOWN]:
                pygame.draw.rect(window1, (224, 192, 160), (100, 230, 260, 20))
                pygame.draw.rect(window1, (224, 192, 160), (215, 110, 20, 250))

                pygame.draw.polygon(surface=window1, color=(224, 192, 160), points=[(150, 150), (300, 150), (225, 40)])
                pygame.draw.polygon(surface=window1, color=(224, 192, 160), points=[(150, 350), (300, 350), (225, 440)])
                pygame.draw.polygon(surface=window1, color=(224, 192, 160), points=[(100, 170), (100, 310), (10, 240)])
                pygame.draw.polygon(surface=window1, color=(224, 192, 160), points=[(350, 170), (350, 310), (450, 240)])
                await client.write_gatt_char(write_characteristic, bytes(array_struct_empty))
        window.fill((224, 192, 160))
        window.blit(window1, window_rect)
        pygame.display.flip()
    pygame.quit()
    exit()

