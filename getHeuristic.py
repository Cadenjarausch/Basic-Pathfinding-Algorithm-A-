import numpy as np
import random as r

def getHeuristic(nodes, endPos, currentPos):
    
    endY = nodes[endPos].row
    endX = nodes[endPos].col

    currentY = nodes[currentPos].row
    currentX = nodes[currentPos].col
    
    heuristic = abs(currentX - endX) + abs(currentY - endY)
    
    return(heuristic)