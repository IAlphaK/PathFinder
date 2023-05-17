from flask import app

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
##########################################################################################





##########################################################################################
main_window.show()

sys.exit(app.exec())