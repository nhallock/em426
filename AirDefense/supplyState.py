import enum

class DemandState(enum.Enum):
    INACTIVE = 1, 
    UNAVAILABLE = 2, 
    AVAILABLE = 3,
    ACTIVE = 4,
