# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.9.210202.1

import typing, winrt
import enum

_ns_module = winrt._import_ns_module("Windows.Devices.Display")

try:
    import winrt.windows.foundation
except:
    pass

try:
    import winrt.windows.graphics
except:
    pass

class DisplayMonitorConnectionKind(enum.IntEnum):
    INTERNAL = 0
    WIRED = 1
    WIRELESS = 2
    VIRTUAL = 3

class DisplayMonitorDescriptorKind(enum.IntEnum):
    EDID = 0
    DISPLAY_ID = 1

class DisplayMonitorPhysicalConnectorKind(enum.IntEnum):
    UNKNOWN = 0
    H_D15 = 1
    ANALOG_T_V = 2
    DVI = 3
    HDMI = 4
    LVDS = 5
    SDI = 6
    DISPLAY_PORT = 7

class DisplayMonitorUsageKind(enum.IntEnum):
    STANDARD = 0
    HEAD_MOUNTED = 1
    SPECIAL_PURPOSE = 2

DisplayMonitor = _ns_module.DisplayMonitor