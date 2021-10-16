# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.9.210202.1

import typing, winrt
import enum

_ns_module = winrt._import_ns_module("Windows.Media.Audio")

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
    import winrt.windows.foundation.numerics
except:
    pass

try:
    import winrt.windows.media
except:
    pass

try:
    import winrt.windows.media.capture
except:
    pass

try:
    import winrt.windows.media.core
except:
    pass

try:
    import winrt.windows.media.devices
except:
    pass

try:
    import winrt.windows.media.effects
except:
    pass

try:
    import winrt.windows.media.mediaproperties
except:
    pass

try:
    import winrt.windows.media.render
except:
    pass

try:
    import winrt.windows.media.transcoding
except:
    pass

try:
    import winrt.windows.storage
except:
    pass

class AudioDeviceNodeCreationStatus(enum.IntEnum):
    SUCCESS = 0
    DEVICE_NOT_AVAILABLE = 1
    FORMAT_NOT_SUPPORTED = 2
    UNKNOWN_FAILURE = 3
    ACCESS_DENIED = 4

class AudioFileNodeCreationStatus(enum.IntEnum):
    SUCCESS = 0
    FILE_NOT_FOUND = 1
    INVALID_FILE_TYPE = 2
    FORMAT_NOT_SUPPORTED = 3
    UNKNOWN_FAILURE = 4

class AudioGraphCreationStatus(enum.IntEnum):
    SUCCESS = 0
    DEVICE_NOT_AVAILABLE = 1
    FORMAT_NOT_SUPPORTED = 2
    UNKNOWN_FAILURE = 3

class AudioGraphUnrecoverableError(enum.IntEnum):
    NONE = 0
    AUDIO_DEVICE_LOST = 1
    AUDIO_SESSION_DISCONNECTED = 2
    UNKNOWN_FAILURE = 3

class AudioNodeEmitterDecayKind(enum.IntEnum):
    NATURAL = 0
    CUSTOM = 1

class AudioNodeEmitterSettings(enum.IntFlag):
    NONE = 0
    DISABLE_DOPPLER = 0x1

class AudioNodeEmitterShapeKind(enum.IntEnum):
    OMNIDIRECTIONAL = 0
    CONE = 1

class MediaSourceAudioInputNodeCreationStatus(enum.IntEnum):
    SUCCESS = 0
    FORMAT_NOT_SUPPORTED = 1
    NETWORK_ERROR = 2
    UNKNOWN_FAILURE = 3

class MixedRealitySpatialAudioFormatPolicy(enum.IntEnum):
    USE_MIXED_REALITY_DEFAULT_SPATIAL_AUDIO_FORMAT = 0
    USE_DEVICE_CONFIGURATION_DEFAULT_SPATIAL_AUDIO_FORMAT = 1

class QuantumSizeSelectionMode(enum.IntEnum):
    SYSTEM_DEFAULT = 0
    LOWEST_LATENCY = 1
    CLOSEST_TO_DESIRED = 2

class SetDefaultSpatialAudioFormatStatus(enum.IntEnum):
    SUCCEEDED = 0
    ACCESS_DENIED = 1
    LICENSE_EXPIRED = 2
    LICENSE_NOT_VALID_FOR_AUDIO_ENDPOINT = 3
    NOT_SUPPORTED_ON_AUDIO_ENDPOINT = 4
    UNKNOWN_ERROR = 5

class SpatialAudioModel(enum.IntEnum):
    OBJECT_BASED = 0
    FOLD_DOWN = 1

AudioDeviceInputNode = _ns_module.AudioDeviceInputNode
AudioDeviceOutputNode = _ns_module.AudioDeviceOutputNode
AudioFileInputNode = _ns_module.AudioFileInputNode
AudioFileOutputNode = _ns_module.AudioFileOutputNode
AudioFrameCompletedEventArgs = _ns_module.AudioFrameCompletedEventArgs
AudioFrameInputNode = _ns_module.AudioFrameInputNode
AudioFrameOutputNode = _ns_module.AudioFrameOutputNode
AudioGraph = _ns_module.AudioGraph
AudioGraphBatchUpdater = _ns_module.AudioGraphBatchUpdater
AudioGraphConnection = _ns_module.AudioGraphConnection
AudioGraphSettings = _ns_module.AudioGraphSettings
AudioGraphUnrecoverableErrorOccurredEventArgs = _ns_module.AudioGraphUnrecoverableErrorOccurredEventArgs
AudioNodeEmitter = _ns_module.AudioNodeEmitter
AudioNodeEmitterConeProperties = _ns_module.AudioNodeEmitterConeProperties
AudioNodeEmitterDecayModel = _ns_module.AudioNodeEmitterDecayModel
AudioNodeEmitterNaturalDecayModelProperties = _ns_module.AudioNodeEmitterNaturalDecayModelProperties
AudioNodeEmitterShape = _ns_module.AudioNodeEmitterShape
AudioNodeListener = _ns_module.AudioNodeListener
AudioStateMonitor = _ns_module.AudioStateMonitor
AudioSubmixNode = _ns_module.AudioSubmixNode
CreateAudioDeviceInputNodeResult = _ns_module.CreateAudioDeviceInputNodeResult
CreateAudioDeviceOutputNodeResult = _ns_module.CreateAudioDeviceOutputNodeResult
CreateAudioFileInputNodeResult = _ns_module.CreateAudioFileInputNodeResult
CreateAudioFileOutputNodeResult = _ns_module.CreateAudioFileOutputNodeResult
CreateAudioGraphResult = _ns_module.CreateAudioGraphResult
CreateMediaSourceAudioInputNodeResult = _ns_module.CreateMediaSourceAudioInputNodeResult
EchoEffectDefinition = _ns_module.EchoEffectDefinition
EqualizerBand = _ns_module.EqualizerBand
EqualizerEffectDefinition = _ns_module.EqualizerEffectDefinition
FrameInputNodeQuantumStartedEventArgs = _ns_module.FrameInputNodeQuantumStartedEventArgs
LimiterEffectDefinition = _ns_module.LimiterEffectDefinition
MediaSourceAudioInputNode = _ns_module.MediaSourceAudioInputNode
ReverbEffectDefinition = _ns_module.ReverbEffectDefinition
SetDefaultSpatialAudioFormatResult = _ns_module.SetDefaultSpatialAudioFormatResult
SpatialAudioDeviceConfiguration = _ns_module.SpatialAudioDeviceConfiguration
SpatialAudioFormatConfiguration = _ns_module.SpatialAudioFormatConfiguration
SpatialAudioFormatSubtype = _ns_module.SpatialAudioFormatSubtype
IAudioInputNode = _ns_module.IAudioInputNode
IAudioInputNode2 = _ns_module.IAudioInputNode2
IAudioNode = _ns_module.IAudioNode
IAudioNodeWithListener = _ns_module.IAudioNodeWithListener
