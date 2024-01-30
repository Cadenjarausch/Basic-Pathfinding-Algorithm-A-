import random as r
import numpy as np

def createEnvironment():
    j = 0
    i = 0
#    lowerbound = 5
#    upperbound = 10
#    size = r.randint(lowerbound, upperbound)
    size = 100
    width = size
    height = size
    
    nodes = []
    
    while i < width:
        j = 0
        while j < height:
            posNum = j + (NODE.totalRows * i)
            newNode = NODE(j, i, posNum)
            nodes.append(newNode)
            j += 1
        i += 1
    
    return(nodes)


WHITE = (255, 255, 255)
RED = (255, 0, 0)
TURQUOISE = (64, 224, 208)

class NODE():
    totalRows = 100
    def __init__(self, col, row, posNum):
        self.color = WHITE
        self.row = row
        self.col = col
        self.posNum = posNum
        
    def makeObstacle(self):
        self.color = RED