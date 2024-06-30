from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QLineEdit, QVBoxLayout, QGridLayout
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

        layout = QGridLayout(self)
        self.setLayout(layout)

        self.label1 = QLabel("Username :")
        layout.addWidget(self.label1,0,0)
        self.label2 = QLabel("Password :")
        layout.addWidget(self.label2,1,0)

        self.input1 = QLineEdit()
        layout.addWidget(self.input1,0,1)
        self.input2 = QLineEdit()
        layout.addWidget(self.input2,1,1)

        button = QPushButton("submit")
        # button.setFixedWidth(80)
        button.clicked.connect(self.display)
        layout.addWidget(button,2,1,Qt.AlignmentFlag.AlignRight)

    def display(self):
        print(self.input1.text())
        print(self.input2.text())

# execution de l'application
app = QApplication(sys.argv)
window = Window()
window.show()
# app.exec()
sys.exit(app.exec())