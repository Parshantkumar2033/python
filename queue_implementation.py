# #using dequeue
# from collections import deque
# q = deque()
# q.append(1)     #inserting the elements
# q.append(2)
# q.append(3)
# q.append(4)
# print(q)

# print(q.popleft(), end = " ")       #popping out the elements
# print(q.popleft())

# print(len(q))       #size of the queue

# print(len(q) == 0)      #checking whether empty or not


# using queue
# from queue import Queue
# q = Queue(maxsize=0) # maxsize <= 0 : for infinite elements
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# print(q)

# print(q.get())      # accessing the elements 
# print(q.get())

# print(q.qsize())    # size of the queue
# print(q.empty())    # whether the queue is empty or full
# print(q.full())


# user defined functions
# q = []
# rI = None
# fI = None

# def empty(Que):
#     if len(Que) == 0:
#         return True
#     else:
#         return False
# def enqueue(Que, value):
#     Que.append(value)
#     if(len(Que) == 1):
#         fI = rI = 0
#     else:
#         rI = len(Que) - 1
    
# def dequeue(Que):
#     if empty(Que) == True:
#         print("No dequeue possible")
#     else:
#         Que.pop(0)

# def peek(Que):
#     if empty(Que) == True:
#         return ('Item not present')
#     else:
#         return Que[0]

# def display(Que):
#     for i in range(len(Que)):
#         print(Que[i], end = " ")
#     print()


# q = []
# rI = None
# fI = None

# def empty(Que):
#     if len(Que) == 0:
#         return True
#     else:
#         return False

# def enqueue(Que, value):
#     Que.append(value)
#     if len(Que) == 1:
#         rI = fI = 0
#     else:
#         rI = len(Que) - 1

# def dequeue(Que):
#     if empty(Que) == True:
#         print("dequeue not possible")

#     else:
#         Que.pop(0)

# def peek(Que):
#     if empty(Que) == True:
#         return None
#     else:
#         return Que[0]

# def display(Que):
#     if empty(Que) == True:
#         return None
#     else:
#         for i in range(len(Que)):
#             print(Que[i], end = " ")
#         print()


# def main():
#     enqueue(q, 1)
#     enqueue(q, 2)
#     enqueue(q, 3)
#     enqueue(q, 4)
#     print("Queue is : ", end = "")
#     display(q)

#     dequeue(q)
#     dequeue(q)
#     print("Queue is : ", end = "")
#     display(q)

#     print("Top element is : ", peek(q))

# if __name__ == "__main__":
#     main()

# CIRCULAR QUEUE IMPLEMENTATION USING ARRAY
# class Circular:
#     def __init__(self, k):            # k no. of elements
#         self.k = k
#         self.q = [None] * self.k        # initializing the array
#         self.head = -1
#         self.tail = -1

#     def enqueue(self, data):
#         if (self.tail + 1) % self.k == self.head :       
#             print("Queue is full")
#         elif self.head == -1:       # queue is empty   
#             self.head = 0
#             self.tail = 0
#             self.q[self.tail] = data        # first element in the queue
#         else:
#             self.tail = (self.tail + 1) % self.k        # intially the size of tail = 0 therefore, incremented by one
#             self.q[self.tail] = data

#     def dequeue(self):
#         if self.head == -1:
#             print("Empty queue")
#         elif self.head == self.tail :           # one element is present in the queue
#             self.head = -1
#             self.tail = -1
#             return self.q[self.head]
#         else:
#             temp = self.q[self.head]
#             self.head = (self.head + 1) % self.k
#             return temp
        
#     def display(self):
#         if self.head == -1:
#             print("Empty queue")                             #         ___ ___ ____ ___ ___ ___ ____
#         elif self.tail >= self.head:                        # queue : |___|___|head|___|___|___|tail|
#             for i in range(self.head, self.tail + 1):
#                 print(self.q[i], end = " ")
#         else:
#             for i in range(self.head, self.k + 1):          # queue : |   |   |tail|   |head|   |   |
#                 print(self.q[self.head])
#             for j in range(0, self.tail + 1):
#                 print(self.q[j], end = " ")
#             print()


# from queue import LifoQueue    

# def initialize():
#     q = []
#     stack = LifoQueue()
#     head = tail = None

# def display(self):
#     if len(self.q) == 0:
#         print("Empty queue")
#         return
#     else:
#         for i in range(0, len(self.q)):
#             print(self.q[i], end = " ")

# def enqueue(self, value):
#     self.value = value
#     self.q.append(self.value)
#     if len(self.q) == 1:
#         self.head = self.tail = 0
#     else:
#         self.tail = len(self.q) - 1
    
# def dequeue(self):
#     if len(self.q) == 0:
#         print("Empty queue")
#         return 
#     else:
#         return self.q.pop(0)
    
# def peak(self):
#     if len(self.q) == 0:
#         print("No top element present")
#         return 
#     else:
#         return self.q[0]

# def isEmpty(self):
#     if len(self.q) == 0:
#         return True
#     else:
#         return False  
# def reverse(self):
#     if len(self.q) == 0:
#         print("No element to reverse")
#         return
#     while not isEmpty():
#         self.stack.put(dequeue())
#     while not self.stack.empty():
#         enqueue(self.stack.get())
#     display()

