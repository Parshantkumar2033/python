# IMPLEMENTING STACK USING LINKED LIST
# here the list pointing from newly created node to the oldest node being the last element in the linked list
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Stack:
#     def __init__(self):
#         self.head = None
#         self.length = 0


#     def put(self, data):
#         n = Node(data)
#         a = self.head       # a is previous self.head
#         self.head = n       # now, the newly created node will become the head of the stack
#         self.head.next = a  # and the new node will be pointing to the previous node which was saved in "a" earlier
#         self.length += 1

#     def get(self):
#         if self.length == 0:
#             return "Empty stack"
#         a = self.head       # self.head is the last element in the stack
#         self.head = a.next  # shifting the head to the next node
#         a.next = None       # making the node to be pointing None, top element to be removed from the stack
#         self.length -= 1
#         return a.data       # returning the data of the node whose next pointed is pointing null

#     def isEmpty(self):
#         if self.length == 0:
#             return True
#         else:
#             return False

#     def peek(self):
#         if self.isEmpty():
#             return None
#         else:
#             return self.head.data

#     def size(self):
#         return self.length

# stack = Stack()
# stack.put(1)
# stack.put(2)
# stack.put(3)
# stack.put(4)
# stack.put(5)
# print("No. of elements : ", stack.size())
# print("Removed : ", stack.get())
# print("Removed : ", stack.get())
# print("No. of elements : ", stack.size())
# print("Peek : ", stack.peek())
# stack.put(12)
# stack.put(13)
# stack.put(14)
# print("size : ", stack.size())
# print("Peek : ", stack.peek())


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Single:
#     def __init__(self):
#         self.head = None
#         self.nodes = 1

#     def traversal(self):
#         print()
#         if self.head is None:
#             print("Empty linked list")
#         else:
#             a = self.head
#             while a is not None:
#                 print(a.data, end=" ")
#                 a = a.next

#     def insert_at_beg(self, ndata):
#         print()
#         new = Node(ndata)
#         new.next = self.head
#         self.head = new

#     def insert_at_end(self, ndata):
#         print()
#         new = Node(ndata)
#         if self.head is None:
#             self.head = new
#             return
#         a = self.head
#         while a.next is not None:
#             a = a.next
#         a.next = new
#         new.next = None

#     def insert_at_sep(self, pos, ndata):
#         print()
#         new = Node(ndata)
#         a = self.head
#         for i in range(1, pos - 1):
#             a = a.next
#         new.next = a.next
#         a.next = new

#     def del_at_beg(self):
#         # print()
#         a = self.head
#         self.head = a.next
#         # temp = a
#         a.next = None
#         return a.data

#     def del_at_end(self):
#         print()
#         prev = self.head
#         n = self.head.next
#         while n.next is not None:
#             n = n.next
#             prev = prev.next
#         prev.next = None
#         return n.data

#     def del_at_sep(self, pos):
#         print()
#         p1 = self.head.next
#         p2 = self.head
#         for i in range(1, pos - 1):
#             p1 = p1.next
#             p2 = p2.next
#         p2.next = p1.next
#         p1.next = None
#         return p1.data

#     def insert(self, new):
#         if self.head is None:
#             self.head = new
#             new.next = None
#             return
#         a = self.head
#         while a.next is not None:
#             a = a.next
#         a.next = new
#         new.next = None
#         self.nodes += 1

#     def tail(self, new):
#         a = self.head
#         while a.next is not None:
#             a = a.next
#         a.next = new

#     def ele_from_last(self, pos):
#         a = self.head
#         prev = self.head
#         for i in range(1, pos - 1):
#             a = a.next
#             if a.next is None:
#                 return print("\nNo such position is present in the linked list")
#         a = a.next
#         while a.next is not None:
#             a = a.next
#             prev = prev.next
#         return print(f"\n{pos}th element from end is : ", prev.data)

#     # using brute force
#     # def find_loop(self):
#     #     a = self.head
#     #     visited = []

#     #     while a.next is not None:
#     #         if a not in  visited:
#     #             visited.append(a)
#     #         else:
#     #             return print("Loop present")
#     #         a = a.next

