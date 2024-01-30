from colorama import init, Fore
init(convert=True)
import numpy as np
import random as r

def createStartEnd(nodes, obstacleLocs):
    
    startPoint = r.randint(0,len(nodes) - 1)
    endPoint = r.randint(0,len(nodes) - 1)
    
    #Checks to see if the chosen start/end points lie on an obstacle
    while (startPoint in obstacleLocs):
        startPoint = r.randint(0,len(nodes) - 1)
    while (endPoint in obstacleLocs):
        endPoint = r.randint(0,len(nodes) - 1)

    return(startPoint,endPoint)