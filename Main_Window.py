# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\20190822\MainWindow.ui'
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
        icon.addPixmap(QtGui.QPixmap(":/images/77.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget{\n"
"\n"
"    \n"
"    background: rgb(139, 197, 255);\n"
"\n"
"}\n"
"\n"
"/**********子界面背景**********/\n"
"QWidget#customWidget {\n"
"        background: rgb(173, 202, 232);\n"
"}\n"
"\n"
"/**********子界面中央背景**********/\n"
"QWidget#centerWidget {\n"
"        background: rgb(232, 241, 252);\n"
"}\n"
"\n"
"/**********主界面样式**********/\n"
"QWidget#mainWindow {\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: rgb(232, 241, 252);\n"
"}\n"
"\n"
"QWidget#messageWidget {\n"
"        background: rgba(173, 202, 232, 50%);\n"
"}\n"
"\n"
"QWidget#loadingWidget {\n"
"        border: none;\n"
"        border-radius: 5px;\n"
"        background: rgb(187, 212, 238);\n"
"}\n"
"\n"
"QWidget#remoteWidget {\n"
"        border-top-right-radius: 10px;\n"
"        border-bottom-right-radius: 10px;\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        border-left: none;\n"
"        background: transparent;\n"
"}\n"
"\n"
"StyledWidget {\n"
"        qproperty-normalColor: rgb(65, 65, 65);\n"
"        qproperty-disableColor: rgb(180, 180, 180);\n"
"        qproperty-highlightColor: rgb(0, 160, 230);\n"
"        qproperty-errorColor: red;\n"
"}\n"
"\n"
"QProgressIndicator {\n"
"        qproperty-color: rgb(2, 65, 132);\n"
"}\n"
"\n"
"/**********提示**********/\n"
"QToolTip{\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: white;\n"
"        color: rgb(51, 51, 51);\n"
"}\n"
"\n"
"/**********菜单栏**********/\n"
"QMenuBar {\n"
"        background: rgb(187, 212, 238);\n"
"        /*border: 1px solid rgb(111, 156, 207);*/\n"
"        border-left: none;\n"
"        border-right: none;\n"
"        border-bottom:1px solid rgb(111, 156, 207);\n"
"}\n"
"QMenuBar::item {\n"
"        border: 1px solid transparent;\n"
"        padding: 5px 10px 5px 10px;\n"
"        background: transparent;\n"
"}\n"
"QMenuBar::item:enabled {\n"
"        color: rgb(2, 65, 132);\n"
"}\n"
"QMenuBar::item:!enabled {\n"
"        color: rgb(155, 155, 155);\n"
"}\n"
"QMenuBar::item:enabled:selected {\n"
"        border-top-color: rgb(111, 156, 207);\n"
"        border-bottom-color: rgb(111, 156, 207);\n"
"        background: rgb(198, 224, 252);\n"
"}\n"
"\n"
"/**********菜单**********/\n"
"QMenu {\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: rgb(232, 241, 250);\n"
"}\n"
"QMenu::item {\n"
"        height: 22px;\n"
"        padding: 0px 25px 0px 20px;\n"
"}\n"
"QMenu::item:enabled {\n"
"        color: rgb(84, 84, 84);\n"
"}\n"
"QMenu::item:!enabled {\n"
"        color: rgb(155, 155, 155);\n"
"}\n"
"QMenu::item:enabled:selected {\n"
"        color: rgb(2, 65, 132);\n"
"        background: rgba(255, 255, 255, 200);\n"
"}\n"
"QMenu::separator {\n"
"        height: 1px;\n"
"        background: rgb(111, 156, 207);\n"
"}\n"
"QMenu::indicator {\n"
"        width: 13px;\n"
"        height: 13px;\n"
"}\n"
"QMenu::icon {\n"
"        padding-left: 2px;\n"
"        padding-right: 2px;\n"
"}\n"
"\n"
"/**********状态栏**********/\n"
"\n"
"\n"
"/**********分组框**********/\n"
"QGroupBox {\n"
"        font-size: 15px;\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        border-radius: 4px;\n"
"        margin-top: 10px;\n"
"}\n"
"QGroupBox::title {\n"
"        color: rgb(56, 99, 154);\n"
"        top: -12px;\n"
"        left: 10px;\n"
"}\n"
"\n"
"/**********页签项**********/\n"
"QTabWidget::pane {\n"
"        border: none;\n"
"        border-top: 6px solid rgb(0, 78, 161);\n"
"        background: rgb(187, 212, 238);\n"
"}\n"
"QTabWidget::tab-bar {\n"
"        border: none;\n"
"}\n"
"QTabBar::tab {\n"
"        border: none;\n"
"        border-top-left-radius: 4px;\n"
"        border-top-right-radius: 4px;\n"
"        color: white;\n"
"        background: #00000000;\n"
"        height: 28px;\n"
"        min-width: 85px;\n"
"        margin-right: 5px;\n"
"        padding-left: 5px;\n"
"        padding-right: 5px;\n"
"}\n"
"QTabBar::tab:hover {\n"
"        background: #00000000;\n"
"}\n"
"QTabBar::tab:selected {\n"
"        color: white;\n"
"        background: #00000000;\n"
"}\n"
"\n"
"QTabWidget#tabWidget::pane {\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: rgb(232, 241, 252);\n"
"        \n"
"}\n"
"\n"
"QTabBar#tabBar::tab {\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        border-bottom: none;\n"
"        color: rgb(70, 71, 73);\n"
"        background: transparent;\n"
"}\n"
"QTabBar#tabBar::tab:hover {\n"
"        color: rgb(2, 65, 132);\n"
"}\n"
"QTabBar#tabBar::tab:selected {\n"
"        color: rgb(2, 65, 132);\n"
"        background: rgb(232, 241, 252);\n"
"}\n"
"\n"
"/**********表头**********/\n"
"QHeaderView{\n"
"        border: none;\n"
"        border-bottom: 2px solid rgb(100, 160, 220);\n"
"        background: transparent;\n"
"        min-height: 30px;\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"        border: none;\n"
"        color: rgb(2, 65, 132);\n"
"        background: transparent;\n"
"        padding-left: 5px;\n"
"}\n"
"QHeaderView::section:horizontal:hover {\n"
"        color: white;\n"
"        background: rgb(0, 78, 161);\n"
"}\n"
"QHeaderView::section:horizontal:pressed {\n"
"        color: white;\n"
"        background: rgb(6, 94, 187);\n"
"}\n"
"QHeaderView::up-arrow {\n"
"        width: 13px;\n"
"        height: 11px;\n"
"        padding-right: 5px;\n"
"        image: url(:/White/topArrow);\n"
"        subcontrol-position: center right;\n"
"}\n"
"\n"
"\n"
"QHeaderView::down-arrow {\n"
"        width: 13px;\n"
"        height: 11px;\n"
"        padding-right: 5px;\n"
"        image: url(:/White/bottomArrow);\n"
"        subcontrol-position: center right;\n"
"}\n"
"\n"
"\n"
"\n"
"/**********表格**********/\n"
"QTableView {\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: rgb(224, 238, 255);\n"
"        gridline-color: rgb(111, 156, 207);\n"
"}\n"
"QTableView::item {\n"
"        padding-left: 5px;\n"
"        padding-right:5px;\n"
"        border: none;\n"
"        background: white;\n"
"        border-right: 1px solid rgb(111, 156, 207);\n"
"        border-bottom: 1px solid rgb(111, 156, 207);\n"
"}\n"
"QTableView::item:selected {\n"
"        background: rgb(100, 160, 220);\n"
"}\n"
"QTableView::item:selected:!active {\n"
"        color: rgb(65, 65, 65);\n"
"}\n"
"QTableView::indicator {\n"
"        width: 20px;\n"
"        height: 20px;\n"
"}\n"
"\n"
"\n"
"/**********滚动条-水平**********/\n"
"QScrollBar:horizontal {\n"
"        height: 20px;\n"
"        background: transparent;\n"
"        margin-top: 3px;\n"
"        margin-bottom: 3px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"        height: 20px;\n"
"        min-width: 30px;\n"
"        background: rgb(170, 200, 230);\n"
"        margin-left: 15px;\n"
"        margin-right: 15px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"        background: rgb(165, 195, 225);\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"        width: 15px;\n"
"        background: transparent;\n"
"        image: url(:/White/arrowLeft);\n"
"        subcontrol-position: left;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"        width: 15px;\n"
"        background: transparent;\n"
"        image: url(:/White/arrowRight);\n"
"        subcontrol-position: right;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"        background: rgb(170, 200, 230);\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {\n"
"        background: rgb(170, 200, 230);\n"
"}\n"
"QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal {\n"
"        background: transparent;\n"
"}\n"
"\n"
"/**********滚动条-垂直**********/\n"
"QScrollBar:vertical {\n"
"        width: 20px;\n"
"        background: transparent;\n"
"        margin-left: 3px;\n"
"        margin-right: 3px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"        width: 20px;\n"
"        min-height: 30px;\n"
"        background: rgb(165, 195, 225);\n"
"        margin-top: 15px;\n"
"        margin-bottom: 15px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"        background: rgb(165, 195, 225);\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"        height: 15px;\n"
"        background: transparent;\n"
"        image: url(:/White/topArrow);\n"
"        subcontrol-position: top;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"        height: 15px;\n"
"        background: transparent;\n"
"        image: url(:/White/bottomArrow);\n"
"        subcontrol-position: bottom;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {\n"
"        background: rgb(170, 200, 230);\n"
"}\n"
"QScrollBar::add-line:vertical:hover {\n"
"        background: rgb(170, 200, 230);\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"        background: transparent;\n"
"}\n"
"\n"
"QScrollBar#verticalScrollBar:vertical {\n"
"        margin-top: 30px;\n"
"}\n"
"\n"
"/**********下拉列表**********/\n"
"QComboBox {\n"
"        height: 25px;\n"
"        border-radius: 4px;\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: white;\n"
"}\n"
"QComboBox:enabled {\n"
"        color: rgb(84, 84, 84);\n"
"}\n"
"QComboBox:!enabled {\n"
"        color: rgb(80, 80, 80);\n"
"}\n"
"QComboBox:enabled:hover, QComboBox:enabled:focus {\n"
"        color: rgb(51, 51, 51);\n"
"}\n"
"QComboBox::drop-down {\n"
"        width: 20px;\n"
"        border: none;\n"
"        background: transparent;\n"
"}\n"
"QComboBox::drop-down:hover {\n"
"        background: rgba(255, 255, 255, 30);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: white;\n"
"        outline: none;\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"        height: 25px;\n"
"        color: rgb(73, 73, 73);\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"        background: rgb(232, 241, 250);\n"
"        color: rgb(2, 65, 132);\n"
"}\n"
"\n"
"/**********进度条**********/\n"
"QProgressBar{\n"
"        border: none;\n"
"        text-align: center;\n"
"        color: white;\n"
"        background: rgb(173, 202, 232);\n"
"}\n"
"QProgressBar::chunk {\n"
"        background: rgb(16, 135, 209);\n"
"}\n"
"\n"
"QProgressBar#progressBar {\n"
"        border: none;\n"
"        text-align: center;\n"
"        color: white;\n"
"        background-color: transparent;\n"
"        background-image: url(\":/White/progressBar\");\n"
"        background-repeat: repeat-x;\n"
"}\n"
"QProgressBar#progressBar::chunk {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        background-image: url(\":/White/progressBarChunk\");\n"
"        background-repeat: repeat-x;\n"
"}\n"
"\n"
"/**********复选框**********/\n"
"QCheckBox{\n"
"        spacing: 5px;\n"
"}\n"
"QCheckBox:enabled:checked{\n"
"        color: rgb(2, 65, 132);\n"
"}\n"
"QCheckBox:enabled:!checked{\n"
"        color: rgb(70, 71, 73);\n"
"}\n"
"QCheckBox:enabled:hover{\n"
"        color: rgb(0, 78, 161);\n"
"}\n"
"QCheckBox:!enabled{\n"
"        color: rgb(80, 80, 80);\n"
"}\n"
"QCheckBox::indicator {\n"
"        width: 20px;\n"
"        height: 20px;\n"
"}\n"
"\n"
"\n"
"\n"
"/**********单选框**********/\n"
"QRadioButton{\n"
"        spacing: 5px;\n"
"}\n"
"QRadioButton:enabled:checked{\n"
"        color: rgb(2, 65, 132);\n"
"}\n"
"QRadioButton:enabled:!checked{\n"
"        color: rgb(70, 71, 73);\n"
"}\n"
"QRadioButton:enabled:hover{\n"
"        color: rgb(0, 78, 161);\n"
"}\n"
"QRadioButton:!enabled{\n"
"        color: rgb(80, 80, 80);\n"
"}\n"
"QRadioButton::indicator {\n"
"        width: 20px;\n"
"        height: 20px;\n"
"}\n"
"\n"
"\n"
"/**********输入框**********/\n"
"QLineEdit {\n"
"        border-radius: 4px;\n"
"        height: 25px;\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: white;\n"
"}\n"
"QLineEdit:enabled {\n"
"        color: rgb(84, 84, 84);\n"
"}\n"
"QLineEdit:enabled:hover, QLineEdit:enabled:focus {\n"
"        color: rgb(51, 51, 51);\n"
"}\n"
"QLineEdit:!enabled {\n"
"        color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"/**********文本编辑框**********/\n"
"QTextEdit {\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        color: rgb(70, 71, 73);\n"
"        background: rgb(187, 212, 238);\n"
"}\n"
"\n"
"/**********滚动区域**********/\n"
"QScrollArea {\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: rgb(187, 212, 238);\n"
"}\n"
"\n"
"/**********滚动区域**********/\n"
"QWidget#transparentWidget {\n"
"        background: transparent;\n"
"}\n"
"\n"
"/**********微调器**********/\n"
"QSpinBox {\n"
"        border-radius: 4px;\n"
"        height: 24px;\n"
"        min-width: 40px;\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: white;\n"
"}\n"
"QSpinBox:enabled {\n"
"        color: rgb(60, 60, 60);\n"
"}\n"
"QSpinBox:enabled:hover, QSpinBox:enabled:focus {\n"
"        color: rgb(51, 51, 51);\n"
"}\n"
"QSpinBox:!enabled {\n"
"        color: rgb(210, 210, 210);\n"
"        background: transparent;\n"
"}\n"
"QSpinBox::up-button {\n"
"        border-left: 1px solid rgb(111, 156, 207);\n"
"        width: 18px;\n"
"        height: 12px;\n"
"        border-top-right-radius: 4px;\n"
"        image: url(:/White/upButton);\n"
"}\n"
"QSpinBox::up-button:!enabled {\n"
"        background: transparent;\n"
"}\n"
"QSpinBox::up-button:enabled:hover {\n"
"        background: rgb(255, 255, 255, 30);\n"
"}\n"
"QSpinBox::down-button {\n"
"        border-left: 1px solid rgb(111, 156, 207);\n"
"        width: 18px;\n"
"        height: 12px;\n"
"        border-bottom-right-radius: 4px;\n"
"        image: url(:/White/downButton);\n"
"}\n"
"QSpinBox::down-button:!enabled {\n"
"        background: transparent;\n"
"}\n"
"QSpinBox::down-button:hover {\n"
"        background: rgb(255, 255, 255, 30);\n"
"}\n"
"\n"
"/**********标签**********/\n"
"QLabel#grayLabel {\n"
"        color: rgb(70, 71, 73);\n"
"}\n"
"\n"
"QLabel#highlightLabel {\n"
"        color: rgb(2, 65, 132);\n"
"}\n"
"\n"
"QLabel#redLabel {\n"
"        color: red;\n"
"}\n"
"\n"
"QLabel#grayYaHeiLabel {\n"
"        color: rgb(175, 175, 175);\n"
"        font-size: 16px;\n"
"}\n"
"\n"
"QLabel#blueLabel {\n"
"        color: rgb(0, 160, 230);\n"
"}\n"
"\n"
"QLabel#listLabel {\n"
"        color: rgb(51, 51, 51);\n"
"}\n"
"\n"
"QLabel#lineBlueLabel {\n"
"        background: rgb(0, 78, 161);\n"
"}\n"
"\n"
"QLabel#graySeperateLabel {\n"
"        background: rgb(200, 220, 230);\n"
"}\n"
"\n"
"QLabel#seperateLabel {\n"
"        background: rgb(112, 153, 194);\n"
"}\n"
"\n"
"QLabel#radiusBlueLabel {\n"
"        border-radius: 15px;\n"
"        color: white;\n"
"        font-size: 16px;\n"
"        background: rgb(0, 78, 161);\n"
"}\n"
"\n"
"QLabel#skinLabel[colorProperty=\"normal\"] {\n"
"        color: rgb(56, 99, 154);\n"
"}\n"
"QLabel#skinLabel[colorProperty=\"highlight\"] {\n"
"        color: rgb(0, 160, 230);\n"
"}\n"
"\n"
"QLabel#informationLabel {\n"
"        qproperty-pixmap: url(:/White/information);\n"
"}\n"
"\n"
"QLabel#errorLabel {\n"
"        qproperty-pixmap: url(:/White/error);\n"
"}\n"
"\n"
"QLabel#successLabel {\n"
"        qproperty-pixmap: url(:/White/success);\n"
"}\n"
"\n"
"QLabel#questionLabel {\n"
"        qproperty-pixmap: url(:/White/question);\n"
"}\n"
"\n"
"QLabel#warningLabel {\n"
"        qproperty-pixmap: url(:/White/warning);\n"
"}\n"
"\n"
"QLabel#groupLabel {\n"
"        color: rgb(56, 99, 154);\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        font-size: 15px;\n"
"        border-top-color: transparent;\n"
"        border-right-color: transparent;\n"
"        border-left-color: transparent;\n"
"}\n"
"\n"
"/**********按钮**********/\n"
"QToolButton#nsccButton {\n"
"        border: none;\n"
"        color: rgb(2, 65, 132);\n"
"        background: transparent;\n"
"        padding: 10px;\n"
"        qproperty-icon: url(:/White/nscc);\n"
"        qproperty-iconSize: 32px 32px;\n"
"        qproperty-toolButtonStyle: ToolButtonTextUnderIcon;\n"
"}\n"
"QToolButton#nsccButton:hover {\n"
"        background: rgb(187, 212, 238);\n"
"}\n"
"\n"
"QToolButton#transferButton {\n"
"        border: none;\n"
"        color: rgb(2, 65, 132);\n"
"        background: transparent;\n"
"        padding: 10px;\n"
"        qproperty-icon: url(:/White/transfer);\n"
"        qproperty-iconSize: 32px 32px;\n"
"        qproperty-toolButtonStyle: ToolButtonTextUnderIcon;\n"
"}\n"
"QToolButton#transferButton:hover {\n"
"        background: rgb(187, 212, 238);\n"
"}\n"
"\n"
"/**********按钮**********/\n"
"QPushButton{\n"
"        border-radius: 4px;\n"
"        border: none;\n"
"        width: 75px;\n"
"        height: 25px;\n"
"        \n"
"    font: 75 9pt \"System\";\n"
"}\n"
"QPushButton:enabled {\n"
"        background: rgb(120, 170, 220);\n"
"        color: white;\n"
"}\n"
"QPushButton:!enabled {\n"
"        background: rgb(180, 180, 180);\n"
"        color: white;\n"
"}\n"
"QPushButton:enabled:hover{\n"
"        background: rgb(100, 160, 220);\n"
"}\n"
"QPushButton:enabled:pressed{\n"
"        background: rgb(0, 78, 161);\n"
"}\n"
"\n"
"QPushButton#blueButton {\n"
"        color: white;\n"
"}\n"
"QPushButton#blueButton:enabled {\n"
"        background: rgb(0, 78, 161);\n"
"        color: white;\n"
"}\n"
"QPushButton:!enabled {\n"
"        background: rgb(180, 180, 180);\n"
"        color: white;\n"
"}\n"
"QPushButton#blueButton:enabled:hover {\n"
"        background: rgb(2, 65, 132);\n"
"}\n"
"QPushButton#blueButton:enabled:pressed {\n"
"        background: rgb(6, 94, 187);\n"
"}\n"
"\n"
"QPushButton#selectButton {\n"
"        border: none;\n"
"        border-radius: none;\n"
"        border-left: 1px solid rgb(111, 156, 207);\n"
"        background: transparent;\n"
"        image: url(:/White/scan);\n"
"        color: rgb(51, 51, 51);\n"
"}\n"
"QPushButton#selectButton:enabled:hover{\n"
"        background: rgb(187, 212, 238);\n"
"}\n"
"QPushButton#selectButton:enabled:pressed{\n"
"        background: rgb(120, 170, 220);\n"
"}\n"
"\n"
"QPushButton#linkButton {\n"
"        background: transparent;\n"
"        color: rgb(0, 160, 230);\n"
"        text-align:left;\n"
"}\n"
"QPushButton#linkButton:hover {\n"
"        color: rgb(20, 185, 255);\n"
"        text-decoration: underline;\n"
"}\n"
"QPushButton#linkButton:pressed {\n"
"        color: rgb(0, 160, 230);\n"
"}\n"
"\n"
"QPushButton#transparentButton {\n"
"        background: transparent;\n"
"}\n"
"\n"
"/*****************标题栏按钮*******************/\n"
"QPushButton#minimizeButton {\n"
"        border-radius: none;\n"
"        border-bottom-left-radius: 4px;\n"
"        border-bottom-right-radius: 4px;\n"
"        background: rgb(120, 170, 220);\n"
"        image: url(:/White/minimizeHover);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton#maximizeButton[maximizeProperty=\"restore\"] {\n"
"        border-radius: none;\n"
"        border-bottom-left-radius: 4px;\n"
"        border-bottom-right-radius: 4px;\n"
"        background: rgb(120, 170, 220);\n"
"        image: url(:/White/restoreHover);\n"
"}\n"
"QPushButton#maximizeButton[maximizeProperty=\"restore\"]:hover {\n"
"        image: url(:/White/restore);\n"
"}\n"
"QPushButton#maximizeButton[maximizeProperty=\"restore\"]:pressed {\n"
"        image: url(:/White/restorePressed);\n"
"}\n"
"\n"
"QPushButton#closeButton {\n"
"        border-radius: none;\n"
"        border-bottom-left-radius: 4px;\n"
"        border-bottom-right-radius: 4px;\n"
"        background: rgb(120, 170, 220);\n"
"        image: url(:/White/closeHover);\n"
"}\n"
"QPushButton#closeButton:hover {\n"
"        image: url(:/White/close);\n"
"}\n"
"QPushButton#closeButton:pressed {\n"
"        image: url(:/White/closePressed);\n"
"}\n"
"\n"
"QPushButton#skinButton {\n"
"        border-radius: none;\n"
"        border-bottom-left-radius: 4px;\n"
"        border-bottom-right-radius: 4px;\n"
"        background: rgb(120, 170, 220);\n"
"        image: url(:/White/skinHover);\n"
"}\n"
"QPushButton#skinButton:hover {\n"
"        image: url(:/White/skin);\n"
"}\n"
"QPushButton#skinButton:pressed {\n"
"        image: url(:/White/skinPressed);\n"
"}\n"
"\n"
"QPushButton#feedbackButton {\n"
"        border-radius: none;\n"
"        border-bottom-left-radius: 4px;\n"
"        border-bottom-right-radius: 4px;\n"
"        background: rgb(120, 170, 220);\n"
"        image: url(:/White/feedbackHover);\n"
"}\n"
"QPushButton#feedbackButton:hover {\n"
"        image: url(:/White/feedback);\n"
"}\n"
"QPushButton#feedbackButton:pressed {\n"
"        image: url(:/White/feedbackPressed);\n"
"}\n"
"\n"
"QPushButton#closeTipButton {\n"
"        border-radius: none;\n"
"        border-image: url(:/White/close);\n"
"        background: transparent;\n"
"}\n"
"\n"
"\n"
"QPushButton#changeSkinButton{\n"
"        border-radius: 4px;\n"
"        border: 2px solid rgb(111, 156, 207);\n"
"        background: rgb(204, 227, 252);\n"
"}\n"
"QPushButton#changeSkinButton:hover{\n"
"        border-color: rgb(60, 150, 200);\n"
"}\n"
"QPushButton#changeSkinButton:pressed, QPushButton#changeSkinButton:checked{\n"
"        border-color: rgb(0, 160, 230);\n"
"}\n"
"\n"
"QPushButton#transferButton {\n"
"        padding-left: 5px;\n"
"        padding-right: 5px;\n"
"        color: white;\n"
"        background: rgb(0, 78, 161);\n"
"}\n"
"QPushButton#transferButton:hover {\n"
"        background: rgb(2, 65, 132);\n"
"}\n"
"QPushButton#transferButton:pressed {\n"
"        background: rgb(6, 94, 187);\n"
"}\n"
"\n"
"\n"
"QPushButton#openButton {\n"
"        border-radius: none;\n"
"        background: transparent;\n"
"}\n"
"QPushButton#openButton:hover {\n"
"        image: url(:/White/openHover);\n"
"}\n"
"QPushButton#openButton:pressed {\n"
"        image: url(:/White/openPressed);\n"
"}\n"
"\n"
"QPushButton#deleteButton {\n"
"        border-radius: none;\n"
"        image: url(:/White/delete);\n"
"        background: transparent;\n"
"}\n"
"QPushButton#deleteButton:hover {\n"
"        image: url(:/White/deleteHover);\n"
"}\n"
"QPushButton#deleteButton:pressed {\n"
"        image: url(:/White/deletePressed);\n"
"}\n"
"\n"
"QPushButton#menuButton {\n"
"        text-align: left center;\n"
"        padding-left: 3px;\n"
"        color: rgb(84, 84, 84);\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: white;\n"
"}\n"
"QPushButton#menuButton::menu-indicator{\n"
"        subcontrol-position: right center;\n"
"        subcontrol-origin: padding;\n"
"        image: url(:/White/arrowBottom);\n"
"        padding-right: 3px;\n"
"}\n"
"\n"
"\n"
"/*QTableView 左上角样式*/\n"
"QTableView QTableCornerButton::section {\n"
"    color: white;/*文字颜色*/\n"
"    background-color: rgba(255, 255, 255, 100);/*背景色*/\n"
"    border: 5px solid rgba(255, 255, 255, 100);/*边框*/\n"
"    border-radius:0px;/*边框圆角*/\n"
"    border-color: rgba(255, 255, 255, 100);/*边框颜色*/\n"
"    font: bold 11pt;/*字体大小*/\n"
"    padding:12px 0 0 10px;/*内边距*/\n"
" }\n"
"QHeaderView::section{background:rgba(255, 255, 255, 100);}\n"
"\n"
"\n"
"QComboBox::drop-down {/*右侧按钮*/\n"
"    width: 20px;/*宽度*/\n"
"    background:  rgb(255, 255, 255,30);/*背景颜色*/\n"
"\n"
"    border-left-width: 1px;   /*加左边框线（可以不要，下同）*/\n"
"    border-left-style: solid;  /*左边框线类型*/\n"
"    border-left-color: gray;  /*左边框线颜色*/\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QTabBar::tab:hover {\n"
"        background: rgb(255, 255, 255, 40);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"        color: white;\n"
"        background: #00000000;\n"
"}\n"
"\n"
"/*这是Qtabwidget的borderr的显示*/\n"
"QTabWidget#tabWidget::pane {\n"
"        border: 0px solid rgb(45, 45, 45);\n"
"\n"
"        margin-top: 1px;\n"
"}\n"
"\n"
"QTabBar#tabBar::tab {\n"
"        border: 1px solid rgb(45, 45, 45);\n"
"        border-bottom: none;\n"
"        background: transparent;\n"
"}\n"
"\n"
"QTabBar#tabBar::tab:hover {\n"
"        color: black;\n"
"}\n"
"QTabBar#tabBar::tab:selected {\n"
"        color: black;\n"
"        background: rgb(57, 58, 60);\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane {\n"
"        border: none;\n"
"        border-top: 0px solid rgb(0, 160, 230);\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"        border: none;\n"
"}\n"
"\n"
"/*这是一个导航栏的QSS*/\n"
"QToolBox {\n"
"    background:rgb(120, 170, 220);\n"
"    border:0px solid rgb(120, 170, 220);\n"
"    border-radius:12px;\n"
"}\n"
" \n"
"QToolBox::tab {\n"
"    background:rgb(100, 170, 220);\n"
"    border-radius:8px;\n"
"    font:95 12pt \"微軟正黑體\";\n"
"    color:black;\n"
"}\n"
" \n"
"/* 被选中的标签 */\n"
"QToolBox::tab:selected {\n"
"    /* 字体加粗,斜体 */\n"
"    \n"
"    font: 15pt \"叶根友毛笔行书2.0版\";\n"
"    color:rgb(129, 107, 255);\n"
"}\n"
"QTextEdit{background:rgb(120, 170, 220);\n"
"    border-radius:5px;\n"
"color:black;\n"
"    font: 75 9pt \"System\";\n"
"}\n"
"")
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        MainWindow.setIconSize(QtCore.QSize(200, 200))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolBox_navigation = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox_navigation.setGeometry(QtCore.QRect(20, 60, 161, 361))
        self.toolBox_navigation.setMinimumSize(QtCore.QSize(161, 0))
        self.toolBox_navigation.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.toolBox_navigation.setStyleSheet("*{border:none;}")
        self.toolBox_navigation.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.toolBox_navigation.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.toolBox_navigation.setLineWidth(1)
        self.toolBox_navigation.setMidLineWidth(1)
        self.toolBox_navigation.setObjectName("toolBox_navigation")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 161, 121))
        self.page.setObjectName("page")
        self.but_eng2_3 = QtWidgets.QPushButton(self.page)
        self.but_eng2_3.setGeometry(QtCore.QRect(-10, 0, 171, 41))
        self.but_eng2_3.setObjectName("but_eng2_3")
        self.but_eng2_4 = QtWidgets.QPushButton(self.page)
        self.but_eng2_4.setGeometry(QtCore.QRect(-10, 40, 171, 41))
        self.but_eng2_4.setObjectName("but_eng2_4")
        self.but_eng2_9 = QtWidgets.QPushButton(self.page)
        self.but_eng2_9.setGeometry(QtCore.QRect(-10, 80, 171, 41))
        self.but_eng2_9.setObjectName("but_eng2_9")
        self.toolBox_navigation.addItem(self.page, "")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 161, 121))
        self.page_5.setObjectName("page_5")
        self.but_eng2_1 = QtWidgets.QPushButton(self.page_5)
        self.but_eng2_1.setGeometry(QtCore.QRect(0, 0, 161, 41))
        self.but_eng2_1.setObjectName("but_eng2_1")
        self.but_eng2_7 = QtWidgets.QPushButton(self.page_5)
        self.but_eng2_7.setGeometry(QtCore.QRect(0, 40, 161, 41))
        self.but_eng2_7.setObjectName("but_eng2_7")
        self.but_eng2_8 = QtWidgets.QPushButton(self.page_5)
        self.but_eng2_8.setGeometry(QtCore.QRect(0, 80, 161, 41))
        self.but_eng2_8.setObjectName("but_eng2_8")
        self.toolBox_navigation.addItem(self.page_5, "")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setGeometry(QtCore.QRect(0, 0, 161, 121))
        self.page_6.setObjectName("page_6")
        self.but_eng2_2 = QtWidgets.QPushButton(self.page_6)
        self.but_eng2_2.setGeometry(QtCore.QRect(-10, 0, 171, 41))
        self.but_eng2_2.setObjectName("but_eng2_2")
        self.but_eng2_5 = QtWidgets.QPushButton(self.page_6)
        self.but_eng2_5.setGeometry(QtCore.QRect(-10, 40, 171, 41))
        self.but_eng2_5.setObjectName("but_eng2_5")
        self.but_eng2_6 = QtWidgets.QPushButton(self.page_6)
        self.but_eng2_6.setGeometry(QtCore.QRect(-10, 80, 171, 51))
        self.but_eng2_6.setObjectName("but_eng2_6")
        self.toolBox_navigation.addItem(self.page_6, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 161, 121))
        self.page_3.setObjectName("page_3")
        self.pushButton_13 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_13.setGeometry(QtCore.QRect(-10, -10, 171, 51))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_14.setGeometry(QtCore.QRect(-10, 40, 171, 51))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_15.setGeometry(QtCore.QRect(-10, 90, 171, 41))
        self.pushButton_15.setObjectName("pushButton_15")
        self.toolBox_navigation.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 161, 121))
        self.page_4.setObjectName("page_4")
        self.pushButton_19 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_19.setGeometry(QtCore.QRect(-10, 0, 171, 41))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_20.setGeometry(QtCore.QRect(-10, 40, 171, 41))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_23 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_23.setGeometry(QtCore.QRect(-10, 80, 171, 41))
        self.pushButton_23.setObjectName("pushButton_23")
        self.toolBox_navigation.addItem(self.page_4, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 161, 121))
        self.page_2.setObjectName("page_2")
        self.pushButton_16 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_16.setGeometry(QtCore.QRect(-10, 0, 171, 41))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_17.setGeometry(QtCore.QRect(-10, 40, 171, 41))
        self.pushButton_17.setObjectName("pushButton_17")
        self.but_check_update = QtWidgets.QPushButton(self.page_2)
        self.but_check_update.setGeometry(QtCore.QRect(-10, 80, 171, 41))
        self.but_check_update.setObjectName("but_check_update")
        self.toolBox_navigation.addItem(self.page_2, "")
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setGeometry(QtCore.QRect(0, 0, 161, 121))
        self.page_7.setObjectName("page_7")
        self.pushButton_33 = QtWidgets.QPushButton(self.page_7)
        self.pushButton_33.setGeometry(QtCore.QRect(-10, 0, 171, 41))
        self.pushButton_33.setStyleSheet("*{color:red;}")
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(self.page_7)
        self.pushButton_34.setGeometry(QtCore.QRect(-10, 40, 171, 41))
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.page_7)
        self.pushButton_35.setGeometry(QtCore.QRect(-10, 80, 171, 41))
        self.pushButton_35.setObjectName("pushButton_35")
        self.toolBox_navigation.addItem(self.page_7, "")
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setGeometry(QtCore.QRect(0, 0, 161, 121))
        self.page_11.setObjectName("page_11")
        self.toolBox_navigation.addItem(self.page_11, "")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(180, 40, 1101, 771))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textEdit = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit.setGeometry(QtCore.QRect(70, 20, 901, 671))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textedit_work_show = QtWidgets.QTextEdit(self.tab_4)
        self.textedit_work_show.setEnabled(True)
        self.textedit_work_show.setGeometry(QtCore.QRect(73, 16, 991, 621))
        self.textedit_work_show.setStyleSheet("*{\n"
"\n"
"    font: 10pt \"STFangsong\";\n"
"}")
        self.textedit_work_show.setObjectName("textedit_work_show")
        self.but_upload = QtWidgets.QPushButton(self.tab_4)
        self.but_upload.setGeometry(QtCore.QRect(390, 650, 93, 51))
        self.but_upload.setStyleSheet("*{color:black;}")
        self.but_upload.setObjectName("but_upload")
        self.but_download = QtWidgets.QPushButton(self.tab_4)
        self.but_download.setGeometry(QtCore.QRect(570, 650, 93, 51))
        self.but_download.setStyleSheet("*{color:black;}")
        self.but_download.setObjectName("but_download")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tab_line = QtWidgets.QTableWidget(self.tab_5)
        self.tab_line.setGeometry(QtCore.QRect(70, 0, 311, 591))
        self.tab_line.setObjectName("tab_line")
        self.tab_line.setColumnCount(2)
        self.tab_line.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tab_line.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tab_line.setHorizontalHeaderItem(1, item)
        self.tab_size = QtWidgets.QTableWidget(self.tab_5)
        self.tab_size.setGeometry(QtCore.QRect(620, 0, 311, 591))
        self.tab_size.setObjectName("tab_size")
        self.tab_size.setColumnCount(2)
        self.tab_size.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tab_size.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tab_size.setHorizontalHeaderItem(1, item)
        self.but_size_confire = QtWidgets.QPushButton(self.tab_5)
        self.but_size_confire.setGeometry(QtCore.QRect(940, 370, 61, 51))
        self.but_size_confire.setObjectName("but_size_confire")
        self.lin_line = QtWidgets.QLineEdit(self.tab_5)
        self.lin_line.setGeometry(QtCore.QRect(400, 160, 113, 41))
        self.lin_line.setObjectName("lin_line")
        self.lin_line_use = QtWidgets.QLineEdit(self.tab_5)
        self.lin_line_use.setGeometry(QtCore.QRect(400, 280, 113, 41))
        self.lin_line_use.setObjectName("lin_line_use")
        self.lin_size_use = QtWidgets.QLineEdit(self.tab_5)
        self.lin_size_use.setGeometry(QtCore.QRect(950, 280, 113, 41))
        self.lin_size_use.setObjectName("lin_size_use")
        self.lin_size = QtWidgets.QLineEdit(self.tab_5)
        self.lin_size.setGeometry(QtCore.QRect(950, 160, 113, 41))
        self.lin_size.setObjectName("lin_size")
        self.label = QtWidgets.QLabel(self.tab_5)
        self.label.setGeometry(QtCore.QRect(440, 200, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_5)
        self.label_2.setGeometry(QtCore.QRect(420, 320, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.tab_5)
        self.label_5.setGeometry(QtCore.QRect(990, 200, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.tab_5)
        self.label_7.setGeometry(QtCore.QRect(970, 320, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.com_line_choice = QtWidgets.QComboBox(self.tab_5)
        self.com_line_choice.setGeometry(QtCore.QRect(400, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.com_line_choice.setFont(font)
        self.com_line_choice.setObjectName("com_line_choice")
        self.com_line_choice.addItem("")
        self.com_line_choice.addItem("")
        self.com_line_choice.addItem("")
        self.com_size_choice = QtWidgets.QComboBox(self.tab_5)
        self.com_size_choice.setGeometry(QtCore.QRect(950, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.com_size_choice.setFont(font)
        self.com_size_choice.setObjectName("com_size_choice")
        self.com_size_choice.addItem("")
        self.com_size_choice.addItem("")
        self.com_size_choice.addItem("")
        self.but_size_confire_2 = QtWidgets.QPushButton(self.tab_5)
        self.but_size_confire_2.setGeometry(QtCore.QRect(1020, 370, 61, 51))
        self.but_size_confire_2.setObjectName("but_size_confire_2")
        self.but_line_confire = QtWidgets.QPushButton(self.tab_5)
        self.but_line_confire.setGeometry(QtCore.QRect(390, 360, 61, 51))
        self.but_line_confire.setObjectName("but_line_confire")
        self.but_size_confire_3 = QtWidgets.QPushButton(self.tab_5)
        self.but_size_confire_3.setGeometry(QtCore.QRect(470, 360, 61, 51))
        self.but_size_confire_3.setObjectName("but_size_confire_3")
        self.tabWidget.addTab(self.tab_5, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(130, 520, 31, 16))
        self.label_11.setObjectName("label_11")
        self.lin_email = QtWidgets.QLineEdit(self.widget)
        self.lin_email.setGeometry(QtCore.QRect(70, 470, 161, 41))
        self.lin_email.setObjectName("lin_email")
        self.lin_bumen_name = QtWidgets.QLineEdit(self.widget)
        self.lin_bumen_name.setGeometry(QtCore.QRect(70, 380, 161, 41))
        self.lin_bumen_name.setObjectName("lin_bumen_name")
        self.lin_card_id = QtWidgets.QLineEdit(self.widget)
        self.lin_card_id.setGeometry(QtCore.QRect(70, 290, 161, 41))
        self.lin_card_id.setObjectName("lin_card_id")
        self.lab_lh_address = QtWidgets.QLabel(self.widget)
        self.lab_lh_address.setGeometry(QtCore.QRect(850, 20, 41, 31))
        self.lab_lh_address.setStyleSheet("")
        self.lab_lh_address.setObjectName("lab_lh_address")
        self.lin_worker_id = QtWidgets.QLineEdit(self.widget)
        self.lin_worker_id.setGeometry(QtCore.QRect(70, 210, 161, 41))
        self.lin_worker_id.setObjectName("lin_worker_id")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 20, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_37 = QtWidgets.QPushButton(self.widget)
        self.pushButton_37.setGeometry(QtCore.QRect(220, 580, 71, 51))
        self.pushButton_37.setObjectName("pushButton_37")
        self.lin_bumen_id = QtWidgets.QLineEdit(self.widget)
        self.lin_bumen_id.setGeometry(QtCore.QRect(280, 380, 161, 41))
        self.lin_bumen_id.setObjectName("lin_bumen_id")
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setGeometry(QtCore.QRect(120, 430, 61, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setGeometry(QtCore.QRect(330, 430, 61, 21))
        self.label_13.setObjectName("label_13")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(140, 250, 31, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton_38 = QtWidgets.QPushButton(self.widget)
        self.pushButton_38.setGeometry(QtCore.QRect(240, 140, 51, 21))
        self.pushButton_38.setObjectName("pushButton_38")
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setGeometry(QtCore.QRect(330, 340, 61, 16))
        self.label_14.setObjectName("label_14")
        self.lin_worker_name = QtWidgets.QLineEdit(self.widget)
        self.lin_worker_name.setGeometry(QtCore.QRect(280, 210, 161, 41))
        self.lin_worker_name.setObjectName("lin_worker_name")
        self.tab_user_all = QtWidgets.QTableWidget(self.widget)
        self.tab_user_all.setEnabled(True)
        self.tab_user_all.setGeometry(QtCore.QRect(510, 60, 561, 641))
        self.tab_user_all.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab_user_all.setObjectName("tab_user_all")
        self.tab_user_all.setColumnCount(8)
        self.tab_user_all.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tab_user_all.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_user_all.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_user_all.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_user_all.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_user_all.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_user_all.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_user_all.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_user_all.setHorizontalHeaderItem(7, item)
        self.lin_phone = QtWidgets.QLineEdit(self.widget)
        self.lin_phone.setGeometry(QtCore.QRect(280, 290, 161, 41))
        self.lin_phone.setObjectName("lin_phone")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(130, 340, 51, 16))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(340, 260, 31, 16))
        self.label_6.setObjectName("label_6")
        self.com_adnim_choice = QtWidgets.QComboBox(self.widget)
        self.com_adnim_choice.setGeometry(QtCore.QRect(210, 80, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.com_adnim_choice.setFont(font)
        self.com_adnim_choice.setObjectName("com_adnim_choice")
        self.com_adnim_choice.addItem("")
        self.com_adnim_choice.addItem("")
        self.com_adnim_choice.addItem("")
        self.tabWidget.addTab(self.widget, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.pushButton = QtWidgets.QPushButton(self.tab_7)
        self.pushButton.setGeometry(QtCore.QRect(360, 170, 421, 241))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.but_lost_seek = QtWidgets.QPushButton(self.tab)
        self.but_lost_seek.setGeometry(QtCore.QRect(690, 20, 191, 91))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/undraw_team_chat_y27k.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_lost_seek.setIcon(icon1)
        self.but_lost_seek.setIconSize(QtCore.QSize(100, 100))
        self.but_lost_seek.setObjectName("but_lost_seek")
        self.but_history = QtWidgets.QPushButton(self.tab)
        self.but_history.setGeometry(QtCore.QRect(30, 140, 191, 181))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/undraw_reading_book_4wjf.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_history.setIcon(icon2)
        self.but_history.setIconSize(QtCore.QSize(100, 100))
        self.but_history.setObjectName("but_history")
        self.but_lend_registe = QtWidgets.QPushButton(self.tab)
        self.but_lend_registe.setGeometry(QtCore.QRect(690, 140, 191, 181))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/undraw_experience_design_eq3j.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_lend_registe.setIcon(icon3)
        self.but_lend_registe.setIconSize(QtCore.QSize(100, 100))
        self.but_lend_registe.setObjectName("but_lend_registe")
        self.but_machine_use = QtWidgets.QPushButton(self.tab)
        self.but_machine_use.setGeometry(QtCore.QRect(470, 140, 191, 181))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/undraw_everyday_life_hjnw.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_machine_use.setIcon(icon4)
        self.but_machine_use.setIconSize(QtCore.QSize(100, 100))
        self.but_machine_use.setObjectName("but_machine_use")
        self.but_tcp_show = QtWidgets.QPushButton(self.tab)
        self.but_tcp_show.setGeometry(QtCore.QRect(320, 350, 271, 181))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/undraw_file_manager_j85s.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_tcp_show.setIcon(icon5)
        self.but_tcp_show.setIconSize(QtCore.QSize(150, 150))
        self.but_tcp_show.setObjectName("but_tcp_show")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab)
        self.pushButton_11.setGeometry(QtCore.QRect(630, 350, 251, 181))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/undraw_link_shortener_mvf6.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon6)
        self.pushButton_11.setIconSize(QtCore.QSize(150, 150))
        self.pushButton_11.setObjectName("pushButton_11")
        self.but_serson_computer_resigner = QtWidgets.QPushButton(self.tab)
        self.but_serson_computer_resigner.setGeometry(QtCore.QRect(470, 20, 191, 91))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/undraw_referral_4ki4.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_serson_computer_resigner.setIcon(icon7)
        self.but_serson_computer_resigner.setIconSize(QtCore.QSize(80, 80))
        self.but_serson_computer_resigner.setObjectName("but_serson_computer_resigner")
        self.but_newthing_registe = QtWidgets.QPushButton(self.tab)
        self.but_newthing_registe.setGeometry(QtCore.QRect(250, 140, 191, 181))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/undraw_detailed_information_3sp6.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_newthing_registe.setIcon(icon8)
        self.but_newthing_registe.setIconSize(QtCore.QSize(100, 100))
        self.but_newthing_registe.setObjectName("but_newthing_registe")
        self.but_wire_machine_bind = QtWidgets.QPushButton(self.tab)
        self.but_wire_machine_bind.setGeometry(QtCore.QRect(250, 20, 191, 91))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/undraw_right_places_h9n3.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_wire_machine_bind.setIcon(icon9)
        self.but_wire_machine_bind.setIconSize(QtCore.QSize(100, 100))
        self.but_wire_machine_bind.setObjectName("but_wire_machine_bind")
        self.but_thing_lh = QtWidgets.QPushButton(self.tab)
        self.but_thing_lh.setGeometry(QtCore.QRect(30, 350, 251, 181))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/undraw_personal_notebook_sobb.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_thing_lh.setIcon(icon10)
        self.but_thing_lh.setIconSize(QtCore.QSize(150, 150))
        self.but_thing_lh.setObjectName("but_thing_lh")
        self.but_thing_resigner = QtWidgets.QPushButton(self.tab)
        self.but_thing_resigner.setGeometry(QtCore.QRect(30, 20, 191, 91))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/undraw_fall_thyk.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_thing_resigner.setIcon(icon11)
        self.but_thing_resigner.setIconSize(QtCore.QSize(100, 100))
        self.but_thing_resigner.setCheckable(False)
        self.but_thing_resigner.setChecked(False)
        self.but_thing_resigner.setObjectName("but_thing_resigner")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab)
        self.pushButton_12.setGeometry(QtCore.QRect(140, 560, 191, 91))
        self.pushButton_12.setIcon(icon11)
        self.pushButton_12.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_12.setCheckable(False)
        self.pushButton_12.setChecked(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_21 = QtWidgets.QPushButton(self.tab)
        self.pushButton_21.setGeometry(QtCore.QRect(360, 560, 191, 91))
        self.pushButton_21.setIcon(icon11)
        self.pushButton_21.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_21.setCheckable(False)
        self.pushButton_21.setChecked(False)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.tab)
        self.pushButton_22.setGeometry(QtCore.QRect(590, 560, 191, 91))
        self.pushButton_22.setIcon(icon11)
        self.pushButton_22.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_22.setCheckable(False)
        self.pushButton_22.setChecked(False)
        self.pushButton_22.setObjectName("pushButton_22")
        self.starck_warning = QtWidgets.QStackedWidget(self.tab)
        self.starck_warning.setGeometry(QtCore.QRect(890, 20, 191, 511))
        self.starck_warning.setObjectName("starck_warning")
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.text_warning = QtWidgets.QTextEdit(self.page_12)
        self.text_warning.setGeometry(QtCore.QRect(20, 0, 161, 531))
        self.text_warning.setStyleSheet("")
        self.text_warning.setObjectName("text_warning")
        self.starck_warning.addWidget(self.page_12)
        self.page_14 = QtWidgets.QWidget()
        self.page_14.setObjectName("page_14")
        self.text_thing_enough_show = QtWidgets.QTextEdit(self.page_14)
        self.text_thing_enough_show.setGeometry(QtCore.QRect(20, 0, 161, 531))
        self.text_thing_enough_show.setStyleSheet("")
        self.text_thing_enough_show.setObjectName("text_thing_enough_show")
        self.starck_warning.addWidget(self.page_14)
        self.page_13 = QtWidgets.QWidget()
        self.page_13.setObjectName("page_13")
        self.pushButton_36 = QtWidgets.QPushButton(self.page_13)
        self.pushButton_36.setGeometry(QtCore.QRect(20, 0, 161, 531))
        self.pushButton_36.setObjectName("pushButton_36")
        self.starck_warning.addWidget(self.page_13)
        self.but_right = QtWidgets.QPushButton(self.tab)
        self.but_right.setGeometry(QtCore.QRect(930, 0, 61, 21))
        self.but_right.setStyleSheet("\n"
"QPushButton{\n"
"    font-size: 14px;/*字体大小*/\n"
"    color:#00000000;/*颜色*/\n"
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
"    padding-right:9px;/*上边距*/\n"
"\n"
"}")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/images/tria.net.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_right.setIcon(icon12)
        self.but_right.setIconSize(QtCore.QSize(15, 15))
        self.but_right.setObjectName("but_right")
        self.but_warning_flash = QtWidgets.QPushButton(self.tab)
        self.but_warning_flash.setGeometry(QtCore.QRect(960, 1, 71, 20))
        self.but_warning_flash.setStyleSheet("\n"
"QPushButton{\n"
"    font-size: 14px;/*字体大小*/\n"
"    color:rgb(255, 10, 46);/*颜色*/\n"
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
        self.but_warning_flash.setObjectName("but_warning_flash")
        self.but_left = QtWidgets.QPushButton(self.tab)
        self.but_left.setGeometry(QtCore.QRect(1030, 0, 71, 21))
        self.but_left.setStyleSheet("\n"
"QPushButton{\n"
"    font-size: 14px;/*字体大小*/\n"
"    color:#00000000;/*颜色*/\n"
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
"    padding-left:9px;/*上边距*/\n"
"\n"
"}")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/images/trian.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_left.setIcon(icon13)
        self.but_left.setIconSize(QtCore.QSize(15, 15))
        self.but_left.setObjectName("but_left")
        self.pushButton_39 = QtWidgets.QPushButton(self.tab)
        self.pushButton_39.setGeometry(QtCore.QRect(910, 560, 161, 141))
        self.pushButton_39.setStyleSheet("*{color:red;\n"
"\n"
"}")
        self.pushButton_39.setObjectName("pushButton_39")
        self.tabWidget.addTab(self.tab, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_7.setGeometry(QtCore.QRect(470, 150, 421, 241))
        self.pushButton_7.setObjectName("pushButton_7")
        self.lab_server_ip = QtWidgets.QLabel(self.tab_8)
        self.lab_server_ip.setGeometry(QtCore.QRect(130, 50, 21, 16))
        self.lab_server_ip.setObjectName("lab_server_ip")
        self.label_10 = QtWidgets.QLabel(self.tab_8)
        self.label_10.setGeometry(QtCore.QRect(120, 190, 31, 16))
        self.label_10.setObjectName("label_10")
        self.label_15 = QtWidgets.QLabel(self.tab_8)
        self.label_15.setGeometry(QtCore.QRect(120, 350, 31, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_8)
        self.label_16.setGeometry(QtCore.QRect(110, 530, 72, 15))
        self.label_16.setObjectName("label_16")
        self.lin_server_ip = QtWidgets.QLineEdit(self.tab_8)
        self.lin_server_ip.setGeometry(QtCore.QRect(170, 40, 181, 31))
        self.lin_server_ip.setObjectName("lin_server_ip")
        self.lin_server_admin = QtWidgets.QLineEdit(self.tab_8)
        self.lin_server_admin.setGeometry(QtCore.QRect(172, 180, 181, 31))
        self.lin_server_admin.setObjectName("lin_server_admin")
        self.lin_server_password = QtWidgets.QLineEdit(self.tab_8)
        self.lin_server_password.setGeometry(QtCore.QRect(172, 340, 181, 31))
        self.lin_server_password.setObjectName("lin_server_password")
        self.lin_server_database = QtWidgets.QLineEdit(self.tab_8)
        self.lin_server_database.setGeometry(QtCore.QRect(180, 520, 171, 31))
        self.lin_server_database.setObjectName("lin_server_database")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_6.setGeometry(QtCore.QRect(360, 190, 421, 241))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lab_version_gif = QtWidgets.QLabel(self.tab_2)
        self.lab_version_gif.setGeometry(QtCore.QRect(200, 30, 631, 500))
        self.lab_version_gif.setText("")
        self.lab_version_gif.setObjectName("lab_version_gif")
        self.lab_version = QtWidgets.QLabel(self.tab_2)
        self.lab_version.setGeometry(QtCore.QRect(470, 560, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lab_version.setFont(font)
        self.lab_version.setObjectName("lab_version")
        self.tabWidget.addTab(self.tab_2, "")
        self.widget1 = QtWidgets.QWidget()
        self.widget1.setObjectName("widget1")
        self.but_white_interface = QtWidgets.QRadioButton(self.widget1)
        self.but_white_interface.setGeometry(QtCore.QRect(100, 40, 21, 19))
        self.but_white_interface.setText("")
        self.but_white_interface.setChecked(False)
        self.but_white_interface.setObjectName("but_white_interface")
        self.but_blue_interface = QtWidgets.QRadioButton(self.widget1)
        self.but_blue_interface.setGeometry(QtCore.QRect(100, 170, 21, 19))
        self.but_blue_interface.setText("")
        self.but_blue_interface.setChecked(True)
        self.but_blue_interface.setObjectName("but_blue_interface")
        self.but_black_interface = QtWidgets.QRadioButton(self.widget1)
        self.but_black_interface.setGeometry(QtCore.QRect(100, 300, 21, 19))
        self.but_black_interface.setText("")
        self.but_black_interface.setObjectName("but_black_interface")
        self.pushButton_25 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_25.setGeometry(QtCore.QRect(170, 10, 93, 81))
        self.pushButton_25.setStyleSheet("*{background:white;\n"
"border-radius:10px;\n"
"color:black;\n"
"}")
        self.pushButton_25.setObjectName("pushButton_25")
        self.face = QtWidgets.QPushButton(self.widget1)
        self.face.setGeometry(QtCore.QRect(170, 140, 93, 81))
        self.face.setStyleSheet("*{\n"
"background:rgb(100, 170, 220);\n"
"border-radius:10px;}")
        self.face.setObjectName("face")
        self.but_blac = QtWidgets.QPushButton(self.widget1)
        self.but_blac.setGeometry(QtCore.QRect(170, 270, 93, 81))
        self.but_blac.setStyleSheet("*{background:black;\n"
"border-radius:10px;}")
        self.but_blac.setObjectName("but_blac")
        self.tabWidget.addTab(self.widget1, "")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(1090, 10, 131, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(1220, 0, 41, 41))
        self.pushButton_24.setStyleSheet("\n"
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
        self.pushButton_24.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/images/search.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_24.setIcon(icon14)
        self.pushButton_24.setObjectName("pushButton_24")
        self.but_admin_register = QtWidgets.QPushButton(self.centralwidget)
        self.but_admin_register.setGeometry(QtCore.QRect(60, 0, 31, 31))
        self.but_admin_register.setToolTipDuration(-1)
        self.but_admin_register.setStyleSheet("\n"
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
        self.but_admin_register.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/images/robot.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_admin_register.setIcon(icon15)
        self.but_admin_register.setIconSize(QtCore.QSize(30, 30))
        self.but_admin_register.setFlat(False)
        self.but_admin_register.setObjectName("but_admin_register")
        self.but_admin_info_show = QtWidgets.QPushButton(self.centralwidget)
        self.but_admin_info_show.setGeometry(QtCore.QRect(90, 4, 81, 25))
        self.but_admin_info_show.setStyleSheet("*{color:rgb(255, 8, 41)}")
        self.but_admin_info_show.setObjectName("but_admin_info_show")
        self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_28.setGeometry(QtCore.QRect(20, 450, 161, 121))
        self.pushButton_28.setObjectName("pushButton_28")
        self.lcd_clock = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_clock.setGeometry(QtCore.QRect(570, 10, 121, 21))
        self.lcd_clock.setStyleSheet("*{border:none;\n"
"color:rgb(120, 170, 220)\n"
"}")
        self.lcd_clock.setDigitCount(10)
        self.lcd_clock.setObjectName("lcd_clock")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 570, 181, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.stackedWidget.setAcceptDrops(False)
        self.stackedWidget.setAccessibleName("")
        self.stackedWidget.setAccessibleDescription("")
        self.stackedWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setLineWidth(1)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.pushButton_32 = QtWidgets.QPushButton(self.page_8)
        self.pushButton_32.setGeometry(QtCore.QRect(0, 30, 161, 141))
        self.pushButton_32.setObjectName("pushButton_32")
        self.stackedWidget.addWidget(self.page_8)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.dial = QtWidgets.QDial(self.page_10)
        self.dial.setGeometry(QtCore.QRect(29, 13, 111, 101))
        self.dial.setObjectName("dial")
        self.stackedWidget.addWidget(self.page_10)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.pushButton_31 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_31.setGeometry(QtCore.QRect(0, 20, 161, 101))
        self.pushButton_31.setObjectName("pushButton_31")
        self.stackedWidget.addWidget(self.page_9)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(22, 0, 31, 31))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionserson = QtWidgets.QAction(MainWindow)
        self.actionserson.setObjectName("actionserson")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")

        self.retranslateUi(MainWindow)
        self.toolBox_navigation.setCurrentIndex(6)
        self.toolBox_navigation.layout().setSpacing(7)
        self.tabWidget.setCurrentIndex(5)
        self.starck_warning.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)
        self.but_eng2_1.clicked.connect(MainWindow.Set_Natigation_Window)
        self.but_eng2_2.clicked.connect(MainWindow.Set_Natigation_Window)
        self.pushButton_13.clicked.connect(MainWindow.Set_Natigation_Window)
        self.but_check_update.clicked.connect(MainWindow.eng2_2_funcation_choice)
        self.pushButton_19.clicked.connect(MainWindow.Set_Natigation_Window)
        self.pushButton_17.clicked.connect(MainWindow.Set_Natigation_Window)
        self.but_eng2_3.clicked.connect(MainWindow.Set_Natigation_Window)
        self.but_eng2_4.clicked.connect(MainWindow.Set_Natigation_Window)
        self.pushButton_33.clicked.connect(MainWindow.Exit)
        self.but_admin_register.clicked.connect(MainWindow.Set_Natigation_Window)
        self.but_admin_info_show.clicked.connect(MainWindow.Set_Natigation_Window)
        self.but_wire_machine_bind.clicked.connect(MainWindow.eng2_2_funcation_choice)
        self.pushButton_37.clicked.connect(MainWindow.confire_admin_reslute)
        self.but_thing_resigner.clicked.connect(MainWindow.eng2_2_funcation_choice)
        self.but_serson_computer_resigner.clicked.connect(MainWindow.eng2_2_funcation_choice)
        self.but_lost_seek.clicked.connect(MainWindow.eng2_2_funcation_choice)
        self.but_history.clicked.connect(MainWindow.eng2_2_funcation_choice)
        self.but_newthing_registe.clicked.connect(MainWindow.eng2_2_funcation_choice)
        self.but_machine_use.clicked.connect(MainWindow.eng2_2_funcation_choice)
        self.but_lend_registe.clicked.connect(MainWindow.eng2_2_funcation_choice)
        self.but_thing_lh.clicked.connect(MainWindow.eng2_2_funcation_choice)
        self.pushButton_38.clicked.connect(MainWindow.Clear_All)
        self.but_white_interface.clicked.connect(MainWindow.Choose_Interface)
        self.but_blue_interface.clicked.connect(MainWindow.Choose_Interface)
        self.but_black_interface.clicked.connect(MainWindow.Choose_Interface)
        self.but_right.clicked.connect(MainWindow.Change_Warning_Show)
        self.but_left.clicked.connect(MainWindow.Change_Warning_Show)
        self.but_warning_flash.clicked.connect(MainWindow.Show_Hanf_Year_No_Use_Thing)
        self.but_upload.clicked.connect(MainWindow.Download_File)
        self.but_download.clicked.connect(MainWindow.Upload_File)
        self.tab_user_all.cellDoubleClicked['int','int'].connect(MainWindow.admin_double_click)
        self.lin_worker_id.returnPressed.connect(MainWindow.Seek_User_Info)
        self.but_tcp_show.clicked.connect(MainWindow.eng2_2_funcation_choice)
        self.tab_size.cellDoubleClicked['int','int'].connect(MainWindow.Line_Size_Get_Double_Click_Data)
        self.but_size_confire.clicked.connect(MainWindow.Line_Size_Confire)
        self.but_line_confire.clicked.connect(MainWindow.Line_Size_Confire)
        self.tab_line.cellDoubleClicked['int','int'].connect(MainWindow.Line_Size_Get_Double_Click_Data)
        self.but_warning_flash.clicked.connect(MainWindow.thing_security_ont_enough)
        self.pushButton_16.clicked.connect(MainWindow.Set_Natigation_Window)
        self.pushButton_20.clicked.connect(MainWindow.Set_Natigation_Window)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "主界面"))
        self.but_eng2_3.setText(_translate("MainWindow", "线体尺寸管理"))
        self.but_eng2_4.setText(_translate("MainWindow", "未开发"))
        self.but_eng2_9.setText(_translate("MainWindow", "未开发"))
        self.toolBox_navigation.setItemText(self.toolBox_navigation.indexOf(self.page), _translate("MainWindow", "管理"))
        self.but_eng2_1.setText(_translate("MainWindow", "主界面 "))
        self.but_eng2_7.setText(_translate("MainWindow", "未开发"))
        self.but_eng2_8.setText(_translate("MainWindow", "未开发"))
        self.toolBox_navigation.setItemText(self.toolBox_navigation.indexOf(self.page_5), _translate("MainWindow", "ENG2-1"))
        self.but_eng2_2.setText(_translate("MainWindow", "主界面"))
        self.but_eng2_5.setText(_translate("MainWindow", "未开发"))
        self.but_eng2_6.setText(_translate("MainWindow", "未开发"))
        self.toolBox_navigation.setItemText(self.toolBox_navigation.indexOf(self.page_6), _translate("MainWindow", "ENG2-2"))
        self.pushButton_13.setText(_translate("MainWindow", "更改"))
        self.pushButton_14.setText(_translate("MainWindow", "注册"))
        self.pushButton_15.setText(_translate("MainWindow", "注销"))
        self.toolBox_navigation.setItemText(self.toolBox_navigation.indexOf(self.page_3), _translate("MainWindow", "账号"))
        self.pushButton_19.setText(_translate("MainWindow", "界面样式"))
        self.pushButton_20.setText(_translate("MainWindow", "server ip"))
        self.pushButton_23.setText(_translate("MainWindow", "未开发"))
        self.toolBox_navigation.setItemText(self.toolBox_navigation.indexOf(self.page_4), _translate("MainWindow", "设置"))
        self.pushButton_16.setText(_translate("MainWindow", "版本"))
        self.pushButton_17.setText(_translate("MainWindow", "功能介绍"))
        self.but_check_update.setText(_translate("MainWindow", "检查更新"))
        self.toolBox_navigation.setItemText(self.toolBox_navigation.indexOf(self.page_2), _translate("MainWindow", "帮助说明"))
        self.pushButton_33.setText(_translate("MainWindow", "EXIT"))
        self.pushButton_34.setText(_translate("MainWindow", "未开发"))
        self.pushButton_35.setText(_translate("MainWindow", "未开发"))
        self.toolBox_navigation.setItemText(self.toolBox_navigation.indexOf(self.page_7), _translate("MainWindow", "关于"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'System\'; font-size:9pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600;\">ghgh</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))
        self.textedit_work_show.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'STFangsong\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.but_upload.setText(_translate("MainWindow", "下载"))
        self.but_download.setText(_translate("MainWindow", "上传"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Page"))
        item = self.tab_line.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "线体"))
        item = self.tab_line.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "是否使用"))
        item = self.tab_size.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "尺寸"))
        item = self.tab_size.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "是否使用"))
        self.but_size_confire.setText(_translate("MainWindow", "确认"))
        self.label.setText(_translate("MainWindow", "线体"))
        self.label_2.setText(_translate("MainWindow", "是否使用"))
        self.label_5.setText(_translate("MainWindow", "尺寸"))
        self.label_7.setText(_translate("MainWindow", "是否使用"))
        self.com_line_choice.setItemText(0, _translate("MainWindow", "增加"))
        self.com_line_choice.setItemText(1, _translate("MainWindow", "修改"))
        self.com_line_choice.setItemText(2, _translate("MainWindow", "删除"))
        self.com_size_choice.setItemText(0, _translate("MainWindow", "增加"))
        self.com_size_choice.setItemText(1, _translate("MainWindow", "修改"))
        self.com_size_choice.setItemText(2, _translate("MainWindow", "删除"))
        self.but_size_confire_2.setText(_translate("MainWindow", "清除"))
        self.but_line_confire.setText(_translate("MainWindow", "确认"))
        self.but_size_confire_3.setText(_translate("MainWindow", "清除"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Page"))
        self.label_11.setText(_translate("MainWindow", "邮箱"))
        self.lab_lh_address.setText(_translate("MainWindow", "0"))
        self.pushButton_2.setText(_translate("MainWindow", "刷新"))
        self.pushButton_37.setText(_translate("MainWindow", "确认"))
        self.label_12.setText(_translate("MainWindow", "部门名称"))
        self.label_13.setText(_translate("MainWindow", "部门代码"))
        self.label_3.setText(_translate("MainWindow", "工号"))
        self.pushButton_38.setText(_translate("MainWindow", "清除"))
        self.label_14.setText(_translate("MainWindow", "手机号码"))
        item = self.tab_user_all.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "工号"))
        item = self.tab_user_all.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tab_user_all.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "厂牌ID"))
        item = self.tab_user_all.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "手机号码"))
        item = self.tab_user_all.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "部门名称"))
        item = self.tab_user_all.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "部门代码"))
        item = self.tab_user_all.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "邮箱"))
        item = self.tab_user_all.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "时间"))
        self.label_4.setText(_translate("MainWindow", "厂牌ID"))
        self.label_6.setText(_translate("MainWindow", "姓名"))
        self.com_adnim_choice.setItemText(0, _translate("MainWindow", "修改"))
        self.com_adnim_choice.setItemText(1, _translate("MainWindow", "删除"))
        self.com_adnim_choice.setItemText(2, _translate("MainWindow", "增加"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "账号"))
        self.pushButton.setText(_translate("MainWindow", "未开发"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "eng2-1"))
        self.but_lost_seek.setText(_translate("MainWindow", "耗损记录\n"
"  查询"))
        self.but_history.setText(_translate("MainWindow", "历史记录"))
        self.but_lend_registe.setText(_translate("MainWindow", "借用登记"))
        self.but_machine_use.setText(_translate("MainWindow", "机种设定"))
        self.but_tcp_show.setText(_translate("MainWindow", "未开发"))
        self.pushButton_11.setText(_translate("MainWindow", "未开发"))
        self.but_serson_computer_resigner.setText(_translate("MainWindow", "serson登记\n"
" 机台登记"))
        self.but_newthing_registe.setText(_translate("MainWindow", "新品入库\n"
"  盘点"))
        self.but_wire_machine_bind.setText(_translate("MainWindow", "线材机种\n"
"  绑定"))
        self.but_thing_lh.setText(_translate("MainWindow", "物品料号\n"
"  设定"))
        self.but_thing_resigner.setText(_translate("MainWindow", "物品登记"))
        self.pushButton_12.setText(_translate("MainWindow", "未开发"))
        self.pushButton_21.setText(_translate("MainWindow", "未开发"))
        self.pushButton_22.setText(_translate("MainWindow", "未开发"))
        self.text_warning.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'System\'; font-size:9pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:11pt; color:#ff011a;\"> 半年未使用物品</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:11pt; color:#000000;\"><br /></p></body></html>"))
        self.text_thing_enough_show.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'System\'; font-size:9pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:11pt; color:#ff011a;\">  库存不足物品</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:11pt; color:#000000;\"><br /></p></body></html>"))
        self.pushButton_36.setText(_translate("MainWindow", "未开发"))
        self.but_right.setText(_translate("MainWindow", "左边"))
        self.but_warning_flash.setText(_translate("MainWindow", "警示区"))
        self.but_left.setText(_translate("MainWindow", "右边"))
        self.pushButton_39.setText(_translate("MainWindow", "未开发"))
        self.pushButton_7.setText(_translate("MainWindow", "未开发"))
        self.lab_server_ip.setText(_translate("MainWindow", "IP"))
        self.label_10.setText(_translate("MainWindow", "账号"))
        self.label_15.setText(_translate("MainWindow", "密码"))
        self.label_16.setText(_translate("MainWindow", "database"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "Page"))
        self.pushButton_6.setText(_translate("MainWindow", "未开发"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "Page"))
        self.lab_version.setText(_translate("MainWindow", "版本0.0.1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Page"))
        self.pushButton_25.setText(_translate("MainWindow", "默认"))
        self.face.setText(_translate("MainWindow", "蓝天"))
        self.but_blac.setText(_translate("MainWindow", "黑夜"))
        self.but_admin_register.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">登录</span></p></body></html>"))
        self.but_admin_info_show.setText(_translate("MainWindow", "游客"))
        self.pushButton_28.setText(_translate("MainWindow", "未开发"))
        self.pushButton_32.setText(_translate("MainWindow", "未开发"))
        self.pushButton_31.setText(_translate("MainWindow", "今天事项"))
        self.actionserson.setText(_translate("MainWindow", "serson机台登记"))
        self.action.setText(_translate("MainWindow", "线材与机种绑定"))
        self.action_2.setText(_translate("MainWindow", "物品耗损使用查询"))
        self.action_3.setText(_translate("MainWindow", "物品历史记录查询"))
        self.action_4.setText(_translate("MainWindow", "新品入库与盘点功能"))
        self.action_5.setText(_translate("MainWindow", "机种使用设定"))

import wire_images_rc
