import os
import sys

from PyQt5.QtWidgets import QDialog
from uiFilesConvertedInPyFile.modalPayementFrais import Ui_payementFrais
from Custom_Widgets.Widgets import *

class DialoguePayementFrais(QDialog): #cette classe hérite de la classe QDialog
    def __init__(self): # le constructeur de la classe
        super().__init__() # appel du constructeur de QDialog
        self.pi = Ui_payementFrais() #instanciation de la classe Ui_payementFrais
        self.pi.setupUi(self)

        loadJsonStyle(self, self.pi, jsonFiles={
            "jsonFiles/stylePayementFrais.json"
        })
        # SHOW WINDOW
        self.show()
