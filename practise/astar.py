def h(n):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0
}
    return H_dist[n]


graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)],
}

def astar(start,goal):
    open_set = set(start)
    closed_set = set()
    g = {}
    parents = {}
    g[start] = 0
    parents[start] = start
    while open_set:
        n = None
        for node in open_set:
            if n == None or g[node] + h(node) < g[n] + h(n): 
                n = node
        if n == goal or graph[n] == None:
            pass 
        else:
            for (node,wt) in graph[n]:
                if node not in open_set and node not in closed_set:
                    open_set.add(node)
                    parents[node] = n
                    g[node] = g[n] + wt
                else:
                    if g[node] > g[n] + wt:
                        g[node] = g[n] + wt
                        parents[node] = n
                        if node in closed_set:
                            closed_set.remove(node)
                            open_set.add(node)

        if n == None:
            print("path doesnt exist")

        if n== goal:
            path = []
            while parents[n]!=n:
                path.append(n)
                n = parents[n]
            path.append(start)

            path.reverse()
            print("path found",path)
            return path
        
        open_set.remove(n)
        closed_set.add(n)
    print("path doesnt exist")
    return None



astar('A','J')






