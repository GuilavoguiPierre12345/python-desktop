import sys
import httpx
import asyncio
import json

# la classe qui permettra le chargement des fichiers sur le serveur
class FileUploader :
    # La méthode pour l'envoie des données vers l'API
    async def sendFileToApi(self, url, filePath):
        async with httpx.AsyncClient() as client:
            with open(filePath, 'rb') as f: #l'ouverture du fichier en lecture binaire
                response = await client.post(url, files={'file': f})
                f.close()
                return response.json()

#exécution de la méthode sendFileToApi
async def dataSetter():
    fileObj =FileUploader()
    filePath ="avatar.png" # le chemin local du fichier à envoyer
    url ="http://localhost/API_REST/controllers/fetchPython.php" #url de reception du fichier
    response = await fileObj.sendFileToApi(url,filePath)
    return response
setter_response = asyncio.run(dataSetter())
print(setter_response)