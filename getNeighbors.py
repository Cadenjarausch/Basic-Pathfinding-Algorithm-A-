def getNeighbors(nodes, currentPos, obstacleLocs):
    neighbors = []
    row = nodes[currentPos].row
    col = nodes[currentPos].col
    highestRowIndex = nodes[0].totalRows - 1
    topPos = currentPos - nodes[0].totalRows
    bottomPos = currentPos + nodes[0].totalRows
    
    
    #TOP LEFT
    if(row > 0) and (col > 0):
        if(nodes[topPos - 1].posNum not in obstacleLocs):
            neighbors.append(nodes[topPos - 1])
                
    #TOP
    if(row > 0):
        if(nodes[topPos].posNum not in obstacleLocs):
            neighbors.append(nodes[topPos])
        
    #TOP RIGHT
    if(col < highestRowIndex) and (row > 0):
        if (nodes[topPos + 1].posNum not in obstacleLocs):
            neighbors.append(nodes[topPos + 1])
            
    #LEFT
    if(col > 0):
        if(nodes[currentPos - 1].posNum not in obstacleLocs):
            neighbors.append(nodes[currentPos - 1])
            
    #RIGHT
    if(col < highestRowIndex):
        if(nodes[currentPos + 1].posNum not in obstacleLocs):
            neighbors.append(nodes[currentPos + 1])
            
    #BOTTOM LEFT
    if (col > 0) and (row < highestRowIndex):
        if(nodes[bottomPos - 1].posNum not in obstacleLocs):
            neighbors.append(nodes[bottomPos - 1])
            
    #BOTTOM
    if(row < highestRowIndex):
        if(nodes[bottomPos].posNum not in obstacleLocs):
            neighbors.append(nodes[bottomPos])
            
    #BOTTOM RIGHT
    if(row < highestRowIndex) and (col < highestRowIndex):
        if(nodes[bottomPos + 1].posNum not in obstacleLocs):
            neighbors.append(nodes[bottomPos + 1])
    
    return(neighbors)