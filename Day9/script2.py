import math
import matplotlib.pyplot as plt

#Command extraction
commands = [line.split() for line in open('input.txt', 'r')]

rope = [0 for i in range(10)]

direcDict = {'L':-1, 'R':1, 'U':1j, 'D': -1j}
visited = {0}


def getDir(val):
    key = next(key for key, value in direcDict.items() if value == val)
    return key

def distance(a, b):
    return math.sqrt((a.real - b.real)**2 + (a.imag - b.imag)**2)

#Value of cell in rope at index will be modified according to direction
def moveCell(direc, index):
    rope[index] += direcDict[direc]

#Moves head by default, otherwise works the same. Probably unneeded.
def moveHead(direc, index = 0):
    moveCell(direc, index)

#Moves tail.
def moveTail(direc, index = 0):
    #If the Euclidean distance between the relative 'head' cell and 'tail' cell exceeds 2
    if (distance(rope[index-1], rope[index]) > 2):
        #Transform the tail cell twice
        if (rope[index-1].real > rope[index].real):
            moveCell('R',index)
        else:
            moveCell('L',index)
        if (rope[index-1].imag > rope[index].imag):
            moveCell('U', index)
        else:
            moveCell('D', index)
    #If the tail cell and head cell's real or imaginary components do not differ by greater than 1,
    #then move the tail cell once
    elif (abs(rope[index-1].real - rope[index].real) > 1) or (abs(rope[index-1].imag - rope[index].imag) > 1):
        if (rope[index-1].real > rope[index].real):
            moveCell('R',index)
        if (rope[index-1].real < rope[index].real):
            moveCell('L',index)
        if (rope[index-1].imag > rope[index].imag):
            moveCell('U', index)
        if (rope[index-1].imag < rope[index].imag):
            moveCell('D', index)
    #Each time the tail cell must move, it's position is added to a set.
    
    visited.add(rope[-1])


#Moves the head, along with it's tail cells
def moveRope(command):
    direc, amount = command
    #Move the head cell by the given amount in the command
    for i in range(int(amount)):
        moveHead(direc)
        #Iterate through the rest of the rope, moving the tail cells accordingly
        for j in range(1, len(rope)):
            moveTail(direc, j)







print('rope: ', rope)
for command in commands:
    print('command: ', command)
    moveRope(command)
    print('rope: ', rope)
    print('distance: ', distance(rope[0], rope[-1]))
    print()


    # # create data of complex numbers
    
    # # extract real part
    # x = [ele.real for ele in rope]
    # # extract imaginary part
    # y = [ele.imag for ele in rope]
    
    # # plot the complex numbers
    # plt.scatter(x, y)
    # plt.grid()
    # plt.ylabel('Imaginary')
    # plt.xlabel('Real')
    # plt.show()

    


  



print(len(visited))


