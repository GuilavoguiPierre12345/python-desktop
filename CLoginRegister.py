import os
import sys
import asyncio
import socket
import json
# -------------------------TIERCES MODULES -------------------------------
import httpx
from ui_interface import *
from validate_email import validate_email
from Custom_Widgets.Widgets import *
from functools import partial
from PyQt5.QtWidgets import QMessageBox, QDialog,QWidget,QVBoxLayout,QLabel


# -------------------------CUSTOM MODULES ----------------------------------
from ConstantFile import Constantes as constante
from httpSender import dataSetter,dataGetter,dataPutter,dataDeleter
from tablesFile import Tables as tables
from getLocalData import listeProfil, listeNiveau,listeIdLibelleNiveau
from pageMatProfs import ListeProfMatiere
from formulaireModificationEleve import Ui_formulaireModificationEleve

# INITIALIZE APP SETTINGS
settings = QSettings()


class Dialogue(QDialog):
    def __init__(self):
        super().__init__()
        self.di = Ui_formulaireModificationEleve()
        self.di.setupUi(self)

        loadJsonStyle(self, self.di, jsonFiles={
            "style2.json"
        })
        # SHOW WINDOW
        self.show()



## MAIN WINDOW CLASS
class MainWindow(QMainWindow):
    # declaration des propriétés de la classe
    loggedUserInfos = "Vide" #les informations de l'utilisateur connecté
    infosTableEcole = "Vide" #les informations à sauvegarder dans la table ecole
    infosTableNiveau = [] #les informations à sauvegarder dans la table niveau
    infosTableProfil = [] #les informations à sauvegarder dans la table profil
    liste = listeProfil()
    listeNiveau= listeNiveau()
    listeIdLibelles = listeIdLibelleNiveau()
    listeCurrentNiveauLibelle =[]

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.loginBtnEmma.clicked.connect(self.goToDashboard)
        #self.ui.loginBtnEmma.clicked.connect(self.loginFunction)
        self.ui.logOutBtn.clicked.connect(self.logOutFonction)
        self.ui.registerBtnEmma.clicked.connect(self.goToRegisterForm)
        self.ui.loginBtn.clicked.connect(self.goToLoginForm)
        self.ui.registerBtn.clicked.connect(self.registerFunction)
        self.ui.gridEleveUpdateBtn.clicked.connect(self.ouvrir_dialogue_modification_information_eleve)

        # méthode permettant de générer les boutons de profil
        self.BtnProfil(MainWindow.liste)

        # LOAD JSON FILE
        loadJsonStyle(self, self.ui, jsonFiles={
            "style.json"
        })
        # SHOW WINDOW
        self.show()


    #méthode d'ouverture du formulaire de modification d'un eleve
    def ouvrir_dialogue_modification_information_eleve(self):
        dialog = Dialogue()
        dialog.exec_()
        # traitement à effectuer ici

    def loginFunction(self):
        if self.checkInternet():
            email = self.ui.emailUser.text()
            password = self.ui.motDePasseLogin.text()
            #si les champs sont vides
            if email =="" or password=="":
                self.button_clicked("Infos Error")
                self.ui.erreurMessage.setText("Veuillez saisir un mail ou votre password")
                print("Veuillez saisir un mail ou votre password")
                return 0

            if validate_email(email):
                    try:
                        response = asyncio.run(dataSetter(constante.AUTH_URL, {"E_Mail": email,
                                                                                "Mot_de_Passe": password}))
                        if response['error'] == False:
                            #les informations de l'utilisation qui est connecter sur l'application
                            usersInfo = [
                                response['id'],
                                response['user']['Prenom'],
                                response['user']['Nom'],
                                response['user']['Sexe'],
                                response['user']['Telephone'],
                                response['user']['E_Mail'],
                                response['user']['emailSecour'],
                                response['user']['Date_Inscription']
                            ]

                            #affectation des données de l'user connecté à la propriété loggedUserInfos
                            #pour enfin l'enregistrer dans la base des données local
                            MainWindow.loggedUserInfos = usersInfo

                            #affectation de la structure des tables aux variables locales pour
                            #pouvoir les manipuler dans les requêttes de récupération sur le serveru """
                            tableNiveauStruct = tables.niveauTable(self)
                            tableProfilStruct = tables.profilTable(self)
                            tableEcoleStruct = tables.ecoleTable(self)

                            #cette section du code permet de compléter la requêtte de façon
                            #dynamique gèrant l'ajout des virgules dans la requêtte
                            line = ""
                            for i in range(len(tableNiveauStruct["colsName"])):
                                addVirgule = " " if i == len(tableNiveauStruct["colsName"])-1 else ", "
                                line += tableNiveauStruct["tableName"]+"."+tableNiveauStruct["colsName"][i]+" AS "+ tableNiveauStruct["colsName"][i]+"_"+tableNiveauStruct["tableName"]+addVirgule
                            line +=","

                            for i in range(len(tableProfilStruct["colsName"])):
                                addVirgule = " " if i == len(tableProfilStruct["colsName"]) - 1 else ", "
                                line += tableProfilStruct["tableName"] + "." + tableProfilStruct["colsName"][
                                    i] + " AS " + tableProfilStruct["colsName"][i] + "_" + tableProfilStruct[
                                            "tableName"] + addVirgule
                            line += ","

                            for i in range(len(tableEcoleStruct["colsName"])):
                                addVirgule = " " if i == len(tableEcoleStruct["colsName"]) - 1 else ", "
                                line += tableEcoleStruct["tableName"] + "." + tableEcoleStruct["colsName"][
                                    i] + " AS " + tableEcoleStruct["colsName"][i] + "_" + tableEcoleStruct[
                                            "tableName"] + addVirgule

                            self.changeInformations(tableNiveauStruct["tableName"],"0","0","0","0",
                            "0","0","","","LIMIT 0,100","SELECT "+ line +" FROM "+ tableNiveauStruct["tableName"] +
                            " INNER JOIN "+tableProfilStruct["tableName"]+" ON "+tableNiveauStruct["tableName"]+".idProfil="+tableProfilStruct["tableName"]+".idProfilUniv "
                            "INNER JOIN "+tableEcoleStruct["tableName"]+" ON "+tableProfilStruct["tableName"]+".idEcoleMere="+tableEcoleStruct["tableName"]+".idEcole "
                            "WHERE t_profil_univ.idEcoleMere=?",
                            ["242"],tableNiveauStruct["colsName"],tableNiveauStruct["colsType"])

                            self.printLoggedInfoOnDashboard(usersInfo[2],usersInfo[1],usersInfo[5],usersInfo[4])
                            self.goToDashboard() #naviguer vers le homepage
                            self.ui.erreurMessage.setText("") #vider le message d'erreur
                            return usersInfo
                    except Exception as e:
                        self.button_clicked("Server Error")
                        self.ui.erreurMessage.setText("Une erreur est survenu lors de "
                                                      "l'intérogation du server")
                        print("Une erreur est survenu lors de l'intérogation du server :"+ str(e))
                        return 0
            else:
                self.button_clicked("Invalid Email")
                self.ui.erreurMessage.setText("Erreur : email invalide")
                print("email is not valid")
        else :
            self.button_clicked("Connection")
            self.ui.erreurMessage.setText("Erreur : Vérifier votre connexion internet")
            print("Veuillez vérifier votre connexion internet !")

    #traitement pour l'ajout
    def registerFunction(self):
        emailMagoe = self.ui.userMagoeEmail.text()
        emailMagoe = emailMagoe.split()
        registerInfo={
            "Prenom":self.ui.userPrenom.text(),
            "Nom":self.ui.userNom.text(),
            "Telephone":self.ui.userTelephone.text(),
            "E_Mail":self.ui.userMagoeEmail.text(),
            "Sexe":self.ui.userSexe.text(),
            "emailSecour":self.ui.userEmailSecours.text(),
            "Mot_de_Passe":self.ui.userPassword.text()
        }
        #vérification de la connexion internet
        if self.checkInternet():
            try:
                response = asyncio.run(dataSetter(constante.REGISTER_URL,registerInfo))
                if response['error']==False :
                    self.ui.emailUser.setText(self.ui.userMagoeEmail.text())
                    self.goToLoginForm()
                    #ici l'enregistrement des infos de l'user
                    return response
                print(response['error_msg'])

            except Exception as e:
                print("une erreur est arrivée lors de l'inscription : " + str(e))
        else:
            print("you are not connected")

        #vérification de l'existence de l'internet

    #vérification de la connection internet
    def checkInternet(self):
        try:
            socket.create_connection((constante.MAIN_URL,80))
            return  True
        except OSError as e:
            print("Error creating connection :"+ str(e))
            return False

    #navigation de login ===> dashboard(le home)
    def goToDashboard(self):
        self.ui.motDePasseLogin.setText("")
        stackedWidget = self.ui.pagesParent
        stackedWidget.setCurrentIndex(stackedWidget.currentIndex()+2)

    # navigation de login ===> register form(formulaire d'enregistrement)
    def goToRegisterForm(self):
        stackedWidget = self.ui.pagesParent
        stackedWidget.setCurrentIndex(stackedWidget.currentIndex()+1)
    # navigation d'un btn profil ===> la page d'un niveau

    def generateBtnNiveau(self,argument):
        # --------- la suppression des widgets dans le gridLayout -------------------
        layout = self.ui.gridLayout

        # Supprimer tous les widgets du QGridLayout
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        # -------------------------------- FIN --------------------------------
        currentListeLibelle = []
        currentIdLibelle = []

        self.ui.label.setText(str(argument))
        niveauLibelle = MainWindow.listeNiveau[0]
        niveauId =MainWindow.listeNiveau[1]
        idLibelle = MainWindow.listeNiveau[2]

        for i in range(len(niveauId)):
            if argument == niveauId[i]:
                currentListeLibelle.append(niveauLibelle[i])
                currentIdLibelle.append(idLibelle[i])

        self.BtnNiveau(currentListeLibelle, currentIdLibelle)
        MainWindow.listeCurrentNiveauLibelle = currentListeLibelle

    # navigation de register ===> login(formulaire de connexion)

    def goToLoginForm(self):
         stackedWidget = self.ui.pagesParent
         stackedWidget.setCurrentIndex(stackedWidget.currentIndex() - 1)

    def printLoggedInfoOnDashboard(self,nom,prenom,email,contact):
        self.ui.user_FirstName.setText(prenom)
        self.ui.user_Name.setText(nom)
        self.ui.user_MagoeEmail.setText(email)
        self.ui.user_Telephone.setText(contact)

    def changeInformations(self,tblName,idOffLineIndex,idOnLineIndex,labelIndex,idParentIndex,
                singleEntryIndex,dualEntryIndex,reqGroup,reqOrder,reqLimit,reqStringForGet,
                reqArrayForGet,tbl_rowLabel,tbl_rowType):
        data = {
            "bddType":"1",
            "tblName":tblName,
            "idOffLineIndex":idOffLineIndex,
            "idOnLineIndex":idOnLineIndex,
            "labelIndex": labelIndex,
            "idParentIndex":idParentIndex,
            "singleEntryIndex":singleEntryIndex,
            "dualEntryIndex":dualEntryIndex,
            "reqGroup":reqGroup,
            "reqOrder":reqOrder,
            "reqLimit":reqLimit,
            "reqStringForGet":reqStringForGet,
            "reqArrayForGet":reqArrayForGet,
            "tbl_rowLabel":tbl_rowLabel,
            "tbl_rowType":tbl_rowType,
        }
        #try:
        response = asyncio.run(dataSetter(constante.GETGLOBALINFO_URL,data))
        #print(json.dumps(response["item"],indent=4))

        self.tableEcoleInformation(response["item"][4])
        for i in range(len(response["item"])):
            self.tableNiveauInformation(response["item"][i])
            self.tableProfilInformation(response["item"][i])


        #except Exception as e:
            #print("Une erreur survenu lors de l'intérogation du server :" + str(e))
            #return 0

    def tableEcoleInformation(self,ecole):
        info = [
            ecole["idEcoleMere_t_profil_univ"],
            ecole["nomEcole_ecoletable"],
            ecole["idQuartier_ecoletable"],
            ecole["structure_ecoletable"],
            ecole["typeEnseignement_ecoletable"],
            ecole["ficheRenseignement_ecoletable"],
            ecole["presentation_ecoletable"],
            ecole["mission_t_profil_univ"],
            ecole["competence_ecoletable"],
            ecole["admission_ecoletable"],
            ecole["telephone1_ecoletable"],
            ecole["telephone2_ecoletable"],
            ecole["telephone3_ecoletable"],
            ecole["gmail_ecoletable"],
            ecole["yahoo_ecoletable"],
            ecole["magoe_ecoletable"],
            ecole["facebook_ecoletable"],
            ecole["twiter_ecoletable"],
            ecole["istagramme_ecoletable"],
            ecole["abreviation_ecoletable"],
            ecole["slogan_ecoletable"],
            ecole["latitude_ecoletable"],
            ecole["longitude_ecoletable"],
            ecole["rayon_ecoletable"],
            ecole["linkVideo_ecoletable"],
            ecole["idDsee_ecoletable"],
            ecole["nomQuartier_ecoletable"],
            ecole["nomCommune_ecoletable"],
            ecole["nomVille_ecoletable"],
            ecole["nomPays_ecoletable"],
            ecole["nomContinent_ecoletable"],
            ecole["linkPlayStore_ecoletable"],
            ecole["emailParain_ecoletable"],
            ecole["adresseEcole_ecoletable"],
            ecole["emailOperateur_ecoletable"],
            ecole["dateEnrEcol_ecoletable"]

        ]
        MainWindow.infosTableEcole = info

    #Methode pour obetenir les information de la table TNiveau
    def tableNiveauInformation (self,niveau):
         tInfo = [
             niveau["idLibelle_t_niveau_univ"],
             niveau["libelle_t_niveau_univ"],
             niveau["idProfil_t_niveau_univ"],
             niveau["description_t_niveau_univ"],
             niveau["validNiveau_t_niveau_univ"],
             niveau["rang_t_niveau_univ"],
             niveau["libelleProfil_t_niveau_univ"],
             niveau["emailOp_t_niveau_univ"],
             niveau["dateSav_t_niveau_univ"]
         ]
         MainWindow.infosTableNiveau.append(tInfo)

    def tableProfilInformation(self,profil):
        info = [
            profil["idProfilUniv_t_profil_univ"],
            profil["labelProfil_t_profil_univ"],
            profil["idEcoleMere_t_profil_univ"],
            profil["description_t_profil_univ"],
            profil["presentation_t_profil_univ"],
            profil["mission_t_profil_univ"],
            profil["validProfil_t_profil_univ"],
            profil["rang_t_profil_univ"],
            profil["emailRecteur_t_profil_univ"],
            profil["dateProfilUniv_t_profil_univ"]
        ]
        MainWindow.infosTableProfil.append(info)

    #cette méthode permet de partir sur la page : pageMatProfNotes
    def goToPageMatProfNotes(self,argument):
        #appel à la méthode de récupération des infos matiere et professeur sur le serveur
        profMat = ListeProfMatiere()
        listeProfMatAnneGroup = profMat.getMatieres(argument)

        #cet argument est l'id du libelle du niveau
        self.modelGraphiqueProfMat(argument,listeProfMatAnneGroup)

        stackedMp = self.ui.mainPages
        stackedMp.setCurrentIndex(5)
    #cette méthode permet de faire la déconnection (i-e: de la page courante vers le login)
    def logOutFonction(self):
        stackedPp = self.ui.pagesParent
        stackedPp.setCurrentIndex(0)

    def BtnProfil(self,liste):
        listeIdNiveau = MainWindow.listeNiveau[1] #la liste des id des niveaux
        listeLibelleNiveau = MainWindow.listeNiveau[0] #la  liste des niveaux

        listeCurrentNiveauLibelle = []
        for i in range(len(liste[0])):
            currentIdProfil = liste[1][i]
            signalName = 'profilBtn{}'.format(i)
            setattr(self, signalName, QPushButton(self.ui.scrollAreaWidgetContents_4))
            getattr(self, signalName).setObjectName(signalName)
            getattr(self, signalName).setText(liste[0][i])
            getattr(self, signalName).clicked.connect(partial(self.generateBtnNiveau,
                                                              argument=currentIdProfil))

            for i in range(len(listeIdNiveau)):
                if currentIdProfil==listeIdNiveau[i]:
                    listeCurrentNiveauLibelle.append(listeLibelleNiveau[i])


            tailleBtn = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            tailleBtn.setHorizontalStretch(0)
            tailleBtn.setVerticalStretch(0)
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

            self.ui.horizontalLayout_14.addWidget(getattr(self, signalName))

    def BtnNiveau(self,listeLibelleNiveau,currentIdLibelle):

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
                self.ui.gridLayout.addWidget(getattr(self, signalName),i,col,1,1)

    def modelGraphiqueProfMat(self,targetIdLibelle,listInfoBox):
        if listInfoBox is not None:

            for i in range(len(MainWindow.listeIdLibelles)):
                if targetIdLibelle == MainWindow.listeIdLibelles[i]:
                    # création du QVLayout
                    vlayout = QVBoxLayout()

                    # création des étiquettes
                    prof = QLabel("{ }".format(listInfoBox[i]["professeur"]))
                    matiere = QLabel("{ }".format(listInfoBox[i]["matiere"]))
                    groupeped = QLabel("{ }".format(listInfoBox[i]["groupePed"]))

                    #ajout es étiquettes au vlayout
                    vlayout.addWidget(prof)
                    vlayout.addWidget(matiere)
                    vlayout.addWidget(groupeped)

                    #affectation du vlayout au gridlayout
                    self.ui.gridMatiereProf.addWidget(vlayout, i, col, 1, 1)
        else:
            print("Erreur de connexion au serveur")


    def chargementEnCours(self):
        self.ui.loginBtnEmma.setText("Chargement en cours...")
        self.ui.loginBtnEmma.setEnabled(False)
        self.styleBtnChargement = """
            background-color: #248ca1;
            padding: 10px 70px 10px;
            border-radius: 5px;
            width: 250px;
        """
        self.ui.loginBtnEmma.setStyleSheet(self.styleBtnChargement)
        print("waiting for")

    def finChargementEnCours(self):
        self.ui.loginBtnEmma.setText("S'IDENTIFIER")
        self.ui.loginBtnEmma.setEnabled(True)
        self.styleBtnFinChargement ="""
                background-color: #248cd6;
                padding: 10px 70px 10px;
                border-radius: 5px;
                width: 250px;
                    """
        self.ui.loginBtnEmma.setStyleSheet(self.styleBtnFinChargement)
        print("end waiting")

    def button_clicked(self,typeError):
        dlg = QMessageBox()
        dlg.setWindowTitle("Alerte Message")
        if typeError == "Connection":
            dlg.setText("Erreur, vérifier votre connexion internet")
        elif typeError == "Infos Error":
            dlg.setText("Erreur, veuillez saisir vos informations")
        elif typeError == "Server Error":
            dlg.setText("Erreur, une problème de communication avec le serveur, svp assurer vous "
                        "d'avoir une bonne connexion internet")
        else :
            dlg.setText("Erreur, votre adresse email est invalide")
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Ok:
            print("OK!")

"""
    def show_dialog(self):
        dlg = WaitingDialog(self)
        dlg.exec()
"""


