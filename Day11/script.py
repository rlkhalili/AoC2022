import math
import re

fs = open('input.txt', 'r').read().split('\n\n')
monkeys = [i.split('\n') for i in fs]
for i in range(len(monkeys)):
    for j in range(len(monkeys[i])):
        monkeys[i][j] = monkeys[i][j].strip()


class Monkey:
    def __init__(self, items, operation, test) -> None:
        self.items = items
        #String of the operation to be called with exec() function
        self.operation = operation
        exec(operation)
        self.test = test
    def __str__(self) -> str:
        return self.items, self.operation, self.test



operations = []
for row in monkeys:
    code = 'operate = lambda old: ' + row[2][17:]
    operations.append(code)

itemBags = []
for row in monkeys:
    x = []
    for i in (row[1][16:].split(', ')):
        x.append(int(i))
    itemBags.append(x)

tests = []
for row in monkeys:
    t = re.findall(r'\d+', (', '.join(row[3:])))
    for i in range(len(t)):
        t[i] = int(str(t[i]))
    tests.append(t)

inspections = [0 for i in range(len(monkeys))]
    
print(itemBags)
#Applies the each monkeys respective operations to its contents 
for rounds in range(20):
    for bag in range(len(itemBags)):
        while not (itemBags[bag] == []):
            inspections[bag] += 1
            operate = None
            exec(operations[bag])
            itemBags[bag][0] = math.floor(operate(itemBags[bag][0]) / 3)
            # print(itemBags[bag][0], end=' ')
            if (itemBags[bag][0] % tests[bag][0] == 0):
                itemBags[tests[bag][1]].append(itemBags[bag][0])
            else:
                itemBags[tests[bag][2]].append(itemBags[bag][0])
            del itemBags[bag][0]

        # print()



print('------------------------')
print(itemBags)
print(inspections)
result = sorted(inspections)[-2:]
print(result[0]*result[1])
