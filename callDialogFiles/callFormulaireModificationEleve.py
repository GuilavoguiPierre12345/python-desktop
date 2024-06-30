import os
import sys

from PyQt5.QtWidgets import QMessageBox, QDialog,QWidget,QVBoxLayout,QLabel
from uiFilesConvertedInPyFile.formulaireModificationEleve import Ui_formulaireModificationEleve
from Custom_Widgets.Widgets import *

class DialogueUpdateEleve(QDialog):
    def __init__(self):
        super().__init__()
        self.di = Ui_formulaireModificationEleve()
        self.di.setupUi(self)

        loadJsonStyle(self, self.di, jsonFiles={
            "jsonFiles/styleFormulaireModificationEleve.json"
        })
        # SHOW WINDOW
        self.show()