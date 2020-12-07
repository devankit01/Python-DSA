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
    def __init__(self):
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

    #Push
    def push(self,data):
        self.list.append(data)

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




st = Stack()
st.push(1)
st.push(2)
st.push(3)

# st.pop()

print(st.isEmpty())
print(st)
print(st.peek())

    
