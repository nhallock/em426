from pickle import FALSE
from demand import Demand
from supply import Supply
# from agent import Agent
from actState import ActState

class Act():
    def __init__(self, agent, supply, demand):
        self._agent = agent
        self._supply = supply
        self._demand = demand
        self._effort = demand.getSecondsRequired()
        self._success = FALSE
        self._end = None

    def GetSet(self, timeStart, agent, supply, demand):
        self._agent = agent
        self._supply = supply
        self._demand = demand
        self._start = timeStart
        self._state = ActState.START
    
    def attempt(self):
        self._supply.attempt(self)


    # --- GETTERS AND SETTERS ---
    def getAgent(self):
        return self._agent
    def setAgent(self, agent):
        self._agent = agent

    def getSupply(self):
        return self._supply
    def setSupply(self, supply):
        self._supply = supply

    def getDemand(self):
        return self._demand
    def setDemand(self, demand):
        self._demand = demand

    def getEffort(self):
        return self._effort
    def setEffort(self, effort):
        self._effort = effort

    def getStart(self):
        return self._start
    def setStart(self, start):
        self._start = start

    def getState(self):
        return self._state
    def setState(self, state):
        self._state = state
