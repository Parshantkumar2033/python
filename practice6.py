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