
from heapq import heappop, heappush


#   Read the input, and convert the matrix of characters to a 2d list of characters called 'fs'
fs = []
for i in open('input.txt', 'r').read().split():
    tmp = []
    for j in i:
        tmp.append(j)
    fs.append(tmp)


#   Converts a char array to an array of height values for their respective index
def charToHeight(charArray):
    heightArr = []

    for i in range(len(charArray)):
        _ = []
        for j in range(len(charArray[0])):
            if (charArray[i][j] == 'S'):
                _.append(ord('a') - 97)
            elif (charArray[i][j] == 'E'):
                _.append(ord('z') - 97)
            else:
                _.append(ord(charArray[i][j]) - 97)
        heightArr.append(_)
        _ = []  # Reset the _ list

            

    return heightArr


#   Height matrix of the input character array
a = charToHeight(fs)

with open('ouHeight.txt', 'w') as f:
    def printGrid(grid):
        for row in grid:
            print(" ".join(["{:2d}".format(x) for x in row]), file=f)



#   Returns an adjacency list for a position in the height matrix, such that cells must be
#   adjacent to the passed position, and be at most 1 greater in value
# TODO: Make this more concise
def getAdjacencyList(array, i, j):
    adjacencyList = []

    #   Check for neighbors
    if j > 0 and (array[i][j-1] < array[i][j] or abs(array[i][j-1] - array[i][j]) <= 1):
        adjacencyList.append((i, j-1))

    if j < len(array[0]) - 1 and (array[i][j+1] < array[i][j] or abs(array[i][j+1] - array[i][j]) <= 1):
        adjacencyList.append((i, j+1))

    if i > 0 and (array[i-1][j] < array[i][j] or abs(array[i-1][j] - array[i][j]) <= 1):
        adjacencyList.append((i-1, j))

    if i < len(array) - 1 and (array[i+1][j] < array[i][j] or abs(array[i+1][j] - array[i][j]) <= 1):
        adjacencyList.append((i+1, j))

    return adjacencyList

#   Create a dictionary of all the positions of the input
adjacListMap = {}
for row in range(len(a)):
    for col in range(len(a[0])):
        adjacListMap[(row, col)] = getAdjacencyList(a, row, col)

print(len(adjacListMap))

#   Returns a list of the positions in the shortest path from start to end 
def shortestPath(adjacencyList, start, end):
    # Initialize a priority queue for Dijkstra's algorithm
    queue = [(0, [start])]
    seen = set()

    # Perform Dijkstra's algorithm
    while queue:
        (cost, path) = heappop(queue)
        vertex = path[-1]
        if vertex not in seen:
            seen.add(vertex)
            if vertex == end:
                return path
            for neighbor in adjacencyList[vertex]:
                heappush(queue, (cost + 1, path + [neighbor]))

    # Return empty list if no path was found
    return []


def find_char(char_array, target):
    for i in range(len(char_array)):
        for j in range(len(char_array[0])):
            if char_array[i][j] == target:
                return (i, j)
    return (-1, -1)

def find_all_chars(char_array, target):
    indices = []
    for i in range(len(char_array)):
        for j in range(len(char_array[0])):
            if char_array[i][j] == target:
                indices.append((i, j))
    return indices


start = find_all_chars(fs, 'a')
end = find_char(fs, 'E')

sPath = []
for i in start:
    sPath.append(shortestPath(adjacListMap, i, end))

#   The length is decremented as the list includes the starting position

pathsLengths = []
for i in sPath:
    if len(i) > 0:
        pathsLengths.append(len(i) - 1)

print(min(pathsLengths))