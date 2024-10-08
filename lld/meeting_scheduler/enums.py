from enum import Enum


class EventStatus(Enum):
    SCHEDULED = "SCHEDULED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"

class EventType(Enum):
    ONCE = "ONCE"
    RECURRING = "RECURRING"

class RecurringType(Enum):
    NONE = "NONE"
    EVERY_DAY = "EVERY_DAY"
    EVERY_WEEK = "EVERY_WEEK"
    EVERY_MONTH = "EVERY_MONTH"