import sys

from dialogFiles.dialogForWaiting import Ui_Dialog
from PyQt6.QtWidgets import QApplication,QDialog,QMainWindow

class WaitingDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)

