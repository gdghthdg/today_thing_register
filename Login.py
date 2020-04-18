# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\20190822\LOGIN.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(819, 792)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/77.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("*{\n"
"\n"
"  font-family:century gothic;\n"
"  \n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"  background:#214264;\n"
"  border-radius:60px;\n"
"  \n"
"}\n"
"\n"
"QToolButton{\n"
"  border-radius:60px;\n"
"  background:#214264;\n"
"}\n"
"\n"
"\n"
"\n"
"QFrame{\n"
"  border-radius:40px;\n"
"  background:#00000000;\n"
"}\n"
"\n"
"QLineEdit{\n"
"  background:transparent;\n"
"  color:#black;\n"
"  border:none;\n"
"  font-size:25px;\n"
"  border-bottom:1px solid #717072\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"  color:white;\n"
"  font-size:24px;\n"
"}\n"
"\n"
"QPushButton#exit,mini{\n"
"  background:#00000000;\n"
"  border-radius:3px;\n"
"}\n"
"QPushButton#mini{\n"
"  background:#00000000;\n"
"  border-radius:3px;\n"
"}")
        self.lab_background = QtWidgets.QLabel(Form)
        self.lab_background.setGeometry(QtCore.QRect(170, 140, 501, 581))
        self.lab_background.setStyleSheet("*{background:rgb(85, 170, 255);}")
        self.lab_background.setText("")
        self.lab_background.setObjectName("lab_background")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(360, 80, 121, 121))
        self.toolButton.setStyleSheet("\n"
"QToolButton{\n"
"  color:white;\n"
"  border-radius:60px;\n"
"  font-size:24px;\n"
"  }\n"
"\n"
"QToolButton:hover{\n"
"  font-size:26px;\n"
"}\n"
"\n"
"QToolButton:pressed\n"
"{\n"
"      /*padding-left:6px;左边距*/\n"
"    padding-top:9px;/*上边距*/\n"
"\n"
"}")
        self.toolButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/admin.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(64, 64))
        self.toolButton.setObjectName("toolButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(290, 390, 271, 41))
        self.lineEdit.setStyleSheet("*{color:rgb(85, 170, 255)}")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(340, 590, 171, 41))
        self.pushButton.setStyleSheet("\n"
"QPushButton{\n"
"  color:white;\n"
"  border-radius:20px;\n"
"  font-size:24px;\n"
"  }\n"
"\n"
"QPushButton:hover{\n"
"  font-size:26px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  color:#333;\n"
"  border-radius:15px;\n"
"  background:#49ebff;\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(250, 549, 91, 20))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("QRadioButton{\n"
"\n"
"  font-size:15px;\n"
"}")
        self.radioButton.setIconSize(QtCore.QSize(60, 15))
        self.radioButton.setObjectName("radioButton")
        self.forget_button = QtWidgets.QPushButton(Form)
        self.forget_button.setGeometry(QtCore.QRect(530, 547, 61, 21))
        self.forget_button.setStyleSheet("QPushButton{\n"
" font-size:10px;\n"
"background:#00000000;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"  color:black;\n"
"  border-radius:20px;\n"
"  font-size:14px;\n"
"  }\n"
"\n"
"QPushButton:hover{\n"
"  color:red;\n"
"  border-radius:15px;\n"
"  background:#00000000;\n"
"}")
        self.forget_button.setObjectName("forget_button")
        self.exit = QtWidgets.QPushButton(Form)
        self.exit.setGeometry(QtCore.QRect(630, 150, 31, 28))
        self.exit.setStyleSheet("\n"
"QPushButton{\n"
"  color:white;\n"
"  border-radius:20px;\n"
"  font-size:24px;\n"
"  }\n"
"\n"
"QPushButton:hover{\n"
"  font-size:26px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"padding-top:9px;/*上边距*/\n"
"\n"
"}")
        self.exit.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/exit.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon2)
        self.exit.setObjectName("exit")
        self.forget_button_2 = QtWidgets.QPushButton(Form)
        self.forget_button_2.setGeometry(QtCore.QRect(410, 550, 41, 21))
        self.forget_button_2.setStyleSheet("QPushButton{\n"
" font-size:10px;\n"
"background:#00000000;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"  color:black;\n"
"  border-radius:20px;\n"
"  font-size:14px;\n"
"  }\n"
"\n"
"QPushButton:hover{\n"
"  color:red;\n"
"  border-radius:15px;\n"
"  background:#00000000;\n"
"}")
        self.forget_button_2.setObjectName("forget_button_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(350, 300, 151, 31))
        self.label.setStyleSheet("*{background:#00000000;\n"
"color:#214264;\n"
"    \n"
"}")
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 470, 271, 41))
        self.lineEdit_2.setStyleSheet("*{color:rgb(85, 170, 255)}")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        self.exit.clicked.connect(Form.Exit)
        self.pushButton.clicked.connect(Form.Login_Reslute)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEdit, self.lineEdit_2)
        Form.setTabOrder(self.lineEdit_2, self.pushButton)
        Form.setTabOrder(self.pushButton, self.radioButton)
        Form.setTabOrder(self.radioButton, self.forget_button)
        Form.setTabOrder(self.forget_button, self.exit)
        Form.setTabOrder(self.exit, self.forget_button_2)
        Form.setTabOrder(self.forget_button_2, self.toolButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "          username"))
        self.pushButton.setText(_translate("Form", "LOGIN"))
        self.pushButton.setShortcut(_translate("Form", "Return"))
        self.radioButton.setText(_translate("Form", "记住密码"))
        self.forget_button.setText(_translate("Form", "忘记密码"))
        self.forget_button_2.setText(_translate("Form", "注册"))
        self.label.setText(_translate("Form", "LOGIN HERE"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "          password"))

import wire_images_rc
