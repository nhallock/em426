from activityType import ActivityType
from agent import Agent
import matplotlib.pyplot as plt
from agentMode import AgentMode

from airTrackTypes import AirTrackTypes
from demand import Demand

class Technician(Agent):
    def __init__(self, name, state, position_x, position_y, agentTime):
        super().__init__(name, state, position_x, position_y, agentTime)
        self._globalTime = 0
        self.threatPerception = []
        self.civilPerception = []
        self._supplies = []
        self._demands = []

    def fieldOfView(self, radius):
        fieldOfView = plt.Circle((self._position_x, self._position_y), radius, fill=False)
        return fieldOfView

    def checkFieldOfView(self, fieldOfViewRadius, worldAssets):
        self._agentTime = self._agentTime + 30
        self._state = AgentMode.ACTING
        for track in worldAssets:
            if (((track._position_x - self._position_x)^2) + ((track._position_y - self._position_y)^2) < (fieldOfViewRadius^2)):
                print(track._name, " is INSIDE FOV")
                
                if (track._type == AirTrackTypes.THREAT):
                    self.threatPerception.append(track)

                else: self.civilPerception.append(track)
            
            else:
                print(track._name, "is OUTSIDE FOV")    

        self._state = AgentMode.OBSERVING
        return self.threatPerception, self.civilPerception

    # def sendInformationUp(self, previousTime):
    def sendInformationUp(self, blueAssets):
        self._state = AgentMode.ACTING
        self._agentTime = self._agentTime + 30

        tech_req_send = Demand(self, 'tech_req_send', ActivityType.REPORTING, 30, 0, 0)
        self._demands.append(tech_req_send)

        self._state = AgentMode.OBSERVING
        return tech_req_send

    def getPerception(self):
        for i in self.threatPerception:
            print(i._name)

    def requestOrders(self):
        self._state = AgentMode.OBSERVING
        self._agentTime = self._agentTime + 10
        print("technician has requested orders")

        # Create demand for orders
        tech_req_orders = Demand(self, 'tech_req_orders', ActivityType.ORDERS, 20, 0, 0)
        self._demands.append(tech_req_orders)
        return tech_req_orders

    def receiveOrders(self, orders):
        pass

    def getAgentTime(self):
        print("Technician Agent Time: ", self._agentTime)
        return self._agentTime
        
    def getDemands(self):
        return self._demands

    def getSupplies(self):
        return self._supplies    