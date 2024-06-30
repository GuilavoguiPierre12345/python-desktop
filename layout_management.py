from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,QLineEdit, 
    QVBoxLayout,QHBoxLayout, QGridLayout
)

from PyQt6.QtCore import Qt 
from PyQt6.QtGui import QIcon # tout ce qui est graphique se trouve dans le module QtGui
import sys

class Window(QWidget):
    def __init__(self): # le self fait reference a la classe courante
        super().__init__() # initialisation du constructeur de la classe parente (QWidget)
        # self.resize(400, 400)
        self.setWindowIcon(QIcon("ico.jpg"))
        self.setWindowTitle("Formation PyQt 6")
        self.setContentsMargins(20,20,20,20)

        vbox = QVBoxLayout(self)
        self.setLayout(vbox)

        button = QPushButton("Bouton 1")
        vbox.addWidget(button)
        button = QPushButton("Bouton 2")
        vbox.addWidget(button)
        button = QPushButton("Bouton 3")
        vbox.addWidget(button)

   
# execution de l'application
app = QApplication(sys.argv)
window = Window()
window.show()
# app.exec()
sys.exit(app.exec())