# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(481, 423)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 190, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.photo = QtWidgets.QLabel(Dialog)
        self.photo.setGeometry(QtCore.QRect(120, 10, 221, 161))
        self.photo.setText("")
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 230, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_image = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_image.setGeometry(QtCore.QRect(170, 280, 113, 25))
        self.lineEdit_image.setObjectName("lineEdit_image")
        self.lineEdit_voice = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_voice.setGeometry(QtCore.QRect(170, 330, 113, 25))
        self.lineEdit_voice.setObjectName("lineEdit_voice")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 280, 121, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 330, 121, 17))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.pushButton_2.setText(_translate("Dialog", "PushButton"))
        self.label.setText(_translate("Dialog", "% Image correct"))
        self.label_2.setText(_translate("Dialog", "% Voice correct"))
