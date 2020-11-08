class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def ADD(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            n = self.head
            while n.ref is not None:
                # print(n.data, "=>", end=" ")
                n = n.ref
            n.ref = newNode



    def ADD_AT_BEGIN(self, data):
        newNode = Node(data)
        newNode.ref = self.head
        self.head = newNode

    def ADD_AT_END(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = newNode

    def ADD_AFTER_ELEMENT(self, data, x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print('Node is Not Found')
        else:
            newNode = Node(data)
            newNode.ref = n.ref
            n.ref = newNode

    def ADD_BEFORE_ELEMENT(self, data, x):
        # n = self.head
        if self.head is None:
            print('Linked List is Empty')
            return

        if self.head.data == x:
            newNode = Node(data)
            newNode.ref = self.head
            self.head = newNode
            return
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n.ref is None:
                print('ELement not Found')
            else:
                newNode = Node(data)
                newNode.ref = n.ref
                n.ref = newNode

    def traverse(self):
        if self.head is None:
            print("LL is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "=>", end=" ")
                n = n.ref


LL1 = SLinkedList()

LL1.ADD_AT_END(10)
LL1.ADD_AT_END(20)
LL1.ADD_AT_END(30)
LL1.ADD_AT_END(40)
LL1.ADD_AT_END(50)
# LL1.ADD_BEFORE_ELEMENT(10,30)
# LL1.ADD_AFTER_ELEMENT(40,20)

LL1.ADD(60)


print(LL1.traverse())
'''
node1 = Node(1)
print(node1) # Output : <__main__.Node object at 0x0000023B55B4C5C8>

'''
