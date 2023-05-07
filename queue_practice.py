#   REVERSING QUEUE USING ADT
# from queue import LifoQueue    
# class Create:
#     def __init__(self):
#         self.q = []
#         self.stack = LifoQueue()
#         self.head = self.tail = None

#     def display(self):
#         if len(self.q) == 0:
#             print("Empty queue")
#             return
#         else:
#             for i in range(0, len(self.q)):
#                 print(self.q[i], end = " ")
    
#     def enqueue(self, value):
#         self.value = value
#         self.q.append(self.value)
#         if len(self.q) == 1:
#             self.head = self.tail = 0
#         else:
#             self.tail = len(self.q) - 1
        

#     def dequeue(self):
#         if len(self.q) == 0:
#             print("Empty queue")
#             return 
#         else:
#             return self.q.pop(0)
        
#     def peak(self):
#         if len(self.q) == 0:
#             print("No top element present")
#             return 
#         else:
#             return self.q[0]
    
#     def isEmpty(self):
#         if len(self.q) == 0:
#             return True
#         else:
#             return False  

#     def reverse(self):
#         if len(self.q) == 0:
#             print("No element to reverse")
#             return
#         while not self.isEmpty():
#             self.stack.put(self.dequeue())
#         while not self.stack.empty():
#             self.enqueue(self.stack.get())
#         return self.q

# ele = list(map(int, input("Enter elements : ").split()))
# create = Create()
# for i in ele:
#     create.enqueue(i)

# print("Currently the queue is : ", end = "")
# create.display()
# print()
# print("Reversed queue : ", end = "")
# print(create.reverse())
# create.dequeue()
# create.dequeue()
# print("New queue : ", end = "")
# create.display()
# print("\nReverse queue : ", create.reverse())



#   IMPLEMENTING QUEUE USING TWO STACKS
# from queue import LifoQueue
# class Solution:
#     def __init__(self):
#         self.count = 0
#         self.ar = []
#         self.stack1 = LifoQueue()
#         self.stack2 = LifoQueue()
        
#     def enqueue(self, val):
#         self.value = val
#         if not self.stack1.empty():
#             while not self.stack1.empty():
#                 self.stack2.put(self.stack1.get())
#             self.stack2.put(self.value)
#         else:
#             self.stack2.put(self.value)
#         self.count += 1
    
#     def dequeue(self):
#         if self.stack1.empty():
#             if self.stack2.empty():
#                 return "Empty queue"
#             else:
#                 while not self.stack2.empty():
#                     self.stack1.put(self.stack2.get()) 
#         self.count -= 1          
#         return self.stack1.get()
        
#     def display(self):
#         if self.stack1.empty():
#             if self.stack2.empty():
#                 return "Empty queue"
#             else:
#                 while not self.stack2.empty():
#                     temp = self.stack2.get()
#                     self.ar.append(temp)
#                     self.stack1.put(temp)

#         for i in self.ar:
#             self.stack2.put(i)
#         while not self.stack1.empty():
#             print(self.stack1.get(), end = " ")
        
#     def size(self):
#         if self.count == 0:
#             return "Empty queue"
#         else:
#             return self.count
        
#     def main(self):
#         self.enqueue(1)
#         self.enqueue(2)
#         self.enqueue(3)
#         self.enqueue(4)
#         self.enqueue(5)
#         self.enqueue(6)
#         self.dequeue()
#         print()
#         self.display()
#         self.enqueue(7)
#         self.enqueue(8)
#         print()
#         self.display()
#         self.dequeue()
#         self.dequeue()
#         self.dequeue()
#         print()
#         self.display()
 
# solution = Solution()
# solution.main()


# IMPLEMENTING STACK USING 2 QUEUE
# class Solution:
#     def __init__(self):
#         self.count1 = 0
#         self.count2 = 0
#         self.que1 = []
#         self.que2 = []

#     def empty(self, arr):
#         if len(arr) == 0:
#             return True
#         else:
#             return False

