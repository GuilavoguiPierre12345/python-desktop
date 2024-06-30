import sys
import os
import asyncio
import socket
import json
#------------------------ les modules tierces ------------------------------


# ------------------------- customs module-----------------------------------
from ConstantFile import Constantes as constante
from httpSender import dataSetter,dataGetter
from tablesFile import Tables as tables

class ListeProfMatiere:

    def getMatieres(self,idNiveau,anneeScolaire = 2022):

        """ affectation de la structure des tables aux variables locales pour
        pouvoir les manipuler dans les requêttes de récupération sur le serveru """
        tableMatiereStruct = tables.matiereTable(self)
        tableProfStruct = tables.profTable(self)

        """ cette section du code permet de compléter la requêtte de façon
         dynamique gèrant l'ajout des virgules dans la requêtte"""
        line = ""
        for i in range(len(tableMatiereStruct["colsName"])):
            addVirgule = " " if i == len(tableMatiereStruct["colsName"]) - 1 else ", "
            line += tableMatiereStruct["tableName"] + "." + tableMatiereStruct["colsName"][i] + " AS " + \
                    tableMatiereStruct["colsName"][i] + "_" + tableMatiereStruct["tableName"] + addVirgule
        line += ","

        for i in range(len(tableProfStruct["colsName"])):
            addVirgule = " " if i == len(tableProfStruct["colsName"]) - 1 else ", "
            line += tableProfStruct["tableName"] + "." + tableProfStruct["colsName"][
                i] + " AS " + tableProfStruct["colsName"][i] + "_" + tableProfStruct[
                        "tableName"] + addVirgule

        liste = self.recuperationInformations(
        tableMatiereStruct["tableName"],
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "",
        "",
        "LIMIT 0,100",
        "SELECT " + line +
        " FROM " + tableMatiereStruct["tableName"] +
        " LEFT JOIN " + tableProfStruct["tableName"] +
        " ON " + tableMatiereStruct["tableName"] + ".id=" + tableProfStruct["tableName"] + ".idMatiere "
        "WHERE t_matiere_univ.idNiveau="+ str(idNiveau) +
        " AND t_professeur_univ.anneeUniv="+ str(anneeScolaire)  +" ORDER BY t_matiere_univ.label ASC,"
        " t_professeur_univ.idProf DESC LIMIT 0, 100",
        ["242"],
        tableMatiereStruct["colsName"],
        tableMatiereStruct["colsType"])

        return liste

    def recuperationInformations(self, tblName, idOffLineIndex, idOnLineIndex, labelIndex, idParentIndex,
        singleEntryIndex, dualEntryIndex, reqGroup, reqOrder, reqLimit, reqStringForGet,
        reqArrayForGet, tbl_rowLabel, tbl_rowType):
        # la structure à envoyer au serveur pour la récupération des données cibles
        data = {
        "bddType": "1",
        "tblName": tblName,
        "idOffLineIndex": idOffLineIndex,
        "idOnLineIndex": idOnLineIndex,
        "labelIndex": labelIndex,
        "idParentIndex": idParentIndex,
        "singleEntryIndex": singleEntryIndex,
        "dualEntryIndex": dualEntryIndex,
        "reqGroup": reqGroup,
        "reqOrder": reqOrder,
        "reqLimit": reqLimit,
        "reqStringForGet": reqStringForGet,
        "reqArrayForGet": reqArrayForGet,
        "tbl_rowLabel": tbl_rowLabel,
        "tbl_rowType": tbl_rowType,
        }


        try:
            response = asyncio.run(dataSetter(constante.GETGLOBALINFO_URL, data))
            # si pas de données trouvées par la requêtte
            if type(response) is dict:
                schoolData = response["item"]
                listeInfoBox = []
                for i in range(len(schoolData)):
                    dicoItem = {}
                    dicoItem["matiere"] = schoolData[i]["label_t_matiere_univ"]
                    dicoItem["professeur"] = schoolData[i]["prenom_t_professeur_univ"]+" "+schoolData[i]["nom_t_professeur_univ"]
                    dicoItem["groupePed"] = schoolData[i]["groupePedag_t_professeur_univ"]
                    dicoItem["annee"] = schoolData[i]["anneeUiv_t_professeur_univ"]

                    listeInfoBox.append(dicoItem)

                return listeInfoBox

            if response["error_get"] == True:
                print("Error au niveau de la requêtte")
                return 0

        except Exception as e:
            print("Une erreur de communication avec le serveur , vérifier votre connexion")

if __name__ == "__main__":
    cla = ListeProfMatiere()
    cla.getMatieres(2460,2022)
