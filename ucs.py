#AI3:UCS graph

import heapq

def get_adjacency_matrix():
    num_vertices = int(input("Enter the number of vertices: "))
    adjacency_matrix = []
    print("Enter the adjacency matrix row by row:")
    for i in range(num_vertices):
        adjacency_matrix.append(list(map(int, input().split())))
    return num_vertices, adjacency_matrix

def ucs(graph, start, goal):
    heap = [(0, start, [])]
    visited = set()
    while heap:
        cost, node, path = heapq.heappop(heap)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == goal:
                return cost, path
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + weight, neighbor, path))
    return float("inf"), []

def ucs_traversal(graph, start):
    heap = [(0, start, [])]
    visited = set()
    traversal_path = []
    itr = 0
    while heap:
        cost, node, path = heapq.heappop(heap)
        if node not in visited:
            visited.add(node)
            traversal_path.append(node)
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + weight, neighbor, path))
        print("Iteration",itr,":",traversal_path)
        itr = itr+1
    return traversal_path

num_vertices, adjacency_matrix = get_adjacency_matrix()
graph = {}
for i in range(num_vertices):
    graph[i] = []
    for j in range(num_vertices):
        if adjacency_matrix[i][j] > 0:
            graph[i].append((j, adjacency_matrix[i][j]))

start = int(input("Enter the starting node: "))
goal = int(input("Enter the goal node: "))
cost, solution_path = ucs(graph, start, goal)
print("Cost:", cost)
print("Solution path:", solution_path)
traversal_path = ucs_traversal(graph, start)
print("Traversal path:", traversal_path)

# 0 1 3 2 0 0 0 
# 0 0 0 0 2 0 0
# 0 0 0 0 3 0 4
# 0 0 0 0 0 2 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 1
# 0 0 0 0 0 0 0

# 0 2 3 1 0 0 0 0 0 0
# 0 0 0 0 6 7 0 0 0 0 
# 0 0 0 0 0 0 4 0 0 0
# 0 0 0 0 0 0 2 4 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 1 0
# 0 0 0 0 0 0 0 0 4 1 
# 0 0 0 0 0 0 0 0 0 5
# 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0

