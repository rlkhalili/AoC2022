#File open
fs = open('input.txt', 'r')
fs = (fs.read()).split('\n')

def isOnEdge(arr, x, y):
    if (x == (len(arr) - 1) or x <= 0) or (y == (len(arr) - 1) or y <= 0): return True
    return False

#Initialize grid
treeGrid = []
for i in fs:
    tempArr = []
    for j in i:
        tempArr.append(j)
    treeGrid.append(tempArr)

visibleTrees = (len(treeGrid) * 2) + ((len(treeGrid[0]) - 2) * 2)
# print(visibleTrees)

for rows in range(len(treeGrid)):
    for col in range(len(treeGrid[rows])):
        # print(treeGrid[rows][col], '.', col, rows, sep='.', end=' ')
        # print(isOnEdge(treeGrid, rows, col), end=' ')

        #TODO This will check is the current cell's value is the greatest in both the row or column. What it should
        #do is increment visibleTrees if it is the greatest from any direction
        if (not isOnEdge(treeGrid, rows, col)):
            # if (treeGrid[rows][col] == max(treeGrid[rows])):
            colList = []
            for j in range(len(treeGrid)):
                colList.append(treeGrid[j][col])

            #Checking if cell is greatest in the two sections of rows and columns (non-inclusive of cell)
            if ( (treeGrid[rows][col] > max(treeGrid[rows][0:col])) or
                (treeGrid[rows][col] > max(treeGrid[rows][col + 1:])) or
                (treeGrid[rows][col] > max(colList[0:rows])) or
                (treeGrid[rows][col] > max(colList[rows + 1:])) ):
                visibleTrees += 1


print(visibleTrees)
