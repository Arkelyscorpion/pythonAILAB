import heapq
graph = {
    'S' : [('A',1),('B',3),('C',5)],
    'A' : [('G',3)],
    'B' : [('F',5)],
    'C' : [('E',2)],
    'E' : [('D',1)],
    'G' : [],
    'F' : [('D',-10)],
    'D' : []
}

def ucs(graph,start,goal):
    heap = [(0,start,[])]
    visited = set()
    while heap:
        cost,node,path = heapq.heappop(heap)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == goal:
                return cost,path
            for nbr,wt in graph[node]:
                if nbr not in visited:
                    heapq.heappush(heap,(cost+wt,nbr,path))
    return float("inf"),[]

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

print(ucs(graph,'S','D'))
print(ucs_traversal(graph,'S'))
