import queue


class Stack:
    def __init__(self):
        self.stackArr = []
    def print(self):
        for i in range(len(self.stackArr)):
            print(self.stackArr[i])
    def add(self, val):
        self.stackArr.append(val)
    def remove(self):
        self.stackArr.pop() 

class QueueX:
    def __init__(self):
        self.queueArr = []
    def print(self):
        for i in range(len(self.queueArr)):
            print(self.queueArr[i])
        return
    def add(self, val):
        self.queueArr.append(val)
    def remove(self):
        del self.queueArr[0]
        return
queueStruct = QueueX()
queueStruct.add(10)
queueStruct.add(20)
queueStruct.add(50)
queueStruct.print()
queueStruct.remove()

