class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Single:
    def __init__(self):
        self.head = None
        self.nodes = 0

    def traversal(self):
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
        if self.head is None:
            return print("Empyt linked list.")
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
        b = self.head
        while b is not None:
            a.data, b.data = b.data, a.data
            a = a.next
            if a.next is None:
                break
            else:
                a = a.next
                b = b.next.next


    # splitting a linked lists in halves
    def split_list(self):
        if self.head is None:
            return print("Empty linked list")
        a = self.head
        b = self.head

        while a.next is not self.head:
            a = a.next
            if a.next is self.head:
                break
            else:
                a = a.next
                b = b.next
        temp2 = b.next
        temp1 = a.next
        b.next = None
        a.next = None
        return temp1, temp2             # temp1 and temp2 are heads of new splitted linked lists


    # reversing a linked list
    def reverse_list(self, head):
        if head is None or head.next is None:
            return head
        rest = self.reverse_list(head.next)
        head.next.next = head
        head.next = None
        return rest


    # checking palindrome in a circular linked list
    def panlindrome(self):
        if self.head is None:
            return print("Empty linked list")
        
        # splitting the linked list
        p1 = self.head
        p2 = self.head
        while p1.next is not self.head:
            p1 = p1.next
            if p1.next is self.head:
                break
            else:
                p1 = p1.next
                p2 = p2.next
        temp1 = p1.next
        temp2 = p2.next
        p1.next = None
        p2.next = None

        # reversing the second linked list
        prev = None
        curr = temp2
        while curr.next is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        curr.next = prev

        temp2 = curr
        # temp2 has become the head for the second list(after split)
        # traversing the list for checking
        # while temp2 is not None:
        #     print(temp2.data, end = " ") 
        #     temp2 = temp2.next
        # print()
        while temp1.next is not None and temp2 is not None:
            if temp1.data == temp2.data:
                temp1 = temp1.next
                temp2 = temp2.next
            else:
                return print("Not a palindrome")
        return print("palindrome")

    # PROBLEM 41
    def cloning_list(self, obj):
        a = obj.head
        table = dict()
        if a is None:
            return print("Empty list")
        while a is not None:
            new = Node(a.data)
            table[a] = new
            a = a.next
        b = obj.head
        prev = None
        while b is not None:

            # 1st method
            # we can use insert() method too but, in this method we have to iterate again 
            # and again to get to the last node
            # self.insert(table[b])                
            # b = b.next

            # 2nd method
            # in this case we keep track of the prev node and just pointing that
            # node to the next node
            if self.head is None:
                self.head = table[b]
                self.head.next = None
                prev = self.head
                b = b.next
                continue
            prev.next = table[b]
            prev = prev.next
            prev.next = None
            b = b.next
            
    # more efficient method for the cloning of a linked list 
    # as it doesn't need to iterate over for the setting the pointers.
    # all requirement things are done in one scan
    def clone_no_space(self, obj):
        a = obj.head
        prev = None
        while a is not None:
            if self.head is None:
                n = Node(a.data)
                self.head = n
                prev = n
                n.next = None
                a = a.next
                continue
            n = Node(a.data)
            prev.next = n
            n.next = None
            prev = prev.next
            a = a.next


    # aranging the even elements in the beginning of the linked list 
    # without deforming the order
    def arange_list(self):
        prev = None
        curr = self.head
        o = None
        temp = None
        a = None
        while curr is not None:
            if curr.data % 2 == 0:
                if prev is None:
                    a = curr
                    prev = curr
                    curr = curr.next
                    continue
                prev.next = curr
                prev = curr
                curr = curr.next
                continue
            if curr.data % 2 == 1:
                if o is None:
                    temp = curr
                    o = curr
                    curr = curr.next
                    continue
                o.next = curr
                o = o.next
                curr = curr.next
                continue
        if prev is not None:
            prev.next = temp
            o.next = None
            self.head = a
        else:
            self.head = temp

    # finding first modular node from the end of the linked list
    def modular_node(self, k):
        prev = None
        count = 1
        table = dict()
        curr = self.head
        if k <= 0:
            return None, None
        while curr is not None:
            if prev is None:
                if count % k == 0:
                    prev = curr
                    curr = curr.next
                    count += 1
                    table[prev] = count - 1
                    continue
                else:
                    curr = curr.next
                    count += 1
                    continue
            if count % k == 0:
                prev = curr
                curr = curr.next
                count += 1
                table[prev] = count - 1
            else:
                curr = curr.next
                count += 1
        if prev is None:
            return "No such node possible", None 

        return table[prev], prev.data
    

    # finding fractional node
    def fractional_node(self, m):
        import math
        a = self.head
        f = None

        size = 0
        while a is not None:
            a = a.next
            size += 1
            if a is not None:
                a = a.next 
                size += 1
                if a is not None:
                    a = a.next
                    size += 1
        print("Size : ", size)
        if size < m:
            return print("No such node possible"), None
        curr = self.head
        for i in range(1, math.ceil(size/m)):
            curr = curr.next
        return curr, math.ceil(size/m)

    # find the root(nth) node in the linked list, given n is no. of nodes
    def root_node(self):
        import math
        if self.head is None:
            return "Empty linked list"
        curr = self.head
        prev = None
        i = 1
        while curr is not None:
            if prev is None:
                prev = math.isqrt(i)
                curr = curr.next
                i += 1
                continue
            prev =  math.isqrt(i)
            curr = curr.next
            i += 1
        return prev


    # # reversing first k elements in a list                        # ERROR!
    # def first_k_reverse(self, k):

    #     # split the first k size list
    #     a = self.head
    #     for i in range(1, k):
    #         a = a.next
    #     p = a.next
    #     a.next = None

    #     # reversing the list with first k elements
    #     prev = None
    #     curr = self.head
    #     while curr.next is not None:
    #         nxt = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = nxt
    #     curr.next = prev
    #     temp = curr


    #     # merging the two lists, making the original one
    #     while temp.next is not None:
    #         temp = temp.next
    #     temp.next = p
    #     self.head = temp

    #     ptr = self.head 
    #     while ptr.next is not None:
    #         ptr = ptr.next
    #     ptr.next = self.head







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
n1 = Node(2)
n2 = Node(8)
n3 = Node(6)
n4 = Node(12)
n5 = Node(0)
n6 = Node(4)
n7 = Node(14)
n8 = Node(10)
n9 = Node(16)
n10 = Node(18)
sll1.insert(n1)
sll1.insert(n2)
sll1.insert(n3)
sll1.insert(n4)
sll1.insert(n5)
sll1.insert(n6)
sll1.insert(n7)
sll1.insert(n8)
sll1.insert(n9)
sll1.insert(n10)
n10.next = None

