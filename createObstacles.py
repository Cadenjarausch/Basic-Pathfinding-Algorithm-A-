import numpy as np
import random as r

def createObstacles(numObstacles,nodes):
    
    (obstacleLocs) = []
    
    for x in range(numObstacles):
        newObstacleLoc = r.randint(0, (len(nodes) - 1))     
        (obstacleLocs).append(newObstacleLoc)
        
        for obj in nodes:
            if (obj.posNum == (obstacleLocs)[x]):
                obj.makeObstacle()
            
    return(obstacleLocs)