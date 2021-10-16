# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.9.210202.1

import typing, winrt
import enum

_ns_module = winrt._import_ns_module("Windows.Media.MediaProperties")

try:
    import winrt.windows.foundation
except:
    pass

try:
    import winrt.windows.foundation.collections
except:
    pass

try:
    import winrt.windows.media.core
except:
    pass

try:
    import winrt.windows.storage
except:
    pass

try:
    import winrt.windows.storage.streams
except:
    pass

class AudioEncodingQuality(enum.IntEnum):
    AUTO = 0
    HIGH = 1
    MEDIUM = 2
    LOW = 3

class MediaMirroringOptions(enum.IntFlag):
    NONE = 0
    HORIZONTAL = 0x1
    VERTICAL = 0x2

class MediaPixelFormat(enum.IntEnum):
    NV12 = 0
    BGRA8 = 1
    P010 = 2

class MediaRotation(enum.IntEnum):
    NONE = 0
    CLOCKWISE90_DEGREES = 1
    CLOCKWISE180_DEGREES = 2
    CLOCKWISE270_DEGREES = 3

class MediaThumbnailFormat(enum.IntEnum):
    BMP = 0
    BGRA8 = 1

class SphericalVideoFrameFormat(enum.IntEnum):
    NONE = 0
    UNSUPPORTED = 1
    EQUIRECTANGULAR = 2

class StereoscopicVideoPackingMode(enum.IntEnum):
    NONE = 0
    SIDE_BY_SIDE = 1
    TOP_BOTTOM = 2

class VideoEncodingQuality(enum.IntEnum):
    AUTO = 0
    H_D1080P = 1
    H_D720P = 2
    WVGA = 3
    NTSC = 4
    PAL = 5
    VGA = 6
    QVGA = 7
    UHD2160P = 8
    UHD4320P = 9

AudioEncodingProperties = _ns_module.AudioEncodingProperties
ContainerEncodingProperties = _ns_module.ContainerEncodingProperties
H264ProfileIds = _ns_module.H264ProfileIds
ImageEncodingProperties = _ns_module.ImageEncodingProperties
MediaEncodingProfile = _ns_module.MediaEncodingProfile
MediaEncodingSubtypes = _ns_module.MediaEncodingSubtypes
MediaPropertySet = _ns_module.MediaPropertySet
MediaRatio = _ns_module.MediaRatio
Mpeg2ProfileIds = _ns_module.Mpeg2ProfileIds
TimedMetadataEncodingProperties = _ns_module.TimedMetadataEncodingProperties
VideoEncodingProperties = _ns_module.VideoEncodingProperties
IMediaEncodingProperties = _ns_module.IMediaEncodingProperties
