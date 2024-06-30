"""
Application de CRUD en PYQT5 et Python
Autheur : GUILAVOGUI FOROMO PIERRE
"""
import sqlite3

class Communication():
    #---------------- le constructeur de la classe
    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        cursor = self.connection.cursor()
    # ------------------- la méthode d'insertion ------------------
    def insert_into_table(self,code,designation,prixunitaire,quantite,categorie):
        sql = '''
            INSERT INTO produits (code,designation,prixunitaire,quantite,categorie)
            VALUES ('{}', '{}', '{}', '{}', '{}')
        '''.format(code, designation, prixunitaire,quantite, categorie)
        cursor.execute(sql)
        self.connection.commit()
        cursor.close()

    def select_produits(self):
        sql = "SELECT * FROM produits"
        cursor.execute(sql)
        prod = cursor.fetchall()
        self.connection.commit()
        cursor.close()
        return prod

    def select_produit(self,code_produit):
        sql = ''' SELECT * FROM produits WHERE code = {} '''.format(code_produit)
        cursor.execute(sql)
        prod = cursor.fetchone()
        self.connection.commit()
        cursor.close()
        return prod

    def update_produit(self,update_values):
        sql = " UPDATE produits SET designation=:designation,prixunitaire=:prix," \
              "quantite=:quantite,categorie=:categorie WHERE code =:codeupdate"
        cursor.execute(sql,update_values)
        nombre = cursor.rowcount()
        self.connection.commit()
        cursor.close()
        return nombre

    def delete_produit(self,codeproduit):
        sql = "DELETE FROM produits WHERE code ={}".format(codeproduit)
        cursor.execute(sql)
        self.connection.commit()
        cursor.close()
        return "Suppression valide"






