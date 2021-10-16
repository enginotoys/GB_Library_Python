# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.9.210202.1

import typing, winrt
import enum

_ns_module = winrt._import_ns_module("Windows.Web.Syndication")

try:
    import winrt.windows.data.xml.dom
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
    import winrt.windows.security.credentials
except:
    pass

class SyndicationErrorStatus(enum.IntEnum):
    UNKNOWN = 0
    MISSING_REQUIRED_ELEMENT = 1
    MISSING_REQUIRED_ATTRIBUTE = 2
    INVALID_XML = 3
    UNEXPECTED_CONTENT = 4
    UNSUPPORTED_FORMAT = 5

class SyndicationFormat(enum.IntEnum):
    ATOM10 = 0
    RSS20 = 1
    RSS10 = 2
    RSS092 = 3
    RSS091 = 4
    ATOM03 = 5

class SyndicationTextType(enum.IntEnum):
    TEXT = 0
    HTML = 1
    XHTML = 2

RetrievalProgress = _ns_module.RetrievalProgress
TransferProgress = _ns_module.TransferProgress
SyndicationAttribute = _ns_module.SyndicationAttribute
SyndicationCategory = _ns_module.SyndicationCategory
SyndicationClient = _ns_module.SyndicationClient
SyndicationContent = _ns_module.SyndicationContent
SyndicationError = _ns_module.SyndicationError
SyndicationFeed = _ns_module.SyndicationFeed
SyndicationGenerator = _ns_module.SyndicationGenerator
SyndicationItem = _ns_module.SyndicationItem
SyndicationLink = _ns_module.SyndicationLink
SyndicationNode = _ns_module.SyndicationNode
SyndicationPerson = _ns_module.SyndicationPerson
SyndicationText = _ns_module.SyndicationText
ISyndicationClient = _ns_module.ISyndicationClient
ISyndicationNode = _ns_module.ISyndicationNode
ISyndicationText = _ns_module.ISyndicationText