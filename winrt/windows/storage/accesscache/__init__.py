# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.9.210202.1

import typing, winrt
import enum

_ns_module = winrt._import_ns_module("Windows.Storage.AccessCache")

try:
    import winrt.windows.foundation
except:
    pass

try:
    import winrt.windows.foundation.collections
except:
    pass

try:
    import winrt.windows.storage
except:
    pass

class AccessCacheOptions(enum.IntFlag):
    NONE = 0
    DISALLOW_USER_INPUT = 0x1
    FAST_LOCATIONS_ONLY = 0x2
    USE_READ_ONLY_CACHED_COPY = 0x4
    SUPPRESS_ACCESS_TIME_UPDATE = 0x8

class RecentStorageItemVisibility(enum.IntEnum):
    APP_ONLY = 0
    APP_AND_SYSTEM = 1

AccessListEntry = _ns_module.AccessListEntry
AccessListEntryView = _ns_module.AccessListEntryView
ItemRemovedEventArgs = _ns_module.ItemRemovedEventArgs
StorageApplicationPermissions = _ns_module.StorageApplicationPermissions
StorageItemAccessList = _ns_module.StorageItemAccessList
StorageItemMostRecentlyUsedList = _ns_module.StorageItemMostRecentlyUsedList
IStorageItemAccessList = _ns_module.IStorageItemAccessList
