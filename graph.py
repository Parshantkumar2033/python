# # def printmatrix(matrix):
# #     r, c = len(matrix), len(matrix[0])
# #     for i in range(r):
# #         for j in range(c):
# #             print(matrix[i][j], end = " ")
# #         print()
        

# # v,e = map(int, input("Enter the no. of vertices and edges : ").split())
# # matrix = [[0]*v for i in range(v)]
# # for i in range(e):
# #     u, v = map(str, input().split())
# #     u = ord(u) - ord('A')
# #     v = ord(v) - ord('A')
# #     matrix[u][v] = 1
# #     matrix[v][u] = 1
    
# # printmatrix(matrix)


# # USER INPUT, IMPLEMENTATION OF ADJACENCY LIST
# # edges = [("A", "B"), ("A", "C"), ("B", "C"),
# #             ("B", "D"), ("B", "E"), ("C", "D"), ("D", "E")]
# class Graph:
#     def __init__(self, nodes):
#         self.nodes = nodes
#         self.adj_list = {}

#         for node in self.nodes:
#             self.adj_list[node] = []

#     def add_edge(self, u, v):
#         self.adj_list[u].append(v)
#         self.adj_list[v].append(u)

#     def print_adj(self):
#         for node in self.nodes:
#             print(node, ":", self.adj_list[node])

# edges = []
# n = int(input("Enter the no. of edges : "))
# for i in range(n):
#     u, v = map(str, input().split()) 
#     edges.append((u, v))
# print("\nEdges b/w : ", end = ""), print(edges)

# no_of_nodes = int(input("\nEnter the no. of nodes : "))
# nodes = []
# for i in range(no_of_nodes):
#     N = input(f"{i+1} node : ")
#     nodes.append(N)

# print("\nNodes : ", end = ""), print(nodes)

# graph = Graph(nodes)
# for u, v in edges:
#     graph.add_edge(u, v)

# print("The adjacency list of the graph is :-")
# graph.print_adj()




# # for u, v in edges:
# #     graph.add_edge(u, v)


list = [1,1,2,3,4,2,1,3]
n = len(list)
arr = [0]*10
final_list = []
for i in list:
    arr[i] += i
for i in range(len(arr)):
    if arr[i] > 1:
        final_list.append(i)

final_list.sort()
if len(final_list) > 1:
    print(final_list)
else:
    print("False")
