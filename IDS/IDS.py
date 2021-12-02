from collections import defaultdict

class Graph:
    
    def __init__(self,vertices):
        
        self.V = vertices
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def DLS(self,root,goal,maxDepth):
        
        if root == goal: 
            return True
        
        if maxDepth <= 0:
            return False
        
        for i in self.graph[root]:
            if (self.DLS(i,goal,maxDepth-1)):
                return True
        return False
        
    def IDS(self,root,goal,maxDepth):
        
        for i in range(maxDepth):
            if (self.DLS(root,goal,i)):
                return True
        return False 
        
g = Graph(7);
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,5)
g.addEdge(2,6)

root = 0
goal = 3
maxDepth = 1

if g.IDS(root,goal,maxDepth) == True:
    print("\nGoal is reacheable from root within max Depth")
else:
    print("\nGoal is NOT reacheable from root within max Depth")
   