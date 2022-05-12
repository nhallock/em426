class Supply: 
    
    # Constructor Method
    def __init__(self, owner, name, activityType, secondsAvailable):
        self._name = name
        self._owner = owner
        
        self._activityType = activityType
        self._secondsAvailable = secondsAvailable


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
    





