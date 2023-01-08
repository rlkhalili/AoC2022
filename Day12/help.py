class Node:
    def __init__(self, data=None, next=None) -> None:
       self.data = data
       self.next = next

    def __str__(self) -> str:
        if (self.next == None): return str(self.data)
        return str(self.data) + ' -> ' + self.next.__str__()

    def getVal(self):
        if (self.next == None): return [self.data]
        return [self.data] + self.next.getVal()

class LinkedList:
    def __init__(self) -> None:
       self.head = None

    def add(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def __str__(self) -> str:
       return self.head.__str__()

    def getChildren(self):
        return self.head.next.getVal()

    def getHead(self):
        return self.head.data

def print2dArr(arr):
  for row in arr:
    for elem in row:
      print(elem, end=' ')
    print()

def searchGrid(array, item):
  for row in range(len(array)):
    for element in range(len(array[row])):
      if array[row][element] == item:
        return [row, element]
  return None

