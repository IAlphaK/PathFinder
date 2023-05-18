from collections import defaultdict
import heapq


class BidirectionalGraph:
    def _init_(self):
        self.graph_forward = defaultdict(list)
        self.graph_backward = defaultdict(list)

    def addEdge(self, start, end, weight, directed=True):
        self.graph_forward[start].append((end, weight))
        self.graph_backward[end].append((start, weight))
        if not directed:
            self.graph_forward[end].append((start, weight))
            self.graph_backward[start].append((end, weight))

    def bidirectionalSearch(self, start, goals):
        queue_forward = [(0, start, [])]  # (total_cost, current_node, path)
        queue_backward = [(0, goals, [])]  # (total_cost, current_node, path)
        visited_forward = {start: (0, [])}  # {node: (total_cost, path)}
        visited_backward = {goals: (0, [])}  # {node: (total_cost, path)}
        intersect_node = None
        min_cost = float('inf')

        while queue_forward and queue_backward:
            forward_cost, current_forward, path_forward = heapq.heappop(queue_forward)
            backward_cost, current_backward, path_backward = heapq.heappop(queue_backward)

            if forward_cost + backward_cost >= min_cost:
                # The optimal path has been found
                break

            if current_forward in visited_backward:
                intersect_node = current_forward
                min_cost = forward_cost + backward_cost

            if current_backward in visited_forward:
                intersect_node = current_backward
                min_cost = forward_cost + backward_cost

            neighbors_forward = self.graph_forward[current_forward]
            neighbors_backward = self.graph_backward[current_backward]

            for neighbor, weight in neighbors_forward:
                total_cost = forward_cost + weight
                if neighbor not in visited_forward or total_cost < visited_forward[neighbor][0]:
                    visited_forward[neighbor] = (total_cost, path_forward + [current_forward])
                    heapq.heappush(queue_forward, (total_cost, neighbor, path_forward + [current_forward]))

            for neighbor, weight in neighbors_backward:
                total_cost = backward_cost + weight
                if neighbor not in visited_backward or total_cost < visited_backward[neighbor][0]:
                    visited_backward[neighbor] = (total_cost, [current_backward] + path_backward)
                    heapq.heappush(queue_backward, (total_cost, neighbor, [current_backward] + path_backward))

        if intersect_node is None:
            return [], float('inf')  # No path found, return empty path and infinite cost

        forward_path, forward_cost = visited_forward[intersect_node]
        backward_path, backward_cost = visited_backward[intersect_node]
        path = forward_path + [intersect_node] + list(reversed(backward_path))
        return path, forward_cost + backward_cost