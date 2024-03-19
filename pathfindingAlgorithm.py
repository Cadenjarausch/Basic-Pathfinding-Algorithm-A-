from createEnvironment import createEnvironment
from createStartEnd import createStartEnd
from createObstacles import createObstacles
from generateGraphic import generateGraphic
from initializeEnvironment import initializeEnvironment
from NODE import NODE
from aStar import aStar

#numObstacles only to be used when generating random environment
numObstacles = 5

#Start and End Point as determined by the user (or randomized in createStartEnd)
startPoint = 0
endPoint = 24

#Input environment (for testing initializeEnvironment)
environment = [[1,1,1,1,1],[1,0,0,1,0],[1,0,0,1,0],[1,0,0,1,0],[1,1,1,1,1]]
#environment = [[1,1,1,1,1],[1,0,0,1,0],[1,0,0,1,0],[1,0,0,1,0],[1,1,1,1,1],[1,0,0,1,0],[1,0,0,1,0],[1,0,0,1,0],[1,1,1,1,1]]

#Pass in environemnt matrix of 1's (if free) and 0's (if obstacles)
nodes = initializeEnvironment(environment)

#Generate a random environment with numObstacle many obstacles
#nodes = createEnvironment()
#obstacleLocs = createObstacles(numObstacles,nodes)

#Make Startpoint and Endpoint
startPoint, endPoint = createStartEnd(nodes)

#print(startPoint, endPoint)

#aStar algorithm used to find optimal path in passed in or random environment
optimalPath,openSet = aStar(startPoint, endPoint, nodes)

#Output results to terminal
generateGraphic(startPoint,endPoint,nodes,optimalPath,openSet)