from collections import defaultdict
class Graph:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, s,find):
        queu = []
        visited = []
        queu.append(s)
        visited.append(s)
        while queu:
            s = queu.pop(0)
            print(s)
            if s==find:
                print("Number has been found")
                exit()
            for i in self.graph[s]:
                if i not in visited:
                    queu.append(i)
                    visited.append(i)

# Driver code

# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)
g.addEdge(3, 6)
g.addEdge(3, 7)

g.addEdge(2, 1)
g.addEdge(3, 1)
g.addEdge(4, 2)
g.addEdge(5, 2)
g.addEdge(6, 3)
g.addEdge(7, 3)