# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\20190822\write_password.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(90, 110, 221, 51))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.but_confire = QtWidgets.QPushButton(Form)
        self.but_confire.setGeometry(QtCore.QRect(160, 180, 93, 51))
        self.but_confire.setObjectName("but_confire")

        self.retranslateUi(Form)
        self.but_confire.clicked.connect(Form.confire)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "         請輸入密碼"))
        self.but_confire.setText(_translate("Form", "確認"))

