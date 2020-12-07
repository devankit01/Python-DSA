# Operations
'''
-Create stack
-Push
-Pop
-Peek
-isEmpty
-isFull
-deleteStack
'''

class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)


    #isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    #isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    #isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    # Push
    def Push(self,value):
        if self.isFull():
            return 'Stack Full'
        else:
            self.list.append(value)
            return 'Inserted successfully'

    #Pop
    def pop(self):
        if self.isEmpty():
            return "Empty Stack"
        else:
            return self.list.pop()

    #Peek
    def peek(self):
        return self.list[0]

    #Delete
    def delete(self):
        self.list = None




st = Stack(5)

# st.Push(1)

print(st.isEmpty())
print(st.isFull())

    

    