sll1.traversal()
print()

# for merging two linked lists having elements in ascending order
# sll2 = Single()
# m1 = Node(1)
# m2 = Node(11)
# m3 = Node(5)
# m4 = Node(3)
# m5 = Node(7)
# m6 = Node(15)
# m7 = Node(13)
# m8 = Node(9)
# sll2.insert(m1)
# sll2.insert(m2)
# sll2.insert(m3)
# sll2.insert(m4)
# sll2.insert(m5)
# sll2.insert(m6)
# sll2.insert(m7)
# sll2.insert(m8)
# m8.next = None

# sll2.traversal()
# print()

# sll1.sort_ll()
# print("sll1.sorted : ", end = "")
# sll1.traversal()
# print()

# sll2.sort_ll()
# print("sll2.sorted : ", end = "")
# sll2.traversal()
# print()

# mrg = Merge()
# mrg.merge_sorted_ll(sll1, sll2)


# finding the root(nth) node
# node = sll1.root_node()
# print(node)

# node , pos = sll1.fractional_node(4)
# print("Data : ", node.data)
# print("position : ", pos)

# node , data = sll1.modular_node(15)
# print("Node position : ", node)
# print("Data : ", data)

# sll1.arange_list()
# sll1.traversal()
# sll2 = Single()
# # sll2.cloning_list(sll1)
# # sll2.traversal()

# print()
# sll2.clone_no_space(sll1)
# sll2.traversal()

# print("Original : ", end = "")
# sll1.traversal()
# # a, b = sll1.split_list()
# # while a is not None:
# #     print(a.data, end = " ")
# #     a = a.next
# # print()
# # while b is not None:
# #     print(b.data, end = " ")
# #     b = b.next
# # print()
# # sll1.panlindrome()
# sll1.first_k_reverse(4)
# sll1.traversal()








# PROBLEMS ON CIRCULAR SINGLY LINKED LIST 
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
#         print(a.data)

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

#     def joseph_function(self, m):
#         if m == 0:
#             return print("Invalid number")
#         if self.head is None:
#             return print("Empty linked list")
#         prev = None
#         curr = self.head
#         if m == 1:
#             a = self.head
#             while a.next is not self.head:
#                 a = a.next
#             while True:
#                 if curr.next == curr:
#                     break
#                 a.next = curr.next
#                 temp = curr.next
#                 curr.next = None
#                 curr = temp
#             self.head = curr
#             return

#         # while curr.next != curr:              # O(m*n)
#         #     for i in range(0, m - 1):
#         #         prev = curr
#         #         curr = curr.next
#         #     prev.next = curr.next
#         #     print("Deleted : ", curr.data)
#         #     temp = curr.next
#         #     curr.next = None
#         #     curr = temp
#         # self.head = curr
#         # print()

#         count = 1                               # O(n) : if m is smaller comparitively to n
#         while curr.next != curr:                # O(m*n) : if m is almost equal to n
#             if count == m:
#                 count = 0
#                 prev.next = curr.next
#                 prev = curr
#                 print("Deleted : ", curr.data)
#                 temp = curr.next
#                 curr.next = None
#                 curr = temp
#             else:
#                 prev = curr
#                 curr = curr.next
#             count += 1
#         self.head = curr

        



# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# n5 = Node(5)
# n6 = Node(6)
# n7 = Node(7)
# n8 = Node(8)
# n9 = Node(9)
# n10 = Node(10)
# n11 = Node(11)
# n12 = Node(12)
# n13 = Node(13)
# n14 = Node(14)
# sll = Single()
# sll.insertEnd(n1)
# sll.insertEnd(n2)
# sll.insertEnd(n3)
# sll.insertEnd(n4)
# sll.insertEnd(n5)
# sll.insertEnd(n6)
# sll.insertEnd(n7)
# sll.insertEnd(n8)
# sll.insertEnd(n9)
# sll.insertEnd(n10)
# sll.insertEnd(n11)
# sll.insertEnd(n12)
# sll.insertEnd(n13)
# sll.insertEnd(n14)
# # sll.display()
# # n = int(input("Number to be eliminate : "))
# # sll.joseph_function(n)
# # sll.display()

