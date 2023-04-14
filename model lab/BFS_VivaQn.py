# graph = {
#   'A':['B','C'],
#   'B':['D','E'],
#   'C':['F','G'],
#   'D':['H','I'],
#   'E':['J','K'],
#   'F':['L','M'],
#   'G':['N','O'],
#   'H':['I'],
#   'I':['J'],
#   'J':['K'],
#   'K':['L'],
#   'L':['M'],
#   'M':['N'],
#   'N':['O'],
#   'O':[]
# }

# graph = {
#   'A' : ['B','C'],
#   'B' : ['D','E'],
#   'C' : ['F','G'],
#   'G' : ['K'],
#   'D' : ['H','I'],
#   'E' : ['J'],
#   'J' : ['M'],
#   'H' : ['L'],
#   'I' : [],
#   'L' : [],
#   'M' : [],
#   'K' : [],
#   'F' : [],
# }

graph = {
  'A' : ['D','B'],
  'B' : ['E','C','G'],
  'C' : ['A'],
  'D' : ['C'],
  'E' : ['H'],
  'F' : [],
  'G' : ['F'],
  'H' : ['G','F']
}

path = []
def bfs(node):
  visited = []
  queue = []     
  # path.append(node) 
  visited.append(node)
  queue.append(node)

  while queue:          
    m = queue.pop(0) 
    print (m, end = " ") 
    # if(m == ending):
    #   # path.append(m)
    #   # print(path)
    #   break

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
        # path.append(neighbour)

# visited = {'A': False,'B' : False,'C' : False,'D' : False, 'E' : False,'F' : False,'G' : False,'H': False,'I' : False,'J' : False,'K' : False,'L' : False,'M' : False}


def printpath(node,ending):
  visited  =[]
  visited.append(node)
  path.append(node)
  if node == ending:
    print(path)
  else:
    for i in graph[node]:
      if i not in visited:
        printpath(i,ending)
  path.pop()
  visited.remove(node)


visited = []
def dfs(node):
  print(node,end=' ')
  visited.append(node)
  for i in graph[node]:
    if i not in visited:
      dfs(i)


print("Using BFS : ")
bfs('A')
print("DFS")
# printpath('A','F')
dfs('A')