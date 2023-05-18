from collections import defaultdict
import networkx as nx

class dfsGraph:
    # Constructor
    def __init__(self):
        # Default dictionary to store graph
        self.graph = defaultdict(list)
        self.weights = defaultdict(dict)

    # Function to perform DFS and return the path and subgraph
    def get_path_and_subgraph(self, graph, start, goals):
        visited = set()
        path = []
        self.dfs(graph, start, goals, visited, path)

        sub_graph = graph.subgraph(path)  # Create subgraph from the traversed nodes
        return path, sub_graph

    # Recursive DFS function
    def dfs(self, graph, node, goals, visited, path):
        visited.add(node)
        path.append(node)
        if node in goals:
            return True  # Goal node found, stop the traversal
        for neighbor in graph[node]:
            if neighbor not in visited:
                goal_found = self.dfs(graph, neighbor, goals, visited, path)
                if goal_found:
                    return True  # Goal node found, stop the traversal
        path.pop()  # Remove the current node from the path
        return False  # Goal node not found in the current traversal
