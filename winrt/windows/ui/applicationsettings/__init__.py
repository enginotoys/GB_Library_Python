# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.9.210202.1

import typing, winrt
import enum

_ns_module = winrt._import_ns_module("Windows.UI.ApplicationSettings")

try:
    import winrt.windows.foundation
except:
    pass

try:
    import winrt.windows.foundation.collections
except:
    pass

try:
    import winrt.windows.security.credentials
except:
    pass

try:
    import winrt.windows.system
except:
    pass

try:
    import winrt.windows.ui.popups
except:
    pass

class SupportedWebAccountActions(enum.IntFlag):
    NONE = 0
    RECONNECT = 0x1
    REMOVE = 0x2
    VIEW_DETAILS = 0x4
    MANAGE = 0x8
    MORE = 0x10

class WebAccountAction(enum.IntEnum):
    RECONNECT = 0
    REMOVE = 1
    VIEW_DETAILS = 2
    MANAGE = 3
    MORE = 4

AccountsSettingsPane = _ns_module.AccountsSettingsPane
AccountsSettingsPaneCommandsRequestedEventArgs = _ns_module.AccountsSettingsPaneCommandsRequestedEventArgs
AccountsSettingsPaneEventDeferral = _ns_module.AccountsSettingsPaneEventDeferral
CredentialCommand = _ns_module.CredentialCommand
SettingsCommand = _ns_module.SettingsCommand
WebAccountCommand = _ns_module.WebAccountCommand
WebAccountInvokedArgs = _ns_module.WebAccountInvokedArgs
WebAccountProviderCommand = _ns_module.WebAccountProviderCommand