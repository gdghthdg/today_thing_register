# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\today_thing_register\UI\wireandmachine_lh.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1286, 765)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/20.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(300, 130, 951, 541))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.tableWidget.setFont(font)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
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
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(110, 510, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.but_confire = QtWidgets.QPushButton(self.centralwidget)
        self.but_confire.setGeometry(QtCore.QRect(50, 620, 75, 51))
        self.but_confire.setObjectName("but_confire")
        self.but_falsh = QtWidgets.QPushButton(self.centralwidget)
        self.but_falsh.setGeometry(QtCore.QRect(820, 32, 71, 51))
        self.but_falsh.setObjectName("but_falsh")
        self.lin_TYPEOF = QtWidgets.QLineEdit(self.centralwidget)
        self.lin_TYPEOF.setGeometry(QtCore.QRect(60, 220, 171, 31))
        self.lin_TYPEOF.setObjectName("lin_TYPEOF")
        self.lin_WUPIN_NAME = QtWidgets.QLineEdit(self.centralwidget)
        self.lin_WUPIN_NAME.setGeometry(QtCore.QRect(60, 300, 171, 31))
        self.lin_WUPIN_NAME.setObjectName("lin_WUPIN_NAME")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, 410, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(670, 50, 114, 19))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(110, 340, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 30, 71, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.pushButton_2.setStyleSheet("*{background:#00000000;}")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/retutn.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lin_THING_LH = QtWidgets.QLineEdit(self.centralwidget)
        self.lin_THING_LH.setGeometry(QtCore.QRect(60, 380, 171, 31))
        self.lin_THING_LH.setObjectName("lin_THING_LH")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.but_CLEAN = QtWidgets.QPushButton(self.centralwidget)
        self.but_CLEAN.setGeometry(QtCore.QRect(180, 620, 75, 51))
        self.but_CLEAN.setObjectName("but_CLEAN")
        self.lin_TXM = QtWidgets.QLineEdit(self.centralwidget)
        self.lin_TXM.setGeometry(QtCore.QRect(60, 130, 171, 31))
        self.lin_TXM.setObjectName("lin_TXM")
        self.lin_thing_march = QtWidgets.QLineEdit(self.centralwidget)
        self.lin_thing_march.setGeometry(QtCore.QRect(60, 470, 171, 31))
        self.lin_thing_march.setObjectName("lin_thing_march")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 260, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1286, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_to_lend = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_to_lend.setIcon(icon2)
        self.action_to_lend.setObjectName("action_to_lend")
        self.action_lend = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/lend.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_lend.setIcon(icon3)
        self.action_lend.setObjectName("action_lend")
        self.menu.addAction(self.action_to_lend)
        self.menu.addAction(self.action_lend)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.return_mainwindow)
        self.lin_THING_LH.returnPressed.connect(MainWindow.return_mainwindow)
        self.but_falsh.clicked.connect(MainWindow.Set_Table)
        self.but_confire.clicked.connect(MainWindow.confire_reslute)
        self.but_CLEAN.clicked.connect(MainWindow.Clear_All)
        self.lin_TXM.returnPressed.connect(MainWindow.Seek_Info)
        self.pushButton.clicked.connect(MainWindow.delete)
        self.tableWidget.cellDoubleClicked['int','int'].connect(MainWindow.Get_Table_Date)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "盘点与新品"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "物品全称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "物品种类"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "条形码"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "物品料号"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "物品价格"))
        self.label_8.setText(_translate("MainWindow", "物品价格"))
        self.but_confire.setText(_translate("MainWindow", "确认"))
        self.but_falsh.setText(_translate("MainWindow", "刷新"))
        self.label_7.setText(_translate("MainWindow", "物品料号"))
        self.label_3.setText(_translate("MainWindow", "线材机种绑定信息"))
        self.label_6.setText(_translate("MainWindow", "物品全称"))
        self.pushButton.setText(_translate("MainWindow", "刪除"))
        self.label_5.setText(_translate("MainWindow", "条形码"))
        self.but_CLEAN.setText(_translate("MainWindow", "清除"))
        self.label.setText(_translate("MainWindow", "物品种类"))
        self.menu.setTitle(_translate("MainWindow", "项目"))
        self.action_to_lend.setText(_translate("MainWindow", "導入數據"))
        self.action_lend.setText(_translate("MainWindow", "導出數據"))

import wire_images_rc