from collections import defaultdict
class Graph:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v, weight, directed=True):
        self.graph[u].append((v, weight, directed))
        if not directed:
            self.graph[v].append((u, weight, directed))

    # Function to print a BFS of graph
    def printpath(self, start, goals):
        queue = []
        visited = []
        queue.append((start, []))  # Store the path along with each vertex
        visited.append(start)
        while queue:
            vertex, path = queue.pop(0)
            path.append(vertex)
            print(vertex)
            if vertex in goals:
                return path
            for i, weight, directed in self.graph[vertex]:
                if i not in visited:
                    if not directed or (directed and i not in path):
                        queue.append((i, list(path)))  # Create a new copy of the path for each neighbor
                    visited.append(i)