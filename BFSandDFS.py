print("Enter the Number of Nodes : ")
n = int(input())
nodes = [[0 for i in range(n+1)] for i in range(n+1)]
visited = [0 for i in range(n+1)]
n = n + 1
print("Enter the Number of Edges : ")
edges = int(input())
print("Enter the Edges (a b) : ")
for i in range(edges):
	a,b = map(int,input().split())
	nodes[a][b] = 1
	nodes[b][a] = 1
print("Enter the Starting Element : ")
start = int(input())	

def bfs(x):
	print("BFS : ", end = '')
	queue = [x]
	while(len(queue) != 0):
		current_node = queue[0]		
		visited[current_node] = 1
		queue = queue[1:]
		print(current_node,end = ' ')	
		for i in range(n):
			if(visited[i] == 0 and nodes[current_node][i] == 1):
				queue.append(i)
bfs(start)
print()
visited = [0 for i in range(n)]

def dfs(x):
	print(x,end = ' ')
	visited[x] = 1
	for i in range(n):
		if(nodes[x][i] == 1 and visited[i] == 0):
			dfs(i)
		
print("DFS : ", end = '')
dfs(start)