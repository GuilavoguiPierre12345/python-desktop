import os
import sys

from Custom_Widgets.Widgets import *

from uiFilesConvertedInPyFile.ui_interface import *
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
        liste_des_libelles_des_profils=[]
        liste_des_id_des_profils=[]
        liste_des_libelles_et_id_des_drofils=[]
        information_sur_les_profils=db.selectData(profilT,profilT["colsName"],1,2,2,2,2,2,2,1,"","","0","10")
        for i in range(len(information_sur_les_profils)):
            liste_des_libelles_des_profils.append(information_sur_les_profils[i][1])
            liste_des_id_des_profils.append(information_sur_les_profils[i][0])

        liste_des_libelles_et_id_des_drofils.append(liste_des_libelles_des_profils)
        liste_des_libelles_et_id_des_drofils.append(liste_des_id_des_profils)
        #print (listeLibelleProfil)
        return liste_des_libelles_et_id_des_drofils

    def listeNiveau():

        liste_des_libelles_des_niveaux = []
        liste_des_id_profils_dans_table_niveau = []
        liste_des_libelles_id_dans_table_niveau=[]
        liste_des_id_des_libelles_dans_table_niveau = []

        informations_sur_les_niveaux= db.selectData(NiveauT,NiveauT['colsName'],1,2,2,2,2,2,2,1,"","","0","50")
        for i in range(len(informations_sur_les_niveaux)):
            liste_des_libelles_des_niveaux.append(informations_sur_les_niveaux[i][1])
            liste_des_id_profils_dans_table_niveau.append(informations_sur_les_niveaux[i][2])
            liste_des_id_des_libelles_dans_table_niveau.append(informations_sur_les_niveaux[i][0])

        liste_des_libelles_id_dans_table_niveau.append(liste_des_libelles_des_niveaux)
        liste_des_libelles_id_dans_table_niveau.append(liste_des_id_profils_dans_table_niveau)
        liste_des_libelles_id_dans_table_niveau.append(liste_des_id_des_libelles_dans_table_niveau)

        #print(json.dumps(listeLibelleIdNiveau, indent=4))
        #listeLibelleIdNiveau=listeLibelleNiveau + listeIdProfilNiveau
        return liste_des_libelles_id_dans_table_niveau

    def listeIdLibelleNiveau():
        listeIdentifiantNiveau = []
        data= db.selectData(NiveauT,NiveauT['colsName'],1,2,2,2,2,2,2,1,"","","0","50")
        for i in range(len(data)):
            listeIdentifiantNiveau.append(data[i][0])

        #print(listeIdentifiantNiveau)
        return listeIdentifiantNiveau

#print(listeProfil())
#----------------------------------------------------------------
