li = [1,5,2,7,52,23,12]
# li.sort()
# print(li)
# li.reverse()
# print(li)

# li.append(10)
# print(li)

# li.insert(1, 30)
# print(li)

# new = ["head", "to", "north"]
# li.extend(new)
# print(li)

# li.pop(3)    #removes element at 3rd index
# print(li)

# print(len(li))\

# li = ['parshant', 'kushagra', 'raushan', 'rajat']
# for item in li:
#     print(item)
# print(li.index('kushagra'))



n = int(input("Enter the no. of students : "))
marks = []
for i in range(0, n):
    mar = int(input("Enter the marks : "))
    marks.append(mar)

print(marks)

max = marks[0]
for j in range(0, len(marks)):
    if(max < marks[j]):
        max = marks[j]

print("Max. marks is = ",max)

# strip() function is used for deleting the spaces at the beginning and at the end of any character
