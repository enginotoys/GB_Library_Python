# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.9.210202.1

import typing, winrt
import enum

_ns_module = winrt._import_ns_module("Windows.Media.DialProtocol")

try:
    import winrt.windows.devices.enumeration
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

try:
    import winrt.windows.storage.streams
except:
    pass

try:
    import winrt.windows.ui.popups
except:
    pass

class DialAppLaunchResult(enum.IntEnum):
    LAUNCHED = 0
    FAILED_TO_LAUNCH = 1
    NOT_FOUND = 2
    NETWORK_FAILURE = 3

class DialAppState(enum.IntEnum):
    UNKNOWN = 0
    STOPPED = 1
    RUNNING = 2
    NETWORK_FAILURE = 3

class DialAppStopResult(enum.IntEnum):
    STOPPED = 0
    STOP_FAILED = 1
    OPERATION_NOT_SUPPORTED = 2
    NETWORK_FAILURE = 3

class DialDeviceDisplayStatus(enum.IntEnum):
    NONE = 0
    CONNECTING = 1
    CONNECTED = 2
    DISCONNECTING = 3
    DISCONNECTED = 4
    ERROR = 5

DialApp = _ns_module.DialApp
DialAppStateDetails = _ns_module.DialAppStateDetails
DialDevice = _ns_module.DialDevice
DialDevicePicker = _ns_module.DialDevicePicker
DialDevicePickerFilter = _ns_module.DialDevicePickerFilter
DialDeviceSelectedEventArgs = _ns_module.DialDeviceSelectedEventArgs
DialDisconnectButtonClickedEventArgs = _ns_module.DialDisconnectButtonClickedEventArgs
DialReceiverApp = _ns_module.DialReceiverApp
