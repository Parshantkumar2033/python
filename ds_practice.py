# from queue import LifoQueue
# class Solution:
#     def compare(): # i is the index at which we are comparing in the string
#         # if ((stack.get() == '/' or '*') and (string[i] == '/' or '*')) or ((stack.get() == '/' or '*') and (string[i] == '+' or '-')) or ((stack.get() == '+' or '-') and (string[i] == '+' or '-')):
#         #     return True
#         # else:
#         #     return False
#         prec = ['/', '*', '+', '-']
#         for i in range(len(prec)-1):
#             if ( stack.get() == prec[0]):
#                 return prec[0]
#             elif (stack.get() not in prec[(i+1): ]):
#                 return stack.get()



# stack = LifoQueue()
# string = 'A*B/C'
# signs = ['+', '-', '*', '/']
# final_string = []
# for i in string[:3]:
#     if ((i in string) in signs):
#         stack.put(string[i])
#     else:
#         final_string.append(string[i])

# from queue import LifoQueue

# class Solution:
#     def __init__(self, elements, postfix):
#         self.elements = elements
#         self.postfix = postfix

#     def __str__(self):
#         return str(self.postfix)
        
#     def solve(self):
#         stack = LifoQueue()
    
#         prec = { '/' : 1,
#                 '*' : 1,
#                 '+' : 2,
#                 '-' : 2,
#                 '(' : 3}
        
#         for item in self.elements:
#             if (item == '('):
#                 stack.put(item)
#                 print("1st")
#             elif item.isalnum():
#                 self.postfix.append(item)
#                 print("2nd")
#             elif item == ')':
#                 while not stack.empty() and stack.get() != '(':
#                     self.postfix.append(stack.get())
#                     print("3.1")
#                 # remove the '(' from stack
#                 if not stack.empty() and stack.get() == '(':
#                     stack.get()
#                     print("3.2")
#             else:
#                 if stack.empty():
#                     stack.put(item)
#                     print("4.1")
#                 elif prec[stack.get()] >= prec[item]:
#                     while not stack.empty() and prec[stack.get()] >= prec[item]:
#                         self.postfix.append(stack.get())
#                         print("4.2")
#                         # stack.get()
#                     stack.put(item)
#                     print("4.3")
#                 else:
#                     stack.put(item)
#                     print("4.5")
#         while not stack.empty():
#             self.postfix.append(stack.get())
#             print("4.6")        
#         return " ".join(self.postfix)
    
# result = []
# solution = Solution('A+(B*C)', result)
# solution.solve()
# print(result) 
# from queue import LifoQueue
# class Evaluate:
#     def __init__(self, postfix):
#         self.postfix = postfix
#     def __str__(self):
#         return str(print(self.stack.get()))
    
#     def math(self, op1, operator, op2):
#         self.operator = operator
#         if self.operator == '/':
#             return op2 / op1
#         elif self.operator == '*':
#             return op1*op2
#         elif self.operator == '+':
#             return op1+op2
#         elif self.operator == '-':
#             return op2 - op1
        
#     def solve(self):
#         stack = LifoQueue()
#         operators = ['/', '*', '+', '-']
#         for item in self.postfix:
#             if item in '0123456789':
#                 stack.put(int(item))
#             elif item in operators:
#                 op1 = stack.get()
#                 op2 = stack.get()
#                 result = self.math(op1, item , op2)
#                 stack.put(result)
#         return stack.get()
# object = Evaluate('426*+51-*8+')   
# print(object.solve()) 


# from queue import LifoQueue
# class Solution:
#     def __init__(self):
#         self.operatorStack = LifoQueue()
#         self.operandStack = LifoQueue()

#     def __str__(self):
#         return self.operatorStack.get()
    
#     def solve(self):
#         infix = '(2+4)*(8/2)'
#         count = 1
#         item_no = 1
#         length = len(infix)
#         for item in infix:
#             if item in '0123456789(':
#                 self.operandStack.put(item)
#             elif item in ['+', '-', '*', '/']:
#                 self.operatorStack.put(item)
#             elif item == ')' or item_no == length:
#                 operand1 = self.operandStack.get()
#                 operand2 = self.operandStack.get()
#                 operator = self.operatorStack.get()
#                 a = self.operandStack.get()
#                 result = Solution.math(operand1, operand2, operator)
#                 print(f"{a} {operand2} {operator} {operand1} {item} = ", end = "")
#                 str_result = str(result)
#                 print(str_result)
#                 self.operandStack.put(str_result)
#                 count += 1
            
#         while not self.operatorStack.empty() :
#             print("entered the while loop.")
#             opr1 = self.operandStack.get()
#             opr2 = self.operandStack.get()
#             oprtr = self.operatorStack.get()
#             print(f"{opr2} {oprtr} {opr1} = ", end = "")
#             rslt = Solution.math(opr1, opr2, oprtr )
#             new_result = str(rslt)
#             self.operandStack.put(new_result)
        

#         return self.operandStack.get()

#     def math(op1, op2, operator):
#         operator = operator
#         op1 = int(op1)
#         op2 = int(op2)
#         if operator == '/':
#             return op2 / op1
#         elif operator == '*':
#             return op1 * op2
#         elif operator == '+':
#             return op1 + op2
#         elif operator == '-':
#             return op2 - op1

# solution = Solution()
# final_result = solution.solve()
# print(final_result)

from queue import LifoQueue                                 # PALINDROME
class Solution:
    def __init__(self):
        self.stack1 = LifoQueue()
        self.stack2 = LifoQueue()
        
    def __str__(self):
        return self.stack.get()
#     def palindrome(self, a):
#         list = a
#         for i in range(len(list)):
#             if list[i] in ['x', 'X'] :
#                 indx = i
#                 break

#         count1 = 0
#         count2 = 0
#         for i in range(len(list)):
#             if i >= 0 and i < indx :
#                 self.stack.put(list[i])
#                 count1 += 1
#             elif i > indx and self.stack.empty() == False :
#                 if self.stack.get() == list[i] :
#                     count2 += 1
#             elif i == indx :
#                 pass
#             else:
#                 print(f"{list[i]} is ambiguios")
#                 count2 += 1

#         if count1 == count2 :
#             return 'palindrome'
#         else:
#             return 'not palindrome'
# string = 'PanlindromexemordnilnaP'
# solution = Solution()
# res = solution.palindrome(string)
# print(res)        

#     def twoStack(self, list):
#         self.list = list
#         print("Initially : ", self.list)
#         low = 0
#         high = len(self.list) - 1
#         for i in range(len(self.list)):
#             self.stack1.put(self.list[low])
#             low += 1
#             self.stack2.put(self.list[high])
#             high -= 1
#             if high < low :
#                 # self.stack1.put(self.list[low])
#                 # self.stack2.put(self.list[high])
#                 break

#         self.list1 = []
#         self.list2 = []
#         while self.stack1.empty() == False and self.stack2.empty() == False :
#             self.list1.append(self.stack1.get())
#             self.list2.append(self.stack2.get())

#         print(*self.list1, sep = " ")
#         print(*self.list2, sep = " ")

# solution = Solution()
# list = [1,4,6,2,8,11,0,7]
# solution.twoStack(list)


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