from collections import defaultdict
import heapq


class UCS_Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, start, end, weight, directed=True):
        self.graph[start].append((end, int(weight), directed))
        if not directed:
            self.graph[end].append((start, int(weight), directed))

    def printpath(self, start, goals):
        visited = set()
        priority_queue = [(0, start, [])]  # (total_cost, current_node, path)

        while priority_queue:
            cost, current_node, path = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)
            path.append(current_node)

            if current_node in goals:
                print("Path found:", path)  # Print the path when a goal node is reached
                return path

            if current_node in self.graph:
                neighbors = self.graph[current_node]
                for neighbor, weight, directed in neighbors:
                    if neighbor not in visited:
                        heapq.heappush(priority_queue, (cost + weight, neighbor, path[:]))

        print("No path found.")
        return []  # No path found
