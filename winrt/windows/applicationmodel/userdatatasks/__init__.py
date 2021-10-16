# WARNING: Please don't edit this file. It was generated by Python/WinRT v0.9.210202.1

import typing, winrt
import enum

_ns_module = winrt._import_ns_module("Windows.ApplicationModel.UserDataTasks")

try:
    import winrt.windows.foundation
except:
    pass

try:
    import winrt.windows.foundation.collections
except:
    pass

try:
    import winrt.windows.system
except:
    pass

class UserDataTaskDaysOfWeek(enum.IntFlag):
    NONE = 0
    SUNDAY = 0x1
    MONDAY = 0x2
    TUESDAY = 0x4
    WEDNESDAY = 0x8
    THURSDAY = 0x10
    FRIDAY = 0x20
    SATURDAY = 0x40

class UserDataTaskDetailsKind(enum.IntEnum):
    PLAIN_TEXT = 0
    HTML = 1

class UserDataTaskKind(enum.IntEnum):
    SINGLE = 0
    RECURRING = 1
    REGENERATING = 2

class UserDataTaskListOtherAppReadAccess(enum.IntEnum):
    FULL = 0
    SYSTEM_ONLY = 1
    NONE = 2

class UserDataTaskListOtherAppWriteAccess(enum.IntEnum):
    LIMITED = 0
    NONE = 1

class UserDataTaskListSyncStatus(enum.IntEnum):
    IDLE = 0
    SYNCING = 1
    UP_TO_DATE = 2
    AUTHENTICATION_ERROR = 3
    POLICY_ERROR = 4
    UNKNOWN_ERROR = 5

class UserDataTaskPriority(enum.IntEnum):
    NORMAL = 0
    LOW = -1
    HIGH = 1

class UserDataTaskQueryKind(enum.IntEnum):
    ALL = 0
    INCOMPLETE = 1
    COMPLETE = 2

class UserDataTaskQuerySortProperty(enum.IntEnum):
    DUE_DATE = 0

class UserDataTaskRecurrenceUnit(enum.IntEnum):
    DAILY = 0
    WEEKLY = 1
    MONTHLY = 2
    MONTHLY_ON_DAY = 3
    YEARLY = 4
    YEARLY_ON_DAY = 5

class UserDataTaskRegenerationUnit(enum.IntEnum):
    DAILY = 0
    WEEKLY = 1
    MONTHLY = 2
    YEARLY = 4

class UserDataTaskSensitivity(enum.IntEnum):
    PUBLIC = 0
    PRIVATE = 1

class UserDataTaskStoreAccessType(enum.IntEnum):
    APP_TASKS_READ_WRITE = 0
    ALL_TASKS_LIMITED_READ_WRITE = 1

class UserDataTaskWeekOfMonth(enum.IntEnum):
    FIRST = 0
    SECOND = 1
    THIRD = 2
    FOURTH = 3
    LAST = 4

UserDataTask = _ns_module.UserDataTask
UserDataTaskBatch = _ns_module.UserDataTaskBatch
UserDataTaskList = _ns_module.UserDataTaskList
UserDataTaskListLimitedWriteOperations = _ns_module.UserDataTaskListLimitedWriteOperations
UserDataTaskListSyncManager = _ns_module.UserDataTaskListSyncManager
UserDataTaskManager = _ns_module.UserDataTaskManager
UserDataTaskQueryOptions = _ns_module.UserDataTaskQueryOptions
UserDataTaskReader = _ns_module.UserDataTaskReader
UserDataTaskRecurrenceProperties = _ns_module.UserDataTaskRecurrenceProperties
UserDataTaskRegenerationProperties = _ns_module.UserDataTaskRegenerationProperties
UserDataTaskStore = _ns_module.UserDataTaskStore
