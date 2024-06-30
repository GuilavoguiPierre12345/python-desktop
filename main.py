"""
Application de CRUD en PYQT5 et Python
Autheur : GUILAVOGUI FOROMO PIERRE
"""
import  sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QHeaderView
from PyQt5.QtCore import QPropertyAnimation,QEasingCurve
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from connexion_sqlite import Communication

class MainPrincipal(QMainWindow):
    def __init__(self):
        super(MainPrincipal,self).__init__()
        loadUi('design1.ui',self)

        #instance de le base de donnée
        self.database = Communication()
        # connexion des boutons d'entête au différente méthode
        self.btn_minimiser.hide()
        #self.btn_menu.clicked.connect(self.deplacer_menu)
        self.btn_reduire.clicked.connect(self.methode_reduire)
        self.btn_minimiser.clicked.connect(self.methode_minimiser)
        self.btn_maximiser.clicked.connect(self.methode_maximiser)
        self.btn_fermer.clicked.connect(lambda: self.close())

        # les boutons de traitement d'action
        """self.btn_actualiser.clicked.connect(self.methode_actualiser)
        self.btn_suppr.clicked.connect(self.methode_supprimer)
        self.btn_enreg.clicked.connect(self.methode_enregistrer)
        self.btn_miseajour.clicked.connect(self.methode_miseajour)
        self.btn_suppr_recherche.clicked.connect(self.methode_rechercher)
        self.btn_recherche.clicked.connect(self.methode_rechercher) """

        #-------- désactivation des boutons agrandir, reduire, minimiser --------------
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        #gripSize
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # ------- connexion des boutons aux différentes pages -------------------------
        self.btn_page_enreg.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(
            self.page_enreg))
        self.btn_page_suppr.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(
            self.page_suppr))
        self.btn_page_realisation.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(
            self.page_realisation))
        self.btn_page_database.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(
            self.page_db))
        self.btn_page_miseajour.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(
            self.page_miseajour))
        self.btn_page_apropos.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(
            self.page_apropos))
        self.btn_page_aide.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(
            self.page_aide))
        self.btn_page_param.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(
            self.page_params))

        #le traitement de la taille des tableaux
        self.table_suppr.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_produits.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def methode_reduire(self):
        self.showMinimized()

    def methode_maximiser(self):
        self.showMaximized()
        self.btn_maximiser.hide()
        self.btn_minimiser.show()

    def methode_minimiser(self):
        self.showNormal()
        self.btn_minimiser.hide()
        self.btn_maximiser.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainPrincipal()
    mainwindow.show()
    app.exec()