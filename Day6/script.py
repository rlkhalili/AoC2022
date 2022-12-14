fs = open('input.txt', 'r')

datastream = (fs.readlines())


def allUniqueChar (str):
    sortStr = sorted(str)
    for i in sortStr:
        sortStr.remove(i)
        if i in sortStr:
            return False
    return True
        
def charsProcessed(s, uniqueChar = 4):
    buffer = s[:uniqueChar]
    for i in range(uniqueChar, len(s), 1):
        # print (buffer + str(i))
        if (allUniqueChar(buffer)): 
            print (buffer)
            return i
            break
        buffer = buffer[1:] + s[i]
    return 0

for i in datastream:
    print(charsProcessed(i.rstrip(), 14))