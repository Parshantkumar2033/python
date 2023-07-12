# from queue import LifoQueue
# import math as m
# class Solution:
#     def __init__(self, arr):
#         self.stack1 = LifoQueue()
#         self.stack2 = LifoQueue()
#         self.list = arr

#     def __str__(self):
#         return self.stack1.get() and self.stack2.get()
    
#     def solve(self):
#         low = 0
#         high = len(self.list) 
#         mid = m.ceil(( low + high )/2)
#         count1 = 0
        
#         for i in self.list:
#             if count1 < mid :
#                 self.stack1.put(i)
#                 count1 += 1
#             elif count1 >= mid and count1 < high :
#                 self.stack2.put(i)
#                 count1 += 1

#         self.new_list1 = []
#         self.new_list2 = []
#         while not self.stack1.empty():
#             self.new_list1.append(self.stack1.get())
#         while not self.stack2.empty():
#             self.new_list2.append(self.stack2.get())
#         return self.new_list1 , self.new_list2    
    
# a = list(map(int, input("Elements(with spaces) : ").split()))
# solution = Solution(a)
# result1, result2 = solution.solve()
# print(result1)    
# print(result2)


from queue import LifoQueue
import math 

class Solution:
    def __init__(self, arr, m):
        self.list = arr
        self.stacks = []    # list of the stacks(currently empty)
        self.m = m          # no. of stacks to be created
        for i in range(self.m):
            self.stacks.append(LifoQueue())     # list of stacks is created

    def main(self):
        n = len(self.list)
        # init = math.floor(n/self.m)
        fin = math.floor(n/self.m)      # calculating floor(n/m)
        init = 0
        count = 1
        
        for i in range(self.m):                 # filling the stacks which were created on line49
            
            for j in range(init, fin):
                self.stacks[i].put(self.list[j])
            count += 1
            init = fin
            fin = math.floor(count*(n/self.m))

        final_list = {}                         # all the stacks are being stored in the form of list in dictionary
        for i in range(self.m):
            key = f"key{i}"
            value = []
            while not self.stacks[i].empty():           # filling the value for each key 
                value.append(self.stacks[i].get())
            final_list[key] = value
            
        return final_list

while True:
    ar = list(map(int, input("Enter the elements(with spaces in b/w) : ").split()))         # taking input from user(the list from which stacks are to create)
    m = int(input("No. of stacks : "))
    if len(ar) < m :
        continue
    else :
        break
    
solution = Solution(ar, m)
final_result = solution.main()

print("The final stacks are :-")
for item in final_result.values():               # Printing the values in the dictionary on keys
    print(item)




# dictionary = {}
# for i in range(3):
#     print(f"\nfor i = {i} :-")
#     value = []
#     for j in range(3):
#         key = f"key{i}"
#         value.append(input("Enter : "))
#         dictionary[key] = value
# 
# for item in dictionary.values():
#     print(item)


# from queue import LifoQueue
# class Solution:
#     def __init__(self, arr):
#         self.list = arr
#         self.stack = LifoQueue()
    
#     def __str__(self):
#         return self.stack.get()

#     def main(self):
        
#         dictionary = {}
#         count = 0
#         for i in self.list:
#             if self.stack.empty():
#                 self.stack.put(i)
#             elif i == (int(self.stack.get()) + 1):
#                 p = self.stack.put(i)
#                 print(f"{p} is pushed in stack")
#             else:
#                 print("entered else")
#                 value = []    # cannot put value inside while loop, if will only store the value at that particular instance not the whole list
#                 key = f"key{count}"
#                 while not self.stack.empty():
#                     print(f"while{count}")
#                     value.append(self.stack.get())
#                 dictionary[key] = value
#                 self.stack.put(i)
#                 count += 1
                    
#         return dictionary

# a = list(map(int, input("Enter the array(with spaces in b/w) : ").split()))
# solution = Solution(a)
# final_dict = solution.main()
# for item in final_dict.values():
#     print(item)


# from queue import LifoQueue
# def removeString(str):
#     string = str
#     print("2")
#     stack = LifoQueue()
#     print("3")
#     cnt1 = 1
#     cnt2 = 1
#     cnt3 = 1
#     for i in range(len(string)):
        
#         if stack.empty() :
#             print(f"3.1.{cnt1}")
#             stack.put(string[i])
#             cnt1 +=1
        
#         elif stack.get() == string[i] and not stack.empty():
#             print(f"3.2.{cnt2}")
#             print("rep. element")
#             cnt2 += 1
#         else:
#             print(f"3.3.{cnt3}")
#             stack.put(string[i])
#             cnt3 += 1

#     lst = []
#     cnt4 = 1
#     while not stack.empty():
#         print(f"while{cnt4}")
#         lst.append(stack.get())
#         cnt4 += 1
#     final_string = ''.join(lst)
#     print("final_string")
#     return final_string

# if __name__ == "__main__":
#     strng = input("Enter string : ")
#     print("1")
#     print(removeString(strng))