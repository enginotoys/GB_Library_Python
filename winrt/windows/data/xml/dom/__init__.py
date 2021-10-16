# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.9.210202.1

import typing, winrt
import enum

_ns_module = winrt._import_ns_module("Windows.Data.Xml.Dom")

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

try:
    import winrt.windows.storage.streams
except:
    pass

class NodeType(enum.IntEnum):
    INVALID = 0
    ELEMENT_NODE = 1
    ATTRIBUTE_NODE = 2
    TEXT_NODE = 3
    DATA_SECTION_NODE = 4
    ENTITY_REFERENCE_NODE = 5
    ENTITY_NODE = 6
    PROCESSING_INSTRUCTION_NODE = 7
    COMMENT_NODE = 8
    DOCUMENT_NODE = 9
    DOCUMENT_TYPE_NODE = 10
    DOCUMENT_FRAGMENT_NODE = 11
    NOTATION_NODE = 12

DtdEntity = _ns_module.DtdEntity
DtdNotation = _ns_module.DtdNotation
XmlAttribute = _ns_module.XmlAttribute
XmlCDataSection = _ns_module.XmlCDataSection
XmlComment = _ns_module.XmlComment
XmlDocument = _ns_module.XmlDocument
XmlDocumentFragment = _ns_module.XmlDocumentFragment
XmlDocumentType = _ns_module.XmlDocumentType
XmlDomImplementation = _ns_module.XmlDomImplementation
XmlElement = _ns_module.XmlElement
XmlEntityReference = _ns_module.XmlEntityReference
XmlLoadSettings = _ns_module.XmlLoadSettings
XmlNamedNodeMap = _ns_module.XmlNamedNodeMap
XmlNodeList = _ns_module.XmlNodeList
XmlProcessingInstruction = _ns_module.XmlProcessingInstruction
XmlText = _ns_module.XmlText
IXmlCharacterData = _ns_module.IXmlCharacterData
IXmlNode = _ns_module.IXmlNode
IXmlNodeSelector = _ns_module.IXmlNodeSelector
IXmlNodeSerializer = _ns_module.IXmlNodeSerializer
IXmlText = _ns_module.IXmlText