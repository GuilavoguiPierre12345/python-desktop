import sys

from PyQt5.QtWidgets import QMainWindow
from uiFilesConvertedInPyFile.ui_interface import Ui_MainWindow

class customTableWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ti = Ui_MainWindow()
        self.ti.setupUi(self)
        self.ti.payementMainPages.currentChanged.connect(self.show_table_payement)

    def show_table_payement(self):
        print("test value")
        self.table = self.ti.tablePayementFraisScolarite
        self.table.setColumnCount(10)  # le nombre total de colonne
        self.table.setRowCount(10)

        headers_label = ["N°", "Nom et Prenom", "Inscription Payé",
                         "Inscription Reste", "Tranche 1 Payé", "Tranche 1 Reste", "Tranche 2 Payé",
                         "Tranche 2 Reste", "Total Payé", "Total à Payer",
                         "Reste"]  # les nom des entêtes de tableau
        self.table_width(len(headers_label))
        self.table.setHorizontalHeaderLabels(headers_label)

    def table_width(self, col, width=200):
        self.table = self.ti.tablePayementFraisScolarite
        w = width
        for i in range(0, col, 1):
            if i == 0:
                w = 60
                self.table.setColumnWidth(i, w)
            elif i == 1:
                w = 400
                self.table.setColumnWidth(i, w)
            else:
                self.table.setColumnWidth(i, width)