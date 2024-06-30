import sys
import sqlite3

#la classe Register pour l'inscription d'un user
class Handler:
    #le constructeur de la classe
    def __init__(self,dbname):
        self.conn = sqlite3.connect(dbname)
        self.cur = self.conn.cursor()

    #La méthode pour vérifier l'existence d'une table
    def verifyIfTableExists(self,tableStruct):
        sql = "SELECT name FROM sqlite_master WHERE type = 'table' AND name =:name"
        response = self.cur.execute(sql,{"name":tableStruct['tableName'],})
        self.conn.commit()
        if response.fetchone() is None:
            return False
        else :
            return True

    #la méthode création des tables
    def createTable(self,tableStruct):
        try:
            line = ""
            for i in range(len(tableStruct["colsName"])):
                line += tableStruct["colsName"][i] + " " + tableStruct["colsType"][i]
            sql = "CREATE TABLE IF NOT EXISTS " + tableStruct["tableName"] + "(" + line + ")"
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print("Error creating table :" + str(e))

    #la méthode d'insertion d'un utilisateur
    def insertData(self,tableStruct,insertValues): #insertValues est une liste de donnée qui doit
        # provenir de l'interface utilisateur et tableStruct est la structure de la table à créer
        self.createTable(tableStruct)
        try:
            line = ",".join(tableStruct["colsName"])
            l =line.split(",")
            marker = ""
            for i in range(len(l)):
                marker +="?" if i == len(l)-1 else "?,"

            sqlInsert = "INSERT INTO " + tableStruct["tableName"] + "("+line+") VALUES("+ marker +")"
            self.cur.execute(sqlInsert,insertValues)
            self.conn.commit()
            print("ajout effectuer avec success")
        except Exception as e:
            print("Error inserting data into database :"+str(e))

    #la méthode de modification d'un utilisateur
    def updateData(self,tableStruct,updateValues):
        colsName = tableStruct["colsName"]
        line = ""
        for i in range(1, len(colsName)):
            line += colsName[i] + "=?" if (i == len(colsName) - 1) else colsName[i] + "=?,"

        sqlUpdate = "UPDATE "+tableStruct["tableName"] +" SET "+ line +" WHERE "+tableStruct[
            "colsName"][0]+"=?"
        self.cur.execute(sqlUpdate,updateValues)
        self.conn.commit()
        print("Mise à jour effectuer avec success")

    #la méthode d'Affichage les utilisateurs
    def selectData(self,tableStruct,selectValues,ind1,ind2,ind3,ind4,ind5,ind6,ind7,typeR,
                   groupBy,orderBy,debutR,pasRe):
        sql = "SELECT * FROM " + tableStruct["tableName"] + " WHERE "
        if typeR == 1 :
            sql += tableStruct["colsName"][ind1] + " = " + "\""+ selectValues[ind1] +"\""
        elif typeR == 2 :
            sql += tableStruct["colsName"][ind1] + " = " + "\""+ selectValues[ind1]+"\"" + " AND " + \
                   tableStruct["colsName"][ind2] + " = " + "\""+ selectValues[ind2]+"\""
        elif typeR == 3:
            sql += tableStruct["colsName"][ind1] + " = " + "\""+ selectValues[ind1]+"\"" + " AND " + \
                   tableStruct["colsName"][ind2] + " = " + "\""+ selectValues[ind2]+"\"" + " AND " + \
                   tableStruct["colsName"][ind3] + " = " + "\""+ selectValues[ind3]+"\""
        elif typeR == 4:
            sql += tableStruct["colsName"][ind1] + " = " + "\""+ selectValues[ind1]+"\"" + " AND " + \
                   tableStruct["colsName"][ind2] + " = " + "\""+ selectValues[ind2]+"\"" + " AND " + \
                   tableStruct["colsName"][ind3] + " = " + "\""+ selectValues[ind3]+"\"" + " AND " + \
                   tableStruct["colsName"][ind4] + " = " + "\""+ selectValues[ind4]+"\""
        elif typeR == 5:
            sql += tableStruct["colsName"][ind1] + " = " + "\""+ selectValues[ind1]+"\"" + " AND " + \
                   tableStruct["colsName"][ind2] + " = " + "\""+ selectValues[ind2]+"\"" + " AND " + \
                   tableStruct["colsName"][ind3] + " = " + "\""+ selectValues[ind3]+"\"" + " AND " + \
                   tableStruct["colsName"][ind4] + " = " + "\""+ selectValues[ind4]+"\"" + " AND " + \
                   tableStruct["colsName"][ind5] + " = " + "\""+ selectValues[ind5]+"\""
        elif typeR == 6:
            sql += tableStruct["colsName"][ind1] + " = " + "\""+ selectValues[ind1]+"\""+"\"" + " AND " + \
                   tableStruct["colsName"][ind2] + " = " + "\""+ selectValues[ind2]+"\""+"\"" + " AND " + \
                   tableStruct["colsName"][ind3] + " = " + "\""+ selectValues[ind3]+"\""+"\"" + " AND " + \
                   tableStruct["colsName"][ind4] + " = " + "\""+ selectValues[ind4]+"\""+"\"" + " AND " + \
                   tableStruct["colsName"][ind5] + " = " + "\""+ selectValues[ind5]+"\""+"\"" + " AND " + \
                   tableStruct["colsName"][ind6] + " = " + "\""+ selectValues[ind6]+"\""+"\""
        else:
            sql += tableStruct["colsName"][ind1] + " = " + "\""+ selectValues[ind1]+"\"" + " AND " + \
                   tableStruct["colsName"][ind2] + " = " + "\""+ selectValues[ind2]+"\"" + " AND " + \
                   tableStruct["colsName"][ind3] + " = " + "\""+ selectValues[ind3]+"\"" + " AND " + \
                   tableStruct["colsName"][ind4] + " = " + "\""+ selectValues[ind4]+"\"" + " AND " + \
                   tableStruct["colsName"][ind5] + " = " + "\""+ selectValues[ind5]+"\"" + " AND " + \
                   tableStruct["colsName"][ind6] + " = " + "\""+ selectValues[ind6]+"\"" + " AND " + \
                   tableStruct["colsName"][ind7] + " = " + "\""+ selectValues[ind7]+"\""
        sql += groupBy + orderBy + " LIMIT " + debutR + "," + pasRe

        response = self.cur.execute(sql)
        #print(response)
        return response.fetchall() #affichage des donnée après exécution de la requête
        self.conn.commit() #validation de la transaction implicite

    # la méthode pour la suppression d'un utilisateur
    def deleteData(self, tableStruct, selectValues, ind1, ind2, ind3, ind4, ind5, ind6, ind7, typeR):
        sql = "DELETE FROM " + tableStruct["tableName"] + " WHERE "
        if typeR == 1:
            sql += tableStruct["colsName"][ind1] + " = " + "\"" + selectValues[ind1] + "\""
        elif typeR == 2:
            sql += tableStruct["colsName"][ind1] + " = " + "\"" + selectValues[
                ind1] + "\"" + " AND " + \
                   tableStruct["colsName"][ind2] + " = " + "\"" + selectValues[ind2] + "\""
        elif typeR == 3:
            sql += tableStruct["colsName"][ind1] + " = " + "\"" + selectValues[
                ind1] + "\"" + " AND " + \
                   tableStruct["colsName"][ind2] + " = " + "\"" + selectValues[
                       ind2] + "\"" + " AND " + \
                   tableStruct["colsName"][ind3] + " = " + "\"" + selectValues[ind3] + "\""
        elif typeR == 4:
            sql += tableStruct["colsName"][ind1] + " = " + "\"" + selectValues[
                ind1] + "\"" + " AND " + \
                   tableStruct["colsName"][ind2] + " = " + "\"" + selectValues[
                       ind2] + "\"" + " AND " + \
                   tableStruct["colsName"][ind3] + " = " + "\"" + selectValues[
                       ind3] + "\"" + " AND " + \
                   tableStruct["colsName"][ind4] + " = " + "\"" + selectValues[ind4] + "\""
        elif typeR == 5:
            sql += tableStruct["colsName"][ind1] + " = " + "\"" + selectValues[
                ind1] + "\"" + " AND " + \
                   tableStruct["colsName"][ind2] + " = " + "\"" + selectValues[
                       ind2] + "\"" + " AND " + \
                   tableStruct["colsName"][ind3] + " = " + "\"" + selectValues[
                       ind3] + "\"" + " AND " + \
                   tableStruct["colsName"][ind4] + " = " + "\"" + selectValues[
                       ind4] + "\"" + " AND " + \
                   tableStruct["colsName"][ind5] + " = " + "\"" + selectValues[ind5] + "\""
        elif typeR == 6:
            sql += tableStruct["colsName"][ind1] + " = " + "\"" + selectValues[
                ind1] + "\"" + "\"" + " AND " + \
                   tableStruct["colsName"][ind2] + " = " + "\"" + selectValues[
                       ind2] + "\"" + "\"" + " AND " + \
                   tableStruct["colsName"][ind3] + " = " + "\"" + selectValues[
                       ind3] + "\"" + "\"" + " AND " + \
                   tableStruct["colsName"][ind4] + " = " + "\"" + selectValues[
                       ind4] + "\"" + "\"" + " AND " + \
                   tableStruct["colsName"][ind5] + " = " + "\"" + selectValues[
                       ind5] + "\"" + "\"" + " AND " + \
                   tableStruct["colsName"][ind6] + " = " + "\"" + selectValues[ind6] + "\"" + "\""
        else:
            sql += tableStruct["colsName"][ind1] + " = " + "\"" + selectValues[
                ind1] + "\"" + " AND " + \
                   tableStruct["colsName"][ind2] + " = " + "\"" + selectValues[
                       ind2] + "\"" + " AND " + \
                   tableStruct["colsName"][ind3] + " = " + "\"" + selectValues[
                       ind3] + "\"" + " AND " + \
                   tableStruct["colsName"][ind4] + " = " + "\"" + selectValues[
                       ind4] + "\"" + " AND " + \
                   tableStruct["colsName"][ind5] + " = " + "\"" + selectValues[
                       ind5] + "\"" + " AND " + \
                   tableStruct["colsName"][ind6] + " = " + "\"" + selectValues[
                       ind6] + "\"" + " AND " + \
                   tableStruct["colsName"][ind7] + " = " + "\"" + selectValues[ind7] + "\""

        response = self.cur.execute(sql)
        self.conn.commit()  # validation de la transaction implicite
        print("Suppression effectuer avec success")


    #le destructeur de la connexion à la base
    def __del__(self):
        self.cur.close()
        self.conn.close()
