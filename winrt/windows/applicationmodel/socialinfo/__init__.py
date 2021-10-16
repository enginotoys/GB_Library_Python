# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.9.210202.1

import typing, winrt
import enum

_ns_module = winrt._import_ns_module("Windows.ApplicationModel.SocialInfo")

try:
    import winrt.windows.foundation
except:
    pass

try:
    import winrt.windows.foundation.collections
except:
    pass

try:
    import winrt.windows.graphics.imaging
except:
    pass

try:
    import winrt.windows.storage.streams
except:
    pass

class SocialFeedItemStyle(enum.IntEnum):
    DEFAULT = 0
    PHOTO = 1

class SocialFeedKind(enum.IntEnum):
    HOME_FEED = 0
    CONTACT_FEED = 1
    DASHBOARD = 2

class SocialFeedUpdateMode(enum.IntEnum):
    APPEND = 0
    REPLACE = 1

class SocialItemBadgeStyle(enum.IntEnum):
    HIDDEN = 0
    VISIBLE = 1
    VISIBLE_WITH_COUNT = 2

SocialFeedChildItem = _ns_module.SocialFeedChildItem
SocialFeedContent = _ns_module.SocialFeedContent
SocialFeedItem = _ns_module.SocialFeedItem
SocialFeedSharedItem = _ns_module.SocialFeedSharedItem
SocialItemThumbnail = _ns_module.SocialItemThumbnail
SocialUserInfo = _ns_module.SocialUserInfo