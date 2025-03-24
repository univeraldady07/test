from collections import defaultdict, deque

class Graph:
    def __init__(self):  # Fixed constructor
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            print(vertex)

            for neighbour in self.graph[vertex]:
                if neighbour not in visited:  # Fixed condition
                    visited.add(neighbour)
                    queue.append(neighbour)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 4)
g.add_edge(2, 3)

print("BFS:")
g.bfs(0)
