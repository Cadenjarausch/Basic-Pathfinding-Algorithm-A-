from NODE import NODE
from getNeighbors import getNeighbors
from getFScore import getFScore

def aStar(startNode, endNode, nodes):
    #Create a variable that is the node under consideration and initialize to starting point
    currentNode = nodes[startNode]

    #Create a list of all the elements being considered (Under consideration)
    openSet = [currentNode]

    #Create a list of all the elements already considered (Not under consideration)
    closedSet = []

    #Create a list, each element containing all of the nodes travelled to get to the current node under consideration
    cameFrom = []

    #Initialize an Index Variable to Keep Track of List Positions in Open List
    currentIndex = 0

    while (len(openSet) != 0 and currentNode != nodes[endNode]):
        print(len(openSet))
        print("Current Index: %d",currentIndex)
        #Remove Current Node From Open Set and Add it to Closed Set
        openSet.pop(currentIndex)
        closedSet.append(currentNode)

        #Find the neighbors of the current node and append to the open set 
        neighbors = (getNeighbors(nodes, currentNode.posNum, closedSet, openSet))

        for x in neighbors:
            if x not in openSet and x not in closedSet:
                openSet.append(x)
        
        lowestF = NODE.totalRows*NODE.totalColumns
        for index, node in enumerate(openSet):
            node.f = getFScore(nodes, endNode, node.posNum)

            #If the Calculated FScore is Lower than the Previous Lowest, that is the New FScore and that Node is Under Consideration
            if (node.f < lowestF) or (node.h == 0):
                lowestF = node.f
                currentNode = node
                currentIndex = index

        parentNode = currentNode.parent
        pathTravelled = []

        while(parentNode != None):
            pathTravelled.append(parentNode)
            parentNode = parentNode.parent

        cameFrom.append(pathTravelled)

    if (currentNode == nodes[endNode]):
        print("Came from matrix: %d", cameFrom)
        optimalPath = cameFrom[-1]

        for x in cameFrom:
            for y in x:
                print(y.posNum, "\n")

    else:
        optimalPath = None
        print("Path not possible!")

    return(optimalPath, openSet)