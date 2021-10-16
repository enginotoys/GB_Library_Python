# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.9.210202.1

import typing, winrt
import enum

_ns_module = winrt._import_ns_module("Windows.Gaming.Input.Custom")

try:
    import winrt.windows.foundation
except:
    pass

try:
    import winrt.windows.gaming.input
except:
    pass

try:
    import winrt.windows.storage.streams
except:
    pass

class GipFirmwareUpdateStatus(enum.IntEnum):
    COMPLETED = 0
    UP_TO_DATE = 1
    FAILED = 2

class GipMessageClass(enum.IntEnum):
    COMMAND = 0
    LOW_LATENCY = 1
    STANDARD_LATENCY = 2

class XusbDeviceSubtype(enum.IntEnum):
    UNKNOWN = 0
    GAMEPAD = 1
    ARCADE_PAD = 2
    ARCADE_STICK = 3
    FLIGHT_STICK = 4
    WHEEL = 5
    GUITAR = 6
    GUITAR_ALTERNATE = 7
    GUITAR_BASS = 8
    DRUM_KIT = 9
    DANCE_PAD = 10

class XusbDeviceType(enum.IntEnum):
    UNKNOWN = 0
    GAMEPAD = 1

GameControllerVersionInfo = _ns_module.GameControllerVersionInfo
GipFirmwareUpdateProgress = _ns_module.GipFirmwareUpdateProgress
GameControllerFactoryManager = _ns_module.GameControllerFactoryManager
GipFirmwareUpdateResult = _ns_module.GipFirmwareUpdateResult
GipGameControllerProvider = _ns_module.GipGameControllerProvider
HidGameControllerProvider = _ns_module.HidGameControllerProvider
XusbGameControllerProvider = _ns_module.XusbGameControllerProvider
ICustomGameControllerFactory = _ns_module.ICustomGameControllerFactory
IGameControllerInputSink = _ns_module.IGameControllerInputSink
IGameControllerProvider = _ns_module.IGameControllerProvider
IGipGameControllerInputSink = _ns_module.IGipGameControllerInputSink
IHidGameControllerInputSink = _ns_module.IHidGameControllerInputSink
IXusbGameControllerInputSink = _ns_module.IXusbGameControllerInputSink
