from collections import defaultdict
import heapq

class BidirectionalGraph:
    def __init__(self):
        self.graph_forward = defaultdict(list)
        self.graph_backward = defaultdict(list)

    def addEdge(self, start, end, weight, directed=True):
        weight = int(weight) if weight.isnumeric() else float(weight)
        self.graph_forward[start].append((end, weight))
        self.graph_backward[end].append((start, weight))
        if not directed:
            self.graph_forward[end].append((start, weight))
            self.graph_backward[start].append((end, weight))

    def printpath(self, start, goals):
        queue_forward = [(0, start, [])]
        queue_backward = [(0, goal, []) for goal in goals]
        visited_forward = {start: (0, [])}
        visited_backward = {goal: (0, []) for goal in goals}
        intersect_nodes = set()
        min_cost = float('inf')

        while queue_forward and queue_backward:
            forward_cost, current_forward, path_forward = heapq.heappop(queue_forward)
            backward_cost, current_backward, path_backward = heapq.heappop(queue_backward)

            if forward_cost + backward_cost >= min_cost:
                break

            if current_forward in visited_backward:
                intersect_nodes.add(current_forward)
                min_cost = forward_cost + backward_cost

            if current_backward in visited_forward:
                intersect_nodes.add(current_backward)
                min_cost = forward_cost + backward_cost

            if forward_cost <= visited_forward[current_forward][0]:
                for neighbor, weight in self.graph_forward[current_forward]:
                    total_cost = forward_cost + weight
                    if neighbor not in visited_forward or total_cost < visited_forward[neighbor][0]:
                        visited_forward[neighbor] = (total_cost, path_forward + [current_forward])
                        heapq.heappush(queue_forward, (total_cost, neighbor, path_forward + [current_forward]))

            if backward_cost <= visited_backward[current_backward][0]:
                for neighbor, weight in self.graph_backward[current_backward]:
                    total_cost = backward_cost + weight
                    if neighbor not in visited_backward or total_cost < visited_backward[neighbor][0]:
                        visited_backward[neighbor] = (total_cost, [current_backward] + path_backward)
                        heapq.heappush(queue_backward, (total_cost, neighbor, [current_backward] + path_backward))

        for intersect_node in intersect_nodes:
            forward_path, forward_cost = visited_forward[intersect_node]
            backward_path, backward_cost = visited_backward[intersect_node]
            path = forward_path + [intersect_node] + list(reversed(backward_path))
            print(f"Path to {intersect_node} found: {path}")
