# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.9.210202.1

import typing, winrt
import enum

_ns_module = winrt._import_ns_module("Windows.Networking.Proximity")

try:
    import winrt.windows.foundation
except:
    pass

try:
    import winrt.windows.foundation.collections
except:
    pass

try:
    import winrt.windows.networking
except:
    pass

try:
    import winrt.windows.networking.sockets
except:
    pass

try:
    import winrt.windows.storage.streams
except:
    pass

class PeerDiscoveryTypes(enum.IntFlag):
    NONE = 0
    BROWSE = 0x1
    TRIGGERED = 0x2

class PeerRole(enum.IntEnum):
    PEER = 0
    HOST = 1
    CLIENT = 2

class PeerWatcherStatus(enum.IntEnum):
    CREATED = 0
    STARTED = 1
    ENUMERATION_COMPLETED = 2
    STOPPING = 3
    STOPPED = 4
    ABORTED = 5

class TriggeredConnectState(enum.IntEnum):
    PEER_FOUND = 0
    LISTENING = 1
    CONNECTING = 2
    COMPLETED = 3
    CANCELED = 4
    FAILED = 5

ConnectionRequestedEventArgs = _ns_module.ConnectionRequestedEventArgs
PeerFinder = _ns_module.PeerFinder
PeerInformation = _ns_module.PeerInformation
PeerWatcher = _ns_module.PeerWatcher
ProximityDevice = _ns_module.ProximityDevice
ProximityMessage = _ns_module.ProximityMessage
TriggeredConnectionStateChangedEventArgs = _ns_module.TriggeredConnectionStateChangedEventArgs
