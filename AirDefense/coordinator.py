from argparse import Action
from activityType import ActivityType
from agent import Agent
from agentMode import AgentMode
from supply import Supply
from demand import Demand
from airTrack import AirTrack

class Coordinator(Agent):
    def __init__(self, name, state, position_x, position_y, agentTime):
        super().__init__(name, state, position_x, position_y, agentTime)

        self.threatPerception = []
        self.civilPerception = []
        self._state = AgentMode.WAITING
        self._supplies = []
        self._demands = []

        self.receiveInfomationSuccess = 0


    def receiveInfomation(self, threatPerception, civilPerception):
        if (self._state == AgentMode.WAITING):
            self._agentTime = self._agentTime + 10
            
            self.civilPerception = civilPerception
            self.threatPerception = threatPerception

            print('Coordinator Received Information')
            self.receiveInformationSuccess = 1
            # self._state = AgentMode.INTERPRETING
            coord_rec_report = Supply(self, "coord_rec_report", ActivityType.REPORTING, 30)
            self._supplies.append(coord_rec_report)

            return coord_rec_report

        else: 
            print('Coordinator Cannot Receive Information')  
            self.receiveInformationSuccess = 0

    def interpretInformation(self):
        self._state = AgentMode.INTERPRETING
        self._agentTime = self._agentTime + 20

        # check if the coordinator knows about any threats
        if self.threatPerception and self.civilPerception:
            self._state = AgentMode.ACTING
            self._agentTime = self._agentTime + 2
            
            coord_req_orders = Demand(self, "coord_req_decon", ActivityType.ORDERS, 10, 0, 0)
            self._demands.append(coord_req_orders)
            
            #print("CLEAR THE AIRSPACE")

            # divert the civil air tracks
            for track in self.civilPerception:
                track.divert()
                self._agentTime = self._agentTime + 5

            self._state = AgentMode.WAITING    

        return coord_req_orders

    def getAgentTime(self):
        print("Coordinator Agent Time: ", self._agentTime)
        return self._agentTime

    def getDemands(self):
        return self._demands

    def getSupplies(self):
        return self._supplies 

    