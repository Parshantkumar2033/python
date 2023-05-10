# IMPLEMENTING STACK USING LINKED LIST
# here the list pointing from newly created node to the oldest node being the last element in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.length = 0


    def put(self, data):
        n = Node(data)
        a = self.head       # a is previous self.head
        self.head = n       # now, the newly created node will become the head of the stack
        self.head.next = a  # and the new node will be pointing to the previous node which was saved in "a" earlier
        self.length += 1 

    def get(self):
        if self.length == 0:
            return "Empty stack"
        a = self.head       # self.head is the last element in the stack
        self.head = a.next  # shifting the head to the next node
        a.next = None       # making the node to be pointing None, top element to be removed from the stack
        self.length -= 1
        return a.data       # returning the data of the node whose next pointed is pointing null
    
    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False
        
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.head.data
        
    def size(self):
        return self.length
    
stack = Stack()
stack.put(1)
stack.put(2)
stack.put(3)
stack.put(4)
stack.put(5)
print("No. of elements : ", stack.size())
print("Removed : ", stack.get())
print("Removed : ", stack.get())
print("No. of elements : ", stack.size())
print("Peek : ", stack.peek())
stack.put(12)
stack.put(13)
stack.put(14)
print("size : ", stack.size())
print("Peek : ", stack.peek())