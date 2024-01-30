from colorama import init, Fore
init(convert=True)

#Color Definitions
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

def generateGraphic(startPoint,endPoint,obstacleLocs,nodes,optimalPath):
    print("Obstacle Locs: ", obstacleLocs)

    for obj in nodes:
            
        if (obj.posNum == startPoint):
            obj.color = BLUE
            print(Fore.BLUE + ".", end="" + Fore.WHITE)
        elif (obj.posNum == endPoint):
            print(Fore.MAGENTA + ".", end="" + Fore.WHITE)
        elif (obj.posNum in obstacleLocs):
            print(Fore.RED + ".", end="" + Fore.WHITE)
        elif (obj.posNum in optimalPath):
            print(Fore.GREEN + ".", end="" + Fore.WHITE)
        else:
            print(".", end="")
        
        if (not((obj.col + 1) % (obj.totalRows))):
            print("\n")
            
    return()