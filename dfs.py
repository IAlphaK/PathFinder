from collections import defaultdict
class dfsGraph:
    # Constructor
    def __init__(self):
        # Default dictionary to store graph
        self.graph = defaultdict(list)
        self.weights = defaultdict(dict)

    # Function to add an edge to the graph
    def addEdge(self, u, v, weight=1, directed=True):
        self.graph[u].append(v)
        self.weights[u][v] = weight
        if not directed:
            self.graph[v].append(u)
            self.weights[v][u] = weight

    # Function to perform DFS and print the path
    def printpath(self, start, goals):
        visited = set()
        self.dfs(start, goals, visited, [])

    # Recursive DFS function
    def dfs(self, node, goals, visited, path):
        visited.add(node)
        path.append(node)
        if node == goals:
            print(*path, sep='\n')  # Print the path
            return True  # Goal node found, stop the traversal
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                goal_found = self.dfs(neighbor, goals, visited, path)
                if goal_found:
                    return True  # Goal node found, stop the traversal
        path.pop()  # Remove the current node from the path
        return False  # Goal node not found in the current traversal