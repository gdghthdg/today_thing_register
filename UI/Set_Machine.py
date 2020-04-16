# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\today_thing_register\UI\Set_Machine.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1286, 761)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("cat.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.lin_machine = QtWidgets.QLineEdit(Form)
        self.lin_machine.setGeometry(QtCore.QRect(220, 79, 191, 41))
        self.lin_machine.setObjectName("lin_machine")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(230, 130, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(229, 354, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(229, 375, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 590, 75, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 590, 75, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(740, 20, 114, 19))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(530, 80, 531, 631))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.tableWidget.setFont(font)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(850, 14, 40, 31))
        self.pushButton_3.setStyleSheet("\n"
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
"      /*padding-left:6px;*/\n"
"    padding-top:9px;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"    background:#00000000;\n"
"    border-radius:7px;\n"
"    \n"
"}\n"
"QPushButton:pressed{/*点击状态*/\n"
"    /*padding-left:3px;/*左边距*/\n"
"    padding-top:9px;/*上边距*/\n"
"}\n"
"\n"
"")
        self.pushButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/Refresh_24px_1158474_easyicon.net.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_3.setObjectName("pushButton_3")
        self.but_return = QtWidgets.QPushButton(Form)
        self.but_return.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.but_return.setStyleSheet("*{background:#00000000;}")
        self.but_return.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/retutn.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_return.setIcon(icon2)
        self.but_return.setIconSize(QtCore.QSize(30, 30))
        self.but_return.setObjectName("but_return")
        self.com_machine_use = QtWidgets.QComboBox(Form)
        self.com_machine_use.setGeometry(QtCore.QRect(220, 300, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.com_machine_use.setFont(font)
        self.com_machine_use.setObjectName("com_machine_use")
        self.com_machine_use.addItem("")
        self.com_machine_use.addItem("")

        self.retranslateUi(Form)
        self.tableWidget.cellDoubleClicked['int','int'].connect(Form.TEST)
        self.pushButton.pressed.connect(Form.confire_reslute)
        self.pushButton_2.pressed.connect(Form.Clean_All)
        self.pushButton_3.pressed.connect(Form.Clean_All)
        self.but_return.clicked.connect(Form.return_mainwindow)
        self.lin_machine.returnPressed.connect(Form.seek_machine_address)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "機種是否使用設定"))
        self.label.setText(_translate("Form", "       机种"))
        self.label_2.setText(_translate("Form", "     是否使用"))
        self.label_4.setText(_translate("Form", "使用True,不使用False"))
        self.pushButton.setText(_translate("Form", "确认"))
        self.pushButton_2.setText(_translate("Form", "清除"))
        self.label_3.setText(_translate("Form", "机种使用情况"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "机种"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "是否使用"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Kitting"))
        self.com_machine_use.setItemText(0, _translate("Form", "True"))
        self.com_machine_use.setItemText(1, _translate("Form", "False"))

import wire_images_rc
