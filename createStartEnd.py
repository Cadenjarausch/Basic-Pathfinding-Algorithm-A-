from NODE import NODE
import random as r

def createStartEnd(nodes):
    
    #Start and End Point in Environment
    startPoint = nodes[r.randint(0,len(nodes) - 1)]
    endPoint = nodes[r.randint(0,len(nodes) - 1)]
    
    #Checks to see if the chosen start/end points lie on an obstacle
    while ((not startPoint.isFree) or (startPoint == endPoint)):
        startPoint = nodes[r.randint(0,len(nodes) - 1)]
    while (not endPoint.isFree or (endPoint == startPoint)):
        endPoint = nodes[r.randint(0,len(nodes) - 1)]

    return(startPoint.posNum, endPoint.posNum)