import createEnvironment
import createStartEnd
import createObstacles
import generateGraphic
import getHeuristic
import getNeighbors
import findOptimalPath

numObstacles = 3
obstacleSizeLim = [5,8]

nodes = createEnvironment.createEnvironment()
obstacleLocs = createObstacles.createObstacles(numObstacles,nodes)
startPoint, endPoint = createStartEnd.createStartEnd(nodes,obstacleLocs)

print("StartPoint: ", startPoint)
print("EndPoint: ", endPoint)

optimalPath = findOptimalPath.findOptimalPath(nodes, startPoint, endPoint, obstacleLocs)
generateGraphic.generateGraphic(startPoint,endPoint,obstacleLocs,nodes,optimalPath)