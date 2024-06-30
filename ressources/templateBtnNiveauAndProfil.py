import sys

from functools import partial
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QSizePolicy,QLabel,QHBoxLayout
from uiFilesConvertedInPyFile.ui_interface import Ui_MainWindow


class GestionBtnNiveauEtProfil(QMainWindow):
    listeCurrentNiveauLibelle = []

    def __init__(self):
        super().__init__()
        self.btn_i = Ui_MainWindow()
        self.btn_i.setupUi(self)
        #self.ajoute()

    def ajoute(self):
        self.btn_i.label_6.setText("Je suis la page d'aide")
        self.btn_i.label_6.setObjectName("label_6")
        print(self.btn_i.label_6.text())

    def LesBoutonsDeProfil(self,listeProfil, listeNiveau):
        self.bt = QPushButton()
        liste_des_id_profil = listeProfil[1]
        liste_des_libelles_profil = listeProfil[0]
        liste_des_id_profil_dans_niveau = listeNiveau[1]
        liste_des_libelles_des_niveaux = listeNiveau[0]
        liste_courante_des_libelles_niveau = []

        #création du layout horizontal
        self.layout_button = QHBoxLayout(self.btn_i.zoneBoutonProfilCible)
        self.layout_button.setObjectName("layout_button")

        # liste = self.btn_i.zoneBoutonProfilCible.children()
        liste = self.layout_button.children()
        print(len(liste))

        for i in range(len(liste_des_id_profil)):
            id_profil_courant = liste_des_id_profil[i]
            nom_du_bouton = 'profilBtn{}'.format(i)
            mon_bouton = QPushButton(str(nom_du_bouton))
            mon_bouton.setObjectName(nom_du_bouton) #définir le nom du bouton en signalname
            mon_bouton.setText(liste_des_libelles_profil[i]) # définir le text à afficher sur le bouton
            #ici à chaque clique sur un bouton profilBtn{} on fait appel à la méthode generer_les_boutons_de_niveau
            mon_bouton.clicked.connect(partial(self.generer_des_boutons_de_niveau,
                                                              id_profil_courant,listeNiveau))

            for i in range(len(liste_des_id_profil_dans_niveau)):
                if id_profil_courant == liste_des_id_profil_dans_niveau[i]:
                    liste_courante_des_libelles_niveau.append(liste_des_libelles_des_niveaux[i])

            taille_btn_profil = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            taille_btn_profil.setHorizontalStretch(0)
            taille_btn_profil.setVerticalStretch(0)
            mon_bouton.setSizePolicy(taille_btn_profil)

            style_sheet = """
                    #{}{{
                        background-color:#26273c;
                        border-radius:10px;
                        text-align: center;
                        font-size: 20px;
                        font-weight: bold;
                        font-family: Century Schoolbook;
                        border: none;
                    }}
                    #{}:hover{{
                        background-color: #006918;
                    }}
                    #{}:pressed{{
                        background-color: black;
                        color: white;
                    }}
            """.format(nom_du_bouton, nom_du_bouton, nom_du_bouton)
            mon_bouton.setStyleSheet(style_sheet)


            self.layout_button.addWidget(mon_bouton)


    def generer_des_boutons_de_niveau(self, id_profil_courant,liste_des_niveaux):
        # --------- la suppression des widgets dans le gridLayout -------------------
        layout = self.btn_i.gridLayout

        # Supprimer tous les widgets du QGridLayout
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        # -------------------------------- FIN --------------------------------
        liste_des_libelles_niveau_cible = []
        liste_des_id_libelle_cible = []

        self.ui.label.setText(str(id_profil_courant))
        liste_des_libelles_des_niveaux = liste_des_niveaux[0]
        liste_des_id_profil_dans_niveau = liste_des_niveaux[1]
        liste_des_id_libelle_niveau = liste_des_niveaux[2]

        for i in range(len(liste_des_id_profil_dans_niveau)):
            if id_profil_courant == liste_des_id_profil_dans_niveau[i]:
                liste_des_libelles_niveau_cible.append(liste_des_libelles_des_niveaux[i])
                liste_des_id_libelle_cible.append(liste_des_id_libelle_niveau[i])

        self.BtnNiveau(liste_des_libelles_niveau_cible, liste_des_id_libelle_cible)
        GestionBtnNiveauEtProfil.listeCurrentNiveauLibelle = liste_des_libelles_niveau_cible



    def BtnNiveau(self, listeLibelleNiveau, currentIdLibelle):

        for i in range(len(listeLibelleNiveau)):
            signalName = 'NiveauBtn{}'.format(i)
            setattr(self, signalName, QPushButton(self.ui.scrollAreaWidgetContents_2))
            getattr(self, signalName).setObjectName(signalName)
            getattr(self, signalName).setText(listeLibelleNiveau[i])
            getattr(self, signalName).clicked.connect(partial(self.goToPageMatProfNotes,
                                                              argument=currentIdLibelle[i]))

            tailleBtn = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            getattr(self, signalName).setSizePolicy(tailleBtn)

            styleSheet = """
                    #{}{{
                        background-color:#26273c;
                        border-radius:10px;
                        text-align: center;
                        font-size: 20px;
                        font-weight: bold;
                        font-family: Century Schoolbook;
                        border: none;
                    }}
                    #{}:hover{{
                        background-color: #006918;
                    }}
                    #{}:pressed{{
                        background-color: black;
                        color: white;
                    }}
            """.format(signalName, signalName, signalName)
            getattr(self, signalName).setStyleSheet(styleSheet)
            for col in range(4):
                self.ui.gridLayout.addWidget(getattr(self, signalName), i, col, 1, 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GestionBtnNiveauEtProfil()
    window.show()
    app.exec_()