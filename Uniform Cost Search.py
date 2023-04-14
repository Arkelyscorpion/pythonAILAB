graph={
"S":{"A":3,"C":5,"B":1},
"A":{"G1":10,"E":7},
"B":{"F":2,"C":2},
"C":{"G3":11},
"D":{"G2":5,"S":6,"B":4},
"E":{"G1":2},
"G3":{"F":0},
"F":{"D":1},
"G1":{},
"G2":{},
    }
visited=set()
queue=[]
goal=input("Input the goal")
def ucs(graph,visited,node):
    visited.add(node)
    queue.append({node:0})
    while queue:
        #print(queue)
        index=0
        maxi=999
        ind=0
        for item in queue:
            if maxi>list(item.values())[0]:
                maxi=list(item.values())[0]
                ind=index
            index+=1
        l=list(queue.pop(ind).keys())[0]
        print(l,end=" ")
        if (l==goal):
            print("Element found")
            return
        
        for neighbour in graph[l]:
            #print(neighbour)
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append({neighbour:graph[l][neighbour]})
ucs(graph,visited,"S")
