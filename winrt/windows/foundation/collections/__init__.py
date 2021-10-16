# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.9.210202.1

import typing, winrt
import enum

_ns_module = winrt._import_ns_module("Windows.Foundation.Collections")

try:
    import winrt.windows.foundation
except:
    pass

class CollectionChange(enum.IntEnum):
    RESET = 0
    ITEM_INSERTED = 1
    ITEM_REMOVED = 2
    ITEM_CHANGED = 3

PropertySet = _ns_module.PropertySet
StringMap = _ns_module.StringMap
ValueSet = _ns_module.ValueSet
IIterable = _ns_module.IIterable
IIterator = _ns_module.IIterator
IKeyValuePair = _ns_module.IKeyValuePair
IMapChangedEventArgs = _ns_module.IMapChangedEventArgs
IMapView = _ns_module.IMapView
IMap = _ns_module.IMap
IObservableMap = _ns_module.IObservableMap
IObservableVector = _ns_module.IObservableVector
IPropertySet = _ns_module.IPropertySet
IVectorChangedEventArgs = _ns_module.IVectorChangedEventArgs
IVectorView = _ns_module.IVectorView
IVector = _ns_module.IVector