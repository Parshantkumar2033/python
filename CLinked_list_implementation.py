# CIRCULAR SINGLY LINKED LIST IMPLEMENTATION

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Single:
#     def __init__(self):
#         self.head = None

#     def insertEnd(self, new):
#         if self.head is None:
#             self.head = new
#             new.next = self.head
#             # print(f"\nIFirst node : {new.data} ")
#             return
#         temp = self.head
#         while temp.next is not self.head:
#             temp = temp.next
#         temp.next = new
#         new.next = self.head
#         # print(f"\n{new.data} IEnd")

#     def insertBeg(self, new):
#         if self.head is None:
#             self.head = new
#             new.next = self.head
#             return
#         temp = self.head
#         a = self.head
#         while a.next is not temp:
#             a = a.next
#         a.next = new
#         self.head = new
#         new.next = temp
#         # print(f"\n{new.data} IBeg")

#     def insertSep(self, pos, new):
#         a = self.head.next
#         prev = self.head
#         print(f"\nInserted {new.data} at position {pos}")
#         for i in range(1, pos - 1):
#             a = a.next
#             prev = prev.next
#         prev.next = new
#         new.next = a        

#     def display(self):
#         a = self.head
#         print("Linked List : ", end = "")
#         while a.next is not self.head:
#             print(a.data, end = " ")
#             if a.next is self.head:
#                 break
#             a = a.next

#     def delBeg(self):
#         if self.head is None:
#             return "Empty linked list"
#         a = self.head
#         temp = self.head
#         while True:
#             a = a.next
#             if a.next is self.head:
#                 break
#         self.head = temp.next
#         a.next = self.head
#         temp.next = None
#         print("\nDBeg:-")

#     def delEnd(self):
#         if self.head is None:
#             return "Empty Linked List"
#         a = self.head.next
#         prev = self.head
#         while True:
#             a = a.next 
#             prev = prev.next
#             if a.next is self.head:
#                 break
#         a.next = None
#         prev.next = self.head
#         print("\nDEnd:-")

#     def delSep(self, pos):
#         if self.head is None:
#             return "empty Linked list"
#         a = self.head.next
#         prev = self.head
#         for i in range(1, pos - 1):
#             a = a.next 
#             prev = prev.next
#         prev.next = a.next
#         print(f"\nDelete {a.data} at position {pos}:-")
#         a.next = None

# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# sll = Single()
# sll.insertEnd(n1)
# sll.insertEnd(n2)
# sll.insertEnd(n3)
# sll.insertEnd(n4)
# sll.display()
# n5 = Node(6)
# n6 = Node(7)
# sll.insertBeg(n5)
# sll.insertBeg(n6)
# sll.display()
# n7 = Node(12)
# n8 = Node(13)
# sll.insertSep(5, n7)
# sll.display()
# sll.insertSep(2, n8)
# sll.display()
# sll.delBeg()
# sll.display()
# sll.delEnd()
# sll.display()
# sll.delSep(3)
# sll.display()



# CIRCULAR DOUBLY LINKED LIST IMPLEMENTATION

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None
    
# class Double:
#     def __init__(self):
#         self.head = None
    
#     def insertEnd(self, new):
#         if self.head is None:
#             self.head = new
#             new.next = self.head
#             new.prev = new
#             return
#         a = self.head
#         while a.next is not self.head:
#             a = a.next
#         a.next = new
#         new.prev = a
#         new.next = self.head
#         self.head.prev = new

#     def insertBeg(self, new):
#         if self.head is None:
#             self.head = new
#             new.next = self.head
#             new.prev = new
#             return
#         a = self.head
#         while a.next is not self.head:
#             a = a.next
#         new.next = self.head
#         new.prev = a
#         self.head.prev = new
#         self.head = new
#         a.next = new

#     def insertSep(self, pos, new):
#         a = self.head.next
#         b = self.head
#         for i in range(1, pos - 1):
#             a = a.next 
#             b = b.next
#         b.next = new
#         new.prev = b
#         new.next = a
#         a.prev = new

#     def fdisplay(self):
#         print()
#         a = self.head
#         print("Forward : ", end = "")
#         while True:
#             print(a.data, end = " ") 
#             if a.next is self.head:
#                 break
#             a = a.next 

#     def bdisplay(self):
#         print()
#         a = self.head
#         temp = self.head
#         print("Backward : ", end = "")
#         while True:
#             a = a.prev
#             print(a.data, end = " ")
#             if a is self.head:
#                 break

#     def delEnd(self):
#         a = self.head
#         a = a.prev
#         b = a.prev
#         b.next = self.head
#         self.head.prev = b
#         a.next = None
#         a.prev = None

#     def delBeg(self):
#         a = self.head
#         b = a.prev
#         an = a.next
#         self.head = an
#         b.next = an
#         an.prev = b
#         a.prev = None
#         a.next = None

#     def delSep(self, pos):
#         a = self.head.next
#         b = self.head
#         for i in range(1, pos - 1):
#             a = a.next 
#             b = b.next
#         b.next = a.next
#         a.next.prev = b
#         a.next = None
#         a.prev = None
        
# n1 = Node(2)
# n2 = Node(3)
# n3 = Node(5)
# n4 = Node(6)
# n5 = Node(4)
# dll = Double()
# dll.insertEnd(n1)
# dll.insertEnd(n2)
# dll.insertEnd(n3)
# dll.insertEnd(n4)
# dll.insertEnd(n5)
# dll.fdisplay()
# dll.bdisplay()
# n6 = Node(10)
# n7 = Node(11)
# dll.insertBeg(n6)
# dll.insertBeg(n7)
# dll.fdisplay()
# dll.bdisplay()
# n8 = Node(21)
# n9 = Node(20)
# dll.insertSep(3, n8)
# dll.fdisplay()
# dll.insertSep(3, n9)
# dll.fdisplay()
# dll.delEnd()
# dll.fdisplay()
# dll.delBeg()
# dll.fdisplay()
# dll.delSep(3)
# dll.delSep(5)
# dll.fdisplay()