# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\20190822\Thing_Check.ui'
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
        icon.addPixmap(QtGui.QPixmap(":/images/cat.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 50, 531, 661))
        self.tabWidget.setStyleSheet("\n"
"\n"
"QTabBar::tab {\n"
"        border-top:0px solid rgb(45, 45, 45);\n"
"        border-top-left-radius: 4px;\n"
"        border-top-right-radius: 4px;\n"
"        color: rgb(175, 175, 175);\n"
"        height: 329px;\n"
"        min-width: 85px;\n"
"        margin-right: 5px;\n"
"        padding-left: 5px;\n"
"        padding-right: 5px;\n"
"}\n"
"")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lin_online = QtWidgets.QLineEdit(self.tab)
        self.lin_online.setGeometry(QtCore.QRect(20, 420, 161, 41))
        self.lin_online.setObjectName("lin_online")
        self.lin_ng_address = QtWidgets.QLineEdit(self.tab)
        self.lin_ng_address.setGeometry(QtCore.QRect(240, 500, 161, 41))
        self.lin_ng_address.setObjectName("lin_ng_address")
        self.lin_ok_address = QtWidgets.QLineEdit(self.tab)
        self.lin_ok_address.setGeometry(QtCore.QRect(20, 500, 161, 41))
        self.lin_ok_address.setObjectName("lin_ok_address")
        self.lin_ng = QtWidgets.QLineEdit(self.tab)
        self.lin_ng.setGeometry(QtCore.QRect(20, 340, 161, 41))
        self.lin_ng.setObjectName("lin_ng")
        self.lin_typeof = QtWidgets.QLineEdit(self.tab)
        self.lin_typeof.setGeometry(QtCore.QRect(20, 250, 161, 41))
        self.lin_typeof.setObjectName("lin_typeof")
        self.lin_thing_truename = QtWidgets.QLineEdit(self.tab)
        self.lin_thing_truename.setGeometry(QtCore.QRect(240, 160, 161, 41))
        self.lin_thing_truename.setObjectName("lin_thing_truename")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(60, 300, 72, 15))
        self.label.setObjectName("label")
        self.com_desc = QtWidgets.QComboBox(self.tab)
        self.com_desc.setGeometry(QtCore.QRect(160, 30, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.com_desc.setFont(font)
        self.com_desc.setObjectName("com_desc")
        self.com_desc.addItem("")
        self.com_desc.addItem("")
        self.com_desc.addItem("")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(50, 210, 81, 16))
        self.label_2.setObjectName("label_2")
        self.lin_ok = QtWidgets.QLineEdit(self.tab)
        self.lin_ok.setGeometry(QtCore.QRect(240, 250, 161, 41))
        self.lin_ok.setObjectName("lin_ok")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(70, 550, 51, 16))
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(170, 590, 71, 51))
        self.pushButton.setObjectName("pushButton")
        self.lin_secureqty = QtWidgets.QLineEdit(self.tab)
        self.lin_secureqty.setGeometry(QtCore.QRect(240, 420, 161, 41))
        self.lin_secureqty.setObjectName("lin_secureqty")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(290, 540, 51, 21))
        self.label_10.setObjectName("label_10")
        self.lin_txm = QtWidgets.QLineEdit(self.tab)
        self.lin_txm.setGeometry(QtCore.QRect(20, 160, 161, 41))
        self.lin_txm.setObjectName("lin_txm")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(50, 470, 91, 16))
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(280, 300, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(280, 390, 72, 15))
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 90, 51, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(280, 210, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(290, 470, 71, 16))
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(60, 390, 72, 15))
        self.label_5.setObjectName("label_5")
        self.lin_bf = QtWidgets.QLineEdit(self.tab)
        self.lin_bf.setGeometry(QtCore.QRect(240, 340, 161, 41))
        self.lin_bf.setObjectName("lin_bf")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.com_ok_ng_on_bf = QtWidgets.QComboBox(self.tab_2)
        self.com_ok_ng_on_bf.setGeometry(QtCore.QRect(160, 10, 121, 41))
        self.com_ok_ng_on_bf.setObjectName("com_ok_ng_on_bf")
        self.com_ok_ng_on_bf.addItem("")
        self.com_ok_ng_on_bf.setItemText(0, "")
        self.com_ok_ng_on_bf.addItem("")
        self.com_ok_ng_on_bf.addItem("")
        self.com_ok_ng_on_bf.addItem("")
        self.com_ok_ng_on_bf.addItem("")
        self.lin_tab_txm = QtWidgets.QLineEdit(self.tab_2)
        self.lin_tab_txm.setGeometry(QtCore.QRect(10, 120, 181, 41))
        self.lin_tab_txm.setObjectName("lin_tab_txm")
        self.lin_tab_peidiao = QtWidgets.QLineEdit(self.tab_2)
        self.lin_tab_peidiao.setGeometry(QtCore.QRect(10, 280, 181, 41))
        self.lin_tab_peidiao.setObjectName("lin_tab_peidiao")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(70, 170, 51, 31))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(60, 330, 72, 21))
        self.label_12.setObjectName("label_12")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 450, 93, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lab_tab_thingnum = QtWidgets.QLabel(self.tab_2)
        self.lab_tab_thingnum.setGeometry(QtCore.QRect(250, 280, 161, 41))
        self.lab_tab_thingnum.setStyleSheet("*{background:rgb(100, 170, 220);}")
        self.lab_tab_thingnum.setText("")
        self.lab_tab_thingnum.setObjectName("lab_tab_thingnum")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(290, 180, 72, 21))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(290, 330, 61, 16))
        self.label_16.setObjectName("label_16")
        self.lab_tab_thingname = QtWidgets.QLabel(self.tab_2)
        self.lab_tab_thingname.setGeometry(QtCore.QRect(251, 119, 161, 41))
        self.lab_tab_thingname.setStyleSheet("*{background:rgb(100, 170, 220);}")
        self.lab_tab_thingname.setText("")
        self.lab_tab_thingname.setObjectName("lab_tab_thingname")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(190, 60, 51, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.tab_2, "")
        self.lab_lh_address = QtWidgets.QLabel(self.centralwidget)
        self.lab_lh_address.setGeometry(QtCore.QRect(930, 10, 41, 21))
        self.lab_lh_address.setStyleSheet("")
        self.lab_lh_address.setObjectName("lab_lh_address")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(830, 10, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tab_thing_all = QtWidgets.QTableWidget(self.centralwidget)
        self.tab_thing_all.setEnabled(True)
        self.tab_thing_all.setGeometry(QtCore.QRect(560, 50, 701, 661))
        self.tab_thing_all.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab_thing_all.setObjectName("tab_thing_all")
        self.tab_thing_all.setColumnCount(10)
        self.tab_thing_all.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tab_thing_all.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_thing_all.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_thing_all.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_thing_all.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_thing_all.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_thing_all.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_thing_all.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_thing_all.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_thing_all.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_thing_all.setHorizontalHeaderItem(9, item)
        self.but_return_bind_wire = QtWidgets.QPushButton(self.centralwidget)
        self.but_return_bind_wire.setGeometry(QtCore.QRect(10, 10, 41, 31))
        self.but_return_bind_wire.setStyleSheet("*{background:#00000000;}")
        self.but_return_bind_wire.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/retutn.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_return_bind_wire.setIcon(icon1)
        self.but_return_bind_wire.setIconSize(QtCore.QSize(30, 30))
        self.but_return_bind_wire.setObjectName("but_return_bind_wire")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1286, 21))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.set_machine_user = QtWidgets.QAction(MainWindow)
        self.set_machine_user.setObjectName("set_machine_user")
        self.act_set_wire_malh = QtWidgets.QAction(MainWindow)
        self.act_set_wire_malh.setObjectName("act_set_wire_malh")
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
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_2.pressed.connect(MainWindow.Set_Table)
        self.lin_txm.returnPressed.connect(MainWindow.Seek_wireinfo)
        self.pushButton_3.clicked.connect(MainWindow.Clean_All)
        self.pushButton.clicked.connect(MainWindow.confire_reslute)
        self.tabWidget.currentChanged['int'].connect(MainWindow.get_tabwidget_int)
        self.tab_thing_all.cellDoubleClicked['int','int'].connect(MainWindow.TEST)
        self.pushButton_4.clicked.connect(MainWindow.confire_reslute)
        self.lin_tab_txm.returnPressed.connect(MainWindow.thing_showinfo)
        self.pushButton_5.clicked.connect(MainWindow.Clean_All)
        self.but_return_bind_wire.clicked.connect(MainWindow.return_mainwindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "物品位置數量盤點"))
        self.label.setText(_translate("MainWindow", "物品种类"))
        self.com_desc.setItemText(0, _translate("MainWindow", "修改"))
        self.com_desc.setItemText(1, _translate("MainWindow", "删除"))
        self.com_desc.setItemText(2, _translate("MainWindow", "增加"))
        self.label_2.setText(_translate("MainWindow", "物品条形码"))
        self.label_9.setText(_translate("MainWindow", "OK位置"))
        self.pushButton.setText(_translate("MainWindow", "确认"))
        self.label_10.setText(_translate("MainWindow", "NG位置"))
        self.label_8.setText(_translate("MainWindow", "产线物品数量"))
        self.label_4.setText(_translate("MainWindow", "库存OK数"))
        self.label_6.setText(_translate("MainWindow", "报废数量"))
        self.pushButton_3.setText(_translate("MainWindow", "清除"))
        self.label_3.setText(_translate("MainWindow", "物品名称"))
        self.label_7.setText(_translate("MainWindow", "安全数量"))
        self.label_5.setText(_translate("MainWindow", "库存NG数"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "增删改查"))
        self.com_ok_ng_on_bf.setItemText(1, _translate("MainWindow", "OK品盤點"))
        self.com_ok_ng_on_bf.setItemText(2, _translate("MainWindow", "NG品盤點"))
        self.com_ok_ng_on_bf.setItemText(3, _translate("MainWindow", "在線品盤點"))
        self.com_ok_ng_on_bf.setItemText(4, _translate("MainWindow", "報廢品盤點"))
        self.label_11.setText(_translate("MainWindow", "條形碼"))
        self.label_12.setText(_translate("MainWindow", "盤點數量"))
        self.pushButton_4.setText(_translate("MainWindow", "確認"))
        self.label_15.setText(_translate("MainWindow", "物品名稱"))
        self.label_16.setText(_translate("MainWindow", "現有數量"))
        self.pushButton_5.setText(_translate("MainWindow", "清除"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "盘点"))
        self.lab_lh_address.setText(_translate("MainWindow", "0"))
        self.pushButton_2.setText(_translate("MainWindow", "刷新"))
        item = self.tab_thing_all.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "物品条码"))
        item = self.tab_thing_all.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "物品名称"))
        item = self.tab_thing_all.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "物品种类"))
        item = self.tab_thing_all.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "库存OK数"))
        item = self.tab_thing_all.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "库存NG数"))
        item = self.tab_thing_all.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "产线数量"))
        item = self.tab_thing_all.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "报废数量"))
        item = self.tab_thing_all.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "安全数量"))
        item = self.tab_thing_all.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "OK位置"))
        item = self.tab_thing_all.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "NG位置"))
        self.menu.setTitle(_translate("MainWindow", "项目"))
        self.set_machine_user.setText(_translate("MainWindow", "设定机种"))
        self.act_set_wire_malh.setText(_translate("MainWindow", "设定线材料号"))
        self.action_to_lend.setText(_translate("MainWindow", "導入數據"))
        self.action_lend.setText(_translate("MainWindow", "導出數據"))

import wire_images_rc
