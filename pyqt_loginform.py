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
        self.setWindowTitle("Formation PyQt6 | Login Form")
        layout = QGridLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10) # mettre les espaces entre les elements du layout
        self.setLayout(layout) 

        title = QLabel("Form Login | Register")
        layout.addWidget(title,0,0,1,3,Qt.AlignmentFlag.AlignCenter)

        username = QLabel("Username:")
        layout.addWidget(username,1,0)
        self.username_value = QLineEdit()
        layout.addWidget(self.username_value,1,1,1,2)


        pwd = QLabel("Password:")
        layout.addWidget(pwd,2,0)
        self.pwd_value = QLineEdit()
        self.pwd_value.setEchoMode(QLineEdit.EchoMode.Password) # changer le mode d'affiche en password
        layout.addWidget(self.pwd_value,2,1,1,2)

        register_btn = QPushButton("Register")
        layout.addWidget(register_btn,3,1)

        login_btn = QPushButton("Login")
        login_btn.clicked.connect(self.login)
        layout.addWidget(login_btn,3,2)

    def login(self):
        credentials = ["yaboigui","yaboigui12"]
        credentials_correct = True

        if self.username_value.text() != credentials[0]:
            credentials_correct = False
            print("username is incorrect")

        if self.pwd_value.text() != credentials[1]:
            credentials_correct = False
            print("password is incorrect")
        
        if credentials_correct:
            self.username_value.setText("")
            self.pwd_value.setText("")
            print("User credentials are correct")




    
# execution de l'application
app = QApplication(sys.argv)
window = Window()
window.show()
# app.exec()
sys.exit(app.exec())