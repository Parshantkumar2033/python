# IMPLEMENTATION OF SINGLY LINKED LIST

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Single:
#     def __init__(self):
#         self.head = None

#     def traversal(self):
#         if self.head is None:
#             print("Empty linked list")
#         else:
#             a = self.head
#             while a is not None:
#                 print(a.data, end = " ")
#                 a = a.next

#     def insert_at_beg(self, ndata):
#         print()
#         new = Node(ndata)
#         new.next = self.head
#         self.head = new
    
#     def insert_at_end(self, ndata):
#         print()
#         new = Node(ndata)
#         a = self.head
#         while a.next is not None:
#             a = a.next
#         a.next = new

#     def insert_at_sep(self, pos, ndata):
#         print()
#         new = Node(ndata)
#         a = self.head
#         for i in range(1, pos - 1):
#             a = a.next
#         new.next = a.next         
#         a.next = new
    
#     def del_at_beg(self):
#         print()
#         a = self.head
#         self.head = a.next
#         a.next = None
    
#     def del_at_end(self):
#         print()
#         prev = self.head
#         n = self.head.next
#         while n.next is not None:
#             n = n.next
#             prev = prev.next
#         prev.next = None

#     def del_at_sep(self, pos):
#         print()
#         p1 = self.head.next
#         p2 = self.head
#         for i in range(1, pos - 1):
#             p1 = p1.next
#             p2 = p2.next
#         p2.next = p1.next
#         p1.next = None      

# ls = Single() 
# n1 = Node(2)
# ls.head = n1
# n2 = Node(4)
# n1.next = n2
# n3 = Node(5)
# n2.next = n3
# n4 = Node(8)
# n3.next = n4
# ls.traversal()
# ls.insert_at_beg(10)
# ls.insert_at_end(15)
# ls.insert_at_end(17)
# ls.traversal()
# ls.del_at_end()
# ls.traversal()
# ls.del_at_sep(3)
# ls.traversal()

# IMPLEMENTING DOUBLY LINKED LIST
# modified

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class Double:
#     def __init__(self):
#         self.head = None
#         self.count = 0

#     def forward_traversal(self):
#         print()
#         if self.head is None:
#             print("Empty linked list")
#         else:
#             a = self.head
#             while a is not None:        # here we are reaching up to the very last pointer
#                 print(a.data, end = " ")
#                 a = a.next

#     def backward_traversal(self):
#         print()
#         if self.head is None:
#             print("Empty linked list")
#         else:
#             a = self.head 
#             while a.next is not None:       # here we are not supposed to reach the last pointer,
#                 a = a.next                  # we will not traverse up to the pointer of the last node
#             while a is not None:
#                 print(a.data, end =  " ")
#                 a = a.prev

#     def insert_at_beg(self, data):
#         print()
#         new = Node(data)
#         a = self.head       # currently head present at n1('a' here)
#         a.prev = new        # pointing n1.previous to new node created
#         new.next = a        # and pointing new node's pointer to the n1
#         self.head = new     # updating the n1 to be new head of the linked list

#     def insert_at_end(self, data):
#         print()
#         new = Node(data)
#         a = self.head
#         while a.next is not None:   # traversing upto the very last node
#             a = a.next
#         a.next = new        # pointing the last node's pointer to new node
#         new.prev = a        # pointing the new node's pointer to the previous node (i.e. "a" here)
#         new.next = None 

#     def insert_at_sep(self, pos, data):
#         print()
#         new = Node(data)
#         a = self.head
#         for i in range(1, pos - 1):
#             a = a.next
#         new.prev = a
#         new.next = a.next
#         a.next.prev = new
#         a.next = new

#     def del_at_beg(self):
#         print()
#         a = self.head
#         self.head = a.next
#         a.next = None
#         self.head.prev = None
    
#     def del_at_end(self):
#         print()
#         a = self.head.next 
#         b = self.head
#         while a.next is not None:
#             a = a.next
#             b = b.next
#         b.next = a.next     # b.next = a.next (that is None)
#         a.prev = None       # a.prev = None ( in order to remove the pointer to the previous node)

#     def del_at_sep(self, pos):
#         print()
#         a = self.head.next
#         b = self.head
#         for i in range(1, pos - 1):
#             a = a.next 
#             b = b.next
#         b.next = a.next
#         a.next.prev = b
#         a.next = None       # removing the next and previous pointer
#         a.prev = None

#     def length(self):
#         print()
#         a = self.head 
#         while a is not None:
#             a = a.next
#             self.count += 1

#         return self.count
    
#     def delete(self, data):     # if you want to delete any data
#         print()
#         n = self.head
#         a = self.head.next
#         b = self.head
#         while a.data != data:
#             a = a.next
#             b = b.next
#             if a.next is None:
#                 print("Error!...")
#                 print(f"{data} not present")
#                 return
        
