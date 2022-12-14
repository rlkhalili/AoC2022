fs = open('input.txt', 'r')

s = []
for i in fs:
    s.append((i.rstrip()).split(','))

def pairContains(pair, fullOverlap = True):
    def rangeToInt(assignRange):
        intList = assignRange.split('-')
        for i in range(len(intList)): intList[i] = int(intList[i])
        return intList

    pairRanges = []
    for i in pair:
        pairRanges.append(rangeToInt(i))
    # print(pairRanges)

    differences = []
    for i in pairRanges:
        differences.append(abs(i[0] - i[1]))
    # print(differences, end='\n\n\n')

    if (fullOverlap == True):
        indexOfWidest = differences.index(max(differences))
        indexOfNarrowest = differences.index(min(differences))
        if (pairRanges[indexOfWidest][0] > pairRanges[indexOfNarrowest][0]): return False
        if (differences[0] == differences[1]) and (pairRanges[indexOfWidest][0] != pairRanges[1][0]): return False
        if (pairRanges[indexOfNarrowest][0] + differences[indexOfNarrowest]) > pairRanges[indexOfWidest][1]: return False
    else:
        if ((pairRanges[0][0] <= pairRanges[1][1]) and (pairRanges[0][1] >= pairRanges[1][0])): return True
        return False
    
fullOverlaps = 0
for item in s:
    if (pairContains(item, False)): fullOverlaps += 1
print(fullOverlaps)