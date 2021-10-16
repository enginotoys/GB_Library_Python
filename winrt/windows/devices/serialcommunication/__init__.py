# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.9.210202.1

import typing, winrt
import enum

_ns_module = winrt._import_ns_module("Windows.Devices.SerialCommunication")

try:
    import winrt.windows.foundation
except:
    pass

try:
    import winrt.windows.storage.streams
except:
    pass

class SerialError(enum.IntEnum):
    FRAME = 0
    BUFFER_OVERRUN = 1
    RECEIVE_FULL = 2
    RECEIVE_PARITY = 3
    TRANSMIT_FULL = 4

class SerialHandshake(enum.IntEnum):
    NONE = 0
    REQUEST_TO_SEND = 1
    X_ON_X_OFF = 2
    REQUEST_TO_SEND_X_ON_X_OFF = 3

class SerialParity(enum.IntEnum):
    NONE = 0
    ODD = 1
    EVEN = 2
    MARK = 3
    SPACE = 4

class SerialPinChange(enum.IntEnum):
    BREAK_SIGNAL = 0
    CARRIER_DETECT = 1
    CLEAR_TO_SEND = 2
    DATA_SET_READY = 3
    RING_INDICATOR = 4

class SerialStopBitCount(enum.IntEnum):
    ONE = 0
    ONE_POINT_FIVE = 1
    TWO = 2

ErrorReceivedEventArgs = _ns_module.ErrorReceivedEventArgs
PinChangedEventArgs = _ns_module.PinChangedEventArgs
SerialDevice = _ns_module.SerialDevice
