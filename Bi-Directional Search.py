graph={
"S":["A","C","B"],
"A":["G1","E"],
"B":["F","C"],
"C":["G3"],
"D":["G2","S","B"],
"E":["G1"],
"G3":["F"],
"F":["D"],
"G1":[],
"G2":[],
}

parent={
"S":[],
"A":[],
"B":[],
"C":[],
"D":[],
"E":[],
"G3":[],
"F":[],
"G1":[],
"G2":[],
}

for key in graph:
    for item in graph[key]:
        parent[item].append(key)
print(parent)
goal=input("Enter the Goal Node : ")
frontvisited=set()
frontqueue=[]
backvisited=set()
backqueue=[]
frontvisited.add("S")
frontqueue.append("S")
backvisited.add(goal)
backqueue.append(goal)
frontpath=""
backpath=""
while frontqueue and backqueue:
    l=frontqueue.pop(0)
    m=backqueue.pop(0)
    frontpath+=l+" "
    backpath+=m+" "
    if (l==m):
        print(frontpath)
        print(backpath)
        break
    for neighbour in graph[l]:
        if neighbour not in backvisited:
            frontvisited.add(neighbour)
            frontqueue.append(neighbour)
    for neighbour in parent[m]:
        if neighbour not in backvisited:
            backvisited.add(neighbour)
            backqueue.append(neighbour)
    


