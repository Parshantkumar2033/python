
def printMatrix(matrix):
    r, c = len(matrix), len(matrix[0])
    for i in range(r):
        for j in range(c):
            print(matrix[i][j], end = " ")
        print()



v, e = map(int, input("Enter the no. of vertices and edges : ").split())
matrix = [[0]*v for i in range(v)]
for i in range(e):
    u, v = map(str, input().split())

    u = ord(u) - ord('A')
    v = ord(v) - ord('A')
    matrix[u][v] = 1
    matrix[v][u] = 1
    print()

printMatrix(matrix)  