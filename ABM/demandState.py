import enum

class DemandState(enum.Enum):
    INACTIVE = 1, 
    PENDING = 2, 
    STARTING = 3,
    ACTIVE = 4,
    COMPLETE = 5,
    DONE = 6,
    IGNORED = 7