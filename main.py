########################################################################
##  RESPONSIVE APP
##  QT GUILAVOGUI PIERRE FOROMO
#########################################################################

import os
import sys

from ui_interface import * #importer toutes les classes qui sont dans ui_interface ici :
# Ui_MainWindow

########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
########################################################################


#main window class
class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        ########################################################################
        #show window
        self.show()

        # -------------------------- section 1 -----------------------------------------
        #traitement d'ouverture du centerMenuContainer
        self.ui.settingsBtn.clicked.connect(lambda:self.ui.centerMenuContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda:self.ui.centerMenuContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda:self.ui.centerMenuContainer.expandMenu())

        #traitement de fermeture du centerMenuContainer
        self.ui.closeCenterMenuBtn.clicked.connect(
            lambda:self.ui.centerMenuContainer.collapseMenu())

        # --------------------------end section 1 -------------------------------------------

        #--------------------------- section 2 ---------------------------------------------
        # traitement d'ouverture du centerMenuContainer
        self.ui.moreMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.profileMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())

        # traitement de fermeture du centerMenuContainer
        self.ui.closeRightMenuContainer.clicked.connect(
            lambda: self.ui.rightMenuContainer.collapseMenu())

        #--------------------------- end section 2 ------------------------------------------


#execute app
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    app.exec_()
    #sys(app.exec_())

