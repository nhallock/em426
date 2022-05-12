from cmath import sqrt
import uuid 

from demand import Demand
from supply import Supply
from signal import Signal
import matplotlib as plt

class Agent: 
    
    # Constructor Method
    def __init__(self, name, state, position_x, position_y, agentTime):
        self._name = name
        self._id = uuid.uuid1()
        self._state = state
        self.demands = []
        self.supplies = []
        self._agentTime = agentTime
        self.awareness = []
        self._position_x = position_x
        self._position_y = position_y
    # --- GETTERS AND SETTERS  ---
    # Name
    def getName(self):
        return self._name
    def setName(self, name):
        self._name = name   

    # Id
    def getId(self):
        return self._id
    

    # State
    def getName(self):
        return self._state
    def setName(self, state):
        self._state = state     

    # TODO:
    def createDemand(self, name, activityType, effort, priority, startTime, satisfaction):
        print("Demand ", name, " created by ", self._name)
        d = Demand(name, activityType, effort, priority, startTime, satisfaction)
        self.demands.append(d)
        self.createSignal(d)

    def createSignal(self, demand):
        signal = Signal(demand)
        
    # s = Supply('mySupply', 'eng', 40, 1)
    def createSupply(self, name, activityType, manHours, peopleAvailable):
        print("Supply ", name, " created by ", self._name)
        s = Supply(name, activityType, manHours, peopleAvailable)
        self.supplies.append(s)    


            
    # TODO:
    def executeTask(self, demand):
        startTime = demand._startTime
        print("Task Started")

   # TODO:
    def getDistance(self, object):
        pass
    #    distance = self._positionX
    #    sqrt()