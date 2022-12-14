file = open('input.txt', 'r')
fs = file.readlines()
#Creates dictionary of the number of stacks
s = {}
commandRowStart = 0
for i in fs:
    if (i.lstrip()[0] == '1'):
        for j in range(int(len(i.replace(' ', '')) - 1)):
            s[str(j+1)] = []
        commandRowStart = fs.index(i) + 2
        break

#Copies stack structure to dictionary 
for line in fs:
    if (line.lstrip()[0] == '1'): break

    for i in range(len(s)):
        if (i == 0):
            s[str(i+1)].append(line[1])
        else: 
            s[str(i+1)].append(line[5 + (4 * (i - 1))])

#Clean up empty cells
for i in s:
    while (s[i][0] == ' '): del s[i][0]

#List of commands
commandsInput = (''.join(fs[commandRowStart:])).split('\n')
try: commandsInput.remove('')
except: print('List already clean')




#Isolates the numbers and their order from a command
def getNumbers(line):
    # outList = []
    # for i in line:
    #     if (i.isnumeric()): outList.append(i)
    # return outList
    outlist = []
    for i in line.split():
        if i.isnumeric(): outlist.append(i)
    return outlist



#Solution one
def moveCrate(commandList):
    num = commandList[0]
    target = commandList[1]
    dest = commandList[2]
    for i in range(int(num)):
        s[dest].insert(0, s[target][0])
        del s[target][0]

#Solution 2
def moveCrateOrdered(commandList):
    num = commandList[0]
    target = commandList[1]
    dest = commandList[2]
    section = s[target][0:int(num)]
    
    if len(section) == 1:         
        s[dest].insert(0, section[0])
    else:
        for i in range(len(section), 0, -1):
            s[dest].insert(0, section[i - 1])

    del s[target][0:int(num)]


print(s)
for i in commandsInput:
    moveCrateOrdered(getNumbers(i))
    # print(getNumbers(i))

topCrates = ''
for i in s:
    topCrates += s[i][0]

print(topCrates)