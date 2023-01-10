from time import sleep

paths = []
x =  open('input.txt', 'r').read().split('\n')
for i in x:
    paths.append(i.split(' -> '))
for i in range(len(paths)):
    for j in range(len(paths[i])):
        paths[i][j] = (paths[i][j].split(','))
        for k in range(len(paths[i][j])):
            paths[i][j][k] = int(paths[i][j][k])

maxCol, maxRow = 0, 0

for i in paths:
    for j in i:
        if j[0] > maxCol: maxCol = j[0]
        if j[1] > maxRow: maxRow = j[1]

#For part two
maxRow += 3
maxCol += maxRow

sandSource = (500,0)
#Paths is [[[498, 4], [498, 6], [496, 6]], [[503, 4], [502, 4], [502, 9], [494, 9]]]
#maxCol, maxRow is 503, 9

# def rockInPath(coord1, coord2, coord):
    # x1, y1 = coord1
    # x2, y2 = coord2
    # x, y = coord
    # return (x1 <= x <= x2) and (y1 <= y <= y2)


# Drawing the vertical grid
def drawSlice(max, rocks, obstacles):
    grid = ''
    rows, cols = (max)
    for i in range(rows):
        for j in range(cols):
            # Print . if j, i is not in any path
            if ((j+1, i) in rocks):
                grid += '#'
            elif (j+1, i) in obstacles:
                grid += 'o'
            elif (j+1, i) == sandSource:
                grid += '+'
            else:
                grid += '.'
        grid += '\n'
    return grid



def getCoordsInPath(coord1, coord2):
    ls = []
    if coord1[0] == coord2[0]:
        for i in range(abs(coord1[1] - coord2[1]) + 1):
            if (coord1[1] - coord2[1] < 0):
                ls.append((coord1[0], coord1[1] + i))
            else:
                ls.append((coord1[0], coord1[1] - i))
        return ls
    if coord1[1] == coord2[1]:
        for i in range(abs(coord1[0] - coord2[0]) + 1):
            if (coord1[0] - coord2[0] < 0):
                ls.append((coord1[0] + i, coord1[1]))
            else:
                ls.append((coord1[0] - i, coord1[1]))
        return ls

    return 0

def getAllPresentCoords(paths):
    x = []
    for j in range(len(paths)):
        a = paths[j]
        for i in range(len(a) - 1):
            x.append(getCoordsInPath(a[i], a[i+1]))

    # print('coords: ',x)
    return {i for sublist in x for i in sublist}

#Done^
rockCoords = getAllPresentCoords(paths)
print(rockCoords)
for i in getCoordsInPath((0,(maxRow - 1)), (maxCol,maxRow - 1)):
    rockCoords.add(i)



# Given a source and a list of coordinates of obstacles, will return the final coordinate of one sand block.
def getSand(source, obstacles):
    sand = source
    #   For part one
    if sand[1] > maxRow: return None
    if (sand[0], sand[1] + 1) not in obstacles:
        sand = sand[0], sand[1] + 1
        return getSand(sand, obstacles)
    elif (sand[0] - 1, sand[1] + 1) not in obstacles:
        sand = sand[0] - 1, sand[1] + 1
        return getSand(sand, obstacles)
    elif (sand[0] + 1, sand[1] + 1) not in obstacles:
        sand = sand[0] + 1, sand[1] + 1
        return getSand(sand, obstacles)
    obstacles.add(sand)
    return sand


grd = None
obstacles = set(rockCoords)
tmp = 0
# for i in range(93):
while (not (getSand(sandSource, obstacles)) == sandSource):
    (getSand(sandSource, obstacles))
    # while (not (getSand(sandSource, obstacles)) == sandSource):
    #      (getSand(sandSource, obstacles))
    tmp += 1
    with open('output.txt', 'w') as f:
        print(grd := drawSlice((maxRow, maxCol), rockCoords, obstacles), file=f)
    # sleep(0.1)

count = 1
for i in grd:
    for j in i:
        if j == 'o': count += 1
print(count)