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

stack=[]

depth=0
limit=1
goal=input("Enter element to search")
s=0
greached=False
while True:
    visited=set()
    stack=[]
    stack.append("S")
    while stack:
        #print(graph)
        n=stack.pop()
        while(graph[n][0]>limit):
            if(stack):
                n=stack.pop()
            else:
                break
    
        depth=graph[n][0]
        if depth<=limit:
            if n not in visited:
                print(n,end="-->")
                if (n==goal):
                    greached=True
                    print("Element found at depth",limit)
                    break
                visited.add(n)
                for neighbour in graph[n][1:]:
                    stack.append(neighbour)
                    if graph[neighbour][0]>graph[n][0]:
                        graph[neighbour][0]=graph[n][0]+1
        else:
            break
    if(not greached):
        print("Element could not be reached with the depth ",limit)
        limit+=1
    else:
        break

if(not greached):
    print("Goal cannot be reached with given depth")
    
        
