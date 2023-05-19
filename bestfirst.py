import networkx as nx


def generate_graph(main_graph,node1, node2, weight):
    """
    Generate a graph without using networkx library, with node1, node2, weight, and heuristic values.
    Initialize all heuristic values to 0.
    Returns the graph generated using networkx library.
    """
    graph = []
    graph.append((node1, node2, weight, 0))  # Assuming the graph is an edge list with (node1, node2, weight, heuristic) format

    # Add more edges to the graph if needed

    # Generate the graph using networkx library
    if main_graph is None:
        main_graph = nx.Graph()
    for edge in graph:
        main_graph.add_edge(edge[0], edge[1], weight=edge[2])

    return main_graph


def add_heuristic_value(graph, informed_node, heuristic_value):
    """
    Check if the informed_node exists in the graph and update its heuristic value.
    """
    if informed_node in graph.nodes:
        graph.nodes[informed_node]['heuristic'] = heuristic_value
        print(informed_node, " Heuristic value set to: ", heuristic_value)
    else:
         print("Node does not exist")


def best_first_search(graph, start_node, goal_nodes):
    """
    Traverse the graph using the Best First Search algorithm based on the graph generated without networkx library.
    Returns the path found by the Best First Search algorithm and the sub-graph generated using networkx library.
    """
    visited = set()
    priority_queue = [(start_node, 0)]
    path = []
    sub_graph = nx.Graph()

    while priority_queue:
        current_node, _ = priority_queue.pop(0)

        if current_node in visited:
            continue

        visited.add(current_node)
        path.append(current_node)
        sub_graph.add_node(current_node)

        if current_node in goal_nodes:
            break

        neighbors = graph.neighbors(current_node)
        for neighbor in neighbors:
            if neighbor not in visited:
                priority = graph[current_node][neighbor]['weight'] + graph.nodes[neighbor].get('heuristic', 0)
                priority_queue.append((neighbor, priority))
                sub_graph.add_edge(current_node, neighbor)

        priority_queue.sort(key=lambda x: x[1])

    return path, sub_graph