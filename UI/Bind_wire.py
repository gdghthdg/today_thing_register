# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\today_thing_register\UI\Bind_wire.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1286, 761)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/99.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QAction{\n"
"background-image: url(:/images/lend.ico);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(280, 470, 31, 31))
        self.label_10.setObjectName("label_10")
        self.inv = QtWidgets.QLineEdit(self.centralwidget)
        self.inv.setGeometry(QtCore.QRect(410, 430, 161, 31))
        self.inv.setClearButtonEnabled(True)
        self.inv.setObjectName("inv")
        self.ias = QtWidgets.QLineEdit(self.centralwidget)
        self.ias.setGeometry(QtCore.QRect(410, 330, 161, 31))
        self.ias.setClearButtonEnabled(True)
        self.ias.setObjectName("ias")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(470, 570, 51, 20))
        self.label_14.setObjectName("label_14")
        self.dirver = QtWidgets.QLineEdit(self.centralwidget)
        self.dirver.setGeometry(QtCore.QRect(212, 530, 161, 31))
        self.dirver.setClearButtonEnabled(True)
        self.dirver.setObjectName("dirver")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(80, 370, 31, 16))
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 270, 51, 16))
        self.label_5.setObjectName("label_5")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(130, 90, 441, 21))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_2.addWidget(self.label_16)
        self.label_18 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_2.addWidget(self.label_18)
        self.label_15 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(470, 180, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(80, 470, 31, 16))
        self.label_9.setObjectName("label_9")
        self.mondel = QtWidgets.QLineEdit(self.centralwidget)
        self.mondel.setGeometry(QtCore.QRect(210, 230, 161, 31))
        self.mondel.setClearButtonEnabled(True)
        self.mondel.setObjectName("mondel")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(480, 270, 21, 16))
        self.label_6.setObjectName("label_6")
        self.ffc = QtWidgets.QLineEdit(self.centralwidget)
        self.ffc.setGeometry(QtCore.QRect(210, 430, 161, 31))
        self.ffc.setClearButtonEnabled(True)
        self.ffc.setObjectName("ffc")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(70, 570, 61, 21))
        self.label_13.setObjectName("label_13")
        self.power_wire = QtWidgets.QLineEdit(self.centralwidget)
        self.power_wire.setGeometry(QtCore.QRect(410, 530, 161, 31))
        self.power_wire.setClearButtonEnabled(True)
        self.power_wire.setObjectName("power_wire")
        self.power_march = QtWidgets.QLineEdit(self.centralwidget)
        self.power_march.setGeometry(QtCore.QRect(10, 530, 161, 31))
        self.power_march.setClearButtonEnabled(True)
        self.power_march.setObjectName("power_march")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 270, 81, 16))
        self.label_4.setObjectName("label_4")
        self.ctag = QtWidgets.QLineEdit(self.centralwidget)
        self.ctag.setGeometry(QtCore.QRect(12, 330, 161, 31))
        self.ctag.setClearButtonEnabled(True)
        self.ctag.setObjectName("ctag")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 170, 31, 16))
        self.label.setObjectName("label")
        self.bi = QtWidgets.QLineEdit(self.centralwidget)
        self.bi.setGeometry(QtCore.QRect(410, 230, 161, 31))
        self.bi.setClearButtonEnabled(True)
        self.bi.setObjectName("bi")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 610, 75, 51))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 170, 31, 16))
        self.label_2.setObjectName("label_2")
        self.agis = QtWidgets.QLineEdit(self.centralwidget)
        self.agis.setGeometry(QtCore.QRect(10, 430, 161, 31))
        self.agis.setClearButtonEnabled(True)
        self.agis.setObjectName("agis")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(260, 570, 71, 21))
        self.label_12.setObjectName("label_12")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(480, 370, 41, 16))
        self.label_8.setObjectName("label_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 610, 75, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.ji_or_skd = QtWidgets.QLineEdit(self.centralwidget)
        self.ji_or_skd.setGeometry(QtCore.QRect(10, 230, 161, 31))
        self.ji_or_skd.setClearButtonEnabled(True)
        self.ji_or_skd.setObjectName("ji_or_skd")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(460, 470, 81, 31))
        self.label_11.setObjectName("label_11")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(140, 60, 441, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.add.setText("")
        self.add.setObjectName("add")
        self.horizontalLayout.addWidget(self.add)
        self.delete_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.delete_2.setText("")
        self.delete_2.setObjectName("delete_2")
        self.horizontalLayout.addWidget(self.delete_2)
        self.change = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.change.setText("")
        self.change.setObjectName("change")
        self.horizontalLayout.addWidget(self.change)
        self.tab_machine_lh = QtWidgets.QTableWidget(self.centralwidget)
        self.tab_machine_lh.setEnabled(True)
        self.tab_machine_lh.setGeometry(QtCore.QRect(610, 60, 651, 611))
        self.tab_machine_lh.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab_machine_lh.setObjectName("tab_machine_lh")
        self.tab_machine_lh.setColumnCount(15)
        self.tab_machine_lh.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tab_machine_lh.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_machine_lh.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_machine_lh.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_machine_lh.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_machine_lh.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_machine_lh.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_machine_lh.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_machine_lh.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_machine_lh.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_machine_lh.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_machine_lh.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_machine_lh.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_machine_lh.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_machine_lh.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_machine_lh.setHorizontalHeaderItem(14, item)
        self.machine = QtWidgets.QLineEdit(self.centralwidget)
        self.machine.setGeometry(QtCore.QRect(12, 130, 161, 31))
        self.machine.setClearButtonEnabled(True)
        self.machine.setObjectName("machine")
        self.size = QtWidgets.QLineEdit(self.centralwidget)
        self.size.setGeometry(QtCore.QRect(210, 130, 161, 31))
        self.size.setClearButtonEnabled(True)
        self.size.setObjectName("size")
        self.systems = QtWidgets.QLineEdit(self.centralwidget)
        self.systems.setGeometry(QtCore.QRect(412, 130, 161, 31))
        self.systems.setClearButtonEnabled(True)
        self.systems.setObjectName("systems")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(860, 20, 51, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.bma = QtWidgets.QLineEdit(self.centralwidget)
        self.bma.setGeometry(QtCore.QRect(212, 330, 161, 31))
        self.bma.setClearButtonEnabled(True)
        self.bma.setObjectName("bma")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(280, 370, 31, 16))
        self.label_17.setObjectName("label_17")
        self.lab_lh_address = QtWidgets.QLabel(self.centralwidget)
        self.lab_lh_address.setGeometry(QtCore.QRect(930, 20, 41, 31))
        self.lab_lh_address.setStyleSheet("")
        self.lab_lh_address.setObjectName("lab_lh_address")
        self.but_return_mainwindows = QtWidgets.QPushButton(self.centralwidget)
        self.but_return_mainwindows.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.but_return_mainwindows.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.but_return_mainwindows.setStyleSheet("*{background:#00000000;}")
        self.but_return_mainwindows.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/retutn.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_return_mainwindows.setIcon(icon1)
        self.but_return_mainwindows.setIconSize(QtCore.QSize(30, 30))
        self.but_return_mainwindows.setObjectName("but_return_mainwindows")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1286, 21))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.action_lend = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/lend.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_lend.setIcon(icon2)
        self.action_lend.setObjectName("action_lend")
        self.action_to_lend = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_to_lend.setIcon(icon3)
        self.action_to_lend.setObjectName("action_to_lend")
        self.menu.addAction(self.action_to_lend)
        self.menu.addAction(self.action_lend)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton_3.pressed.connect(MainWindow.Clean_All)
        self.pushButton.pressed.connect(MainWindow.confire_reslute)
        self.tab_machine_lh.cellDoubleClicked['int','int'].connect(MainWindow.TEST)
        self.pushButton_2.pressed.connect(MainWindow.Set_Table)
        self.machine.returnPressed.connect(MainWindow.Seek_wireinfo)
        self.but_return_mainwindows.clicked.connect(MainWindow.Mian_Window_show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "機種線材設定"))
        self.label_10.setText(_translate("MainWindow", "FFC"))
        self.label_14.setText(_translate("MainWindow", "电源线"))
        self.label_7.setText(_translate("MainWindow", "CTAG"))
        self.label_5.setText(_translate("MainWindow", "MODEL"))
        self.label_16.setText(_translate("MainWindow", "添加"))
        self.label_18.setText(_translate("MainWindow", "删除"))
        self.label_15.setText(_translate("MainWindow", "修改"))
        self.label_3.setText(_translate("MainWindow", "系统"))
        self.label_9.setText(_translate("MainWindow", "AGIS"))
        self.label_6.setText(_translate("MainWindow", "BI"))
        self.label_13.setText(_translate("MainWindow", "驱动板"))
        self.label_4.setText(_translate("MainWindow", "JI_OR_SKD"))
        self.label.setText(_translate("MainWindow", "尺寸"))
        self.pushButton.setText(_translate("MainWindow", "确认"))
        self.label_2.setText(_translate("MainWindow", "机种"))
        self.label_12.setText(_translate("MainWindow", "电流大小"))
        self.label_8.setText(_translate("MainWindow", "IAS"))
        self.pushButton_3.setText(_translate("MainWindow", "清除"))
        self.label_11.setText(_translate("MainWindow", "INV_电源线"))
        item = self.tab_machine_lh.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "机种"))
        item = self.tab_machine_lh.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "尺寸"))
        item = self.tab_machine_lh.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "系统"))
        item = self.tab_machine_lh.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "JI_OR_SKD"))
        item = self.tab_machine_lh.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "MODEL"))
        item = self.tab_machine_lh.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "BI"))
        item = self.tab_machine_lh.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "CTAG"))
        item = self.tab_machine_lh.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "BMA"))
        item = self.tab_machine_lh.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "IAS"))
        item = self.tab_machine_lh.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "AGIS"))
        item = self.tab_machine_lh.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "FFC"))
        item = self.tab_machine_lh.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "INV电源线"))
        item = self.tab_machine_lh.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "驱动板"))
        item = self.tab_machine_lh.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "电流大小"))
        item = self.tab_machine_lh.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "电源线"))
        self.pushButton_2.setText(_translate("MainWindow", "刷新"))
        self.label_17.setText(_translate("MainWindow", "BMA"))
        self.lab_lh_address.setText(_translate("MainWindow", "0"))
        self.menu.setTitle(_translate("MainWindow", "項目"))
        self.action_lend.setText(_translate("MainWindow", "導出數據"))
        self.action_to_lend.setText(_translate("MainWindow", "導入數據"))

import wire_images_rc
