import  sys

#création de la classe qui contient la structure des tables de la base
class Tables :
    #structure de la table utilisateur
    def usersTable(self):
        return {
            "tableName" :"users",
            "colsLibelle" : ["IDENTIFIANT","PRENOM","NOM","SEXE","TELEPHONE","EMAIL","EMAIL DE "
                            "SECOURS","DATE INSCRIPTION"],
            "colsName" :["id","prenom","nom","sexe","telephone","email","emailSecours",
                         "dateInscription"],
            "colsType" :["INTEGER PRIMARY KEY, ", "TEXT NOT NULL, ", "TEXT NOT NULL, ", "TEXT(10) "
                                                                                       "NOT NULL, ",
                         "TEXT NOT NULL, ", "TEXT NOT NULL, ","TEXT NOT NULL, ","TEXT NOT NULL"]
        }

    # la structure de la table d'un user connecté
    def niveauTable(self):
        return {
            "tableName": "t_niveau_univ",
            "colsLibelle": ["idLibelle", "Libellé", "idProfil", "Description",
                    "validNiveau", "Rang", "libelleProfil", "emailOp", "dateSav"],
            "colsName": ["idLibelle", "libelle", "idProfil", "description",
                    "validNiveau", "rang", "libelleProfil", "emailOp", "dateSav"],
            "colsType": ["INTEGER UNSIGNED PRIMARY KEY,", "VARCHAR(255) NOT NULL,", "INT(11) NOT NULL,", "LONGTEXT NOT NULL,",
                    "VARCHAR(255) NOT NULL,", "INT(11) NOT NULL,", "VARCHAR(255) NOT NULL,", "VARCHAR(255) NOT NULL,", "DATETIME NOT NULL"]
        }

    def profilTable(self):
        return {
            "tableName": "t_profil_univ",
            "colsLibelle": ["idProfilUniv", "Libellé", "idEcoleMere", "Description",
                    "Présentation", "Mission", "validProfil", "Rang", "emailRecteur",
                    "dateProfilUniv"
                    ],
            "colsName": ["idProfilUniv", "labelProfil", "idEcoleMere", "description",
                    "presentation", "mission", "validProfil", "rang", "emailRecteur",
                    "dateProfilUniv"
                    ],
            "colsType": ["INTEGER UNSIGNED PRIMARY KEY,", "VARCHAR(255) NOT NULL,", "INT(11) NOT NULL,", "LONGTEXT NOT NULL,",
                    "LONGTEXT NOT NULL,", "LONGTEXT NOT NULL,", "VARCHAR(255) NOT NULL,", "INT(11) NOT NULL,", "VARCHAR(255) NOT NULL,",
                    "DATETIME NOT NULL"
                        ]
        }

    def ecoleTable(self):
        return {
            "tableName": "ecoletable",
            "colsLibelle": ["idEcole", "nomEcole", "idQuartier", "structure",
                    "typeEnseignement", "ficheRenseignement", "presentation", "mission", "competence",
                    "admission", "telephone1", "telephone2", "telephone3", "gmail",
                    "yahoo", "magoe", "facebook", "twiter", "istagramme",
                    "abreviation", "slogan", "latitude", "longitude", "rayon",
                    "linkVideo", "idDsee", "nomQuartier", "nomCommune", "nomVille",
                    "nomPays", "nomContinent", "linkPlayStore", "emailParain", "adresseEcole",
                    "emailOperateur", "dateEnrEcol"
                    ],
            "colsName": ["idEcole", "nomEcole", "idQuartier", "structure",
                    "typeEnseignement", "ficheRenseignement", "presentation", "mission", "competence",
                    "admission", "telephone1", "telephone2", "telephone3", "gmail",
                    "yahoo", "magoe", "facebook", "twiter", "istagramme",
                    "abreviation", "slogan", "latitude", "longitude", "rayon",
                    "linkVideo", "idDsee", "nomQuartier", "nomCommune", "nomVille",
                    "nomPays", "nomContinent", "linkPlayStore", "emailParain", "adresseEcole",
                    "emailOperateur", "dateEnrEcol"
                    ],
            "colsType": ["INTEGER UNSIGNED PRIMARY KEY,", "VARCHAR(255) NOT NULL,", "INT(11) NOT NULL,", "VARCHAR(255) NOT NULL,",
                    "VARCHAR(255) NOT NULL,", "LONGTEXT NOT NULL,", "LONGTEXT NOT NULL,", "LONGTEXT NOT NULL,", "LONGTEXT NOT NULL,",
                    "LONGTEXT NOT NULL,", "VARCHAR(255) NOT NULL,", "VARCHAR(255) NOT NULL,", "VARCHAR(255) NOT NULL,", "VARCHAR(255) NOT NULL,",
                    "VARCHAR(255) NOT NULL,", "VARCHAR(255) NOT NULL,", "VARCHAR(255) NOT NULL,", "VARCHAR(255) NOT NULL,", "VARCHAR(255) NOT NULL,",
                    "VARCHAR(255) NOT NULL,", "TEXT NOT NULL,", "DOUBLE NOT NULL,", "DOUBLE NOT NULL,", "DOUBLE NOT NULL,",
                    "VARCHAR(255) NOT NULL,", "TEXT NOT NULL,", "INT(11) NOT NULL,", "VARCHAR(255) NOT NULL,", "VARCHAR(255) NOT NULL,",
                    "VARCHAR(255) NOT NULL,", "VARCHAR(255) NOT NULL,", "TEXT NOT NULL,", "VARCHAR(255) NOT NULL,", "TEXT NOT NULL,",
                    "VARCHAR(255) NOT NULL,", "DATETIME NOT NULL"
                        ]
        }

    #la structure de la table matière
    def matiereTable(self):
        return {
            "tableName": "t_matiere_univ",
            "colsLibelle":[
                    "id", "Libellé", "idNiveau", "Nombre d'heure par semaine",
                    "Coefficient a/b: a=...", "Coefficient a/b: b=...", "Nombre de notes",
                    "Position", "Matiere valide ?","Type de cours","emailOperateur","dateSav"
                    ],
            "colsName":[
                "id", "label", "idNiveau", "nbrSeance","coefficient1","coefficient2",
                 "nbrNote", "niveau", "validMatiere","idProfil","emailOperateur","dateSav"
                ],

            "colsType": [
                    "INT(11) UNSIGNED PRIMARY KEY,","VARCHAR(255) NOT NULL,", "INT(11) NOT NULL,",
                    "INT(11) NOT NULL,","INT(11) NOT NULL,","INT(11) NOT NULL,","INT(11) NOT NULL,",
                    "VARCHAR(255) NOT NULL,","VARCHAR(255) NOT NULL,","INT(11) NOT NULL,",
                    "VARCHAR(255) NOT NULL,","DATETIME NOT NULL"
                ]
        }

    #la structure de la page professeur
    def profTable(self):
        return {
            "tableName": "t_professeur_univ",
            "colsLibelle": [
                    "idProf", "Email sur Magoé", "idMatiere", "idProfListe",
                    "Année scolaire", "Groupe pédagogique", "idQuartier", "cout", "autoriser",
                    "Prénom", "Nom", "Téléphone", "Sexe", "emailOperateur","dateSavProf"
                    ],
            "colsName":[
                "idProf", "emailProf", "idMatiere", "idProfListe",
                "anneeUniv", "groupePedag", "idQuartier", "cout", "autoriser",
                "prenom", "nom", "telephone", "sexe", "emailOperateur",
                "dateSavProf"
                ],
            "colsType": [
                    "INT(11) UNSIGNED PRIMARY KEY,",
                    "VARCHAR(255) NOT NULL,", "INT(11) NOT NULL,", "INT(11) NOT NULL,",
                    "YEAR(4) NOT NULL,","VARCHAR(255) NOT NULL,", "INT(11) NOT NULL,",
                    "INT(11) NOT NULL,", "VARCHAR(255) NOT NULL,","VARCHAR(255) NOT NULL,",
                    "VARCHAR(255) NOT NULL,", "VARCHAR(255) NOT NULL,", "VARCHAR(255) NOT NULL,",
                    "VARCHAR(255) NOT NULL,","DATETIME NOT NULL"
                ]
        }

    # la structure de la table des enseignant assistant
    def profAssistantTable(self):
        return {
            "tableName": "t_prof_assistant",
            "colsLibelle": [
                    "idProf", "Email sur Magoé", "idMatiere", "idProfListe",
                    "Année scolaire", "Groupe pédagogique", "idQuartier", "cout", "autoriser",
                    "Prénom", "Nom", "Téléphone", "Sexe", "emailOperateur","dateSavProf"
                    ],

            "colsName":[
                "idProf", "emailProf", "idMatiere", "idProfListe",
                "anneeUniv", "groupePedag", "idQuartier", "cout", "autoriser",
                "prenom", "nom", "telephone", "sexe", "emailOperateur",
                "dateSavProf"
                ],
            "colsType": [
                    "INT(11) UNSIGNED PRIMARY KEY,",
                    "VARCHAR(255) NOT NULL,", "INT(11) NOT NULL,", "INT(11) NOT NULL,",
                    "YEAR(4) NOT NULL,","VARCHAR(255) NOT NULL,", "INT(11) NOT NULL,",
                    "INT(11) NOT NULL,", "VARCHAR(255) NOT NULL,","VARCHAR(255) NOT NULL,",
                    "VARCHAR(255) NOT NULL,", "VARCHAR(255) NOT NULL,", "VARCHAR(255) NOT NULL,",
                    "VARCHAR(255) NOT NULL,","DATETIME NOT NULL"
                ]
        }