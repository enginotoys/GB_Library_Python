# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.9.210202.1

import typing, winrt
import enum

_ns_module = winrt._import_ns_module("Windows.Devices.Lights")

try:
    import winrt.windows.foundation
except:
    pass

try:
    import winrt.windows.foundation.numerics
except:
    pass

try:
    import winrt.windows.storage.streams
except:
    pass

try:
    import winrt.windows.system
except:
    pass

try:
    import winrt.windows.ui
except:
    pass

class LampArrayKind(enum.IntEnum):
    UNDEFINED = 0
    KEYBOARD = 1
    MOUSE = 2
    GAME_CONTROLLER = 3
    PERIPHERAL = 4
    SCENE = 5
    NOTIFICATION = 6
    CHASSIS = 7
    WEARABLE = 8
    FURNITURE = 9
    ART = 10

class LampPurposes(enum.IntFlag):
    UNDEFINED = 0
    CONTROL = 0x1
    ACCENT = 0x2
    BRANDING = 0x4
    STATUS = 0x8
    ILLUMINATION = 0x10
    PRESENTATION = 0x20

Lamp = _ns_module.Lamp
LampArray = _ns_module.LampArray
LampAvailabilityChangedEventArgs = _ns_module.LampAvailabilityChangedEventArgs
LampInfo = _ns_module.LampInfo