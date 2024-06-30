import os
import sys

from Custom_Widgets.Widgets import *

from ui_interface import *
from tablesCore import Handler
from tablesFile import Tables

#récupération des informations dans la base de données
db =Handler('testDb.db')
table = Tables()
profilT = table.profilTable()
NiveauT = table.niveauTable()
usersT = table.usersTable()
#Création des tables dans la base de données
db.createTable(usersT)
db.createTable(profilT)
db.createTable(NiveauT)



#Vérification de l'existence de la table
tablExistProfil = db.verifyIfTableExists(profilT)
tablExistNiveau = db.verifyIfTableExists(NiveauT)

#Vérification de l'existence des tables
if not tablExistProfil and not tablExistNiveau:
    print("La table n'exise pas")
else :
    def listeProfil():
        listeLibelleProfil=[]
        listeIdProfil=[]
        listeLibelleIdProfil=[]
        dataProfil=db.selectData(profilT,profilT["colsName"],1,2,2,2,2,2,2,1,"","","0","10")
        for i in range(len(dataProfil)):
            listeLibelleProfil.append(dataProfil[i][1])
            listeIdProfil.append(dataProfil[i][0])

        listeLibelleIdProfil.append(listeLibelleProfil)
        listeLibelleIdProfil.append(listeIdProfil)
        #print (listeLibelleProfil)

        return  listeLibelleIdProfil

    def listeNiveau():

        listeLibelleNiveau = []
        listeIdProfilNiveau = []
        listeLibelleIdNiveau=[]
        libellesId = []

        dataNiveau= db.selectData(NiveauT,NiveauT['colsName'],1,2,2,2,2,2,2,1,"","","0","50")
        for i in range(len(dataNiveau)):
            listeLibelleNiveau.append(dataNiveau[i][1])
            listeIdProfilNiveau.append(dataNiveau[i][2])
            libellesId.append(dataNiveau[i][0])

        listeLibelleIdNiveau.append(listeLibelleNiveau)
        listeLibelleIdNiveau.append(listeIdProfilNiveau)
        listeLibelleIdNiveau.append(libellesId)

        #print(json.dumps(listeLibelleIdNiveau, indent=4))
        #listeLibelleIdNiveau=listeLibelleNiveau + listeIdProfilNiveau
        return listeLibelleIdNiveau

    def listeIdLibelleNiveau():
        listeIdentifiantNiveau = []
        data= db.selectData(NiveauT,NiveauT['colsName'],1,2,2,2,2,2,2,1,"","","0","50")
        for i in range(len(data)):
            listeIdentifiantNiveau.append(data[i][0])

        #print(listeIdentifiantNiveau)
        return listeIdentifiantNiveau

    #listeNiveau()
#----------------------------------------------------------------