#     #     return print("No loop present")

#     # using hash table
#     # def find_loop(self):
#     #     ele = dict()
#     #     a = self.head
#     #     while a.next is not None:
#     #         if a in ele:
#     #             temp = self.head
#     #             count = 1
#     #             while True:
#     #                 if temp is a:
#     #                     print("Position(of loop) : ", count)
#     #                     return
#     #                 temp = temp.next
#     #                 count += 1
#     #         ele[a] = a.data
#     #         a = a.next
#     #     return "No loop is present"



#     # using the floyd cycle finding algorithm
#     # "b" pointer steps one step at each iteration whereas "a" pointer steps two step at each iteration
#     # def find_loop(self):
#     #     a = self.head
#     #     b = self.head
#     #     pos = 1
#     #     check = False
#     #     while a is not None and a.next is not None:
#     #         a = a.next.next
#     #         b = b.next
#     #         if b == a:
#     #             check = True
#     #             break 
#     #     b = self.head
#     #     if check == True:           
#     #         while b != a:
#     #             b = b.next
#     #             a = a.next
#     #             pos += 1
#     #         return b, pos
#     #     return "No loop is present", 0

#     def find_loop(self):
#         a = self.head
#         b = self.head
#         pos = 1
#         check = False
#         while a is not None and a.next is not None:
#             a = a.next.next
#             b = b.next
#             if b == a:
#                 check = True
#                 break 
#         b = self.head
#         if check == True:           
#             while b != a:
#                 b = b.next
#                 # a = a.next
#                 pos += 1
#             return b, pos
#         return "No loop is present", 0
    
#     # returns the data of the node from which the loop begins
#     def data_return(self, b):
#         temp = self.head
#         while temp.next is not None:
#             if temp == b:
#                 break
#             temp = temp.next
#         return temp.data

#     def loop_length(self):
#         b, pos = self.find_loop()
#         length = self.nodes - pos + 1
#         return length
    
#     def delete(self):
#         while self.head is not None:
#             self.del_at_beg()
#             print(end = "")

#     def sort_ll(self):
#         arr = []
#         a = self.head
#         while a is not None:
#             arr.append(a.data)
#             a = a.next
#         arr.sort()
#         self.delete()
#         for i in arr:
#             n = Node(i)
#             self.insert(n)
        
    
#     def sort_insert(self, num):
#         temp = self.head
#         ah = self.head.next
#         while ah.data <= num:
#             if ah.next is None:
#                 break
#             temp = temp.next
#             ah = ah.next
#         if ah.next is None:
#             n = Node(num)
#             ah.next = n
#             n.next = None
#         elif temp is self.head:
#             n = Node(num)            
#             self.head = n
#             n.next = temp
#         else:
#             n = Node(num)
#             temp.next = None
#             temp.next = n
#             n.next = ah
    
#     # reversing linked list using the iteration method
#     # def reverse_list(self):
#     #     prev = None
#     #     curr = self.head
#     #     while curr is not None:
#     #         nxt = curr.next
#     #         curr.next = prev
#     #         prev = curr
#     #         curr = nxt
#     #     self.head = prev

#     #     temp = self.head
#     #     while temp is not None:
#     #         print(temp.data, end = " ")
#     #         temp = temp.next

#     # reversing linked list using the recursion method
#     def reverse_list(self, head):
#         if head is None or head.next is None:
#             return head
#         rest = self.reverse_list(head.next)
#         head.next.next = head
#         head.next = None
#         return rest
    

#     # problem 26
#     # finding the middle of the linked list
#     def middle_element(self):
#         if self.head is None:
#             return print("Empty Linked List")
#         a = self.head 
#         b = self.head
#         while b.next is not None:
#             a = a.next
#             b = b.next.next
#             if b is None:
#                 return print(a.data)
#             if b.next is None:
#                 return print(a.data)

#     # odd-even length of the list      
#     def even_odd(self):
#         b = self.head
#         while True:
#             if b is None:
#                 return print("even length")
#             elif b.next is None:
#                 return print("odd length")
#             b = b.next.next

