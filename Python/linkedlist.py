class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            return
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode
            return
    def print(self):
        current = self.head
        if current == None:
            print("Empty LinkedList")
            return
        while current != None:
            print(current.data )
            current = current.next
    def remove(self, val):
        current = self.head
        previous = current
        if current == None:
            print("Empty LinkedList")
            return
        if val == current.data:
            self.head = self.head.next
            del current
            print(val, "head deleted!")
            return
        while current.data != val:
            previous = current
            current = current.next
        previous.next = current.next
        del current
        print(val, "deleted!")
        return

        



        

newList = LinkedList()
newList.add(5)
newList.add(10)
newList.remove(10)
newList.print()

