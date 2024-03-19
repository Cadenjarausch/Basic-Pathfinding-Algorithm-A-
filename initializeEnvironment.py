import random as r
from NODE import NODE

#Environment is a matrix of 1's (if nodes are free) and 0's (is nodes are obstacles)
def initializeEnvironment(environment):
    createdColumns = 0
    
    nodes = []
    
    while createdColumns < NODE.totalColumns:
        createdRows = 0
        while createdRows < NODE.totalRows:
            posNum = createdRows + (NODE.totalRows * createdColumns)
            newNode = NODE(createdRows, createdColumns, posNum, environment[createdColumns][createdRows])
            nodes.append(newNode)
            createdRows += 1
        createdColumns += 1

    return(nodes)