from ast import MatchSequence
from activityType import ActivityType
from supply import Supply
from demand import Demand
from task import Task

def checkSupplyDemand(tasks, supplies, demands):
        
    for demand in demands:
        for supply in supplies:
            if (demand.getActivityType() == supply.getActivityType()) and (demand.getSecondsRequired() <= supply.getSecondsAvailable()):
                print("MATCH: ", demand.getName(), " ", supply.getName())
                tasks.append(Task(supply, demand))
                # matches.append([supply, demand])            

    if tasks:
        print("Tasks: ", tasks)

    return tasks 
