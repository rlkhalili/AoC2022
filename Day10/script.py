import math

commands = [x.split() for x in (open('input.txt', 'r').read().split('\n'))]
cycle = 0
x = 1

#Part one stuff
# cycleList = [i + 20 for i in range(0, 220, 40)]
# print(cycleList)
# sum = 0
# def checkCycle():
#     if (cycle in cycleList):
#         return cycle * x
#     return 0
# for i in commands:
#     if ('noop' in i):
#         cycle += 1
#         sum += checkCycle()
#     if ('addx' in i):
#         cycle += 1
#         sum += checkCycle()
#         cycle += 1
#         sum += checkCycle()
#         x += int(i[1])

blankSymbol = '.'
pixelSymbol = '#'

def scrnReset(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = blankSymbol

def addSprite(arr, x, cycle):
    row = math.floor(cycle / 40)
    for i in range(-1, 2, 1):
        try:
            arr[row][x + i] = pixelSymbol
        except:
            print(x, row)
    for i in screen:
        for j in i:
            print(j, end='')
        print()
    print('^', x, cycle)

def changeSprite(arr, x, cycle):
    scrnReset(arr)
    addSprite(arr, x, cycle)

def placePixel(arrIn, arrOut, x, cycle):
    row = math.floor(cycle / 40)
    try:
        arrOut[row][cycle % 40] = arrIn[row][cycle % 40]
    except:
        print(row, x)

screen = [[blankSymbol for i in range(40)] for j in range(6)]
screenOut = [[blankSymbol for i in range(40)] for j in range(6)]
changeSprite(screen, x, cycle)
#Part two
for i in commands:
    if ('noop' in i):
        placePixel(screen, screenOut, x, cycle)
        cycle += 1
    if ('addx' in i):
        placePixel(screen, screenOut, x, cycle)
        cycle +=1
        x += int(i[1])

        placePixel(screen, screenOut, x, cycle)

        cycle+=1
        changeSprite(screen, x, cycle)


    
#Printing the screen (internal)
for i in screen:
    for j in i:
        print(j, end='')
    print()
print()
#Printing screen output
for i in screenOut:
    for j in i:
        print(j, end='')
    print()