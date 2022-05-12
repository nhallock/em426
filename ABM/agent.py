from operator import eq
import uuid
from agentMode import AgentMode
from demand import Demand
from demandState import DemandState

from act import Act
from actState import ActState
from activityType import ActivityType

# from signal import Signal
import matplotlib as plt

class Agent: 
    
    # Constructor Method
    def __init__(self, name, mode, agentTime, suppliesQueue, demandsQueue):
        
        pauseEvery = 5
        timeLimt = 500
        
        self._name = name
        self._id = uuid.uuid1()
        self._mode = mode
        
        self.demands = demandsQueue
        self.demandsPending = []
        self.demandsActive = []
        self.demandsMoot = []
        
        self.supplies = suppliesQueue
        self.acts  = []

        self.demandsToRemove = []
        # self.signals = []
        
        self.selectedDemand = None
        self.selectedSupply = None
        self.inProcessAct = None

        self._agentTime = agentTime
        # self.awareness = []

        self._effortWorkCumulative = 0
        self._effortCommCumulative = 0

        # self._position_x = position_x
        # self._position_y = position_y

    # LOOP 
    def agentLoop(self, timeLimit, pauseEvery):
        nextPause = self._agentTime + pauseEvery

        while (self._agentTime <= timeLimit):
            self.step()

            if (nextPause <= self._agentTime and pauseEvery != 0):
                self.mode = AgentMode.PAUSED

        self._mode = AgentMode.TIMELIMITED    
    
    # def start(self, timeLimit, pausePeriod):
    #     self._agentTime = 0
    #     agentLoop(timeLimit, pauseEvery)

    # def continueSim(self, timeLimit, pausePeriod):
    #     self._mode = AgentMode.OBSERVING
    #     agentLoop(timeLimit, pausePeriod)

    
    
    # FROM BRYANS CODE

    # 
    def start(self):
        self.setAgentTime(0)
        # loop(timeLimit.get(), timePausedPeriod.get())


    def reset(self):
        self.setAgentTime(0)
        self.demandsPending = []
        self.demandsActive = []
        self.demandsMoot = []
        acts = []

        self.selectedDemand = None
        self.selectedSupply = None
        self.inProcessAct  = None

        effortWorkCumulative = 0
        effortCommCumulative = 0

        self.mode = AgentMode.INACTIVE

    def step(self):
        if self.getMode() == AgentMode.INACTIVE:
            print(self.getName(), ': INACTIVE')
            self.setMode(AgentMode.OBSERVING)
            return
        
        if self.getMode() == AgentMode.WAITING:
            self.doNothing()
            #print('I am WAITING')
            return

        if self.getMode() == AgentMode.OBSERVING:
            print(self.getName(), ': OBSERVING')
            self.setAgentTime(self.getAgentTime() + 30)
            self.observe()
            return

        if self.getMode() == AgentMode.SELECTING:
            self.setAgentTime(self.getAgentTime() + 30)
            self.select()
            return

             
        if self.getMode() == AgentMode.ACTING:
            print(self.getName(), ': ACTING')
            self.act()
            return
        
        if self.getMode() == AgentMode.COMPLETING:
            print(self.getName(), ':  COMPLETING')
            self.complete()
            return
        
        if self.getMode() == AgentMode.PAUSED:
            print(self.getName(), ':  PAUSED')
            return

    # doNothing()
    def doNothing(self):
        self.setAgentTime(self.getAgentTime() + 30) # 30 seconds
        print(self.getName(), ': DOING NOTHING')
        self.setMode(AgentMode.OBSERVING)

    def observe(self):
        for d in self.demands:
            print(self.getName(), ": LOOKING AT DEMANDS")
            # if d is not currently in dP, dA, or dM
            if (self.demandsPending.count(d) == 0  and
                self.demandsActive.count(d) == 0 and 
                self.demandsMoot.count(d) == 0):

                self.demandsPending.append(d) # add demand to the dP array
                d.setState(DemandState.PENDING) # set the state of the demand to pending
                print(self.getName(), ": SET THE DEMAND STATE TO PENDING")
                break


        if (len(self.demandsPending) == 0 and 
            len(self.demandsActive) == 0):
            self.setMode(AgentMode.WAITING)
            return

        self.setAgentTime(self.getAgentTime() + 30)
        self.setMode(AgentMode.SELECTING)

    def select(self):
        self.retV = None
        print(self.getName(), ": SELECTING")
        self.selectedDemand = None   
        self.demandsToRemove = [] # demandsToRemove.clear
        print(self.getName(), " supplies: ", self.supplies)
        #Demands Active Loop
        # start with our currently active demands
        for d in self.demandsActive: 
            for s in self.supplies:
                if self.isMatch(s,d):    
                    self.setSelectedDemand(d)
                    print(self.getName(), ": SELECTED A DEMAND")
                    self.setSelectedSupply(s) 
                    print(self.getName(), ": SELECTED A SUPPLY")
                    self.retV = AgentMode.ACTING
                    #self.setMode(AgentMode.ACTING)
                    break
                else:
                    print(self.getName(), ": IF I MADE IT HERE, NO SUPPLIES FIT")            
                    self.demandsMoot.append(d)
                    self.demandsToRemove.append(d)

        # demandsActive.removeAll(demandstoRemove)
        if len(self.demandsActive) > 0 and len(self.demandsToRemove) > 0:
            print('*** MADE IT TO REMOVAL***')
            print("Demands Active: ", self.demandsActive)
            print("Demands Moot: ", self.demandsMoot)
            print("Demands to Remove: ", self.demandsToRemove)

        
            for dA in self.demandsActive:
                for dTR in self.demandsToRemove:
                    if (len(self.demandsActive) > 0) and dA.getName() == dTR.getName():
                        self.demandsActive.remove(dA)

        
        if self.retV: 
            self.setMode(self.retV)
            return

        # if we got this far, none of our existing supplies and demands match
		# move on to pending

        self.demandsToRemove = [] # demandsToRemove.clear()

        # Demands Pending Loop
        for d in self.demandsPending:
            for s in self.supplies:
                print(self.getName(), ": IN THE DP LOOP")
                if self.isMatch(s,d):
                    print(self.getName(), ": QUICK CHECK: MATCH")
                    self.setSelectedDemand(d)
                    self.setSelectedSupply(s)
                    d.setState(DemandState.ACTIVE)
                    
                    self.demandsActive.append(d)
                    self.demandsToRemove.append(d)
                    self.retV = AgentMode.ACTING
                    break
                else:
                    self.demandsMoot.append(d)
                    self.demandsToRemove.append(d) # doubles up here

        # if self.demandsPending.count(self.demandsToRemove):
        if len(self.demandsPending) > 0 and len(self.demandsToRemove) > 0:
            for dP in self.demandsPending:
                for dTR in self.demandsToRemove:
                    if (len(self.demandsPending) > 0) and (dP.getName() == dTR.getName()):
                        self.demandsPending.remove(dP)

        self.setMode(AgentMode.OBSERVING)
        return 

    def act(self):
        a = Act(self, self.selectedSupply, self.selectedDemand)
        a.GetSet(self.getAgentTime(), self, self.getSelectedSupply(), self.getSelectedDemand())   # write getSelectedSupply() and getSelectedDemand()
        self.inProcessAct = a
        self.acts.append(a)

        a.attempt() # NEED TO WRITE attempt()
        self._agentTime = a.end   # NEED TO WRITE end

        if a._demand.getActivityType() == ActivityType.WORK: # need to write getActivityType for demand
            self._effortWorkCumulative += a.getEffort()  # need to write a.getEffort()
        
        if a._demand.getActivityType() == ActivityType.COMM:
            self._effortCommCumulative += a.getEffort()

        if (self.selectedDemand.getSecondsRequired() == 0):
            self.setMode(AgentMode.COMPLETING)
        else:
            self.setMode(AgentMode.ACTING)

    def complete(self):
        # self.demandsActive.remove(self.getSelectedDemand())
        for dA in self.demandsActive:
            for dTR in self.demandsToRemove:
                if (len(self.demandsActive) > 0) and (dA.getName() == dTR.getName()):
                    self.demandsActive.remove(dTR)

        self.demandsMoot.append(self.getSelectedDemand())
        self.getSelectedDemand().setState(DemandState.COMPLETE)
        self.setSelectedDemand(None)
        self.setSelectedSupply(None) 
        self.inProcessAct = None

        self.setMode(AgentMode.OBSERVING)

    def isMatch(self, s, d):
        if (s.getActivityType() == d.getActivityType() and 
            s.getSecondsAvailable() <= d.getSecondsRequired()):
            match = 1
        else: 
            match = 0          
        return match

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
    def getMode(self):
        return self._mode
    def setMode(self, mode):
        self._mode = mode     

    # Agent Time
    def getAgentTime(self):
        return self._agentTime
    def setAgentTime(self, agentTime):
        self._agentTime = agentTime 
       
    # #
    def getSelectedSupply(self):
        return self.selectedSupply
    def setSelectedSupply(self, selectedSupply):
        self.selectedSupply =   selectedSupply 

    def getSelectedDemand(self):
        return self.selectedDemand
    def setSelectedDemand(self, selectedDemand):
        self.selectedDemand =   selectedDemand

# TODO
'''
    def commit():
        pass

    def terminate():
        pass
'''

    

