class Node:
    def __init__(self, data):
        self.data = None
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Append

    def Append(self, data):
        if self.head == None:
            self.head = Node(data)
            print(self.head)
            


    def Prepend(self, data):
        pass

DLL = DoublyLinkedList()
DDL.Append(1)