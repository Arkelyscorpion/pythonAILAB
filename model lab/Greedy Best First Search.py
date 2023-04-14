# Greedy Best First Search

from queue import PriorityQueue
v = 8
# graph = [[] for i in range(v)]
graph = {
    'S' : [('A',1),('B',3),('C',5)],
    'A' : [('G',3)],
    'B' : [('F',5)],
    'C' : [('E',2)],
    'E' : [('D',1)],
    'G' : [],
    'F' : [],
    'D' : []
}
# actually use heuristics

def best_first_search(source, target):
    visited = set()
    visited.add(source)
    pq = PriorityQueue()
    pq.put((0, source))
    while pq.empty():
      u = pq.get()[1]
      print(u, end=" ")
      if u == target:
        break
      for v, c in graph[u]:
        if v not in visited:
          visited.add(v)
          pq.put((c, v))
      print()

source = 'S'
target = 'D'

best_first_search(source, target)