# sll = Single()
# n1 = Node(14)
# sll.insert(n1)
# n2 = Node(13)
# sll.insert(n2)
# n3 = Node(12)
# sll.insert(n3)
# n4 = Node(10)
# sll.insert(n4)
# n5 = Node(5)
# sll.insert(n5)
# n6 = Node(4)
# sll.insert(n6)
# n7 = Node(3)
# sll.insert(n7)
# n8 = Node(2)
# sll.insert(n8)
# n9 = Node(1)
# sll.insert(n9)
# n10 = Node(0)
# sll.insert(n10)
# sll.tail(None)
# sll.even_odd()


# sll.middle_element()
# sll.traversal()
# sll.head = sll.reverse_list(sll.head)
# sll.traversal()
# sll.sort_ll()
# num = int(input("\nNumber : "))
# sll.sort_insert(num)
# sll.traversal()
# b, pos = sll.find_loop()
# print("b : ", b)
# print("Starting position of loop : ", pos)
# print("Data at the loop start : ", sll.data_return(b))
# print('Length of the loop : ', sll.loop_length())





## PROBLEM 17

# find the intersection position of the two linked lists 
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class Single:
#     def __init__(self):
#         self.head = None
#         self.nodes = 1

#     def traversal(self):
#         print()
#         if self.head is None:
#             print("Empty linked list")
#         else:
#             a = self.head
#             while a is not None:
#                 print(a.data, end=" ")
#                 a = a.next

#     def insert(self, new):
#         if self.head is None:
#             self.head = new
#             new.next = None
#             return
#         a = self.head
#         while a.next is not None:
#             a = a.next
#         a.next = new
#         new.next = None
#         self.nodes += 1

#     def tail(self, new):
#         a = self.head
#         while a.next is not None:
#             a = a.next
#         a.next = new

# sll1 = Single()
# n1 = Node(1)
# sll1.insert(n1)
# n2 = Node(3)
# sll1.insert(n2)
# n3 = Node(2)
# sll1.insert(n3)
# n4 = Node(10)
# sll1.insert(n4)
# n5 = Node(7)
# sll1.insert(n5)
# n6 = Node(11)
# sll1.insert(n6)

# sll2 = Single()
# m1 = Node(8)
# sll2.insert(m1)
# m2 = Node(12)
# sll2.insert(m2)
# m3 = Node(2)
# sll2.insert(m3)
# m4 = Node(5)
# sll2.insert(m4)
# m5 = Node(15)
# sll2.insert(m5)
# sll2.tail(n4)

# sll1.tail(None)
# sll1.traversal()
# print()
# sll2.traversal()

# n = sll1.head
# hash_table = dict()
# while n is not None:
#     hash_table[n] = n
#     n = n.next

# m = sll2.head
# temp = None
# while m is not None:
#     if m not in hash_table:    
#         hash_table[m] = m
#     elif m in hash_table:
#         temp = hash_table[m]
#         break
#     m = m.next

# count = 1
# a = sll1.head
# while a != temp:
#     a = a.next 
#     count += 1

# count2 = 1
# b = sll2.head
# while b != temp:
#     b = b.next
#     count2 += 1
# print("\nPosition(1st) : ", count)
# print("Position(2ndt) : ", count2)




