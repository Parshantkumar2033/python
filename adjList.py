# from queue import LifoQueue
# from itertools import combinations
# arr = [1, 2, 0, 1, 3, 2, 0]
# n = len(arr)
# if n == 1 or n == 0:
#     print(arr)
# indx = []
# for i in range(n-1):
#     if(arr[i-1] < arr[i] or arr[i] > arr[i+1]):
#         indx.append(i)

# print("The indices are : ", end = "") 
# for i in range(len(indx)):
#     print(arr[i], end = ", ")

# x = '[{}{({[()]})}{[]}()]'

# stack = LifoQueue()
# # closing = LifoQueue()
# for i in x:
#     if(i == '[' or i == '{' or i == '('):
#         stack.put(i)
#     elif (i == ']' or i == '}' or i == ')'):
#         if (stack.empty() == True):
#             print("Error!")
#             break
#         last_element = stack.get()
#         if (i == ']' and last_element != '['):
#             print("error")
#             break
#         elif (i == '}' and last_element != '{'):
#             print("error")
#             break
#         elif (i == ')' and last_element != '('):
#             print("error")
#             break

# if stack.empty() == False :
#     print("Error")
# else:
#     print("Balanced")


# from queue import LifoQueue
# class Solution:
#     def compare(element): # i is the index at which we are comparing in the string
#         # if ((element == '/' or '*') and (string[i] == '/' or '*')) or ((element == '/' or '*') and (string[i] == '+' or '-')) or ((element == '+' or '-') and (string[i] == '+' or '-')):
#         #     return True
#         # else:
#         #     return False
#         prec = ['/', '*', '+', '-']
        
#         if ( element == prec[0] or element == prec[1]):
#              print(prec[0])
             
#         elif (element not in prec[2: ]):
#              print(element)
            
        
        


from queue import LifoQueue
class Solution:
    def __init__(self, elements, postfix):
        self.elements = elements
        self.postfix = postfix

    def __str__(self):
        return str(self.postfix)
        
    def solve(self):
        stack = LifoQueue()
    
        prec = { '/' : 1,
                '*' : 1,
                '+' : 2,
                '-' : 2,
                '(' : 3}
        
        for item in self.elements:
            if (item == '('):
                stack.put(item)
            elif item.isalnum():
                self.postfix.append(item)
            elif item == ')':
                while not stack.get() == '(':
                    self.postfix.append(stack.get())
                stack.get()  # to get "(" from stack

            else:
                if stack.empty():
                    stack.put(item)
                elif prec[stack.get()] > prec[item]:
                    while not stack.empty() and prec[stack.get()] > prec[item]:
                        self.postfix.append(stack.get())
                    stack.put(item)
                else:
                    stack.put(item)
        while stack.empty() == False:
            self.postfix.append(stack.get())
        
        return "".join(self.postfix)
        # print(postfix)
        
    
result = []
solution = Solution('(A+B)*(C+D)', result)
solution.solve()
print(result)

           