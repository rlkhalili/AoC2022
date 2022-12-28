fs = open('input.txt', 'r')

termOut = fs.readlines()
for i in range(len(termOut)): termOut[i] = termOut[i].rstrip()

class Node:
    def __init__(self, name, size=0, children=None, isDirectory=False, parent=None) -> None:
        self.name = name
        self.size = size  
        if (children==None):
            children = {}
        self.children = children
        self.isDirectory = isDirectory
        self.parent = parent
    
    def isChild(self, name):
        if (self.children == {}):
            return False
        for i in self.children:
            if (i == name): return True
        return False

    def __str__(self) -> str:
        s = self.name + '\n'
        for i in self.children:
            s += i + '   '
        return s

    def getSize(self):
        total = 0
        if (not self.isDirectory): return self.size 
        for i in self.children:
            total +=  self.children[i].getSize()
        return total

#Trying it out
root = Node('/', isDirectory=True)
position = root

for i in termOut:
    # print(position)
    cmdArgs = i.split()
    if (cmdArgs[0] == '$'):
        if (cmdArgs[1] == 'ls'): continue
        if (cmdArgs[2] == '/'): position = root
        if (cmdArgs[2] == ".."): position = position.parent
        elif (position.isChild(cmdArgs[2])): position = position.children[cmdArgs[2]]
    else:
        if (cmdArgs[0] == 'dir'):
            newNode = Node(name=cmdArgs[1], isDirectory=True, parent=position)
        else:
            newNode = Node(name=cmdArgs[1], size=int(cmdArgs[0]))
        # print('ew')
        position.children[cmdArgs[1]] = newNode
        # print('e')
        



# print(root)
# print(root.children['a'])
#Part one - running total
runningTotal = 0

#Part Two - unused space
unusedSpace = 70000000 - root.getSize()
makeupSpace = 30000000 - unusedSpace
candidateDir = []

def printTree(root, level=0):
    print("  " * level, root.name)
    if (root.isDirectory):
        #Part one
        if (root.getSize() <= 100000):
            global runningTotal 
            runningTotal += root.getSize()

        #Part two
        if (root.getSize() >= makeupSpace):
            candidateDir.append(root.getSize())

    
    for name, child in root.children.items():
        printTree(child, level + 1)
printTree(root)

#Part one
print(runningTotal)

#Part two
print(min(candidateDir))
