# first = set()
# print(type(first))

# first.add(2)
# first.add((2,4,6,7))
# # first.add({3:5})   we cannot add the hasable data in sets
# print(first)
# first.add(4)
# first.add(5)
# first.add(9)
# print(first)

# a = [first]
# print(a)

# b = [1, 2, 4, 7 ,4 ,9]
# print(b.pop(4))
# print()
# # print(b.remove(2))
# print(b)
from queue import LifoQueue
class Stack:
    def __init__(self, m):
        self.stacks = []
        self.m = m
        for i in range(m):
            self.stacks.append(LifoQueue())
        
    def __str__(self):
        return self.stacks.get()

    def main(self):
        for i in range(self.m):
            # self.stacks[i].append(list(map(int, input("Enter(with spaces) : ").split())))
            a = list(map(int, input("Enter(with spaces) : ").split()))
            self.stacks[i].put(a)
        return self.stacks       # returning a list

num = int(input("Number of stacks : "))
stack = Stack(num)
result = stack.main()   # is a list
print("Stacks are :-")
for i in range(num):
    while not result[i].empty():        #checking(whether empty or not) for each of the stacks present in the result
        print(result[i].get(), sep = " ")           #printing the stack elements which are stored in list result
