PathFinder
==========

Overview
--------

PathFinder is a graphical pathfinding application implemented in Python, utilizing various search algorithms to find paths between nodes in a graph. The application provides both informed and uninformed search algorithms and uses NetworkX for graph representation and PyQt6 for the graphical user interface.

Features
--------

*   **Graph Creation**: Users can create graphs by adding nodes and weighted edges.
    
*   **Algorithm Selection**: Supports both informed and uninformed search algorithms.
    
*   **Graph Visualization**: Displays the graph and highlights the selected path.
    
*   **User Input**: Users can specify the start node, goal node(s), and heuristic values for informed searches.
    

Algorithms Implemented
----------------------

The following pathfinding algorithms are supported:

### **Uninformed Search Algorithms**

1.  **Breadth-First Search (BFS)** - Explores all neighbors before moving to the next level.
    
2.  **Depth-First Search (DFS)** - Explores as far as possible before backtracking.
    
3.  **Depth-Limited Search (DLS)** - DFS with a predefined depth limit.
    
4.  **Iterative Deepening Search (IDS)** - Combines DFS and BFS by gradually increasing the depth limit.
    
5.  **Uniform Cost Search (UCS)** - Expands the least-cost node first.
    
6.  **Bidirectional Search** - Runs two simultaneous searches from start and goal.
    

### **Informed Search Algorithms**

1.  **Greedy Best-First Search** - Expands the node with the lowest heuristic value.
    
2.  _A Search (A-Star)_\* - Expands nodes based on the sum of cost and heuristic.
    

Files and Their Functions
-------------------------

*   **main.py**: The entry point of the application, handling user interaction and algorithm execution.
    
*   **python\_ui.py**: Auto-generated PyQt6 UI file defining the graphical interface.
    
*   **bfs.py**: Implements Breadth-First Search.
    
*   **dfs.py**: Implements Depth-First Search.
    
*   **dls.py**: Implements Depth-Limited Search.
    
*   **ids.py**: Implements Iterative Deepening Search.
    
*   **ucs.py**: Implements Uniform Cost Search.
    
*   **bid.py**: Implements Bidirectional Search.
    
*   **bestfirst.py**: Implements Greedy Best-First Search.
    
*   **astar.py**: Implements A\* Search.
    

Dependencies
------------

*   Python 3.x
    
*   NetworkX
    
*   PyQt6
    
*   Matplotlib
    

Installation
------------

1.  Clone the repository:
```sh
git clone https://github.com/IAlphaK/PathFinder.git
cd PathFinder
```    
2.  Install required dependencies:
```sh
pip install networkx PyQt6 matplotlib
```    
3.  Run the application:
```sh
python main.py
```    

Usage
-----

1.  Launch the application.
    
2.  Select the type of search (Informed or Uninformed).
    
3.  Choose the desired algorithm from the dropdown menu.
    
4.  Add nodes and edges to build the graph.
    
5.  Enter the start node and goal nodes.
    
6.  Click "Generate Graph" to visualize the graph.
    
7.  Click "Find Path" to compute and display the path.
    

License
-------

This project is licensed under the MIT License.
