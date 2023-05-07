import sys
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y = map(lambda i : i ** 2, x)
print(list(y))  # takes more space than, 
for i in y:
    print(i)        # the whole y is not stored in the memory 
                    # instead every time the loop demands for the i, 
                    # lambda creates that value and passes it into y as a result


# print(next(y))  # y = 1  # print(y.__next__())
# print(next(y))  # y = 2
# print(next(7))  # y = 3


while True:
    try:
        value = next(y)
    except StopIteration:
        print("done")
        break

x = range(1, 11)
print(next(iter(x)))        # same as for i in iter(x)


class Iter:
    def __init__(self, n):
        self.n = n 

    def __iter__(self):
        self.current = 0
        return self
    def __next__(self):
        self.current += 1
        if self.current >= self.n:
            raise StopIteration
        
        return self.current
    
# x = Iter(5)
# for i in x:
#     print(i)

x = Iter(5)
itr = iter(x)
print(next(itr))


def generator(n):
    for i in range(n):  # generates for every instance called by the loop below
        yield i         # pause the execution at every yield

for i in generator(5):
    print(i)


# generators using comprehension
x = (i for i in range(10))
for j in x:
    print(j)