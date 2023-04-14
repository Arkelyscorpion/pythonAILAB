graph={
"S":[0,"A","C","B"],
"A":[999,"G1","E"],
"B":[999,"F","C"],
"C":[999,"G3"],
"D":[999,"G2","S","B"],
"E":[999,"G1"],
"G3":[999,"F"],
"F":[999,"D"],
"G1":[999],
"G2":[999],

    }
visited=set()
stack=[]
stack.append("S")
depth=0
limit=int(input("Enter the limit"))
goal=input("Enter element to search")
s=0
greached=False
while stack:
    #print(graph)
    
    n=stack.pop()
    while(graph[n][0]>limit):
        n=stack.pop()
    
    depth=graph[n][0]
    if depth<=limit:
        if n not in visited:
            print(n,end="-->")
            if (n==goal):
                greached=True
                break
            visited.add(n)
            for neighbour in graph[n][1:]:
                stack.append(neighbour)
                if graph[neighbour][0]>graph[n][0]:
                    graph[neighbour][0]=graph[n][0]+1
            #depth+=1
        #print(depth)
        #print(stack)
if(not greached):
    print("Goal cannot be reached with given depth")
    
        
