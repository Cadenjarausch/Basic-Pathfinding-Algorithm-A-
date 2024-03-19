from NODE import NODE
import math as m

def getNeighbors(nodes, currentPos, closedSet, openSet):
    neighbors = []
    currentNode = nodes[currentPos]
    row = currentNode.row
    col = currentNode.col
    highestRowIndex = nodes[0].totalRows - 1
    highestColumnIndex = nodes[0].totalColumns - 1
    topPos = currentPos - nodes[0].totalColumns
    bottomPos = currentPos + nodes[0].totalColumns
    
    
    #TOP LEFT
    if(row > 0) and (col > 0):
        if(nodes[topPos - 1].isFree):
            neighbors.append(nodes[topPos - 1])
            if (nodes[topPos - 1] not in closedSet and nodes[topPos - 1] not in openSet):
                nodes[topPos - 1].parent = currentNode
                nodes[topPos - 1].lengthToParent = m.sqrt(2) * NODE.length / NODE.discreteLvl
                
    #TOP
    if(row > 0):
        if(nodes[topPos].isFree):
            neighbors.append(nodes[topPos])
            if (nodes[topPos] not in closedSet and nodes[topPos] not in openSet):
                nodes[topPos].parent = currentNode
                nodes[topPos].lengthToParent = NODE.length / NODE.discreteLvl
        
    #TOP RIGHT
    if(col < highestColumnIndex) and (row > 0):
        if (nodes[topPos + 1].isFree):
            neighbors.append(nodes[topPos + 1])
            if (nodes[topPos + 1] not in closedSet and nodes[topPos + 1] not in openSet):
                nodes[topPos + 1].parent = currentNode
                nodes[topPos + 1].lengthToParent = m.sqrt(2) * NODE.length / NODE.discreteLvl
            
    #LEFT
    if(col > 0):
        if(nodes[currentPos - 1].isFree):
            neighbors.append(nodes[currentPos - 1])
            if (nodes[currentPos - 1] not in closedSet and nodes[currentPos - 1] not in openSet):
                nodes[currentPos - 1].parent = currentNode
                nodes[currentPos - 1].lengthToParent = NODE.length / NODE.discreteLvl
            
    #RIGHT
    if(col < highestColumnIndex):
        if(nodes[currentPos + 1].isFree):
            neighbors.append(nodes[currentPos + 1])
            if (nodes[currentPos + 1] not in closedSet and nodes[currentPos + 1] not in openSet):
                nodes[currentPos + 1].parent = currentNode
                nodes[currentPos + 1].lengthToParent = NODE.length / NODE.discreteLvl
            
    #BOTTOM LEFT
    if (col > 0) and (row < highestRowIndex):
        if(nodes[bottomPos - 1].isFree):
            neighbors.append(nodes[bottomPos - 1])
            if (nodes[bottomPos - 1] not in closedSet and nodes[bottomPos - 1] not in openSet):
                nodes[bottomPos - 1].parent = currentNode
                nodes[bottomPos - 1].lengthToParent = m.sqrt(2) * NODE.length / NODE.discreteLvl
            
    #BOTTOM
    if(row < highestRowIndex):
        if(nodes[bottomPos].isFree):
            neighbors.append(nodes[bottomPos])
            if (nodes[bottomPos] not in closedSet and nodes[bottomPos] not in openSet):
                nodes[bottomPos].parent = currentNode
                nodes[bottomPos].lengthToParent = NODE.length / NODE.discreteLvl
            
    #BOTTOM RIGHT
    if(row < highestRowIndex) and (col < highestColumnIndex):
        if(nodes[bottomPos + 1].isFree):
            neighbors.append(nodes[bottomPos + 1])
            if (nodes[bottomPos + 1] not in closedSet and nodes[bottomPos + 1] not in openSet):
                nodes[bottomPos + 1].parent = currentNode
                nodes[bottomPos + 1].lengthToParent = m.sqrt(2) * NODE.length / NODE.discreteLvl
    
    return(neighbors)