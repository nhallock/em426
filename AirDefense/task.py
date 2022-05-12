from demand import Demand
from supply import Supply
from agent import Agent


class Task: 
    
    # Constructor Method
    def __init__(self, supply, demand):
        self._name = (supply.getName() + " & " + demand.getName())
        self._demand = demand
        self._supply = supply

    def getName(self):
        return self._name
    def setName(self, name):
        self._name = name   



        
