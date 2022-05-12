from activityType import ActivityType
from agent import Agent
from agentMode import AgentMode
from supply import Supply

class Commander(Agent):
    def __init__(self, name, state, position_x, position_y, agentTime):
        super().__init__(name, state, position_x, position_y, agentTime)

        self.threatPerception = []
        self.civilPerception = []    
        self._supplies = []
        self._demands = []

        self.receiveInfomationSuccess = 0

        self._agentTime = 0
        self._state = AgentMode.WAITING

    def receiveInfomation(self, threatPerception, civilPerception):
        if (self._state == AgentMode.WAITING):
            # print("I GOT THE INFO")
            self._agentTime = self._agentTime + 10
            
            self.civilPerception = civilPerception
            self.threatPerception = threatPerception

            # self._state = AgentMode.INTERPRETING
            self.receiveInformationSuccess = 1
            self._state = AgentMode.WAITING

            print('Commander Received Information')
            # print (self.receiveInformationSuccess)

            cdr_rec_report = Supply(self, "cdr_rec_report", ActivityType.REPORTING, 30)
            self._supplies.append(cdr_rec_report)

            return cdr_rec_report
        else: 
            print('Commander Cannot Receive Information')  
            self.receiveInformationSuccess = 0

        self._state = AgentMode.WAITING    

    def getReceiveInformationSuccess(self):
        return self.receiveInformationSuccess

    def giveOrders(self):
        # give orders to technician to engage
        self._state = AgentMode.ACTING
        self._agentTime = self._agentTime + 10

        cdr_sup_order = Supply(self, "cdr_ord_engage", ActivityType.ORDERS, 30)
        self._supplies.append(cdr_sup_order)

        return cdr_sup_order

    def getAgentTime(self):
        print("Commander Agent Time: ", self._agentTime)
        return self._agentTime

    def getDemands(self):
        return self._demands

    def getSupplies(self):
        return self._supplies 
                    