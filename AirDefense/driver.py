
from unicodedata import name
from click import command
from demand import Demand
from checkSupplyDemand import checkSupplyDemand
from plotTechnicianPerception import plotTechnicianPerception
from supply import Supply
from signal import Signal 

from agent import Agent
from agentType import AgentType

from activityType import ActivityType
from agentMode import AgentMode

from airTrack import AirTrack
from airTrackTypes import AirTrackTypes

from tehnician import Technician
from commander import Commander
from coordinator import Coordinator

from task import Task

import matplotlib.pyplot as plt

# Initialize arrays needed
demands = []
supplies = []
agents = []
matches = []
tasks = []

# Run simulation for one hour
# Tasks are on the order of seconds
timeLimit = 3600 

# Create Blue Assets 
technicianRadius = 200
technicianPosition = [0, 0] 
technician = Technician(AgentType.TECHNICIAN, AgentMode.OBSERVING, technicianPosition[0], technicianPosition[1], 0)
fieldOfView = technician.fieldOfView(technicianRadius)

coordinatorPosition = [5,5]
coordinator = Coordinator(AgentType.COORDINATOR, AgentMode.OBSERVING, coordinatorPosition[0], coordinatorPosition[1], 0)

commanderPosition = [1,1]
commander = Commander(AgentType.COMMANDER, AgentMode.OBSERVING, commanderPosition[0], commanderPosition[1], 0)

# Create world air tracks
threat = AirTrack("missile", AirTrackTypes.THREAT, 0, 190, 180, 20)
commercialFlight = AirTrack("pax jet", AirTrackTypes.CIVILIAN, 75, 120, 45, 15)
commercialFlight2 = AirTrack("pax jet 2", AirTrackTypes.CIVILIAN, 275, 220, 45, 15)



blueAssets = [coordinator, commander]
worldAssets = [threat, commercialFlight,  commercialFlight2]

# Initialize technician perception
technicianFieldOfView = technician.fieldOfView(technicianRadius)
technician.threatPerception, technician.civilPerception = technician.checkFieldOfView(technicianRadius, worldAssets)

# If the technician perceives any threats in the world
if technician.threatPerception:
    
    # Output technician perception to console
    for track in technician.threatPerception:
        print("The tech sees ", track._name, " as threat")

    # Flow the information to the blueAssets (in this case, coordinator and commander)
    # this creates a demand
    techSendInfo = technician.sendInformationUp(blueAssets)
    demands.append(techSendInfo)

    # coordinator receives information
    # this creates a supply
    coord_rec_report = coordinator.receiveInfomation(technician.threatPerception, technician.civilPerception)
    supplies.append(coord_rec_report)

    # commander receives information
    # this creates a supply
    cdr_rec_report = commander.receiveInfomation(technician.threatPerception, technician.civilPerception)
    supplies.append(cdr_rec_report)

    # print("did cdr get info: ", commander.getReceiveInformationSuccess())
    # print("tech gt: ", technician.getGlobalTime())

    if coordinator.receiveInformationSuccess:
        for track in coordinator.threatPerception:
            print("Coordinator is now aware of ", track._name)
            coordinator.getAgentTime()

        demands.append(coordinator.interpretInformation())    
        coordinator.getAgentTime()

    if commander.receiveInformationSuccess:
        for track in commander.threatPerception:
            print("Commander is now aware of ", track._name)
            commander.getAgentTime()
            
            demands.append(technician.requestOrders())
            supplies.append(commander.giveOrders())

    else: 
        print('Commander cannot receive')

technician.getAgentTime()
coordinator.getAgentTime()
commander.getAgentTime()

for demand in demands:
    print("Demand: ", demand.getOwner() ,demand.getName(), demand.getActivityType(), demand.getSecondsRequired())

for supply in supplies:
    print("Supply: ", supply.getOwner(), supply.getName(), supply.getActivityType(), supply.getSecondsAvailable())

# this should not exist
tasks = checkSupplyDemand(tasks, supplies, demands)

print("NumTasks: ", len(tasks))
print("Tasks: ", tasks)


print("TECH Supplies: ", technician.getSupplies())
print("TECH Demands: ", technician.getDemands())

print("COO Supplies: ", coordinator.getSupplies())
print("COO Demands: ", coordinator.getDemands())

print("CDR Supplies: ", commander.getSupplies())
print("CDR Demands: ", commander.getDemands())

# Run through the tasks
# Exectue the task
    # Advance time
    # subtract demand.secondsRequired from supply.secondsAvailable
    # change demand satisfaction to complete
    # remove supply and demand from queue


# # VERIFY WHAT THE TECHNICIAN SEES
# for track in technician.threatPerception:
#     print("The tech sees ", track._name, " as threat")

# for track in technician.civilPerception:
#     print("The tech sees ", track._name, " as friendly")

plotTechnicianPerception(technician.threatPerception, technician.civilPerception, blueAssets, technicianFieldOfView)