#     def enqueue(self, val):
#         self.data = val
#         if self.empty(self.que1):
#             self.que2.append(self.data)
#             self.count2 += 1
#         elif self.empty(self.que2):
#             self.que1.append(self.data)
#             self.count1 += 1

#     def dequeue(self):
#         if (self.count1 + self.count2) == 0:
#             return "Empty queue"
#         elif self.count1 == 0:
#             for i in range(0, (self.count2 - 1)):
#                 self.que1.append(self.que2[i])
#                 self.count1 += 1
#             temp = self.que2[self.count2 - 1]
#             self.que2 = []
#             self.count2 = 0
#             return temp 
#         elif self.count2 == 0:
#             for i in range(0, (self.count1 - 1)):
#                 self.que2.append(self.que1[i])
#                 self.count2 += 1
#             temp = self.que1[self.count1 - 1]
#             self.que1 = []
#             self.count1 = 0
#             return temp
        
#     def display(self):
#         if (self.count1 + self.count2) == 0:
#             return "Empty queue"
#         elif self.count1 != 0:
#             for i in range(0, self.count1):
#                 print(self.que1[i], end = " ")
#         elif self.count2 != 0:
#             for i in range(0, self.count2):
#                 print(self.que2[i], end = " ")
# o = Solution()
# o.enqueue(1)
# o.enqueue(2)
# o.enqueue(3)
# o.enqueue(4)
# o.enqueue(5)
# o.enqueue(6)
# o.display()
# print()
# o.dequeue()
# o.dequeue()
# o.dequeue()
# print("stack:-")
# o.display()
# print()
# o.enqueue(7)
# o.enqueue(8)
# print("stack:-")
# o.display()



# FINDING THE MAXIMUM ELEMENT IN A WINDOW
# class Window:
#     def __init__(self, arr, w):
#         self.arr = arr
#         self.w = w
#         self.que = [None] * self.w

#     def main(self):
#         low = 0
#         high = self.w
#         for i in range(0, (len(self.arr) - (high - 1))):
#             self.index = 0
#             print()
#             for j in range(low, high):
#                 self.que[self.index] = self.arr[j]
#                 self.index += 1                
#             print(f"Max{i} : ", max(self.que))
#             low += 1
#             high += 1
# size = int(input("Window's size : "))
# lst = list(map(int, input("Enter the array : ").split()))
# o = Window(lst, size)
# o.main()


# from queue import Queue, LifoQueue
# import math
# stk = LifoQueue()
# q = Queue()

# def ins_ele(lst):
#     for i in lst:
#         stk.put(i)
#     return stk

# def main():
#     inp = list(map(int, input("Elements : ").split()))
#     stack = ins_ele(inp)
#     a = None
#     b = None
#     while not stack.empty():
#         q.put(stack.get())
#     if q.qsize() % 2 == 0:
#         for i in range(q.qsize()/2):
#             a = q.get()
#             b = q.get()
#             if a == (b + 1) or b == (a + 1):
#                 print(f"({a}, {b})")
#             else:
#                 return 
#     else:
#         print("Unidentified : ", q.get())
#         for i in range(math.floor(q.qsize()/2)):
#             a = q.get()
#             b = q.get()
#             if a == (b + 1) or b == (a + 1):
#                 print(f"({a}, {b})")
#             else:
#                 return
            
# main()


# problem-10
# from queue import Queue
# import math
# que1 = Queue()
# que2 = Queue()
# def initalize(lst):
#     half = math.ceil(len(lst)/2)
#     for i in lst:
#         que1.put(i)
#     return half

# def main():
#     arr = list(map(int, input("Elements : ").split()))
#     half = initalize(arr)
#     for i in range(half):
#         que2.put(que1.get())
#     for i in range(half):
#         temp1 = que1.get()
#         temp2 = que2.get()
#         que1.put(temp2)
#         que1.put(temp1)
#     return que1
# rs = main()
# while not que1.empty():
#     print(que1.get(), end = " ")

