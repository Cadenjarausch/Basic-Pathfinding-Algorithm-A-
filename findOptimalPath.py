import numpy as np
import getNeighbors
import getHeuristic

def findOptimalPath(nodes, startPoint, endPoint, obstacleLocs):
    currentQueue = []
    shortestPath = [startPoint]
    nextStep = startPoint
    lowestHeuristic = getHeuristic.getHeuristic(nodes, endPoint, startPoint)
    
    while (shortestPath[-1] != endPoint):
        currentNode = nextStep
        currentQueue = getNeighbors.getNeighbors(nodes, currentNode, obstacleLocs)
        for obj in currentQueue:
            newHeuristic = getHeuristic.getHeuristic(nodes, endPoint, obj.posNum)
        
            if (newHeuristic < lowestHeuristic):
                lowestHeuristic = newHeuristic
                nextStep = obj.posNum
    
        shortestPath.append(nextStep)
    
    print("Shortest Path: ", shortestPath)
    
    for x in shortestPath:
        nodes[x].color = (64, 224, 208)
    
    return(shortestPath)