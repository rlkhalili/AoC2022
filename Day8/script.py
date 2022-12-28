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
#Part one
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


#Part two

highestViewingScore = 0

viewingScore = 1
for rows in range(len(treeGrid)):
    for col in range(len(treeGrid[rows])):
        colList = []
        for j in range(len(treeGrid)):
            colList.append(treeGrid[j][col])

        directionScore = 0
        #Contains left and up directions
        reverseDirec = [treeGrid[rows][0:col], colList[0:rows]]
        #Contains right and down directions
        direc = [treeGrid[rows][col + 1:], colList[rows + 1:]]

        for x in reverseDirec:
            directionScore = 0
            if (x == []): 
                viewingScore = 0
                break
            for i in list(reversed(x)):
                directionScore += 1

                if treeGrid[rows][col] <= i:
                    break
            viewingScore *= directionScore


        for x in direc:
            directionScore = 0
            if (x == []):
                viewingScore = 0

                break

            for i in (x):
                directionScore += 1

                if treeGrid[rows][col] <= i:
                    break
            viewingScore *= directionScore


        # print (directionScore,end='')
        # for i in (right):
        #     directionScore += 1
        #     if treeGrid[rows][col] <= i:
        #         viewingScore += directionScore
        #         directionScore = 0
        #         break
        if (viewingScore > highestViewingScore): highestViewingScore = viewingScore
        print(str(viewingScore) + ' ', end='')
        viewingScore = 1
    print()

print(highestViewingScore)
print(visibleTrees)
