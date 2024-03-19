#Color Definitions
colors = {
    "RED" : (255, 0, 0),
    "GREEN" : (0, 255, 0),
    "BLUE" : (0, 255, 0),
    "YELLOW" : (255, 255, 0),
    "WHITE" : (255, 255, 255),
    "BLACK" : (0, 0, 0),
    "PURPLE" : (128, 0, 128),
    "ORANGE" : (255, 165 ,0),
    "GREY" : (128, 128, 128),
    "TURQUOISE" : (64, 224, 208),
    "MAGENTA" : (255,0,255),
}

class NODE():
    #environment = [[1,1,1,1,1],[1,0,0,1,0],[1,0,0,1,0],[1,0,0,1,0],[1,1,1,1,1]]
    #environment = [[1,1,1,1,1],[1,0,0,1,0],[1,0,0,1,0],[1,0,0,1,0],[1,1,1,1,1],[1,0,0,1,0],[1,0,0,1,0],[1,0,0,1,0]]
    
    discreteLvl = 1 #Number of nodes per unit length (m)
    height = 5 #Height of Environment (m)
    length = 5 #Length of Environment (m)
    totalRows = height * discreteLvl
    totalColumns = length * discreteLvl
    
    def __init__(self, col, row, posNum, isFree):
        self.color = colors["WHITE"]
        self.row = row
        self.col = col
        self.posNum = posNum
        self.parent = None
        self.lengthToParent = None
        self.g = None
        self.h = None
        self.f = None
        self.isFree = isFree
        #self.open = 0