graph = {
  'A':['B','C'],
  'B':['D','E'],
  'C':['F','G'],
  'D':['H','I'],
  'E':['J','K'],
  'F':['L','M'],
  'G':['N','O'],
  'H':['I'],
  'I':['J'],
  'J':['K'],
  'K':['L'],
  'L':['M'],
  'M':['N'],
  'N':['O'],
  'O':[]
}

visited = []
queue = []     

def bfs(visited, graph, node,ending): 
  visited.append(node)
  queue.append(node)

  while queue:          
    m = queue.pop(0) 
    print (m, end = " ") 
    if(m == ending):
      break

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

print("Using BFS : ")
bfs(visited, graph, 'A','H')
