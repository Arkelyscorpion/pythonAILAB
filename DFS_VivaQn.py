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

visited = set()

def dfs(visited, graph, node): 
    if node not in visited:
        print (node)
        visited.add(node)
        if(node == 'H'):
          return 
        for neighbour in graph[node]:
            return dfs(visited, graph, neighbour)

print("Using DFS : ")
dfs(visited, graph, 'A')