## PROBLEM : 31
# MERGING TWO SORTED LINKED LISTS
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Single:
    def __init__(self):
        self.head = None
        self.nodes = 0

    def traversal(self):
        print()
        if self.head is None:
            print("Empty linked list")
        else:
            a = self.head
            while a is not None:
                print(a.data, end=" ")
                a = a.next

    def insert(self, new):
        self.nodes += 1
        if self.head is None:
            self.head = new
            new.next = None
            return
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = new
        new.next = None
        self.nodes += 1
    
    def length(self):
        return self.nodes

    def tail(self, new):
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = new

    def sort_ll(self):
        arr = []
        a = self.head
        while a is not None:
            arr.append(a.data)
            a = a.next
        arr.sort()
        self.delete()
        for i in arr:
            n = Node(i)
            self.insert(n)
    
    def delete(self):
        while self.head is not None:
            self.del_at_beg()
            print(end = "")

    def del_at_beg(self):
        a = self.head
        self.head = a.next
        a.next = None
        return a.data
    
    # method for merging the two linked lists using list and sorting.   Time complexity : O((l + m)log(l + m))
    def merge_sorted(self, h1, h2):
        head1 = h1
        head2 = h2
        a = []
        b = []
        l = -1
        m = -1
        while head1 is not None:
            a.append(head1.data)
            l += 1
            head1 = head1.next

        while head2 is not None:
            b.append(head2.data)
            m += 1
            head2 = head2.next

        print(a)
        print(b)
        arr = []
        i = 0
        j = 0
        while True:
            if i < l and j < m:
                if a[i] < b[j]:
                    arr.append(a[i]) 
                    i += 1
                elif a[i] == b[j]:
                    arr.append(a[i])
                    i += 1
                else:
                    arr.append(b[j])
                    j += 1

            elif i <= l:
                arr.append(a[i])
                i += 1

            elif j <= m:
                arr.append(b[j])
                j += 1

            else:
                print("both lists finished")
                break
        print(arr)

        self.delete()
        for i in arr:
            n = Node(i)
            self.insert(n)

    # reversing the linked list in pairs
    def pair_reverse(self):
        if self.head is None:
            return print("Empty linked list")
        a = self.head
        b = self.head.next
        while b is not None:
            a.data, b.data = b.data, a.data
            a = a.next
            if a.next is None:
                break
            else:
                a = a.next
                b = b.next.next

# for merging the two sorted linked lists.  Time complexity : O(l + m), where 'l' and 'm' are the lengths of the linked lists
class Merge:
    def __init__(self):
        self.sll = Single()

    def merge_sorted_ll(self, obj1, obj2):
        head1 = obj1.head
        head2 = obj2.head
        if head1 is None and head2 is None:
           return print("Both Linked List are empty.")
        while True:
            if head1 is not None and head2 is not None:
                if head1.data <= head2.data:
                    n = Node(head1.data)
                    self.sll.insert(n)
                    head1 = head1.next

                elif head2.data < head1.data:
                    n = Node(head2.data)
                    self.sll.insert(n)
                    head2 = head2.next
            
            elif head1 is None and head2 is not None:
                n = Node(head2.data)
                self.sll.insert(n)
                head2 = head2.next

            elif head2 is None and head1 is not None:
                n = Node(head1.data)
                self.sll.insert(n)
                head1 = head1.next
            
            else:
                print("\nFINISHED LINKED LISTS.")
                break
        print("\nsll.traversal()")
        a = self.sll.head
        print("sorted linked list : ", end = "")
        while a is not None:
            print(a.data, end = " ")
            a = a.next

            
sll1 = Single()
n1 = Node(1)
sll1.insert(n1)
n2 = Node(3)
sll1.insert(n2)
n3 = Node(2)
sll1.insert(n3)
n4 = Node(10)
sll1.insert(n4)
n5 = Node(7)
sll1.insert(n5)
n6 = Node(11)
sll1.insert(n6)
n7 = Node(0)
sll1.insert(n7)
sll1.tail(None)

sll2 = Single()
m1 = Node(8)
sll2.insert(m1)
m2 = Node(12)
sll2.insert(m2)
m3 = Node(2)
sll2.insert(m3)
m4 = Node(5)
sll2.insert(m4)
m5 = Node(15)
sll2.insert(m5)
m6 = Node(9)
sll2.insert(m6)
sll2.tail(None)

print("Original : ", end = "")
sll1.traversal()
sll1.pair_reverse()
sll1.traversal()

# sll1.sort_ll()
# sll2.sort_ll()

# mrg = Merge()
# mrg.merge_sorted_ll(sll1, sll2)

# print()
# var1 = sll1.head
# var2 = sll2.head
# sll1.merge_sorted(var1, var2)
# sll1.traversal()