import heapq
graph = {
    'A' : [('B',4),('C',6),('D',3)],
    'B' : [('E',4),('F',2)],
    'D' : [('G',4),('H',1)],
    'C' : [],
    'E' : [],
    'F' : [],
    'G' : [],
    'H' : [],
}
traversal_path = []


def ucs(start,goal):
   heap = [(0,start,[])]
   visited = set()
   itr = 0
   while heap:
      cost,node,path = heapq.heappop(heap)
      if node not in visited:
         visited.add(node)
         traversal_path.append(node)
         path = path + [node]
         if node == goal:
            return cost,path
         for neigh,wt in graph[node]:
            if neigh not in visited:
                heapq.heappush(heap,(cost+wt,neigh,path))
      print("Iteration",itr,":",traversal_path)
      itr = itr+1


# def ucs(start,end):
#     heap = [(0,start,[])]
#     visited = set()
#     while heap:
#         cost,node,path = heapq.heappop(heap)
#         if node not in visited:
#             path = path + [node]
#             visited.add(node)
#             if node == end:
#                 return cost,path
#             for n,wt in graph[node]:
#                 if n not in visited:
#                     heapq.heappush


print(ucs('A','G'))