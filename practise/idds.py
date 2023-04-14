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
path = []
def dfs(start,end,maxdepth):
    if start == end:return True
    if maxdepth <= 0: return False
    for node,wt in graph[start]:
        path.append(node)
        if dfs(node,end,maxdepth-1) == True: return True
    return False

def idds(start,end,maxdepth):
    for i in range(maxdepth):
        if dfs(start,end,i): return True
    return False

idds('A','G',3)
print(path)