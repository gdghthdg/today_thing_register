# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\20190822\put_in.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(314, 321)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 61, 16))
        self.label_2.setObjectName("label_2")
        self.lin_new = QtWidgets.QLineEdit(self.centralwidget)
        self.lin_new.setGeometry(QtCore.QRect(140, 130, 113, 21))
        self.lin_new.setClearButtonEnabled(True)
        self.lin_new.setObjectName("lin_new")
        self.lin_maintain = QtWidgets.QLineEdit(self.centralwidget)
        self.lin_maintain.setGeometry(QtCore.QRect(140, 180, 113, 21))
        self.lin_maintain.setClearButtonEnabled(True)
        self.lin_maintain.setObjectName("lin_maintain")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 180, 72, 16))
        self.label_4.setObjectName("label_4")
        self.lin_ok = QtWidgets.QLineEdit(self.centralwidget)
        self.lin_ok.setGeometry(QtCore.QRect(140, 30, 113, 21))
        self.lin_ok.setClearButtonEnabled(True)
        self.lin_ok.setObjectName("lin_ok")
        self.lin_ng = QtWidgets.QLineEdit(self.centralwidget)
        self.lin_ng.setGeometry(QtCore.QRect(140, 80, 113, 21))
        self.lin_ng.setClearButtonEnabled(True)
        self.lin_ng.setObjectName("lin_ng")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 130, 72, 15))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 230, 41, 41))
        self.pushButton.setStyleSheet("\n"
"QPushButton{\n"
"    font-size: 14px;/*字体大小*/\n"
"    color:white;/*颜色*/\n"
"    background: #00000000;/*背景颜色*/\n"
"    border-radius:40px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"      /*padding-left:6px;左边距*/\n"
"    padding-top:9px;/*上边距*/\n"
"\n"
"}\n"
"")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/confirm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(135, 270, 41, 20))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 314, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.confire)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lin_ok, self.lin_ng)
        MainWindow.setTabOrder(self.lin_ng, self.lin_new)
        MainWindow.setTabOrder(self.lin_new, self.lin_maintain)
        MainWindow.setTabOrder(self.lin_maintain, self.pushButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ok退料"))
        self.label_2.setText(_translate("MainWindow", "ng退料"))
        self.label_4.setText(_translate("MainWindow", "维修入库"))
        self.label_3.setText(_translate("MainWindow", "新品入库"))
        self.pushButton.setShortcut(_translate("MainWindow", "Enter"))
        self.label_5.setText(_translate("MainWindow", "確認"))

import wire_images_rc
