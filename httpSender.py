import sys
import httpx
import asyncio
import json


#la classe qui permettra d'envoyer des requêtes http
class HttpHandler :

    #La méthode pour la récupération des données
    async def getDataFromApi(self,url):
        #Spécifier que le client est asynchrone
        try :
            async with httpx.AsyncClient() as client:
                reponse = await client.get(url)
                return reponse.json()
        except Exception as e:
            print("Error aucours de l'affichage des données : " + str(e))


    #La méthode pour l'envoie des données vers l'API
    async def sendDataToApi(self, url,data):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(url, data=data)
                return response.json()
        except Exception as e:
            print("Erreur, un problème lors de l'accès au serveur : " + str(e))

    #La méthode pour la mise à jours des données sur l'api
    async def updateDataToApi(self, url, data):
        try :
            async with httpx.AsyncClient() as client:
                response = await client.put(url, data=data)
                return response.json()
        except Exception:
            print("Error aucours de la mise à jour des données : " + str(e))

    #La méthode pour la suppresion des données dans l'api
    async def deleteDataFromApi(self, url):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.delete(url)
                return response.json()
        except Exception as e:
            print("Error aucours de la suppression : " + str(e))
#Les Executions des méthodes

#Exécution de getDataFromAPI
async def dataGetter():
    http= HttpHandler()
    response = await http.getDataFromApi("https://magoe.fr/addData_json_2_py.php")
    return response
#getter_response = asyncio.run(dataGetter())

#print(getter_response)

#Exécution de sendDataToApi
async def dataSetter(url,data):
    http= HttpHandler()

    # data= {
    #         "tbl_rowLabel":("idLibelle", "libelle", "idProfil", "description","validNiveau", "emailOp", "dateSav" ),
    #         "tbl_rowType":("INT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY,", "VARCHAR(255) NOT NULL,", "INT(11) NOT NULL,", "LONGTEXT NOT NULL,",
    #                         "VARCHAR(255) NOT NULL,", "VARCHAR(255) NOT NULL,", "DATETIME NOT "
    #                                                                             "NULL"),
    #         "tblName":"t_niveau_univ",
    #         "bddType":"1",
    #         "idOffLineIndex":0,
    #         "idOnLineIndex":0,
    #         "labelIndex":0,
    #         "idParentIndex":0,
    #         "singleEntryIndex":2,
    #         "dualEntryIndex":0,
    #         "reqGroup":"",
    #         "reqOrder":"",
    #         "reqLimit":"",
    #         "typeReqGet":"BySingleEntry",
    #         "tbl_rowValue_search": ("idLibelle", "libelle", "7", "description", "validNiveau", "emailOp", "dateSav")
    #     }

    json_data = json.dumps(data,indent=4)
    response = await http.sendDataToApi(url,json_data)

    return response
#setter_response = asyncio.run(dataSetter("https://magoe.fr/android_savMagoeMember_py.php",
    # {"E_Mail":"koligoe@magoe.gn",
#
#                                                                               "Mot_de_Passe":"kpokolo"}))
#print(setter_response)

#Exécution de updateDataToApi
async def dataPutter():
    http= HttpHandler()
    data={"id":5,"nom":"SAKOUVOGUI","prenom":"Madeleine","age":18,"niveau_id":3}
    json_data = json.dumps(data,indent=4)
    response = await http.updateDataToApi("http://localhost/API_REST/controllers/update.php",
                                        json_data)
    return response
#putter_response = asyncio.run(dataPutter())

#Exécution de la deleteDataFromApi
async def dataDeleter():
    http= HttpHandler()
    data={"id":5}
    json_data = json.dumps(data,indent=4)
    response = await http.deleteDataFromApi("http://localhost/API_REST/controllers/delete.php")

    return response
#deleter_response = asyncio.run(dataDeleter())


