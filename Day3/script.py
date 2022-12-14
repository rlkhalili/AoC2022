fs = open('input.txt', 'r')

s = []
for i in fs:
    s.append(i.rstrip())

#For part two, split by groups of three lines
sGroups = [s[i:i+3] for i in range(0, len(s), 3)]


sT = []
#split each string in half
for item in s:
    appe = []
    for i in range(2):
        a = int(i * (len(item) /2)) 
        b = int((i + 1) * ((len(item) / 2)))

        appe.append(item[a: b])
    sT.append(appe)

commonItems = []
#Find the item type that appears in both halves
for item in sT:
    for i in range(len(item[0])):
        if (item[1].find(item[0][i]) != -1):
            commonItems.append((item[0][i]))
            break

#Get priority
def getPriority (char):
    if (char.isupper()):
        return (ord(char) - 38)
    return (ord(char) - 96)

#Part one
total = 0
for i in commonItems:
    total += getPriority(i)


#Part two
badges = []
for item in sGroups:
    for i in item[0]:
        if ((item[1].find(i) != -1) and (item[2].find(i) != -1)):
            badges.append(i)
            break


print(badges)
total = 0
for i in badges:
    total += getPriority(i)

print(total)