import numpy as np

arr = np.array([[1, 2, 3, 4, 5],
                [3, 2, 5, 0, 1],
                [2, 1, 1, 4, 6],
                [0, 0, 1, 3, 6]])

m,n = np.shape(arr)
print("row : ", m)
print("col :", n)

row = arr.shape[0]
print()
print(row)