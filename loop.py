# 1st que
# num = int(input("Enter any value : "))
# print("The mul. table of "+str(num)+" is ")
# for i in range(1, 11) :
#     print(i*num)    


# #que 2 greet all name starting with s
# li = ['harry', 'soham', 'sachin', 'rahul']
# for item in li:
#     if('s' in item[0]):
#         print("Congratulations to "+item)
#     else:
#         print("s is not present in ", [item])



# que 3 sum of first n natural numbers
# a = 0
# while(a < 1):
#     n = int(input("Enter the number : "))
#     sum = 0
#     for i in range(1, (n+1)):
#         sum = sum + i

#     print(sum)

    
#     alp = input("Press 'e' to exit!")
#     if(alp == 'e'):
#         break
#     else:
#         continue




# que 4 find factorial of the numbers
# fac = int(input("Enter the number : "))
# factorial = 1
# for i in range(1, (fac + 1)):
#     factorial = factorial * i

# print(factorial)



# que 7   print the pyramid of stars 
# while(True):
#     n = int(input("Enter the number of lines : "))
#     for i in range(n):
#         print(" " * (n-i-1), end="")
#         print("*" * (2*i + 1), end = "")
#         print(" " * (n-i-1))

#     e = input("Print 'exit' to exit the programme")
#     if(e == ' exit' or e == 'exit ' or ' exit '):
#         break
#     else:
#         continue




# que 8 boundary printing of stars
num = int(input("Enter number:"))

for i in range(0, num):
    for j in range(0, num):
        if i == 0 or j == 0 or j == num-1 or i == num - 1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()

