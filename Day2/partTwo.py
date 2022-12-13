opp = ['A', 'B', 'C']
self =  {
    'X':1,
    'Y':2, 
    'Z':3
    }

outcomes = {
    'Y':3, 
    'Z':6,
    'X':0
    }

fs = open("input.txt", 'r')
s = []
for i in fs:
    s.append(i.rstrip())

#Returns value of score from match
def getOutcome(a):
    outIndex = 0
    oppIndex = 0
    for i in range(3):
        if (a[2] == list(outcomes)[i]): outIndex = i
        if (a[0] == opp[i]): oppIndex = i
        
    # print(outIndex + oppIndex)
    selfChoice = (list(self)[(oppIndex + outIndex) % len(self)])
    return outcomes[a[2]] + self[selfChoice]


# print(getOutcome("B X"))

totalScore = 0
for i in s:
    totalScore += getOutcome(i)

print(totalScore)
