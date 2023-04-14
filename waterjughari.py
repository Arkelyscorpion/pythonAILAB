class water_jug:
    def __init__(self):
        self.visited = []
        self.queue = []
        self.bfs_path = []
        self.solution_path = []
        self.solvable = False
        self.parent = {}
        self.goal = (0,0)

    def bfs(self,a,b,target):
        self.queue.append((0,0))
        while len(self.queue)>0:
            curr_state = self.queue.pop(0)
            if (curr_state[0],curr_state[1]) in self.visited:
                continue
            if (curr_state[0]>a or curr_state[0]<0 or curr_state[1]>b or curr_state[1]<0):
                continue    
            self.bfs_path.append((curr_state[0],curr_state[1]))
            self.visited.append((curr_state[0],curr_state[1]))

            if  curr_state[0]==target or curr_state[1]==target: #Check if GOAL STATE is reached
                self.solvable = True
                if curr_state[0]==target:
                    self.bfs_path.append((curr_state[0],0))
                    self.parent[(curr_state[0],0)] = curr_state
                    self.goal = (curr_state[0],0)
                else:
                    self.bfs_path.append((0,curr_state[1]))
                    self.parent[(0,curr_state[1])] = curr_state
                    self.goal = (0,curr_state[1])
                
                k = self.goal
                
                while k != (0,0):
                    self.solution_path.insert(0,self.parent[k]) 
                    k = self.parent[k]

                self.solution_path.append(self.goal)
                return self.bfs_path,self.solution_path                               #No need to continue bfs after reaching GOAL STATE

            self.queue.append((curr_state[0],b))                #filling jug2
            if (curr_state[0],b) not in self.parent.keys():
                self.parent[(curr_state[0],b)] = curr_state
            self.queue.append((a,curr_state[1]))                #filling jug1
            if (a,curr_state[1]) not in self.parent.keys():
                self.parent[(a,curr_state[1])] = curr_state

            for val in range(1,max(a,b)+1):
                j1 = curr_state[0]+val              #jug2 to jug1
                j2 = curr_state[1]-val
                if (j1==a or j2==0):                    #consider state iff jug1 becomes full or jug2 becomes empty
                    self.queue.append((j1,j2))
                    if (j1,j2) not in self.parent.keys():
                        self.parent[(j1,j2)] = curr_state

                j1 = curr_state[0]-val              #jug1 to jug2
                j2 = curr_state[1]+val
                if (j1==0 or j2==b):                    #consider state iff jug2 becomes full or jug1 becomes empty
                    self.queue.append((j1,j2))
                    if (j1,j2) not in self.parent.keys():
                        self.parent[(j1,j2)] = curr_state
            
            self.queue.append((curr_state[0],0))    #empty jug2
            if (curr_state[0],0) not in self.parent.keys():
                self.parent[(curr_state[0],0)] = curr_state
            self.queue.append((0,curr_state[1]))    #empty jug1
            if (0,curr_state[1]) not in self.parent.keys():
                self.parent[(0,curr_state[1])] = curr_state
        
        if not self.solvable:
            return "NO SOLUTION"

wj1 = water_jug()
bfs_path , solution_path= wj1.bfs(4,3,2)
print(bfs_path)
print(solution_path)