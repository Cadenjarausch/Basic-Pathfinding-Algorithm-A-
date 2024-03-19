from NODE import NODE
import numpy as np
import random as r

def createObstacles(numObstacles,nodes):
    
    (obstacleLocs) = []
    
    for x in range(numObstacles): #For as many obstacles as chosen
        obstacleTopLeft = r.randint(0, (len(nodes) - 1))
        obstacleLen = r.randint(2,3)
        obstacleHeight = r.randint(2,3)
        
        newObstacleLoc = obstacleTopLeft
        (obstacleLocs).append(newObstacleLoc)
        
        for y in range (obstacleLen): #For as long as the obstacle is

            for z in range (obstacleHeight - 1): #For as tall as the obstacle is (Accounts for if height is one (Obstacle already in list))
            
                if ((nodes[newObstacleLoc].row != (nodes[newObstacleLoc].totalRows - 1))): #If the obstacle is not in the bottom row and obstacle height greater than 1
                    newObstacleLoc = newObstacleLoc + nodes[newObstacleLoc].totalRows #Go one row down
                    
                    (obstacleLocs).append(newObstacleLoc) #Add the obstacle to the list
                else:
                    z = (obstacleHeight + 2) #End height for loop
            
            #If the obstacle is not in the rightmost column with length greater than 1
            if ((nodes[newObstacleLoc].col != (nodes[newObstacleLoc].totalRows - 1)) & (obstacleLen > (y + 1))):
                newObstacleLoc = obstacleTopLeft + y + 1
                (obstacleLocs).append(newObstacleLoc)
                y += 1
            else:
                break
            
    for obstacle in obstacleLocs:
        nodes[obstacle].isFree = 0
            
    return(obstacleLocs)