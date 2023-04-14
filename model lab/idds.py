graph = {
    'S' : ['A','B','C'],
    'A' : ['G'],
    'B' : ['F'],
    'C' : ['E'],
    'E' : ['D'],
    'G' : [],
    'F' : [],
    'D' : []
}
path = []
def dls(src,target,maxd):
    if src == target : return True
    if maxd <= 0: return False
    for i in graph[src]:
        path.append(i)
        if dls(i,target,maxd-1): return True
    return False


def idds(src,target,maxd):
    for i in range(maxd):
        if dls(src,target,i):
            return True
    return False


target = 'D'; maxd = 4; src = 'S';
print(idds(src,target,maxd))
print(path,end=' ')