import copy

def bfs():
    def expand(matrix,ind,in1):
        temp=matrix[ind[0]][ind[1]]
        matrix[ind[0]][ind[1]]=matrix[in1[0]][in1[1]]
        matrix[in1[0]][in1[1]]=temp
        return matrix
    def updateparent(news,currs,parent):
        news=tuple(map(tuple, news))
        currs=tuple(map(tuple, currs))
        if news not in parents.keys():
            parents[news] = currs
        return parents
    matrix1=[
        [1,5,2],
        [4,0,3],
        [7,8,6],
        ]
    matrix2=[
        [2,3,1],
        [5,0,7],
        [4,6,8],
        ]

    queue=[matrix1,]

    visited=set()
    mat1=tuple(map(tuple, matrix1))
    parents={mat1:None}
    target=(
        (1,2,3),
        (4,5,6),
        (7,8,0),
        )
    while len(queue)>0:
        #print("hi")
        curr=queue.pop(0)
        currt=tuple(map(tuple, curr))
        #print(currt)
        #print(target)
        if currt in visited:
            continue
        if currt==target:
            break
        visited.add(currt)
        d = dict( (j,(x, y)) for x, i in enumerate(curr) for y, j in enumerate(i) )
        blankspot=d[0]
        #print(blankspot)
        if blankspot == (0,0):
            #print("check")
            ns=expand(copy.deepcopy(curr),[0,0],[0,1])
            
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[0,0],[1,0])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
        elif blankspot==(0,2):
            ns=expand(copy.deepcopy(curr),[0,2],[0,1])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[0,2],[1,2])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
        elif blankspot==(2,0):
            ns=expand(copy.deepcopy(curr),[2,0],[2,1])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[2,0],[1,0])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
        elif blankspot==(2,2):
            #print(curr)
            ns=expand(copy.deepcopy(curr),[2,2],[2,1])
            #print(ns)
            #print(curr)
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[2,2],[1,2])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
        elif blankspot==(0,1):
            ns=expand(copy.deepcopy(curr),[0,1],[0,0])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[0,1],[1,1])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[0,1],[0,2])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
        elif blankspot==(1,0):
            ns=expand(copy.deepcopy(curr),[1,0],[0,0])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[1,0],[2,0])
            parents=updateparent(ns,curr,parents)
            queue.append(expand(curr,[1,0],[2,0]))
            ns=expand(copy.deepcopy(curr),[1,0],[1,1])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
        elif blankspot==(2,1):
            ns=expand(copy.deepcopy(curr),[2,1],[2,0])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[2,1],[2,1])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[2,1],[2,2])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
        elif blankspot==(1,2):
            ns=expand(copy.deepcopy(curr),[1,2],[0,2])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[1,2],[1,1])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[1,2],[2,2])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
        elif blankspot==(1,1):
            ns=expand(copy.deepcopy(curr),[1,1],[0,1])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[1,1],[1,0])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[1,1],[2,1])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[1,1],[1,2])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
    #print(parents)
    curr = target
    path = ''
    print('bfs:')
    while curr != None:
        path = str(curr) + ' -> ' + path
        curr = parents[curr]
        print(path)
    
    #print(parents)
def dfs():
    def expand(matrix,ind,in1):
        temp=matrix[ind[0]][ind[1]]
        matrix[ind[0]][ind[1]]=matrix[in1[0]][in1[1]]
        matrix[in1[0]][in1[1]]=temp
        return matrix
    def updateparent(news,currs,parent):
        news=tuple(map(tuple, news))
        currs=tuple(map(tuple, currs))
        if news not in parents.keys():
            parents[news] = currs
        return parents
    matrix1=[
        [1,5,2],
        [4,0,3],
        [7,8,6],
        ]
    matrix2=[
        [2,3,1],
        [5,0,7],
        [4,6,8],
        ]

    queue=[matrix1,]

    visited=set()
    mat1=tuple(map(tuple, matrix1))
    parents={mat1:None}
    target=(
        (1,2,3),
        (4,5,6),
        (7,8,0),
        )
    c=0
    while len(queue)>0:
        c=c+1
        if(c>100):
            break
        #print("hi")
        curr=queue.pop()
        currt=tuple(map(tuple, curr))
        #print(currt)
        #print(target)
        if currt in visited:
            continue
        if currt==target:
            break
        visited.add(currt)
        d = dict( (j,(x, y)) for x, i in enumerate(curr) for y, j in enumerate(i) )
        blankspot=d[0]
        #print(blankspot)
        if blankspot == (0,0):
            #print("check")
            ns=expand(copy.deepcopy(curr),[0,0],[0,1])
            
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[0,0],[1,0])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
        elif blankspot==(0,2):
            ns=expand(copy.deepcopy(curr),[0,2],[0,1])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[0,2],[1,2])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
        elif blankspot==(2,0):
            ns=expand(copy.deepcopy(curr),[2,0],[2,1])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[2,0],[1,0])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
        elif blankspot==(2,2):
            #print(curr)
            ns=expand(copy.deepcopy(curr),[2,2],[2,1])
            #print(ns)
            #print(curr)
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[2,2],[1,2])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
        elif blankspot==(0,1):
            ns=expand(copy.deepcopy(curr),[0,1],[0,0])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[0,1],[1,1])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[0,1],[0,2])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
        elif blankspot==(1,0):
            ns=expand(copy.deepcopy(curr),[1,0],[0,0])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[1,0],[2,0])
            parents=updateparent(ns,curr,parents)
            queue.append(expand(curr,[1,0],[2,0]))
            ns=expand(copy.deepcopy(curr),[1,0],[1,1])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
        elif blankspot==(2,1):
            ns=expand(copy.deepcopy(curr),[2,1],[2,0])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[2,1],[2,1])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[2,1],[2,2])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
        elif blankspot==(1,2):
            ns=expand(copy.deepcopy(curr),[1,2],[0,2])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[1,2],[1,1])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[1,2],[2,2])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
        elif blankspot==(1,1):
            ns=expand(copy.deepcopy(curr),[1,1],[0,1])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[1,1],[1,0])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[1,1],[2,1])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
            ns=expand(copy.deepcopy(curr),[1,1],[1,2])
            parents=updateparent(ns,curr,parents)
            queue.append(ns)
    #print(parents)
    curr = target
    path = ''
    print('dfs:')
    try:
        while curr != None:
            path = str(curr) + ' -> ' + path
            curr = parents[curr]
            print(path)
        #print(parents)
    except:
        print('final state not reached')
bfs()
dfs()
