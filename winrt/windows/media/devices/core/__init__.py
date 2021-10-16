# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.9.210202.1

import typing, winrt
import enum

_ns_module = winrt._import_ns_module("Windows.Media.Devices.Core")

try:
    import winrt.windows.foundation
except:
    pass

try:
    import winrt.windows.foundation.collections
except:
    pass

try:
    import winrt.windows.foundation.numerics
except:
    pass

try:
    import winrt.windows.media.mediaproperties
except:
    pass

try:
    import winrt.windows.perception.spatial
except:
    pass

class FrameFlashMode(enum.IntEnum):
    DISABLE = 0
    ENABLE = 1
    GLOBAL = 2

CameraIntrinsics = _ns_module.CameraIntrinsics
DepthCorrelatedCoordinateMapper = _ns_module.DepthCorrelatedCoordinateMapper
FrameControlCapabilities = _ns_module.FrameControlCapabilities
FrameController = _ns_module.FrameController
FrameExposureCapabilities = _ns_module.FrameExposureCapabilities
FrameExposureCompensationCapabilities = _ns_module.FrameExposureCompensationCapabilities
FrameExposureCompensationControl = _ns_module.FrameExposureCompensationControl
FrameExposureControl = _ns_module.FrameExposureControl
FrameFlashCapabilities = _ns_module.FrameFlashCapabilities
FrameFlashControl = _ns_module.FrameFlashControl
FrameFocusCapabilities = _ns_module.FrameFocusCapabilities
FrameFocusControl = _ns_module.FrameFocusControl
FrameIsoSpeedCapabilities = _ns_module.FrameIsoSpeedCapabilities
FrameIsoSpeedControl = _ns_module.FrameIsoSpeedControl
VariablePhotoSequenceController = _ns_module.VariablePhotoSequenceController