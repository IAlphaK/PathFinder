import python_ui
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QGraphicsItem, QComboBox, QCheckBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QColor, QPen
from PyQt6.QtWidgets import QGraphicsScene
import tkinter as tk
from tkinter import simpledialog
import sys
import networkx as nx
import matplotlib.pyplot as plt
from bfs import bfsGraph
from dfs import dfsGraph
from BiDirectional import BidirectionalGraph
from UniformCostSearch import UCS_Graph




app = QApplication(sys.argv)
main_window = QMainWindow()
interface = python_ui.Ui_MainWindow()
interface.setupUi(main_window)

#for depth popup
root = tk.Tk()
root.withdraw()

#intialise graph
main_graph= None
#intialising algorthims variables
bfs=bfsGraph()
dfs=dfsGraph()
BiDirectional=BidirectionalGraph()
UniformCostSearch=UCS_Graph()
# Store references to the checkboxes and comboboxes
chk_inform = interface.chk_inform
chk_uninform = interface.chk_uninform
uninformed_dropdown = interface.uninformed_dropdown
i_informedheu = interface.i_informedheu
i_informednode = interface.i_informednode
addnode_heu = interface.addnode_heu
informed_dropdown = interface.informed_dropdown
direction_dropdown = interface.direction_dropdown

# By default, select chk_uninform and show the corresponding combobox
chk_uninform.setChecked(True)
uninformed_dropdown.setEnabled(True)
i_informedheu.setEnabled(False)
i_informednode.setEnabled(False)
addnode_heu.setEnabled(False)
informed_dropdown.setEnabled(False)

# Store references to the qlines
node1_qline = interface.i_n1
node2_qline = interface.i_n2
weight_qline = interface.i_weight
start_node_qline = interface.i_startnode
goal_nodes_qline = interface.i_goalnode

direction=0 #0 is undirected, 1 is directed
chkbox=0 #0 is uninformed, 1 is informed
informed_search = "Best First"  # store the selected informed search algorithm
uninformed_search = "Breadth First Search"  # store the selected uninformed search algorithm
def show_confirmation_popup():
    # Check if there is any previous progress
    if (
        node1_qline.text()
        or node2_qline.text()
        or weight_qline.text()
        or start_node_qline.text()
        or goal_nodes_qline.text()
    ):
        confirmation = QMessageBox.question(
            main_window,
            "Confirmation",
            "Switching will clear all previous progress. Are you sure you want to proceed?",
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel,
        )
        if confirmation == QMessageBox.StandardButton.Cancel:
            return False
        else:
            # Clear the qlines
            node1_qline.clear()
            node2_qline.clear()
            weight_qline.clear()
            start_node_qline.clear()
            goal_nodes_qline.clear()
    return True

def handle_chk_inform():
    if show_confirmation_popup():
        if chk_inform.isChecked():
            chkbox = 1
            chk_uninform.setChecked(False)
            uninformed_dropdown.setEnabled(False)
            i_informedheu.setEnabled(True)
            i_informednode.setEnabled(True)
            addnode_heu.setEnabled(True)
            informed_dropdown.setEnabled(True)
        else:
            chkbox = 0
            i_informedheu.setEnabled(False)
            i_informednode.setEnabled(False)
            addnode_heu.setEnabled(False)
            informed_dropdown.setEnabled(False)

def handle_chk_uninform():
    if show_confirmation_popup():
        if chk_uninform.isChecked():
            chkbox = 0
            chk_inform.setChecked(False)
            uninformed_dropdown.setEnabled(True)
            i_informedheu.setEnabled(False)
            i_informednode.setEnabled(False)
            addnode_heu.setEnabled(False)
            informed_dropdown.setEnabled(False)

def handle_informed_dropdown_change(index):
    global informed_search
    if show_confirmation_popup():
        selected_algorithm = informed_dropdown.itemText(index)
        # Store the selected informed search algorithm
        informed_search = selected_algorithm
def handle_uninformed_dropdown_change(index):
    global uninformed_search
    if show_confirmation_popup():
        selected_algorithm = uninformed_dropdown.itemText(index)
        # Store the selected uninformed search algorithm
        uninformed_search = selected_algorithm
def add_node():
    # Get the text entered in qlines
    node1 = node1_qline.text()
    node2 = node2_qline.text()
    weight = weight_qline.text()

    # Perform validation on the inputs
    if len(node1) != 1 or len(node2) != 1:
        QMessageBox.warning(main_window, "Invalid Input", "Node names should be a single letter.")
        return

    if not weight.isdigit():
        QMessageBox.warning(main_window, "Invalid Input", "Weight should be an integer.")
        return

    process_add(node1,node2,weight)
    # Clear the qlines
    node1_qline.clear()
    node2_qline.clear()
    weight_qline.clear()

inode_qline = interface.i_informednode
heu_qline = interface.i_informedheu
def add_heunode():
    # Get the text entered in qlines
    node1 = inode_qline.text()
    heu = heu_qline.text()

    # Perform validation on the inputs
    if len(node1) != 1:
        QMessageBox.warning(main_window, "Invalid Input", "Node name should be a single letter.")
        return

    if not heu.isdigit():
        QMessageBox.warning(main_window, "Invalid Input", "Weight should be an integer.")
        return
    # Clear the qlines
    inode_qline.clear()
    heu_qline.clear()
