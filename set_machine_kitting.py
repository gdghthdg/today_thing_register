# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\20190822\Set_Machine_kitting.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(185, 249)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 70, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(110, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(70, 200, 51, 28))
        self.pushButton.setObjectName("pushButton")
        self.lab_table_rows = QtWidgets.QLabel(Form)
        self.lab_table_rows.setGeometry(QtCore.QRect(10, 0, 41, 16))
        self.lab_table_rows.setStyleSheet("*{\n"
"color:white;\n"
"}")
        self.lab_table_rows.setText("")
        self.lab_table_rows.setObjectName("lab_table_rows")
        self.checkBox1300 = QtWidgets.QCheckBox(Form)
        self.checkBox1300.setGeometry(QtCore.QRect(130, 70, 21, 20))
        self.checkBox1300.setText("")
        self.checkBox1300.setObjectName("checkBox1300")
        self.checkBox1450 = QtWidgets.QCheckBox(Form)
        self.checkBox1450.setGeometry(QtCore.QRect(130, 120, 21, 19))
        self.checkBox1450.setText("")
        self.checkBox1450.setObjectName("checkBox1450")
        self.checkBox1600 = QtWidgets.QCheckBox(Form)
        self.checkBox1600.setGeometry(QtCore.QRect(130, 170, 21, 19))
        self.checkBox1600.setText("")
        self.checkBox1600.setObjectName("checkBox1600")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.confire)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "1300"))
        self.label_2.setText(_translate("Form", "1450"))
        self.label_3.setText(_translate("Form", "1600"))
        self.label_4.setText(_translate("Form", "站点"))
        self.label_5.setText(_translate("Form", "off/no"))
        self.pushButton.setText(_translate("Form", "OK"))

