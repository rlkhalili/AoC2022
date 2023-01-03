#This is a failed attempt, with the input taking over 50 seconds to complete


import time
start_time = time.time()

class Cell:
    def __init__(self, h=False, t=False, start = False) -> None:
        self.h = h
        self.t = t
        if t: self.visited = True
        else: self.visited = False
        self.start = start

    def __str__(self) -> str:
        if (self.h): return 'H'
        if (self.t): return 'T'
        if (self.start): return 's'
        if (self.visited): return '#'
        return '.'
               
                
def printGrid(array):
    for i in array:
        for j in i:
            print(j, end='')
        print()

def addRowCol(array, direc):
    if direc == 'U':
        array.insert(0, [Cell() for i in range(len(array[0]))])
    if direc == 'D':
        array.append([Cell() for i in range(len(array[0]))])
    if direc == 'L':
        for i in array:
            i.insert(0, Cell())
    if direc == 'R':
        for i in array:
            i.append(Cell())

def findCell(array, att):
    for y in range(len(array)):
        for x in range(len(array[0])):
            if getattr(array[y][x], att):
                return [x, y]





def endOfGrid(array, x, y, direc):
    if direc == 'U':
        if (y-1) >= 0: return False
    if direc == 'R':
        if (x+1) < len(array[0]): return False
    if direc == 'L':
        if (x-1) >= 0: return False
    if direc == 'D':
        if (y+1) < len(array): return False
    return True

def moveCell(array, direc, head = True):

    

    # printGrid(array)
    # print('~~~~~~~~~~~~~~')

    att = None
    if head: att = 'h'
    else: att = 't'

    #Main movement
    x, y = findCell(array, att)
    setattr(array[y][x], att, False)
    if direc == 'R':
        if (endOfGrid(array, x, y, direc)):
            addRowCol(array, direc)
        setattr(array[y][x+1], att, True)
        return
    elif direc == 'U':
        if (endOfGrid(array, x, y, direc)):
            addRowCol(array, direc)
            setattr(array[0][x], att, True)
        else: 
            setattr(array[y-1][x], att, True)
        return
    elif direc == 'D':
        if (endOfGrid(array, x, y, direc)):
            addRowCol(array, direc)
        setattr(array[y + 1][x], att, True)
        
        return 
    elif direc == 'L':
        if (endOfGrid(array, x, y, direc)):
            addRowCol(array, direc)
        if (x == 0):
            setattr(array[y][x], att, True)
        else:
            setattr(array[y][x-1], att, True)
        return 


def moveTail(array, direc):
    hCoord = findCell(array, 'h')
    tCoord = findCell(array, 't')

    if (abs(hCoord[0] - tCoord[0]) > 1) or (abs(hCoord[1] - tCoord[1]) > 1):
        moveCell(array, direc, False)
        tCoord = findCell(array, 't')
        if (not (abs(hCoord[0] == tCoord[0])) and not (abs(hCoord[1] == tCoord[1]))):
            # moveCell(array, direc, False)
            # tCoord = findCell(array, 't')
            
            direcDicY = {-1: 'D', 1:'U'}
            direcDicX = {-1: 'R', 1:'L'}

            if (direc in direcDicX.values()):
                moveCell(array, direcDicY[(tCoord[1] - hCoord[1])], False)
            else:
                moveCell(array, direcDicX[(tCoord[0] - hCoord[0])], False) 

            tCoord = findCell(array, 't')
            array[tCoord[1]][tCoord[0]].visited = True


        else:
            array[tCoord[1]][tCoord[0]].visited = True


# # # def moveCell(array, direc, head = True):
# # #     printGrid(array)
# # #     print('~~~~~~~~~~~~~~')
# # #     for y in range(len(array)):
# # #         for x in range(len(array[0])):
# # #             if array[y][x].h:
# # #                 array[y][x].h = False
# # #                 if direc == 'R':
# # #                     if (endOfGrid(array, x, y, direc)):
# # #                         addRowCol(array, direc)
# # #                     array[y][x + 1].h = True
# # #                     return
# # #                 elif direc == 'U':
# # #                     if (endOfGrid(array, x, y, direc)):
# # #                         addRowCol(array, direc)
# # #                         array[0][x].h = True
# # #                     else: 
# # #                         array[y-1][x].h = True
# # #                     return
# # #                 elif direc == 'D':
# # #                     if (endOfGrid(array, x, y, direc)):
# # #                         addRowCol(array, direc)
# # #                     array[y + 1][x].h = True
                    
# # #                     return 
# # #                 elif direc == 'L':
# # #                     if (endOfGrid(array, x, y, direc)):
# # #                         addRowCol(array, direc)
# # #                     if (x == 0):
# # #                         array[y][x].h = True
# # #                     else:
# # #                         array[y][x - 1].h = True
# # #                     return 

# # #     printGrid(array)
# # #     print('~~~~~~~~~~~~~~')







#Initialize grid as 5x5, with the bottom left as starting
grid = [[Cell() for i in range(5)] for j in range(5)]
grid[4][0].h = True
grid[4][0].visited = True
grid[4][0].t = True
grid[4][0].start = True

#Initialize file reading, extract commands
fs = open('testme.txt', 'r').read().split('\n')
commandList = []
for i in fs:
    if not i == '':
        commandList.append(i.split(' '))



#Input
for i in commandList:
    print(i)

    for j in range(int(i[1])):
        moveCell(grid, i[0])
        moveTail(grid, i[0])
        


# for i in range(5):
#     moveCell(grid,'R')

    


printGrid(grid)

counter = 0
for i in grid:
    for j in i:
        if j.visited:
            counter += 1
print(counter)


print("Process finished --- %s seconds ---" % (time.time() - start_time))

