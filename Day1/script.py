fs = open("input.txt", 'r')

#Convert to elf snack Cal to list
s = []
for line in fs:
    s.append(line.rstrip())

#List of total cal carried per elf
sSimp = []
a = 0
for item in s:
    if (item != ''):
        a += int(item)
    else:
        sSimp.append(a)
        a = 0

#Solution to part one
print(max(sSimp))

#Solution to part two
er = 0
for i in range(3):
    er += max(sSimp)
    sSimp.remove(max(sSimp))
print(er)