# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\20190822\lend_registe.ui'
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
        icon.addPixmap(QtGui.QPixmap(":/images/hands_lend.net.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(60, 10, 1191, 741))
        self.tabWidget.setStyleSheet("QTabBar::tab {\n"
"        border: none;\n"
"        border-top-left-radius: 4px;\n"
"        border-top-right-radius: 4px;\n"
"        \n"
"        height: 247px;\n"
"        min-width: 85px;\n"
"        margin-right: 5px;\n"
"        padding-left: 5px;\n"
"        padding-right: 5px;\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.test_uer_info = QtWidgets.QPlainTextEdit(self.tab)
        self.test_uer_info.setGeometry(QtCore.QRect(30, 340, 491, 381))
        self.test_uer_info.setObjectName("test_uer_info")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(410, 160, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(230, 320, 81, 20))
        self.label_6.setObjectName("label_6")
        self.dat_time = QtWidgets.QDateTimeEdit(self.tab)
        self.dat_time.setGeometry(QtCore.QRect(570, 110, 181, 41))
        self.dat_time.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 10, 1), QtCore.QTime(0, 0, 0)))
        self.dat_time.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2019, 8, 1), QtCore.QTime(0, 0, 0)))
        self.dat_time.setMinimumDate(QtCore.QDate(2019, 8, 1))
        self.dat_time.setCalendarPopup(True)
        self.dat_time.setObjectName("dat_time")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(280, 70, 72, 15))
        self.label.setObjectName("label")
        self.com_address = QtWidgets.QComboBox(self.tab)
        self.com_address.setGeometry(QtCore.QRect(350, 110, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.com_address.setFont(font)
        self.com_address.setEditable(True)
        self.com_address.setMaxVisibleItems(25)
        self.com_address.setObjectName("com_address")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(460, 250, 71, 51))
        self.pushButton.setObjectName("pushButton")
        self.lin_thing_name = QtWidgets.QLineEdit(self.tab)
        self.lin_thing_name.setGeometry(QtCore.QRect(220, 20, 181, 41))
        self.lin_thing_name.setObjectName("lin_thing_name")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(620, 150, 191, 16))
        self.label_4.setObjectName("label_4")
        self.lin_lend_num = QtWidgets.QLineEdit(self.tab)
        self.lin_lend_num.setGeometry(QtCore.QRect(440, 20, 181, 41))
        self.lin_lend_num.setObjectName("lin_lend_num")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(510, 70, 31, 16))
        self.label_7.setObjectName("label_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(580, 250, 71, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(570, 340, 501, 381))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(99)
        self.label_23 = QtWidgets.QLabel(self.tab)
        self.label_23.setGeometry(QtCore.QRect(780, 320, 51, 20))
        self.label_23.setObjectName("label_23")
        self.com_is_not_have_limits = QtWidgets.QComboBox(self.tab)
        self.com_is_not_have_limits.setGeometry(QtCore.QRect(30, 20, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.com_is_not_have_limits.setFont(font)
        self.com_is_not_have_limits.setObjectName("com_is_not_have_limits")
        self.com_is_not_have_limits.addItem("")
        self.com_is_not_have_limits.addItem("")
        self.stackedWidget = QtWidgets.QStackedWidget(self.tab)
        self.stackedWidget.setGeometry(QtCore.QRect(640, 10, 411, 80))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.lin_lend_user_name = QtWidgets.QLineEdit(self.page)
        self.lin_lend_user_name.setGeometry(QtCore.QRect(20, 10, 151, 41))
        self.lin_lend_user_name.setObjectName("lin_lend_user_name")
        self.label_18 = QtWidgets.QLabel(self.page)
        self.label_18.setGeometry(QtCore.QRect(80, 60, 31, 16))
        self.label_18.setObjectName("label_18")
        self.label_8 = QtWidgets.QLabel(self.page)
        self.label_8.setGeometry(QtCore.QRect(240, 60, 72, 15))
        self.label_8.setObjectName("label_8")
        self.lin_lend_user_phone = QtWidgets.QLineEdit(self.page)
        self.lin_lend_user_phone.setGeometry(QtCore.QRect(200, 10, 151, 41))
        self.lin_lend_user_phone.setObjectName("lin_lend_user_phone")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_2 = QtWidgets.QLabel(self.page_3)
        self.label_2.setGeometry(QtCore.QRect(70, 60, 81, 16))
        self.label_2.setObjectName("label_2")
        self.lin_user_number = QtWidgets.QLineEdit(self.page_3)
        self.lin_user_number.setGeometry(QtCore.QRect(20, 10, 181, 41))
        self.lin_user_number.setObjectName("lin_user_number")
        self.stackedWidget.addWidget(self.page_3)
        self.lin_lend_password = QtWidgets.QLineEdit(self.tab)
        self.lin_lend_password.setGeometry(QtCore.QRect(462, 190, 191, 41))
        self.lin_lend_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lin_lend_password.setObjectName("lin_lend_password")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.table_lend_register = QtWidgets.QTableWidget(self.tab_2)
        self.table_lend_register.setGeometry(QtCore.QRect(70, 60, 1001, 651))
        self.table_lend_register.setObjectName("table_lend_register")
        self.table_lend_register.setColumnCount(8)
        self.table_lend_register.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_lend_register.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_lend_register.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_lend_register.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_lend_register.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_lend_register.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_lend_register.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_lend_register.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_lend_register.setHorizontalHeaderItem(7, item)
        self.but_refresh = QtWidgets.QPushButton(self.tab_2)
        self.but_refresh.setGeometry(QtCore.QRect(520, 20, 93, 28))
        self.but_refresh.setObjectName("but_refresh")
        self.com_thing_statius = QtWidgets.QComboBox(self.tab_2)
        self.com_thing_statius.setGeometry(QtCore.QRect(70, 20, 87, 31))
        self.com_thing_statius.setObjectName("com_thing_statius")
        self.com_thing_statius.addItem("")
        self.com_thing_statius.addItem("")
        self.com_thing_statius.addItem("")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.but_return_confirm = QtWidgets.QPushButton(self.tab_3)
        self.but_return_confirm.setGeometry(QtCore.QRect(350, 260, 61, 31))
        self.but_return_confirm.setObjectName("but_return_confirm")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(400, 120, 61, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(770, 20, 61, 20))
        self.label_11.setObjectName("label_11")
        self.lin_return_lend_num = QtWidgets.QLineEdit(self.tab_3)
        self.lin_return_lend_num.setGeometry(QtCore.QRect(340, 70, 201, 41))
        self.lin_return_lend_num.setClearButtonEnabled(True)
        self.lin_return_lend_num.setObjectName("lin_return_lend_num")
        self.table_lend_data = QtWidgets.QTableWidget(self.tab_3)
        self.table_lend_data.setEnabled(True)
        self.table_lend_data.setGeometry(QtCore.QRect(20, 390, 1051, 341))
        self.table_lend_data.setObjectName("table_lend_data")
        self.table_lend_data.setColumnCount(8)
        self.table_lend_data.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_lend_data.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_lend_data.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_lend_data.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_lend_data.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_lend_data.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_lend_data.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_lend_data.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_lend_data.setHorizontalHeaderItem(7, item)
        self.com_return_line = QtWidgets.QComboBox(self.tab_3)
        self.com_return_line.setGeometry(QtCore.QRect(20, 331, 111, 31))
        self.com_return_line.setObjectName("com_return_line")
        self.com_return_name = QtWidgets.QComboBox(self.tab_3)
        self.com_return_name.setGeometry(QtCore.QRect(170, 330, 111, 31))
        self.com_return_name.setObjectName("com_return_name")
        self.label_24 = QtWidgets.QLabel(self.tab_3)
        self.label_24.setGeometry(QtCore.QRect(60, 360, 31, 16))
        self.label_24.setObjectName("label_24")
        self.label_26 = QtWidgets.QLabel(self.tab_3)
        self.label_26.setGeometry(QtCore.QRect(200, 360, 31, 16))
        self.label_26.setObjectName("label_26")
        self.lin_password = QtWidgets.QLineEdit(self.tab_3)
        self.lin_password.setGeometry(QtCore.QRect(340, 200, 201, 41))
        self.lin_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lin_password.setReadOnly(False)
        self.lin_password.setClearButtonEnabled(True)
        self.lin_password.setObjectName("lin_password")
        self.but_is_no_select = QtWidgets.QPushButton(self.tab_3)
        self.but_is_no_select.setGeometry(QtCore.QRect(840, 10, 31, 31))
        self.but_is_no_select.setStyleSheet("*{background:red;}")
        self.but_is_no_select.setText("")
        self.but_is_no_select.setObjectName("but_is_no_select")
        self.frame = QtWidgets.QFrame(self.tab_3)
        self.frame.setGeometry(QtCore.QRect(640, 50, 361, 321))
        self.frame.setStyleSheet("*{\n"
"font: 12pt \"SimSun\";\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lab_thing_name = QtWidgets.QLabel(self.frame)
        self.lab_thing_name.setGeometry(QtCore.QRect(120, 10, 221, 31))
        self.lab_thing_name.setStyleSheet("*{background: rgb(111, 156, 207);}")
        self.lab_thing_name.setText("")
        self.lab_thing_name.setObjectName("lab_thing_name")
        self.lab_lend_time = QtWidgets.QLabel(self.frame)
        self.lab_lend_time.setGeometry(QtCore.QRect(120, 210, 221, 31))
        self.lab_lend_time.setStyleSheet("*{background: rgb(111, 156, 207);}")
        self.lab_lend_time.setText("")
        self.lab_lend_time.setObjectName("lab_lend_time")
        self.lab_phone = QtWidgets.QLabel(self.frame)
        self.lab_phone.setGeometry(QtCore.QRect(120, 130, 221, 31))
        self.lab_phone.setStyleSheet("*{background: rgb(111, 156, 207);}")
        self.lab_phone.setText("")
        self.lab_phone.setObjectName("lab_phone")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(40, 140, 51, 21))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(40, 180, 41, 21))
        self.label_14.setObjectName("label_14")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(20, 252, 91, 21))
        self.label_16.setObjectName("label_16")
        self.lab_user_name = QtWidgets.QLabel(self.frame)
        self.lab_user_name.setGeometry(QtCore.QRect(120, 90, 221, 31))
        self.lab_user_name.setStyleSheet("*{background: rgb(111, 156, 207);}")
        self.lab_user_name.setText("")
        self.lab_user_name.setObjectName("lab_user_name")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(40, 100, 72, 21))
        self.label_12.setObjectName("label_12")
        self.lab_return_time = QtWidgets.QLabel(self.frame)
        self.lab_return_time.setGeometry(QtCore.QRect(120, 250, 221, 31))
        self.lab_return_time.setStyleSheet("*{background: rgb(111, 156, 207);}")
        self.lab_return_time.setText("")
        self.lab_return_time.setObjectName("lab_return_time")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(20, 218, 91, 21))
        self.label_15.setObjectName("label_15")
        self.lab_address = QtWidgets.QLabel(self.frame)
        self.lab_address.setGeometry(QtCore.QRect(120, 170, 221, 31))
        self.lab_address.setStyleSheet("*{background: rgb(111, 156, 207);}")
        self.lab_address.setText("")
        self.lab_address.setObjectName("lab_address")
        self.lab_is_not_return = QtWidgets.QLabel(self.frame)
        self.lab_is_not_return.setGeometry(QtCore.QRect(120, 290, 221, 31))
        self.lab_is_not_return.setStyleSheet("*{background: rgb(111, 156, 207);}")
        self.lab_is_not_return.setText("")
        self.lab_is_not_return.setObjectName("lab_is_not_return")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(40, 60, 72, 21))
        self.label_9.setObjectName("label_9")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(40, 290, 72, 21))
        self.label_17.setObjectName("label_17")
        self.lab_thing_num = QtWidgets.QLabel(self.frame)
        self.lab_thing_num.setGeometry(QtCore.QRect(120, 50, 221, 31))
        self.lab_thing_num.setStyleSheet("*{background: rgb(111, 156, 207);}")
        self.lab_thing_num.setText("")
        self.lab_thing_num.setObjectName("lab_thing_num")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 91, 21))
        self.label_5.setObjectName("label_5")
        self.but_lab_clear = QtWidgets.QPushButton(self.tab_3)
        self.but_lab_clear.setGeometry(QtCore.QRect(460, 260, 61, 31))
        self.but_lab_clear.setObjectName("but_lab_clear")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(135, 330, 31, 28))
        self.pushButton_2.setStyleSheet("\n"
"QPushButton{\n"
"    font-size: 14px;/*字体大小*/\n"
"    color:white;/*颜色*/\n"
"    background: #00000000;/*背景颜色*/\n"
"    border:none;\n"
"\n"
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
"}")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/Refresh_24px_1158474_easyicon.net.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab_3, "")
        self.but_return_bind_wire = QtWidgets.QPushButton(self.centralwidget)
        self.but_return_bind_wire.setGeometry(QtCore.QRect(0, 0, 51, 41))
        self.but_return_bind_wire.setStyleSheet("*{background:#00000000;}")
        self.but_return_bind_wire.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/retutn.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_return_bind_wire.setIcon(icon2)
        self.but_return_bind_wire.setIconSize(QtCore.QSize(30, 30))
        self.but_return_bind_wire.setObjectName("but_return_bind_wire")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
        self.pushButton.clicked.connect(MainWindow.Confire_Lend)
        self.lin_thing_name.returnPressed.connect(MainWindow.Seek_Thing_Info)
        self.but_return_confirm.clicked.connect(MainWindow.Return_Confire)
        self.but_return_bind_wire.clicked.connect(MainWindow.return_mainwindow)
        self.but_refresh.clicked.connect(MainWindow.Set_Table)
        self.pushButton_5.clicked.connect(MainWindow.clear_all)
        self.table_lend_data.cellDoubleClicked['int','int'].connect(MainWindow.get_return_table)
        self.com_return_line.activated['QString'].connect(MainWindow.return_set_table)
        self.com_return_name.activated['QString'].connect(MainWindow.return_set_table)
        self.lin_password.returnPressed.connect(MainWindow.Return_Confire)
        self.com_thing_statius.activated['QString'].connect(MainWindow.Set_Table)
        self.but_lab_clear.clicked.connect(MainWindow.clear_label)
        self.lin_user_number.returnPressed.connect(MainWindow.Seek_User_Info)
        self.com_is_not_have_limits.activated['QString'].connect(MainWindow.interface_chioce)
        self.lin_lend_user_name.returnPressed.connect(MainWindow.seek_no_limeit_user_name)
        self.lin_lend_password.returnPressed.connect(MainWindow.Confire_Lend)
        self.pushButton_2.clicked.connect(MainWindow.return_set_table)
        self.but_refresh.clicked.connect(MainWindow.check_thing_is_return)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lin_thing_name, self.lin_lend_num)
        MainWindow.setTabOrder(self.lin_lend_num, self.lin_user_number)
        MainWindow.setTabOrder(self.lin_user_number, self.com_address)
        MainWindow.setTabOrder(self.com_address, self.lin_lend_password)
        MainWindow.setTabOrder(self.lin_lend_password, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.table_lend_register)
        MainWindow.setTabOrder(self.table_lend_register, self.but_return_confirm)
        MainWindow.setTabOrder(self.but_return_confirm, self.test_uer_info)
        MainWindow.setTabOrder(self.test_uer_info, self.dat_time)
        MainWindow.setTabOrder(self.dat_time, self.lin_return_lend_num)
        MainWindow.setTabOrder(self.lin_return_lend_num, self.table_lend_data)
        MainWindow.setTabOrder(self.table_lend_data, self.but_return_bind_wire)
        MainWindow.setTabOrder(self.but_return_bind_wire, self.but_refresh)
        MainWindow.setTabOrder(self.but_refresh, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.tableWidget)
        MainWindow.setTabOrder(self.tableWidget, self.com_is_not_have_limits)
        MainWindow.setTabOrder(self.com_is_not_have_limits, self.lin_lend_user_phone)
        MainWindow.setTabOrder(self.lin_lend_user_phone, self.com_thing_statius)
        MainWindow.setTabOrder(self.com_thing_statius, self.com_return_line)
        MainWindow.setTabOrder(self.com_return_line, self.com_return_name)
        MainWindow.setTabOrder(self.com_return_name, self.lin_password)
        MainWindow.setTabOrder(self.lin_password, self.but_is_no_select)
        MainWindow.setTabOrder(self.but_is_no_select, self.but_lab_clear)
        MainWindow.setTabOrder(self.but_lab_clear, self.lin_lend_user_name)
        MainWindow.setTabOrder(self.lin_lend_user_name, self.pushButton_5)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "借用登记"))
        self.label_3.setText(_translate("MainWindow", "使用位置"))
        self.label_6.setText(_translate("MainWindow", "借用情况"))
        self.dat_time.setToolTip(_translate("MainWindow", "默认5个小时后,可修改"))
        self.dat_time.setDisplayFormat(_translate("MainWindow", "yyyy-M-d hh:mm:ss"))
        self.label.setText(_translate("MainWindow", "物品名称"))
        self.pushButton.setText(_translate("MainWindow", "确认"))
        self.label_4.setText(_translate("MainWindow", "归还时间"))
        self.label_7.setText(_translate("MainWindow", "数量"))
        self.pushButton_5.setText(_translate("MainWindow", "清除"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "物品名称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "数量"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "借用时间"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "归还时间"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "状态"))
        self.label_23.setText(_translate("MainWindow", "未归还"))
        self.com_is_not_have_limits.setToolTip(_translate("MainWindow", "请选择登记人的类别"))
        self.com_is_not_have_limits.setItemText(0, _translate("MainWindow", "厂内人员"))
        self.com_is_not_have_limits.setItemText(1, _translate("MainWindow", "厂外人员"))
        self.label_18.setText(_translate("MainWindow", "姓名"))
        self.label_8.setText(_translate("MainWindow", "联系方式"))
        self.label_2.setText(_translate("MainWindow", "借用人工号"))
        self.lin_lend_password.setPlaceholderText(_translate("MainWindow", "          密码"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "借用登记"))
        item = self.table_lend_register.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "物品名称"))
        item = self.table_lend_register.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "数量"))
        item = self.table_lend_register.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "人员"))
        item = self.table_lend_register.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "手机"))
        item = self.table_lend_register.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "位置"))
        item = self.table_lend_register.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "借用时间"))
        item = self.table_lend_register.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "归还时间"))
        item = self.table_lend_register.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "状态"))
        self.but_refresh.setText(_translate("MainWindow", "刷新"))
        self.com_thing_statius.setItemText(0, _translate("MainWindow", "借用中"))
        self.com_thing_statius.setItemText(1, _translate("MainWindow", "未歸還"))
        self.com_thing_statius.setItemText(2, _translate("MainWindow", "已歸還"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "借用记录"))
        self.but_return_confirm.setText(_translate("MainWindow", "确认"))
        self.label_10.setText(_translate("MainWindow", "归还数量"))
        self.label_11.setText(_translate("MainWindow", "借用情况"))
        item = self.table_lend_data.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "物品名称"))
        item = self.table_lend_data.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "数量"))
        item = self.table_lend_data.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "人员"))
        item = self.table_lend_data.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "手机"))
        item = self.table_lend_data.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "位置"))
        item = self.table_lend_data.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "借用时间"))
        item = self.table_lend_data.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "归还时间"))
        item = self.table_lend_data.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "状态"))
        self.label_24.setText(_translate("MainWindow", "线体"))
        self.label_26.setText(_translate("MainWindow", "人员"))
        self.lin_password.setPlaceholderText(_translate("MainWindow", "          密码"))
        self.label_13.setText(_translate("MainWindow", "手机"))
        self.label_14.setText(_translate("MainWindow", "位置"))
        self.label_16.setText(_translate("MainWindow", "归还时间"))
        self.label_12.setText(_translate("MainWindow", "人员"))
        self.label_15.setText(_translate("MainWindow", "借用时间"))
        self.label_9.setText(_translate("MainWindow", "数量"))
        self.label_17.setText(_translate("MainWindow", "状态"))
        self.label_5.setText(_translate("MainWindow", "物品名称"))
        self.but_lab_clear.setText(_translate("MainWindow", "清除"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "借用归还"))

import wire_images_rc
