from demand import Demand
from supply import Supply
import uuid

class Signal:
    
    # Constructor Method
    def __init__(self, demand):
        self._name = demand._name
        self._id = uuid.uuid1()
        self._activityType = demand._activityType
        self._effort = demand._effort
        self._priority = demand._priority
        self._startTime = demand._startTime
        self._satisfaction = demand._satisfaction
        print("Signal Created: ", self._id)

