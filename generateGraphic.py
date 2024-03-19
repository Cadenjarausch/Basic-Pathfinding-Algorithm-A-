from NODE import NODE
from NODE import colors
from colorama import init, Fore
init(convert = True)

def generateGraphic(startPoint,endPoint,nodes,optimalPath,openSet):

    for obj in nodes:
            
        if (obj.posNum == startPoint):
            obj.color = colors["BLUE"]
            print(Fore.BLUE + ".", end= "" + Fore.WHITE)
        elif (obj.posNum == endPoint):
            obj.color = colors["MAGENTA"]
            print(Fore.MAGENTA + ".", end= "" + Fore.WHITE)
        elif (not obj.isFree):
            obj.color = colors["RED"]
            print(Fore.RED + ".", end= "" + Fore.WHITE)
        elif (optimalPath != None and obj in optimalPath):
            obj.color = colors["GREEN"]
            print(Fore.GREEN + ".", end= "" + Fore.WHITE)
        elif (obj in openSet):
            obj.color = colors["YELLOW"]
            print(Fore.YELLOW + ".", end= "" + Fore.WHITE)
        else:
            print(".", end= "")
        
        #If the element is on the rightmost side, go to the next row
        if (not((obj.col + 1) % (obj.totalColumns))):
            print("\n")
            
    return()