def start_to_goal_path():
    # Get the text entered in qlines
    start_node = start_node_qline.text()
    goal_nodes = goal_nodes_qline.text()

    # Perform validation on the inputs
    if not start_node.isalpha():
        QMessageBox.warning(main_window, "Invalid Input", "Start node should be a single letter.")
        return

    goal_nodes_list = goal_nodes.split(",")
    for goal_node in goal_nodes_list:
        if not goal_node.isalpha():
            QMessageBox.warning(main_window, "Invalid Input", "Goal nodes should be letters separated by commas.")
            return

    process_output(start_node, goal_node)
    # Clear the qlines
    start_node_qline.clear()
    goal_nodes_qline.clear()

def gen_graph():
    global main_graph
    if main_graph is None:
        print("Error: Graph doesnt exist, add some nodes first")
        return

    pos = nx.spring_layout(main_graph)

    node_size = 200
    node_color = "red"
    node_font_color = "white"
    edge_color = "black"

    fig, ax = plt.subplots()
    nx.draw_networkx_nodes(main_graph, pos, ax=ax, node_size=node_size, node_color=node_color, edgecolors="black")
    nx.draw_networkx_labels(main_graph, pos, ax=ax, font_color=node_font_color)
    nx.draw_networkx_edges(main_graph, pos, ax=ax, edge_color=edge_color)

    edge_labels = nx.get_edge_attributes(main_graph, "w")
    nx.draw_networkx_edge_labels(main_graph, pos, edge_labels=edge_labels, ax=ax)

    ax.axis("off")
    plt.tight_layout()
    plt.show()
def handle_direction_change(index):
    global direction
    if show_confirmation_popup():
        selected_direction = direction_dropdown.itemText(index)
        # Clear the qlines
        node1_qline.clear()
        node2_qline.clear()
        weight_qline.clear()
        start_node_qline.clear()
        goal_nodes_qline.clear()
        # Process the selected direction
        if selected_direction == "Undirected Graph":
            direction=0
        elif selected_direction == "Directed Graph":
            direction=1

def process_add(n1,n2,w):
    global direction,chkbox,informed_search,uninformed_search,main_graph
    if direction == 0: # Handle undirected graph
        if main_graph is None:
            main_graph=nx.Graph()
        main_graph.add_edge(n1,n2,w=w)
        main_graph.add_edge(n2, n1, w=w)

        if chkbox==0: #uninformed
            if uninformed_search == "Breadth First Search":
                bfs.addEdge(n1,n2,w,False)
            elif uninformed_search == "Depth First Search":
                dfs.addEdge(n1, n2, w, False)
            elif uninformed_search == "Depth Limited":
                pass
            elif uninformed_search == "Iterative Deepening":
                pass
            elif uninformed_search == "Uniform Cost Search":
                UniformCostSearch.addEdge(n1, n2, w, False)
            elif uninformed_search == "Bidirectional Search":
                BiDirectional.addEdge(n1, n2, w, False)
        elif chkbox==1: #informed
            if informed_search == "Best First":
                pass
            elif informed_search == "A*":
                pass
    elif direction == 1: # Handle directed graph
        if main_graph is None:
            main_graph=nx.DiGraph()
        main_graph.add_edge(n1, n2, w=w)

        if chkbox==0: #uninformed
            if uninformed_search == "Breadth First Search":
                bfs.addEdge(n1,n2,w,True)
            elif uninformed_search == "Depth First Search":
                dfs.addEdge(n1,n2,w,True)
            elif uninformed_search == "Depth Limited":
                pass
            elif uninformed_search == "Iterative Deepening":
                pass
            elif uninformed_search == "Uniform Cost Search":
                UniformCostSearch.addEdge(n1, n2, w, True)
            elif uninformed_search == "Bidirectional Search":
                BiDirectional.addEdge(n1, n2, w, True)
        elif chkbox==1: #informed
            if informed_search == "Best First":
                pass
            elif informed_search == "A*":
                pass

def process_output(s,g):
    global direction, chkbox, informed_search, uninformed_search
    depth=1
    if chkbox == 0:  # uninformed
        if uninformed_search == "Breadth First Search":
            bfs.printpath(s,g)
        elif uninformed_search == "Depth First Search":
            dfs.printpath(s,g)
        elif uninformed_search == "Depth Limited":
            depth = simpledialog.askinteger("Enter Depth", "Enter Depth:")
            pass
        elif uninformed_search == "Iterative Deepening":
            depth = simpledialog.askinteger("Enter Depth", "Enter Depth:")
            pass
        elif uninformed_search == "Uniform Cost Search":
            UniformCostSearch.printpath(s, g)
        elif uninformed_search == "Bidirectional Search":
            BiDirectional.printpath(s, g)
    elif chkbox == 1:  # informed
        if informed_search == "Best First":
            pass
        elif informed_search == "A*":
            pass

# Connect the signals to their respective slots
chk_inform.stateChanged.connect(handle_chk_inform)
chk_uninform.stateChanged.connect(handle_chk_uninform)
uninformed_dropdown.currentIndexChanged.connect(handle_uninformed_dropdown_change)
informed_dropdown.currentIndexChanged.connect(handle_informed_dropdown_change)
direction_dropdown.currentIndexChanged.connect(handle_direction_change)

interface.gen_path.clicked.connect(start_to_goal_path)
interface.gen_graph.clicked.connect(gen_graph)
interface.node_add.clicked.connect(add_node)
interface.addnode_heu.clicked.connect(add_heunode)

main_window.show()
sys.exit(app.exec())