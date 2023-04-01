string1 = "Currently I am  doing  the coding in python and it's  going  well. And now  I am  finding  the double space  in this  string."
newstring = string1.find("  ")
print(newstring)
change = " "
# a = "_"
# print(string1.replace("  ", a))
string1 = string1.replace("  ",change)
print(string1)