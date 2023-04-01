letter = '''Dear name,
            You are selected!
            Date: date'''
name = input("Enter the name of person = ")
date = input("Enter the date on that particular day =")
letter = letter.replace("name", name)
letter = letter.replace("date", date)
print(letter)
# print(len(letter))
# print(letter.count("parshant"))




print("\n")
print("Please enter only integers")
hello = int(input("Enter the integer = "))
# hello = int(hello)
print(hello)
print(type(hello))