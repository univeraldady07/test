from collections import defaultdict,deque 
class Graph: 
    def __init__(self): 
        self.graph=defaultdict(list) 
    def add_edge(self,u,v): 
        self.graph[u].append(v) 
 
    def dfs(self,start,visited=None): 
        if visited is None: 
            visited=set() 
        visited.add(start) 
        print(start) 
        for neighbour in self.graph[start]: 
            if neighbour not in visited: 
                self.dfs(neighbour,visited) 
 
g=Graph() 
g.add_edge(0,1) 
g.add_edge(0,2) 
g.add_edge(1,4) 
g.add_edge(2,3) 
 
print("DFS:") 
g.dfs(0) 
