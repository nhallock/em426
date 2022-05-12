

from demandState import DemandState


class Demand: 
    
    # Constructor Method
    def __init__(self, name, activityType, secondsRequired, startTime):
        self._name = name

        self._activityType = activityType
        self._secondsRequired = secondsRequired
        self._startTime = startTime
        self._stopTime = startTime + secondsRequired

        self._state = DemandState.INACTIVE

    # def __eq__(self, other):
    #     if not isinstance(other, Demand):
    #         return NotImplemented
    #     return self.id == other.id

    # --- GETTERS AND SETTERS  ---
    # Name
    def getName(self):
        return self._name
    def setName(self, name):
        self._name = name 

    def getOwner(self):
        return self._owner
    def setOwner(self, owner):
        self._owner = owner         

    # Activity Type
    def getActivityType(self):
        return self._activityType
    def setActivityType(self, activityType):
        self._activityType = activityType 

    # Seconds Required
    def getSecondsRequired(self):
        return self._secondsRequired
    def setSecondsRequired(self, secondsRequired):
        self._secondsRequired = secondsRequired

    # Start Time
    def getStartTime(self):
        return self._startTime    
    def setStartTime(self, startTime):
        self._startTime = startTime

    # Satisfaction
    def getSatisfaction(self):
        return self._satisfaction    
    def setSatisfaction(self, satisfaction):
        self._satisfaction = satisfaction

    def getState(self):
        return self._state
    def setState(self, state):
        self._state = state

    def getInfo(self):
        return [self._name, 
                self._activityType, 
                self._effort, 
                self._priority, 
                self._startTime,
                self._satisfaction]    

    

