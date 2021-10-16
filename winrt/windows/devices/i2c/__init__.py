# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.9.210202.1

import typing, winrt
import enum

_ns_module = winrt._import_ns_module("Windows.Devices.I2c")

try:
    import winrt.windows.devices.i2c.provider
except:
    pass

try:
    import winrt.windows.foundation
except:
    pass

try:
    import winrt.windows.foundation.collections
except:
    pass

class I2cBusSpeed(enum.IntEnum):
    STANDARD_MODE = 0
    FAST_MODE = 1

class I2cSharingMode(enum.IntEnum):
    EXCLUSIVE = 0
    SHARED = 1

class I2cTransferStatus(enum.IntEnum):
    FULL_TRANSFER = 0
    PARTIAL_TRANSFER = 1
    SLAVE_ADDRESS_NOT_ACKNOWLEDGED = 2
    CLOCK_STRETCH_TIMEOUT = 3
    UNKNOWN_ERROR = 4

I2cTransferResult = _ns_module.I2cTransferResult
I2cConnectionSettings = _ns_module.I2cConnectionSettings
I2cController = _ns_module.I2cController
I2cDevice = _ns_module.I2cDevice
II2cDeviceStatics = _ns_module.II2cDeviceStatics