from NODE import NODE
import math as m

def getFScore(nodes, endPos, currentPos):

    endNode = nodes[endPos]
    currentNode = nodes[currentPos]

#Calculates the gScore based on amount of nodes traveled until it gets to the start node
    if currentNode.f == None:
        gScore = 0

        parentNode = currentNode.parent

        while(parentNode != None):
            parentNode = parentNode.parent
            gScore += currentNode.lengthToParent

        currentNode.g = gScore

        endY = endNode.row
        endX = endNode.col

        currentY = currentNode.row
        currentX = currentNode.col
        
        currentNode.h = m.sqrt(((currentX - endX)**2) + ((currentY - endY)**2))
        heuristic = currentNode.h

        currentNode.f = gScore + heuristic

    fScore = currentNode.f

    return(fScore)