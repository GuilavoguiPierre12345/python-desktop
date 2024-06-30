import os
import sys
#----------------------module tierces ---------------------------------
from ui_interface import *
from Custom_Widgets.Widgets import *
# ---------------------CUSTOM MODULES ----------------------------------
from CLoginRegister import *
from tablesCore import Handler
from tablesFile import Tables

## EXECUTE APP
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    #sys.exit(app.exec_())

#  ---------------les informations de l'users connecté qui doivent être enregistrer dans la table usersTable ------------------------
userData = window.loggedUserInfos
tableNiveauData = window.infosTableNiveau
tableEcoleData = window.infosTableEcole
tableProfilData = window.infosTableProfil


tablesStruct = Tables() #création de l'instance de la structure des tables
#  ---------------Structure de la table utilisateur------------------------
usersT = tablesStruct.usersTable()
#  ---------------Structure de la table niveau------------------------
niveauT = tablesStruct.niveauTable()
#  ---------------Structure de la table profil------------------------
profilT = tablesStruct.profilTable()
#  ---------------Structure de la table ecole------------------------
ecoleT = tablesStruct.ecoleTable()

db = Handler('testDb.db')
oldUsers = db.selectData(usersT,usersT["colsName"],0,1,2,2,2,2,2,2,
                    "","","0","100")
#print(oldUsers)
#print(userData)

if userData is not None:
    newUserId = userData[0]
#vérification de doublon dans la table users
isExist = False
for i in range(len(oldUsers)):
    #print(type(oldUsers[i][0]),oldUsers[i][0])
    if int(oldUsers[i][0]) == int(newUserId):
        isExist = True
        break

if not isExist:
    db.insertData(usersT, userData)
    db.insertData(ecoleT,tableEcoleData)
    for i in range(len(tableNiveauData)):
        db.insertData(niveauT,tableNiveauData[i])
        db.insertData(profilT,tableProfilData[i])
