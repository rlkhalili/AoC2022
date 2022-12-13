opp = ['A', 'B', 'C']
self =  {
    'X':1,
    'Y':2, 
    'Z':3
    }

outcomes = {
    'd':3,
    'w':6, 
    'l':0
    }

fs = open("input.txt", 'r')
s = []
for i in fs:
    s.append(i.rstrip())

#Returns value of score from match
def getOutcome(a):
    outIndex = 0
    choiceVal = 0
    for i in range(3):
        if (a[0] == opp[i]):outIndex -= i

        if (a[2] == list(self)[i]):
            choiceVal += self[a[2]]
            outIndex += i
        # print (outIndex)
    return outcomes[list(outcomes)[outIndex % len(outcomes)]] + choiceVal

# print(getOutcome("B X"))

totalScore = 0
for i in s:
    totalScore += getOutcome(i)

print(totalScore)
