# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\20190822\database_set.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(669, 308)
        self.lin_server_admin = QtWidgets.QLineEdit(Form)
        self.lin_server_admin.setGeometry(QtCore.QRect(122, 140, 181, 31))
        self.lin_server_admin.setObjectName("lin_server_admin")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(80, 150, 31, 16))
        self.label_10.setObjectName("label_10")
        self.lin_server_ip = QtWidgets.QLineEdit(Form)
        self.lin_server_ip.setGeometry(QtCore.QRect(120, 40, 181, 31))
        self.lin_server_ip.setObjectName("lin_server_ip")
        self.lin_server_database = QtWidgets.QLineEdit(Form)
        self.lin_server_database.setGeometry(QtCore.QRect(440, 40, 171, 31))
        self.lin_server_database.setObjectName("lin_server_database")
        self.lab_server_ip = QtWidgets.QLabel(Form)
        self.lab_server_ip.setGeometry(QtCore.QRect(90, 45, 21, 16))
        self.lab_server_ip.setObjectName("lab_server_ip")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(370, 45, 72, 15))
        self.label_16.setObjectName("label_16")
        self.lin_server_password = QtWidgets.QLineEdit(Form)
        self.lin_server_password.setGeometry(QtCore.QRect(442, 140, 171, 31))
        self.lin_server_password.setObjectName("lin_server_password")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(390, 150, 31, 16))
        self.label_15.setObjectName("label_15")
        self.but_database_lock = QtWidgets.QPushButton(Form)
        self.but_database_lock.setGeometry(QtCore.QRect(300, 210, 93, 28))
        self.but_database_lock.setObjectName("but_database_lock")

        self.retranslateUi(Form)
        self.but_database_lock.clicked.connect(Form.change_database)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lin_server_admin.setPlaceholderText(_translate("Form", "sa"))
        self.label_10.setText(_translate("Form", "账号"))
        self.lin_server_ip.setPlaceholderText(_translate("Form", "172.17.130.106:5900"))
        self.lin_server_database.setPlaceholderText(_translate("Form", "xueshengxinxi"))
        self.lab_server_ip.setText(_translate("Form", "IP"))
        self.label_16.setText(_translate("Form", "database"))
        self.lin_server_password.setPlaceholderText(_translate("Form", "123456"))
        self.label_15.setText(_translate("Form", "密码"))
        self.but_database_lock.setText(_translate("Form", "测试"))

