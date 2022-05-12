import enum

class AgentMode(enum.Enum):
    INACTIVE = 1, 
    OBSERVING = 2, 
    INTERPRETING = 3, 
    ACTING = 4,
    FINISHING = 5,
    WAITING = 6,
    COMPLETING = 7, 
    PAUSED = 8,
    TIMELIMITED = 9
