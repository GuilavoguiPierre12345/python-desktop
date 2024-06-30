# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogFormoUUbLY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import QSS_Resources_rc

class Ui_modeleDialogue(object):
    def setupUi(self, modeleDialogue):
        if not modeleDialogue.objectName():
            modeleDialogue.setObjectName(u"modeleDialogue")
        modeleDialogue.resize(400, 193)
        modeleDialogue.setStyleSheet(u"#popupNotificationBox {\n"
"	background-color : #050304 ;\n"
"	border-radius : 15px ;\n"
"}\n"
"\n"
"#popUpNotificationSous {\n"
"	background-color : #050304 ;\n"
"	border-radius : 10px ;\n"
"}\n"
"\n"
"#closePopUpBtn {\n"
"	background-color:#050304 ;\n"
"}\n"
"\n"
"#notificationTitleText,\n"
"#notificationText{\n"
"	color :#FFFFFF ;\n"
"	background-color:#050304 ;\n"
"	border:\"non\";\n"
"}\n"
"\n"
"\n"
"#notificationTextBox {\n"
"	border: 2px solid white;\n"
"	border-radius:10px;\n"
"}")
        self.verticalLayout = QVBoxLayout(modeleDialogue)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.popupNotificationBox = QWidget(modeleDialogue)
        self.popupNotificationBox.setObjectName(u"popupNotificationBox")
        self.popupNotificationBox.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.popupNotificationBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.popUpNotificationSous = QWidget(self.popupNotificationBox)
        self.popUpNotificationSous.setObjectName(u"popUpNotificationSous")
        self.verticalLayout_30 = QVBoxLayout(self.popUpNotificationSous)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.notificationTitleBox = QWidget(self.popUpNotificationSous)
        self.notificationTitleBox.setObjectName(u"notificationTitleBox")
        self.notificationTitleBox.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout = QHBoxLayout(self.notificationTitleBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.notificationTitleText = QLabel(self.notificationTitleBox)
        self.notificationTitleText.setObjectName(u"notificationTitleText")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notificationTitleText.sizePolicy().hasHeightForWidth())
        self.notificationTitleText.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(12)
        self.notificationTitleText.setFont(font)
        self.notificationTitleText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.notificationTitleText, 0, Qt.AlignLeft)

        self.closePopUpBtn = QPushButton(self.notificationTitleBox)
        self.closePopUpBtn.setObjectName(u"closePopUpBtn")
        icon = QIcon()
        icon.addFile(u":/newPrefix/Icons/x-octagon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closePopUpBtn.setIcon(icon)
        self.closePopUpBtn.setIconSize(QSize(28, 28))

        self.horizontalLayout.addWidget(self.closePopUpBtn, 0, Qt.AlignRight)


        self.verticalLayout_30.addWidget(self.notificationTitleBox, 0, Qt.AlignTop)

        self.notificationTextBox = QWidget(self.popUpNotificationSous)
        self.notificationTextBox.setObjectName(u"notificationTextBox")
        sizePolicy.setHeightForWidth(self.notificationTextBox.sizePolicy().hasHeightForWidth())
        self.notificationTextBox.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.notificationTextBox)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.notificationText = QPlainTextEdit(self.notificationTextBox)
        self.notificationText.setObjectName(u"notificationText")
        self.notificationText.setEnabled(False)

        self.verticalLayout_3.addWidget(self.notificationText)


        self.verticalLayout_30.addWidget(self.notificationTextBox)


        self.verticalLayout_2.addWidget(self.popUpNotificationSous)


        self.verticalLayout.addWidget(self.popupNotificationBox)


        self.retranslateUi(modeleDialogue)

        QMetaObject.connectSlotsByName(modeleDialogue)
    # setupUi

    def retranslateUi(self, modeleDialogue):
        modeleDialogue.setWindowTitle(QCoreApplication.translate("modeleDialogue", u"Dialog", None))
        self.notificationTitleText.setText(QCoreApplication.translate("modeleDialogue", u"Alerte", None))
        self.closePopUpBtn.setText("")
        self.notificationText.setPlainText(QCoreApplication.translate("modeleDialogue", u"super guilao", None))
    # retranslateUi

