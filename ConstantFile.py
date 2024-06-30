import sys

class Constantes:
    DOMAIN_NAME = "magoe.gn"

    MAIN_URL = "www.magoe.fr"
    AUTH_URL = "https://magoe.fr/qcmIdentif_2_android_py.php"
    REGISTER_URL = "https://magoe.fr/android_savMagoeMember_py.php"
    GETGLOBALINFO_URL = "https://magoe.fr/addDataWidthReqStr_json_py.php"
    # ----------------------------------END -------------------------------------------
    SEND_URL = "https://magoe.fr/addData_json_2_py.php"

    DATA =  {
            "tbl_rowLabel":("idLibelle", "libelle", "idProfil", "description","validNiveau", "emailOp", "dateSav" ),
            "tbl_rowType":("INT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY,", "VARCHAR(255) NOT NULL,", "INT(11) NOT NULL,", "LONGTEXT NOT NULL,",
                            "VARCHAR(255) NOT NULL,", "VARCHAR(255) NOT NULL,", "DATETIME NOT "
                                                                                "NULL"),
            "tblName":"t_niveau_univ",
            "bddType":"1",
            "idOffLineIndex":0,
            "idOnLineIndex":0,
            "labelIndex":0,
            "idParentIndex":0,
            "singleEntryIndex":2,
            "dualEntryIndex":0,
            "reqGroup":"",
            "reqOrder":"",
            "reqLimit":"",
            "typeReqGet":"BySingleEntry",
            "tbl_rowValue_search": ("idLibelle", "libelle", "7", "description", "validNiveau", "emailOp", "dateSav")
    }

    row_Labels_Niveau = ["idLibelle", "libelle", "idProfil", "description",
                    "validNiveau", "rang", "libelleProfil", "emailOp", "dateSav"]
    row_Types_Niveau = ["INT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY,", "VARCHAR(255) NOT NULL,", "INT(11) NOT NULL,", "LONGTEXT NOT NULL,",
                    "VARCHAR(255) NOT NULL,", "INT(11) NOT NULL,", "VARCHAR(255) NOT NULL,", "VARCHAR(255) NOT NULL,", "DATETIME NOT NULL"]