#         b.next = a.next
#         a.next.prev = b
#         # a.next = None
#         # a.prev = None
#         print("New linked list : ", end = "")
#         if self.head is None:
#             print("Empty linked list!")
#         else:
#             while n is not None:
#                 print(n.data, end = " ")
#                 n = n.next

# n1 = Node(2)
# sl = Double()
# sl.head = n1

# n2 = Node(6)
# n2.prev = n1
# n1.next = n2

# n3 = Node(9)
# n3.prev = n2
# n2.next = n3

# n4 = Node(1)
# n4.prev = n3
# n3.next = n4

# n5 = Node(5)
# n4.next = n5
# n5.prev = n4

# n6 = Node(8)
# n5.next = n6
# n6.prev = n5

# sl.forward_traversal()
# sl.backward_traversal()

# sl.del_at_end()
# sl.forward_traversal()

# sl.del_at_sep(2)
# sl.forward_traversal()

# print("inserted at end")
# sl.insert_at_end(10)
# sl.insert_at_sep(4, 12)
# sl.insert_at_sep(6, 15)
# print("12 is inserted at 4 and 15 is inserted at 6")
# sl.forward_traversal()
# print("The length of the linked list : ", sl.length())
# sl.delete(9)
# sl.delete(3)




# IMPLEMENTING DOUBLY LINKED LIST

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class Double:
#     def __init__(self):
#         self.head = None
#         self.count = 0

#     def forward_traversal(self):
#         print()
#         if self.head is None:
#             print("Empty linked list")
#         else:
#             a = self.head
#             while a is not None:        # here we are reaching up to the very last pointer
#                 print(a.data, end = " ")
#                 a = a.next

#     def backward_traversal(self):
#         print()
#         if self.head is None:
#             print("Empty linked list")
#         else:
#             a = self.head 
#             while a.next is not None:       # here we are not supposed to reach the last pointer,
#                 a = a.next                  # we will not traverse up to the pointer of the last node
#             while a is not None:
#                 print(a.data, end =  " ")
#                 a = a.prev

#     def insert_at_beg(self, data):
#         new = Node(data)
#         a = self.head       # currently head present at n1('a' here)
#         a.prev = new        # pointing n1.previous to new node created
#         new.next = a        # and pointing new node's pointer to the n1
#         self.head = new     # updating the n1 to be new head of the linked list

#     def insert_at_end(self, data):
#         new = Node(data)
#         a = self.head
#         while a.next is not None:   # traversing upto the very last node
#             a = a.next
#         a.next = new        # pointing the last node's pointer to new node
#         new.prev = a        # pointing the new node's pointer to the previous node (i.e. "a" here)
#         new.next = None 

#     def insert_at_sep(self, pos, data):
#         print()
#         new = Node(data)
#         a = self.head
#         for i in range(1, pos - 1):
#             a = a.next
#         new.prev = a
#         new.next = a.next
#         a.next.prev = new
#         a.next = new

#     def del_at_beg(self):
#         print()
#         a = self.head
#         self.head = a.next
#         a.next = None
#         self.head.prev = None
    
#     def del_at_end(self):
#         print()
#         a = self.head.next 
#         b = self.head
#         while a.next is not None:
#             a = a.next
#             b = b.next
#         b.next = a.next     # b.next = a.next (that is None)
#         a.prev = None       # a.prev = None ( in order to remove the pointer to the previous node)

#     def del_at_sep(self, pos):
#         print()
#         a = self.head.next
#         b = self.head
#         for i in range(1, pos - 1):
#             a = a.next 
#             b = b.next
#         b.next = a.next
#         a.next.prev = b
#         a.next = None       # removing the next and previous pointer
#         a.prev = None

#     def length(self):
#         a = self.head 
#         while a is not None:
#             a = a.next
#             self.count += 1

#         return self.count


# n1 = Node(2)
# sl = Double()
# sl.head = n1

# n2 = Node(6)
# n2.prev = n1
# n1.next = n2

# n3 = Node(9)
# n3.prev = n2
# n2.next = n3

# n4 = Node(1)
# n4.prev = n3
# n3.next = n4

# n5 = Node(5)
# n4.next = n5
# n5.prev = n4

# n6 = Node(8)
# n5.next = n6
# n6.prev = n5

# sl.forward_traversal()
# sl.backward_traversal()

# sl.del_at_end()
# sl.forward_traversal()

# sl.del_at_sep(2)
# sl.forward_traversal()

# print("\ninserted at end")
# sl.insert_at_end(10)
# sl.insert_at_sep(4, 12)
# sl.insert_at_sep(6, 15)
# print("\n12 is inserted at 4 and 15 is inserted at 6")
# sl.forward_traversal()
# print("\nThe length of the linked list : ", sl.length())


