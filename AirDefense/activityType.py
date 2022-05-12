import enum

class ActivityType(enum.Enum):
    REPORTING = 1, 
    DECONFLICTING = 2,
    COMMANDING = 3,
    ORDERS = 4