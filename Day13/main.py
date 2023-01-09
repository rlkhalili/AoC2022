from ast import literal_eval

fs = open('input.txt', 'r').read().split('\n\n')
signal = []
## For part 1
# for i in range(len(signal)):
#     signal[i] = signal[i].split('\n')
#     for j in range(len(signal[i])):
#         signal[i][j] = literal_eval(signal[i][j])
for i in fs:
    for j in i.split('\n'):
        signal.append(literal_eval(j))
signal.append([[2]])
signal.append([[6]])

def packetsIsOrdered(packLeft, packRight):
    #Check if packLeft and packRight are both ints
    if isinstance(packLeft, int) and isinstance(packRight, int):
        if packLeft == packRight: return None
        return packLeft < packRight

    #Check if both lists
    if isinstance(packLeft, list) and isinstance(packRight, list):
        # Iterate through both lists
        for i, j in zip(packLeft, packRight):
            #If current idices' values aren't equal
            if (isOrdered := packetsIsOrdered(i, j)) is not None:
                return isOrdered
        # Else compare list lengths
        return packetsIsOrdered(len(packLeft), len(packRight))

    #If packLeft is int, turn packLeft to int
    if isinstance(packLeft, int): return packetsIsOrdered([packLeft], packRight)
    #Else return vice versa
    return packetsIsOrdered(packLeft, [packRight])


#  For part 1
# a = []
# for i in signal:
#     a.append(packetsIsOrdered(i[0], i[1]))

# b = 0
# for i in range(len(a)):
#     if a[i]: b += i + 1

# print(b)

#Bubble sort
for i in range(1, len(signal)):
    for i in range(1, len(signal)):
        if not packetsIsOrdered(signal[i-1], signal[i]):
            signal[i-1], signal[i] = signal[i], signal[i-1]

for i in signal:
    print(i)

multi = 1
for i in range(len(signal)):
    if signal[i] == [[2]] or signal[i] == [[6]]:
        multi *= i + 1

print(multi)