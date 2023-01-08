from ast import BoolOp
import help

fs = open('test.txt').read().split('\n')
#Creates 2D grid with the letters
grid = []
for i in fs:
    grid.append([*i])
printGrid = help.print2dArr

        #Code below

#A grid equivalent to the letter based grid, here each vertex is the height values
#represented as ints
heightGrid = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (grid[i][j] == 'S'):
            heightGrid[i][j] = 0
        
        elif (grid[i][j] == 'E'):
            heightGrid[i][j] = ord('z') - 96

        else:
            heightGrid[i][j] = ord(grid[i][j].lower()) - 96


#Function gets adjacent (non-diagonal) items that are traversable
def getTraversables(arr, coord):
    row, col = coord
    rows, cols = len(arr), len(arr[0])

    adCoord =  [[row-1, col] if row > 0 else None,
            [row+1, col] if row < rows-1 else None,
            [row, col-1] if col > 0 else None,
            [row, col+1] if col < cols-1 else None]
    
    #Remove all None vals
    adCoord = [x for x in adCoord if x is not None]

    #Check remove if elf can't climb adjacent cell
    # for i in adCoord:
    #     if (abs(arr[i[0]][i[1]] - arr[row][col]) > 1):
    #         adCoord.remove(i)

    for i in adCoord:
        if (
            (arr[i[0]][i[1]] - arr[row][col]) > 1
        ):
            adCoord.remove(i)

    return adCoord

def getAdjecency(coord):
    row, col = coord
    ad = getTraversables(heightGrid, coord)
    lList = help.LinkedList()
    for i in ad:
        lList.add(i)
    lList.add(coord)
    return lList

#Create adjacency list of each cell in the matrix
adjacencyList = {}
for i in range(len(grid)):
    for j in range(len(grid[0])):
        # adjacencyList.append(getAdjecency([i, j]))
        lList = getAdjecency([i, j])
        adjacencyList[str(lList.getHead())] = lList.getChildren()

#Starting and ending coordinates, as row, col
start = help.searchGrid(grid, 'S')
end = help.searchGrid(grid, 'E')


#Breadth first search
def breadthFirstSearch(adjacencyList, start, end):
    # visited = []
    # queue = [start]

    # while queue:
    #     currentRoot = queue.pop(0)
        
    #     for n in adjacencyList[str(currentRoot)]:
    #         if n not in visited:
    #             visited.append(n)
    #             queue.append(n)


    # return visited
    






def depthFirstSearch(adjacencyList, start):
    stack = [start]
    visited = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(adjacencyList[str(vertex)])

    return visited

a = breadthFirstSearch(adjacencyList, start, end)



# returns 36 instead of 31
print(len(a))

# for i in adjacencyList:
#     print(i,':', adjacencyList[i])

def get_direction(c1, c2):
    y1, x1 = c1
    y2, x2 = c2
    if x1 == x2 and y1 == y2:
        return "same point"
    if x1 < x2 and y1 == y2:
        return "right"
    if x1 > x2 and y1 == y2:
        return "left"
    if x1 == x2 and y1 < y2:
        return "down"
    if x1 == x2 and y1 > y2:
        return "up"

# for i in range(1, len(a)):
    
#     print(get_direction(a[i - 1], a[i]))