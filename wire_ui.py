# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\20190822\wire_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1286, 761)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/88.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("\n"
"*{\n"
"    background:url(:/images/8.jpg);\n"
"    font-family:century gothic;\n"
"    font: 9pt \"微軟正黑體\";\n"
"}\n"
"frame_3 QPushButton{\n"
"    font-size: 14px;/*字体大小*/\n"
"    color:black;/*颜色*/\n"
"    background-color: rgb(255, 255, 255,50);/*背景颜色*/\n"
"    border-radius:4px;\n"
"}\n"
"\n"
"/**********标签**********/\n"
"QLabel {\n"
"    border-radius: 10px;\n"
"    \n"
"    font-size: 20px;\n"
"}\n"
"\n"
"\n"
"/**********单行文本框**********/\n"
"QLineEdit {\n"
"    font-size: 17px;/*字体大小*/\n"
"    color: black; /*内容颜色*/\n"
"    height: 25px;    /*高度*/\n"
"    border: 2px solid rgb(100, 100, 100); /*边框粗细和颜色*/\n"
"    border-radius: 10px;  /*边框的弧度*/\n"
"    background: rgb(72, 72, 73, 10%); /*背景颜色*/\n"
"\n"
"}\n"
"\n"
"/**********分组框**********/\n"
"\n"
"QFrame{\n"
"     background:#00000000\n"
"}\n"
"Line{background:rgb(193, 193, 193);}\n"
"\n"
"")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(170, 20, 641, 181))
        self.frame_3.setStyleSheet("\n"
"\n"
"QComboBox {\n"
"    font-size: 19px;/*字体大小*/\n"
"    color: black; /*内容颜色*/\n"
"    min-height: 24px;    /*最小高度*/\n"
"    min-width: 100px; /*最小宽度*/\n"
"    border:2px solid rgb(100, 100, 100); /*边框粗细和颜色*/\n"
"    border-radius:10px;\n"
"    background:rgb(255, 255, 127);\n"
"    /*background:rgb(72, 72, 73,30%)*/\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    font-size: 20px;/*字体大小*/\n"
"    color: black;/*颜色*/\n"
"    border: 1px solid rgb(100, 100, 100);/*边框粗细和颜色*/\n"
"    border-radius: 4px;  /*边框的弧度*/\n"
"    background:white;/*背景颜色*/\n"
"\n"
"    selection-background-color:rgb(181, 181, 181); /*选取时的背景颜色*/\n"
"    selection-color:rgb(255, 0, 0);/*选中时字体颜色*/\n"
"    \n"
"\n"
"}\n"
"\n"
"QComboBox::drop-down {/*右侧按钮*/\n"
"    width:20px;\n"
"    \n"
"    background:  rgb(255, 255, 255,10);/*背景颜色*/\n"
"    border-left-width: 1px;   /*加左边框线（可以不要，下同）*/\n"
"    border-left-style: solid;  /*左边框线类型*/\n"
"    border-left-color: gray;  /*左边框线颜色*/\n"
"    \n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow {\n"
"image: url(:/images/triangle_down_16px_1189852_easyicon.net.ico);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    font-size: 17px;/*字体大小*/\n"
"    color: black; /*内容颜色*/\n"
"    height: 25px;    /*高度*/\n"
"    border: 2px solid rgb(100, 100, 100); /*边框粗细和颜色*/\n"
"    border-radius: 10px;  /*边框的弧度*/\n"
"    background:rgb(255, 255, 127); /*背景颜色*/\n"
"\n"
"}\n"
"\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(0, 80, 81, 20))
        self.label_7.setObjectName("label_7")
        self.com_operation = QtWidgets.QComboBox(self.frame_3)
        self.com_operation.setGeometry(QtCore.QRect(100, 70, 141, 41))
        self.com_operation.setMouseTracking(True)
        self.com_operation.setEditable(False)
        self.com_operation.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.com_operation.setObjectName("com_operation")
        self.com_operation.addItem("")
        self.com_operation.setItemText(0, "")
        self.com_operation.addItem("")
        self.com_operation.addItem("")
        self.com_operation.addItem("")
        self.label_19 = QtWidgets.QLabel(self.frame_3)
        self.label_19.setGeometry(QtCore.QRect(350, 80, 81, 20))
        self.label_19.setObjectName("label_19")
        self.com_method = QtWidgets.QComboBox(self.frame_3)
        self.com_method.setGeometry(QtCore.QRect(440, 70, 141, 41))
        self.com_method.setMouseTracking(True)
        self.com_method.setEditable(False)
        self.com_method.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.com_method.setObjectName("com_method")
        self.label_27 = QtWidgets.QLabel(self.frame_3)
        self.label_27.setGeometry(QtCore.QRect(0, 140, 81, 20))
        self.label_27.setObjectName("label_27")
        self.com_lines = QtWidgets.QComboBox(self.frame_3)
        self.com_lines.setGeometry(QtCore.QRect(100, 130, 141, 41))
        self.com_lines.setMaxVisibleItems(20)
        self.com_lines.setObjectName("com_lines")
        self.label_37 = QtWidgets.QLabel(self.frame_3)
        self.label_37.setGeometry(QtCore.QRect(0, 20, 81, 21))
        self.label_37.setObjectName("label_37")
        self.com_Thing_class = QtWidgets.QComboBox(self.frame_3)
        self.com_Thing_class.setGeometry(QtCore.QRect(100, 10, 191, 41))
        self.com_Thing_class.setObjectName("com_Thing_class")
        self.lin_worker_num = QtWidgets.QLineEdit(self.frame_3)
        self.lin_worker_num.setGeometry(QtCore.QRect(440, 10, 191, 41))
        self.lin_worker_num.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lin_worker_num.setTabletTracking(True)
        self.lin_worker_num.setClearButtonEnabled(True)
        self.lin_worker_num.setObjectName("lin_worker_num")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(350, 20, 81, 20))
        self.label_10.setObjectName("label_10")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_3)
        self.stackedWidget.setGeometry(QtCore.QRect(350, 120, 241, 51))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_12 = QtWidgets.QLabel(self.page)
        self.label_12.setGeometry(QtCore.QRect(0, 20, 81, 20))
        self.label_12.setObjectName("label_12")
        self.pushButton_5 = QtWidgets.QPushButton(self.page)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 10, 141, 41))
        self.pushButton_5.setStyleSheet("\n"
"\n"
"* {\n"
"    font-size: 12px;/*字体大小*/\n"
"    color: black; /*内容颜色*/\n"
"    min-height: 24px;    /*最小高度*/\n"
"    min-width: 100px; /*最小宽度*/\n"
"    border:2px solid rgb(100, 100, 100); /*边框粗细和颜色*/\n"
"    border-radius:10px;\n"
"    background:rgb(119, 174, 255);\n"
"    /*background:rgb(72, 72, 73,30%)*/\n"
"    text-align: center;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_8 = QtWidgets.QLabel(self.page_3)
        self.label_8.setGeometry(QtCore.QRect(0, 20, 81, 20))
        self.label_8.setObjectName("label_8")
        self.lin_quantiy = QtWidgets.QLineEdit(self.page_3)
        self.lin_quantiy.setGeometry(QtCore.QRect(90, 10, 141, 41))
        self.lin_quantiy.setTabletTracking(True)
        self.lin_quantiy.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lin_quantiy.setText("")
        self.lin_quantiy.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lin_quantiy.setCursorPosition(0)
        self.lin_quantiy.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lin_quantiy.setClearButtonEnabled(True)
        self.lin_quantiy.setObjectName("lin_quantiy")
        self.stackedWidget.addWidget(self.page_3)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(440, 430, 331, 291))
        self.frame_4.setStyleSheet("\n"
"QPushButton{\n"
"    font-size: 14px;/*字体大小*/\n"
"    color:GREEN;/*颜色*/\n"
"    background-color: rgb(255, 255, 255,50);/*背景颜色*/\n"
"    border-radius:40px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    /*padding-left:3px;左边距*/\n"
"    padding-top:8px;/*上边距*/\n"
"\n"
"}\n"
"QLabel{font-size:17px;\n"
";\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lin_admin_password = QtWidgets.QLineEdit(self.frame_4)
        self.lin_admin_password.setGeometry(QtCore.QRect(60, 170, 211, 31))
        self.lin_admin_password.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lin_admin_password.setText("")
        self.lin_admin_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lin_admin_password.setClearButtonEnabled(True)
        self.lin_admin_password.setObjectName("lin_admin_password")
        self.but_confirm_data = QtWidgets.QPushButton(self.frame_4)
        self.but_confirm_data.setGeometry(QtCore.QRect(130, 210, 61, 51))
        self.but_confirm_data.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/confirm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_confirm_data.setIcon(icon1)
        self.but_confirm_data.setIconSize(QtCore.QSize(50, 50))
        self.but_confirm_data.setObjectName("but_confirm_data")
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        self.label_11.setGeometry(QtCore.QRect(140, 260, 41, 31))
        self.label_11.setStyleSheet("QLabel{font-size:19px;}")
        self.label_11.setObjectName("label_11")
        self.lin_OK_Serson = QtWidgets.QLineEdit(self.frame_4)
        self.lin_OK_Serson.setEnabled(True)
        self.lin_OK_Serson.setGeometry(QtCore.QRect(40, 40, 101, 41))
        self.lin_OK_Serson.setStyleSheet("")
        self.lin_OK_Serson.setClearButtonEnabled(True)
        self.lin_OK_Serson.setObjectName("lin_OK_Serson")
        self.lab_okserson = QtWidgets.QLabel(self.frame_4)
        self.lab_okserson.setGeometry(QtCore.QRect(80, 80, 31, 21))
        self.lab_okserson.setObjectName("lab_okserson")
        self.lin_Ng_Serson = QtWidgets.QLineEdit(self.frame_4)
        self.lin_Ng_Serson.setEnabled(True)
        self.lin_Ng_Serson.setGeometry(QtCore.QRect(190, 40, 101, 41))
        self.lin_Ng_Serson.setStyleSheet("")
        self.lin_Ng_Serson.setClearButtonEnabled(True)
        self.lin_Ng_Serson.setObjectName("lin_Ng_Serson")
        self.lab_ngserson = QtWidgets.QLabel(self.frame_4)
        self.lab_ngserson.setGeometry(QtCore.QRect(230, 80, 31, 21))
        self.lab_ngserson.setObjectName("lab_ngserson")
        self.lin_Thing_barcode = QtWidgets.QLineEdit(self.frame_4)
        self.lin_Thing_barcode.setGeometry(QtCore.QRect(70, 120, 191, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lin_Thing_barcode.setFont(font)
        self.lin_Thing_barcode.setTabletTracking(False)
        self.lin_Thing_barcode.setStyleSheet("*{\n"
"font-size:15px;\n"
"color:black;\n"
"}")
        self.lin_Thing_barcode.setText("")
        self.lin_Thing_barcode.setDragEnabled(True)
        self.lin_Thing_barcode.setClearButtonEnabled(True)
        self.lin_Thing_barcode.setObjectName("lin_Thing_barcode")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 130, 16, 16))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(900, 20, 281, 151))
        self.frame_5.setStyleSheet("QLabel{background:rgb(255, 255, 127);\n"
"\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.lab_phone = QtWidgets.QLabel(self.frame_5)
        self.lab_phone.setGeometry(QtCore.QRect(140, 100, 131, 41))
        self.lab_phone.setStyleSheet("*{\n"
"font-size:19px;\n"
"border: 2px solid rgb(100, 100, 100);\n"
"}")
        self.lab_phone.setText("")
        self.lab_phone.setObjectName("lab_phone")
        self.lab_worker_name = QtWidgets.QLabel(self.frame_5)
        self.lab_worker_name.setGeometry(QtCore.QRect(140, 0, 131, 41))
        self.lab_worker_name.setStyleSheet("*{\n"
"\n"
"border: 2px solid rgb(100, 100, 100);\n"
"}")
        self.lab_worker_name.setText("")
        self.lab_worker_name.setObjectName("lab_worker_name")
        self.lab_frim = QtWidgets.QLabel(self.frame_5)
        self.lab_frim.setGeometry(QtCore.QRect(140, 50, 131, 41))
        self.lab_frim.setStyleSheet("*{\n"
"\n"
"border: 2px solid rgb(100, 100, 100);\n"
"}")
        self.lab_frim.setText("")
        self.lab_frim.setObjectName("lab_frim")
        self.label_26 = QtWidgets.QLabel(self.frame_5)
        self.label_26.setGeometry(QtCore.QRect(50, 10, 81, 20))
        self.label_26.setStyleSheet("*{background:none;}")
        self.label_26.setObjectName("label_26")
        self.label_15 = QtWidgets.QLabel(self.frame_5)
        self.label_15.setEnabled(True)
        self.label_15.setGeometry(QtCore.QRect(50, 110, 81, 20))
        self.label_15.setStyleSheet("*{background:none;}")
        self.label_15.setObjectName("label_15")
        self.label_25 = QtWidgets.QLabel(self.frame_5)
        self.label_25.setGeometry(QtCore.QRect(90, 60, 41, 21))
        self.label_25.setStyleSheet("*{background:none;}")
        self.label_25.setObjectName("label_25")
        self.Fra_thing_show = QtWidgets.QFrame(self.centralwidget)
        self.Fra_thing_show.setGeometry(QtCore.QRect(900, 170, 301, 261))
        self.Fra_thing_show.setStyleSheet("QLabel{background:rgb(255, 255, 127)/*rgb(72, 72, 73,50%)*/;}\n"
"\n"
"")
        self.Fra_thing_show.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Fra_thing_show.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Fra_thing_show.setObjectName("Fra_thing_show")
        self.lab_wire_name = QtWidgets.QLabel(self.Fra_thing_show)
        self.lab_wire_name.setGeometry(QtCore.QRect(140, 10, 131, 41))
        self.lab_wire_name.setStyleSheet("QLabel\n"
"{\n"
"color:black;\n"
"border: 2px solid rgb(100, 100, 100);\n"
"}")
        self.lab_wire_name.setText("")
        self.lab_wire_name.setObjectName("lab_wire_name")
        self.lab_surplus_num = QtWidgets.QLabel(self.Fra_thing_show)
        self.lab_surplus_num.setGeometry(QtCore.QRect(140, 110, 131, 41))
        self.lab_surplus_num.setStyleSheet("QLabel\n"
"{\n"
"color:red;\n"
"border: 2px solid rgb(100, 100, 100);\n"
"}")
        self.lab_surplus_num.setText("")
        self.lab_surplus_num.setObjectName("lab_surplus_num")
        self.lab_ok_place = QtWidgets.QLabel(self.Fra_thing_show)
        self.lab_ok_place.setGeometry(QtCore.QRect(140, 160, 131, 41))
        self.lab_ok_place.setStyleSheet("QLabel\n"
"{\n"
"color:red;\n"
"border: 2px solid rgb(100, 100, 100);\n"
"}")
        self.lab_ok_place.setText("")
        self.lab_ok_place.setObjectName("lab_ok_place")
        self.lab_ng_place = QtWidgets.QLabel(self.Fra_thing_show)
        self.lab_ng_place.setGeometry(QtCore.QRect(140, 210, 131, 41))
        self.lab_ng_place.setStyleSheet("QLabel\n"
"{\n"
"color:black;\n"
"border: 2px solid rgb(100, 100, 100);\n"
"}")
        self.lab_ng_place.setText("")
        self.lab_ng_place.setObjectName("lab_ng_place")
        self.label_2 = QtWidgets.QLabel(self.Fra_thing_show)
        self.label_2.setGeometry(QtCore.QRect(50, 20, 81, 20))
        self.label_2.setStyleSheet("*{background:none;}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Fra_thing_show)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 81, 20))
        self.label_3.setStyleSheet("*{background:none;}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Fra_thing_show)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 111, 20))
        self.label_4.setStyleSheet("*{background:none;}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.Fra_thing_show)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 111, 20))
        self.label_5.setStyleSheet("*{background:none;}")
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(self.Fra_thing_show)
        self.label_9.setGeometry(QtCore.QRect(50, 70, 81, 20))
        self.label_9.setStyleSheet("*{background:none;}")
        self.label_9.setObjectName("label_9")
        self.lab_Thing_truename = QtWidgets.QLabel(self.Fra_thing_show)
        self.lab_Thing_truename.setGeometry(QtCore.QRect(140, 60, 131, 41))
        self.lab_Thing_truename.setStyleSheet("*{font-size:15px;}\n"
"QLabel\n"
"{\n"
"color:red;\n"
"border: 2px solid rgb(100, 100, 100);\n"
"}")
        self.lab_Thing_truename.setText("")
        self.lab_Thing_truename.setTextFormat(QtCore.Qt.AutoText)
        self.lab_Thing_truename.setObjectName("lab_Thing_truename")
        self.pushButton_2 = QtWidgets.QPushButton(self.Fra_thing_show)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 20, 16, 16))
        self.pushButton_2.setStyleSheet("\n"
"QPushButton{\n"
"    font-size: 14px;/*字体大小*/\n"
"    color:white;/*颜色*/\n"
"    background: none;/*背景颜色*/\n"
"    border-radius:40px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"\n"
"    /*padding-left:3px;左边距*/\n"
"    padding-top:8px;/*上边距*/\n"
"background:rgb(203, 18, 67);\n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.Fra_mac_sys = QtWidgets.QFrame(self.centralwidget)
        self.Fra_mac_sys.setEnabled(True)
        self.Fra_mac_sys.setGeometry(QtCore.QRect(170, 200, 641, 131))
        self.Fra_mac_sys.setStyleSheet("\n"
"\n"
"QComboBox {\n"
"    font-size: 19px;/*字体大小*/\n"
"    color: black; /*内容颜色*/\n"
"    min-height: 24px;    /*最小高度*/\n"
"    min-width: 100px; /*最小宽度*/\n"
"    border: 2px solid rgb(100, 100, 100); /*边框粗细和颜色*/\n"
"    border-radius:8px;\n"
"    background:rgb(72, 72, 73,10%)\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    font-size: 20px;/*字体大小*/\n"
"    color: black;/*颜色*/\n"
"    border: 1px solid rgb(100, 100, 100);/*边框粗细和颜色*/\n"
"    border-radius: 4px;  /*边框的弧度*/\n"
"    background:rgb(128, 128, 128);/*背景颜色*/\n"
"    selection-background-color:rgb(181, 181, 181); /*选取时的背景颜色*/\n"
"    selection-color:rgb(255, 0, 0);/*选中时字体颜色*/\n"
"\n"
"}\n"
"\n"
"QComboBox::drop-down {/*右侧按钮*/\n"
"    width: 20px;/*宽度*/\n"
"    background:  rgb(255, 255, 255,30);/*背景颜色*/\n"
"    border-left-width: 1px;   /*加左边框线（可以不要，下同）*/\n"
"    border-left-style: solid;  /*左边框线类型*/\n"
"    border-left-color: gray;  /*左边框线颜色*/\n"
"\n"
"}")
        self.Fra_mac_sys.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Fra_mac_sys.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Fra_mac_sys.setObjectName("Fra_mac_sys")
        self.com_systems = QtWidgets.QComboBox(self.Fra_mac_sys)
        self.com_systems.setGeometry(QtCore.QRect(440, 10, 141, 41))
        self.com_systems.setStyleSheet("")
        self.com_systems.setObjectName("com_systems")
        self.lab_systems = QtWidgets.QLabel(self.Fra_mac_sys)
        self.lab_systems.setGeometry(QtCore.QRect(380, 20, 41, 21))
        self.lab_systems.setObjectName("lab_systems")
        self.lab_machine = QtWidgets.QLabel(self.Fra_mac_sys)
        self.lab_machine.setGeometry(QtCore.QRect(20, 80, 41, 21))
        self.lab_machine.setObjectName("lab_machine")
        self.lab_size = QtWidgets.QLabel(self.Fra_mac_sys)
        self.lab_size.setGeometry(QtCore.QRect(20, 20, 41, 21))
        self.lab_size.setObjectName("lab_size")
        self.com_size = QtWidgets.QComboBox(self.Fra_mac_sys)
        self.com_size.setGeometry(QtCore.QRect(100, 10, 141, 41))
        self.com_size.setStyleSheet("")
        self.com_size.setCurrentText("")
        self.com_size.setMaxVisibleItems(20)
        self.com_size.setObjectName("com_size")
        self.com_machine = QtWidgets.QComboBox(self.Fra_mac_sys)
        self.com_machine.setGeometry(QtCore.QRect(100, 70, 191, 41))
        self.com_machine.setMaxVisibleItems(20)
        self.com_machine.setObjectName("com_machine")
        self.lab_wire_info = QtWidgets.QLabel(self.centralwidget)
        self.lab_wire_info.setGeometry(QtCore.QRect(1030, 670, 161, 41))
        self.lab_wire_info.setStyleSheet("*{background:#00000000;}")
        self.lab_wire_info.setObjectName("lab_wire_info")
        self.wire_show_test = QtWidgets.QTextEdit(self.centralwidget)
        self.wire_show_test.setEnabled(True)
        self.wire_show_test.setGeometry(QtCore.QRect(950, 430, 321, 241))
        self.wire_show_test.setStyleSheet("*{background:black;\n"
"    border-radius:40px;\n"
"    background: rgb(255, 255, 127)/*rgb(72, 72, 73, 50%)*/;\n"
"color:red;\n"
"border: 2px solid rgb(100, 100, 100);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.wire_show_test.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.wire_show_test.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.wire_show_test.setTabChangesFocus(False)
        self.wire_show_test.setTabStopWidth(100)
        self.wire_show_test.setObjectName("wire_show_test")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 760, 132, 2))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 45, 31, 31))
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
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/Refresh_24px_1158474_easyicon.net.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")
        self.but_comment = QtWidgets.QPushButton(self.centralwidget)
        self.but_comment.setGeometry(QtCore.QRect(60, 8, 31, 31))
        self.but_comment.setStyleSheet("\n"
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
        self.but_comment.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/comment.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_comment.setIcon(icon3)
        self.but_comment.setIconSize(QtCore.QSize(40, 40))
        self.but_comment.setObjectName("but_comment")
        self.lin_comments = QtWidgets.QLineEdit(self.centralwidget)
        self.lin_comments.setGeometry(QtCore.QRect(450, 340, 331, 41))
        self.lin_comments.setStyleSheet("QLineEdit {\n"
"    font-size: 20px;/*字体大小*/\n"
"    color: black; /*内容颜色*/\n"
"    height: 25px;    /*高度*/\n"
"    border: 2px solid rgb(100, 100, 100); /*边框粗细和颜色*/\n"
"    border-radius: 10px;  /*边框的弧度*/\n"
"    background:rgb(72, 72, 73, 10%); /*背景颜色*/\n"
"\n"
"}")
        self.lin_comments.setText("")
        self.lin_comments.setMaxLength(100)
        self.lin_comments.setPlaceholderText("")
        self.lin_comments.setObjectName("lin_comments")
        self.lab_comment = QtWidgets.QLabel(self.centralwidget)
        self.lab_comment.setGeometry(QtCore.QRect(590, 390, 41, 31))
        self.lab_comment.setObjectName("lab_comment")
        self.but_clear = QtWidgets.QPushButton(self.centralwidget)
        self.but_clear.setGeometry(QtCore.QRect(15, 85, 41, 41))
        self.but_clear.setStyleSheet("\n"
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
        self.but_clear.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_clear.setIcon(icon4)
        self.but_clear.setIconSize(QtCore.QSize(40, 40))
        self.but_clear.setObjectName("but_clear")
        self.lcd_clock = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_clock.setGeometry(QtCore.QRect(-10, 720, 151, 31))
        self.lcd_clock.setLineWidth(9)
        self.lcd_clock.setMidLineWidth(0)
        self.lcd_clock.setSmallDecimalPoint(False)
        self.lcd_clock.setDigitCount(10)
        self.lcd_clock.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcd_clock.setObjectName("lcd_clock")
        self.but_clear_2 = QtWidgets.QPushButton(self.centralwidget)
        self.but_clear_2.setGeometry(QtCore.QRect(10, 0, 41, 41))
        self.but_clear_2.setStyleSheet("\n"
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
        self.but_clear_2.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/retutn.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_clear_2.setIcon(icon5)
        self.but_clear_2.setIconSize(QtCore.QSize(32, 32))
        self.but_clear_2.setObjectName("but_clear_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 45, 31, 31))
        self.pushButton_4.setStyleSheet("\n"
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
        self.pushButton_4.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/pen.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon6)
        self.pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lab_tcp_show = QtWidgets.QPushButton(self.centralwidget)
        self.lab_tcp_show.setGeometry(QtCore.QRect(500, 0, 331, 21))
        self.lab_tcp_show.setStyleSheet("*{\n"
"    font-size: 19px;/*字体大小*/\n"
"    color:red;/*颜色*/\n"
"    background: #00000000;/*背景颜色*/\n"
"    border-radius:40px;\n"
"    \n"
"}")
        self.lab_tcp_show.setText("")
        self.lab_tcp_show.setObjectName("lab_tcp_show")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionk_hkh = QtWidgets.QAction(MainWindow)
        self.actionk_hkh.setObjectName("actionk_hkh")
        self.label_7.setBuddy(self.com_operation)
        self.label_19.setBuddy(self.com_method)
        self.label_27.setBuddy(self.com_lines)
        self.label_37.setBuddy(self.com_Thing_class)
        self.label_10.setBuddy(self.lin_worker_num)
        self.label_12.setBuddy(self.lin_quantiy)
        self.label_8.setBuddy(self.lin_quantiy)
        self.label_11.setBuddy(self.lin_admin_password)
        self.lab_systems.setBuddy(self.com_systems)
        self.lab_size.setBuddy(self.com_Thing_class)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.com_size.setCurrentIndex(-1)
        self.com_operation.activated['int'].connect(MainWindow.change_two)
        self.lin_worker_num.editingFinished.connect(MainWindow.Worker_Showinfo)
        self.com_Thing_class.currentTextChanged['QString'].connect(MainWindow.Set_MACorSYS_See)
        self.but_clear.pressed.connect(MainWindow.Clear_all)
        self.com_lines.activated['QString'].connect(MainWindow.Line_Wire_Change_Maching)
        self.com_systems.currentTextChanged['QString'].connect(MainWindow.Thing_Showinfo)
        self.com_Thing_class.currentTextChanged['QString'].connect(MainWindow.Thing_Showinfo)
        self.pushButton.clicked.connect(MainWindow.Line_Wire_Change_Maching)
        self.pushButton.clicked.connect(MainWindow.power_ff_input_machine)
        self.lin_Thing_barcode.returnPressed.connect(MainWindow.Thing_Showinfo)
        self.lin_admin_password.returnPressed.connect(MainWindow.Confirm_Reslut)
        self.but_confirm_data.pressed.connect(MainWindow.Confirm_Reslut)
        self.com_size.activated['QString'].connect(MainWindow.Line_Wire_Change_Maching)
        self.com_size.activated['QString'].connect(MainWindow.power_ff_input_machine)
        self.com_operation.activated['int'].connect(MainWindow.Set_MACorSYS_See)
        self.com_method.activated['QString'].connect(MainWindow.Set_MACorSYS_See)
        self.com_lines.activated['QString'].connect(MainWindow.Set_MACorSYS_See)
        self.com_machine.activated['int'].connect(MainWindow.Thing_Showinfo)
        self.lin_OK_Serson.returnPressed.connect(MainWindow.Serson_is_use)
        self.but_comment.clicked.connect(MainWindow.Set_Comment_see)
        self.pushButton_2.clicked.connect(MainWindow.Set_Thing_Barcode_Me)
        self.com_Thing_class.activated['int'].connect(MainWindow.Line_Wire_Change_Maching)
        self.com_Thing_class.activated['int'].connect(MainWindow.power_ff_input_machine)
        self.pushButton_3.clicked.connect(MainWindow.shutcut)
        self.but_clear_2.clicked.connect(MainWindow.return_mainwindow)
        self.lin_quantiy.editingFinished.connect(MainWindow.Check_Thing_Num)
        self.pushButton_4.clicked.connect(MainWindow.rewrite)
        self.pushButton_5.clicked.connect(MainWindow.put_in_show_function)
        self.com_Thing_class.currentIndexChanged['QString'].connect(MainWindow.change_two)
        self.lin_Ng_Serson.returnPressed.connect(MainWindow.set_focus)
        self.lab_tcp_show.clicked.connect(MainWindow.reset_function)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.com_Thing_class, self.com_method)
        MainWindow.setTabOrder(self.com_method, self.lin_Ng_Serson)
        MainWindow.setTabOrder(self.lin_Ng_Serson, self.lin_comments)
        MainWindow.setTabOrder(self.lin_comments, self.but_confirm_data)
        MainWindow.setTabOrder(self.but_confirm_data, self.lin_worker_num)
        MainWindow.setTabOrder(self.lin_worker_num, self.lin_Thing_barcode)
        MainWindow.setTabOrder(self.lin_Thing_barcode, self.lin_admin_password)
        MainWindow.setTabOrder(self.lin_admin_password, self.com_lines)
        MainWindow.setTabOrder(self.com_lines, self.com_operation)
        MainWindow.setTabOrder(self.com_operation, self.com_systems)
        MainWindow.setTabOrder(self.com_systems, self.lin_quantiy)
        MainWindow.setTabOrder(self.lin_quantiy, self.com_size)
        MainWindow.setTabOrder(self.com_size, self.wire_show_test)
        MainWindow.setTabOrder(self.wire_show_test, self.lin_OK_Serson)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "物品登記"))
        self.label_7.setText(_translate("MainWindow", "操作类型"))
        self.com_operation.setItemText(1, _translate("MainWindow", "入庫"))
        self.com_operation.setItemText(2, _translate("MainWindow", "出庫"))
        self.com_operation.setItemText(3, _translate("MainWindow", "NG品更換"))
        self.label_19.setText(_translate("MainWindow", "操作方式"))
        self.label_27.setText(_translate("MainWindow", "使用线别"))
        self.label_37.setText(_translate("MainWindow", "物品种类"))
        self.label_10.setText(_translate("MainWindow", "领用工号"))
        self.label_12.setText(_translate("MainWindow", "物品数量"))
        self.label_8.setText(_translate("MainWindow", "物品数量"))
        self.lin_admin_password.setPlaceholderText(_translate("MainWindow", "                     密码"))
        self.label_11.setText(_translate("MainWindow", "确认"))
        self.lab_okserson.setText(_translate("MainWindow", "OK"))
        self.lab_ngserson.setText(_translate("MainWindow", "NG"))
        self.lin_Thing_barcode.setPlaceholderText(_translate("MainWindow", "                 条形码"))
        self.pushButton_3.setShortcut(_translate("MainWindow", "Esc"))
        self.label_26.setText(_translate("MainWindow", "领用姓名"))
        self.label_15.setText(_translate("MainWindow", "联系方式"))
        self.label_25.setText(_translate("MainWindow", "课别"))
        self.label_2.setText(_translate("MainWindow", "物品种类"))
        self.label_3.setText(_translate("MainWindow", "库存数量"))
        self.label_4.setText(_translate("MainWindow", "OK存放位置"))
        self.label_5.setText(_translate("MainWindow", "NG存放位置"))
        self.label_9.setText(_translate("MainWindow", "物品全称"))
        self.lab_systems.setText(_translate("MainWindow", "电脑"))
        self.lab_machine.setText(_translate("MainWindow", "机种"))
        self.lab_size.setText(_translate("MainWindow", "尺寸"))
        self.lab_wire_info.setText(_translate("MainWindow", "人员选择线材信息"))
        self.wire_show_test.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setToolTip(_translate("MainWindow", "刷新"))
        self.but_comment.setToolTip(_translate("MainWindow", "备注信息"))
        self.lab_comment.setText(_translate("MainWindow", "备注"))
        self.but_clear.setToolTip(_translate("MainWindow", "清除"))
        self.but_clear_2.setToolTip(_translate("MainWindow", "清除"))
        self.actionk_hkh.setText(_translate("MainWindow", "k,hkh"))

import wire_images_rc
