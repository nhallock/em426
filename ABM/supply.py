from actState import ActState
from demand import Demand


class Supply: 
    
    # Constructor Method
    def __init__(self, name, activityType, secondsAvailable):
        self._name = name
       
        self._activityType = activityType
        self._secondsAvailable = secondsAvailable
    
    # TODO:
    def attempt(self, act):
        d = act._demand

        if ~(Supply.isMatch(self, d)):
            act._success = False
            act.setState(ActState.START)

        actualEffortRemaining = d.getSecondsRequired()

        if actualEffortRemaining > self._secondsAvailable:
            act._effort = self.getSecondsAvailable()
            d.setEffort(d.getEffort() - act._effort)

        else:
            act._effort = actualEffortRemaining
            d.setSecondsRequired(0)

        act.end = act._start + act._effort
        act.success = True
        act.setState(ActState.COMPLETE)
        return
        
    def isMatch(self, demand):
        return (self.getActivityType() == demand.getActivityType())    
    # --- GETTERS AND SETTERS  ---
    # Name
    def getName(self):
        return self._name
    def setName(self, name):
        self._name = name    

    def getOwner(self):
        return self._owner
    def setName(self, owner):
        self._owner = owner   


    # Activity Type
    def getActivityType(self):
        return self._activityType
    def setActivityType(self, activityType):
        self._activityType = activityType 

    # ManHours
    def getSecondsAvailable(self):
        return self._secondsAvailable
    def setSecondsAvailable(self, secondsAvailable):
        self._secondsAvailable = secondsAvailable

    def getInfo(self):
        return [self._name, 
                self._activityType, 
                self._secondsAvailable]    

    # def isMatch(demand):
    #     pass
    





