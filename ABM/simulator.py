from glob import glob
from agent import Agent
from agentType import AgentType
from agentMode import AgentMode
from demand import Demand
from supply import Supply
from activityType import ActivityType


class Simulator:
    
    def __init__(self):
        pass
    
        self._globalTime = 0
        self._timeLimit = 600
        self._agents = []
        self._supplies = []
        self._demands = []

        s1 = Supply('supply1', ActivityType.WORK, 20)
        self._supplies.append(s1)

        s2 = Supply('supply2', ActivityType.COMM, 30)
        self._supplies.append(s2)
        print(self._supplies)

        d1 = Demand('demand1', ActivityType.WORK, 20, 20)
        self._demands.append(d1)  

        d2 = Demand('demand2', ActivityType.COMM, 30, 40)
        self._demands.append(d2)   
        print(self._demands)

        a1 = Agent("a1", AgentMode.WAITING, 0, self._supplies, self._demands)
        self._agents.append(a1)

        a2 = Agent("a2", AgentMode.WAITING, 0, self._supplies, self._demands)
        self._agents.append(a2)



    def globalStep(self, agents):
        # find the agent with the earliest agent time

        nextAgent = None

        earliestAgent = agents[0]
        for a in agents:
            # nextAgent=(nextAgent==null || agent.getAgentTime() < nextAgent.getAgentTime()) ? agent : nextAgent;
            if a.getAgentTime() < earliestAgent.getAgentTime():
                nextAgent = a
            else:
                nextAgent = earliestAgent

        self._globalTime = nextAgent.getAgentTime()

        nextAgent.step()  
        return nextAgent

    def run(self):
        while self._globalTime < self._timeLimit:
            self.globalStep(self._agents)
            print("Global Time: ", self._globalTime)

        for a in self._agents:
            print(a.getName(), "Cumlative Work Effort: ", a._effortWorkCumulative)
            print(a.getName(), "Cumlative Comm Effort: ", a._effortCommCumulative)


'''
    def globalStep(self):
        nextAgent = None
        for a in self.agents:
            nextAgent 


    def reset(self):
        globalTime = 0
'''