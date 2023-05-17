import python_ui
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QGraphicsItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QColor, QPen
from PyQt6.QtWidgets import QGraphicsScene
import sys

app = QApplication(sys.argv)
main_window = QMainWindow()
interface = python_ui.Ui_MainWindow()
interface.setupUi(main_window)

# Store references to the qlines
node1_qline = interface.i_n1
node2_qline = interface.i_n2
weight_qline = interface.i_weight

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

    # Clear the qlines
    node1_qline.clear()
    node2_qline.clear()
    weight_qline.clear()





interface.node_add.clicked.connect(add_node)
main_window.show()
sys.exit(app.exec())
