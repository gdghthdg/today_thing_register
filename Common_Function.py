"""
a common function include

一个弹出输入框的
# 显示输入对话框
# 字符串类型，标题、提示信息、默认输入
# text,ok=QInputDialog.getText(self, "title", "User name:", QLineEdit.Normal, '>>>:')


#一个输入框
# my_list = ['1', '2', '3']
# my_str, ok = QInputDialog.getItem(self, "下拉框", '提示', my_list)
# #print(my_str, ok)

设置窗口无边框
# self.setWindowFlags(Qt.FramelessWindowHint)

#把关闭取消掉
# self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)

# 禁止窗口关闭与放大
# self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint |  # 使能最小化按钮
#                     QtCore.Qt.WindowCloseButtonHint |  # 使能关闭按钮
#                     QtCore.Qt.WindowStaysOnTopHint)

#禁止窗口拉伸
#self.setFixedSize(self.width(), self.height())

#tablewidget一个自适应
# self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
#一个自动换行
# self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
# self.tableWidget.setWordWrap(True)


#把窗口放在最前面,不准切换窗口,顶级窗口
self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)


# 透明处理，移动需要拖动数字
#         self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.SubWindow | QtCore.Qt.WindowStaysOnTopHint)
#         self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)


commin class
    替换字符串                     2>replace str(),两个参数,一个字符串,一个替换的list,返回替换掉的字符串
    去掉除英文与数字外的字符       1>get_english_math()输入的串,返回字符串
    得到时间2019-01-01 00:00:000  0>Get_Now_Time(),返回str时间
    返回一个ftp引用,              0>Ftp(),返回一个ftp引用
    执行sql语句,不返回任何值      1>Execute_Sql_No_Get_Date(sql_order),参数一个sql命令
    执行sql查询命令,返回查询结果  1>Execute_Sql_Get_Date(sql_order),参数一个sql命令,返回执行命令的结果
    从d盘读取机种size            0>Read_loadsize_info(),没有参数,返回一个list的尺寸
    从d盘读取线体line            0>Read_load_info(),没有参数,返回一个list的线体



father class(QMainWindow)
    程序退出                      0>exit_exe()程序退出
    设置gif图片                   2>set_gif(),两个参数,一个gif的地址,一个控件的引用
    设置琴系统的托盘              0>set_system_stock(),一个图片地址
    提示1个选择                   1>Message_one().一个参数,要出现提示的标题,返回你选择的结果,QMessageBox.Yes|QMessageBox.No
    提示2个选择                   1>Message_two().二个参数,要出现提示的标题,返回你选择的结果,QMessageBox.Yes|QMessageBox.No
    窗口居中                      1>center()
    一个控件输入限制其输入         1>testing_machine(),一个参数,控件的引用
    从时间往后往前推几天,得到时间  2>Date_delete()两个参数,一个推前推后天数,一个现在标准时间
    两个不同日期相隔天数           2>data_sub()两个参数,一个日期,一个日期
    从界面打开要选择的文件夹,导入  3>to_lend_function().三个参数,一个删除哪个sql表的sql语句,一个sql表,一个是从excel中要取多少列
    从界面导出数据                 1>lend_function()一个表格控件的名称引用
    一个实时反映本地时间           0>init_timer()其调用了update_time(),返回了一个时间
    lineedit自动补全               2>init_lineedit(),两个参数,一个lineedit的名称引用,一个补全的list数组
    combobox自动补全               2>init_combobox().两个参数,一个combobox的名称引用,一个补全的list的数组


Windows_Move class
    鼠标按下事件                    mousePressEvent()
    鼠标移动事件                    mouseMoveEvent()


CommonHelper class
    读取Qss                         1>readQss(),一个参数,style的address


All_Class_common_Set class
    pass

tablewidget所有的增删改查
Common_Table(QMainWindow)
    从sql得到数据,打印在tablewidget    3>Set_Table() 三个参数 一个get sql查询结果,一个tablewidget_name引用,一个打印几列
    得到table表中的数据,显示在lineedit 3>Get_Table_Click_Data() 三个参数,一个打印在lineedit中的widget_name数组,一个tablewidget引用,一个点击的是第几行
    根据一个数据得到所有的详细数据     2>Seek_table_info() 两个参数,一个查找sql指令,一个要打印的所有widget数组
    得到所有widget中text(为了增修)    1>Get_Window_Info() 一个参数,一个所有的lineedit数组
    上传增加修改的结果到sql server    3>Confire_Change()  三个参数,一个lineedit所有数组,一个combobox中包含增删改查的,一个上传的sql_table_name


窗口事件的重写,继承
Window_event class
    当窗口关闭时                      closeEvent()
    当窗口有动作改变时                changEvent()


键盘事件重写,继承
Keyboard_event class
    键盘按下事件                      keyPressEvent()
    键盘上升事件                      keyReleaseEvent()



鼠标事件的重写,继承
mouse_event class
    鼠标移动事件                      mouseMoveEvent()


"""


from traceback import print_exc
import re
import socket
from threading import Thread
from pymssql import connect
import decimal
import xlwt
import xlrd
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets,QtMultimedia
from datetime import datetime
from PyQt5.QtWidgets import *
from sys import argv,exit,stdout
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp
from Get_Machine_Num_for_excel import Get_Excel_AllMachine_Num
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ftplib import *
import os
import time
from datetime import datetime, timedelta
from PyQt5.QtCore import Qt, pyqtSignal, QPoint


decimal.__version__

time_now=datetime.now()
Time_now=str(time_now)[:10]



# 显示输入对话框
# 字符串类型，标题、提示信息、默认输入
# text,ok=QInputDialog.getText(self, "title", "User name:", QLineEdit.Normal, '>>>:')

#一个输入框
# my_list = ['1', '2', '3']
# my_str, ok = QInputDialog.getItem(self, "下拉框", '提示', my_list)
# #print(my_str, ok)

# self.setWindowFlags(Qt.FramelessWindowHint) #设置无边框
# self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint) #把关闭取消掉

# 禁止窗口关闭与放大
# self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint |  # 使能最小化按钮
#                     QtCore.Qt.WindowCloseButtonHint |  # 使能关闭按钮
#                     QtCore.Qt.WindowStaysOnTopHint)

#禁止窗口拉伸
#self.setFixedSize(self.width(), self.height())

#tablewidget一个自适应，一个自动换行
# self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
# self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
# self.tableWidget.setWordWrap(True)


#把窗口放在最前面,不准切换窗口
#self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

# self.tablewidget.setWordWrap(True)

# 透明处理，移动需要拖动数字
#         self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.SubWindow | QtCore.Qt.WindowStaysOnTopHint)
#         self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

#打包不能用.jpg

#api接口就是用http,tcp/ip用的嗎


#


def set_server_ip_admin_password_database(ip,admin,password,database):
    global server_ip,server_admin,server_password,server_database
    server_ip=ip
    server_admin=admin
    server_password=password
    server_database=database


# server_ip='127.0.0.1:443'
# server_database='management'


server_ip='172.17.130.106'
server_database='xueshengxinxi'

server_admin='sa'
server_password='123456'










#去掉某个标点符号,兩個參數都是list(一个字符型,一个包含去掉字符的数组)
def replace_str(str_name,replace_son):
    str_name=str(str_name)
    for i in replace_son:
        str_name=str_name.replace(i,'')
    return str_name


#只要英文与数字(一个字符)
def get_english_math(str):
    sub_str = re.sub(u"([^\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", str)
    return sub_str


#这是插入时间的正确格式2019-01-01 00:00:000
def Get_Now_Time():
    now_time=str(datetime.now())[:len(str(datetime.now()))-3]
    return now_time

#得到一个时间，后缀是有3个零的数据
def Get_Now_Time_have_zero():
    now_time = str(datetime.now())[:len(str(datetime.now())) - 7] + ':000'
    return now_time

#一个ftp的函数，返回一个ftp引用
def Ftp():
    ftp = FTP()
    ftp.encoding = 'BIG5'
    ftp.set_debuglevel(2)  # 打开调试级别2，显示详细信息
    ftp.connect("10.178.1.98", 21,timeout=55)  # 连接的ftp sever和端口

    ftp.login("hblcmftp", "exploration")  # 连接的用户名，密码
    ftp.dir()

    return ftp


# 执行SQL，而不要数据(sql指令)
def Execute_Sql_No_Get_Date(sql_order):
    try:
        #print('47=%s'%sql_order)
        #Connect = connect('172.17.130.106', 'sa', '123456', 'xueshengxinxi',login_timeout=1)  # 建立连接
        Connect = connect(server_ip, server_admin, server_password, server_database, login_timeout=1)  # 建立连接

        cursor = Connect.cursor()
        cursor.execute(sql_order)
        Connect.commit()
        Connect.close()
        cursor.close()
    except Exception:
        print_exc()


#  执行SQL语句并且有获取数据的要求(SQL指令)
def Execute_Sql_Get_Date(sql_order):
    try:

        ##print(sql_order)
        #Connect = connect('172.17.130.106', 'sa', '123456', 'xueshengxinxi',login_timeout=1)  # 建立连接
        Connect = connect(server_ip, server_admin, server_password, server_database, login_timeout=1)  # 建立连接

        cursor = Connect.cursor()
        cursor.execute(sql_order)
        get_sql_data=cursor.fetchall()
        Connect.commit()
        Connect.close()
        cursor.close()
        ##print(get_sql_data)
        return get_sql_data

    except Exception:
        print_exc(file=open('D://LOG//%s.txt'%Time_now,'a'))


#  从本地读取机种SIZE
def Read_loadsize_info():
    sizes = []
    line_place=open('D:\\config\\machine_size.txt','r',encoding='utf8')
    for file in line_place.readlines():
        file = file[:len(file) - 1]
        sizes.append(file)
#
    # sql_order="select Line_Name from Line_Size_All where Line_Name!='' order by Line_Name "
    # relute=Execute_Sql_Get_Date(sql_order)
    # for size in relute:
    #     sizes.append(size[0])

    #print('本地尺寸', sizes)
    return sizes

##print("这是一个好看的函数")

#  从本地读取线体
def Read_load_info():
    try:
        lines=[]
        line_place=open('D:\\config\\line.txt','r',encoding='utf8')
        for file in line_place.readlines():
            file = file[:len(file) - 1]
            lines.append(file)
        #print(lines)

#        lines.remove('')
    except Exception:
        print_exc()
    return lines


#根据输入的工号得到操作人员的姓名(工作人员的工号,工作人员的名字)
def get_uaer_name(user_num,user_name):
    try:
        get_reslut=''
        sql_order = "select USER_NAME FROM MFG_USER WHERE USER_ID='%s'"%user_num
        get_reslut=Execute_Sql_Get_Date(sql_order)

    except Exception:
        print_exc()


#起点这一手的操作是真的秀
    if len(get_reslut)==0:
        return user_name
        Farther().Message_two('没有此人')
    else:
        return get_reslut[0][0]


# 这是把输入的BARCODE后五位转换为ZERO
def Determine_wire(Thing_Barcode):

    ##print('22=%s'%len(Thing_Barcode[:len(Thing_Barcode) - 5]))
    ##print('23=%s'%Thing_Barcode[:len(Thing_Barcode) - 5])

    if Thing_Barcode[:len(Thing_Barcode) - 5] != '' and len(Thing_Barcode[:len(Thing_Barcode)]) == 13:
        Thing_Barcode = Thing_Barcode[:len(Thing_Barcode) - 5] + '00000'

    else:
        Thing_Barcode = Thing_Barcode[:len(Thing_Barcode) - 3] + '000'
    return Thing_Barcode



#  这是一个限制器（验证器）
def testing_machine(expression):
    reg = QRegExp(expression)
    pValidator = QRegExpValidator()
    pValidator.setRegExp(reg)
    return pValidator



#得到excel得到数据
def Get_Excel_AllMachine(self): #从excel得到机种与数量
    NEW = Get_Excel_AllMachine_Num()
    (Excel_Machine,Dist_XY)=NEW.set_up('2019-6-1','2019-7-1')
    return (Excel_Machine,Dist_XY)

#重写所有继承此类的子类的函数
class No_Main_Window(QMainWindow):

    #重写一个函数，每一个函数信号都会触发一个funtion,重载这个函数就可了，不过最好放在一个通用的类中，这样继承的话
    #就可以一同改变
    # 捕捉窗口的变化，判断是不窗口最小化
    def closeEvent(self, event):
        sender=self.sender()
        #print(sender)
        #print(sender.objectName())

        #print('有关闭的动作')


    def changeEvent(self, event):
    #     # 顶层窗口激活状态改变
    #     if event.type() == QEvent.ActivationChange:
    #         #print('顶层窗口变化')
    #         #self.repaint()
    #         #self.hide()
    #     else:
    #         #print('顶层窗口不变化')
    #         #self.hide()
    #
    #     #print(self.isMinimized())
    #
    #     #这是判断是否最小化的情况
        if self.isMinimized():
            pass
            #self.hide()
            #print('窗口最小化')
    #     else:
    #         #print('窗口不是最小化')
    #
    #     ##print(self.windowState())
    #

#包括设置gif，设置系统托盘，ftp下载文件，上传文件，弹窗提示，
class Farther(QMainWindow):

    # 讀取QSS中的STYLE
    # def __init__(self):
    #     self.center()
    #     self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)


    # def Read_Qss(self):
    #     with open(r'.\style.qss') as file:
    #         str = file.readlines()
    #         str = ''.join(str).strip('\n')
    #     self.setStyleSheet(str)
    #     self.show()
    #程序退出的總集

    def exit_exe(self):
        os._exit(0)
        # exit(1)
        # return

    #设置gif图片,(输入gif的地址,label的pyqt 的名称)
    def set_gif(self,gif_address,lab_widget):
        self.gif = QMovie(gif_address)
        self.gif.setScaledSize(lab_widget.size())
        # self.gif.setScaledSize(QSize(150, 150))
        lab_widget.setMovie(self.gif)
        self.gif.start()

    #设置软件一个系统托盘，得到一个(图片的名称)
    def set_system_stock(self,ico_address):
            self.tray = QSystemTrayIcon()  # 创建系统托盘对象
            self.icon = QIcon(ico_address)  # 创建图标
            self.tray.setIcon(self.icon)  # 设置系统托盘图标

            #self.tray.activated.connect(self.TuoPanEvent)  # 设置托盘点击事件处理函数

            self.tray_menu = QMenu(QApplication.desktop())  # 创建菜单
            self.RestoreAction = QAction(u'还原 ', self, triggered=self.showNormal)  # 添加一级菜单动作选项(还原主窗口)
            self.QuitAction = QAction(u'退出 ', self, triggered=os._exit)  # 添加一级菜单动作选项(退出程序)
            self.tray_menu.addAction(self.RestoreAction)  # 为菜单添加动作
            self.tray_menu.addAction(self.QuitAction)
            self.tray.setContextMenu(self.tray_menu)  # 设置系统托盘菜单



    #下载every_day_work
    def Download_File(self):
        try:
            ftp = Ftp()
            file = '/hblcmftp/AllType/Personal Files/何健文/最新/Updata/每日工作.txt'
            fp = open(r'D:\config\每日工作.txt', 'wb')  # 以写模式在本地打开文件
            ftp.retrbinary('RETR %s' % file, fp.write, 90240000)  # 接收服务器上文件并写入本地文件
            ftp.set_debuglevel(0)  # 关闭调试
            ftp.quit()
            fp.close()
            fp=open('D:\config\每日工作.txt','r+',encoding='UTF-8')
            ##print('448=%s'%fp.read())
            data_file=fp.read()
            ##print('451=',data_file)
            self.textedit_work_show.setPlainText(data_file)
            fp.close()

            if self.sender().text()=='下载':
                self.Message_two('下载成功')

        except Exception:
            print_exc()

    # 上传every_day_work
    def Upload_File(self):
        try:
            if self.Message_two('是否上传') == QMessageBox.Yes:
                ftp = Ftp()
                file = '/hblcmftp/AllType/Personal Files/何健文/最新/Updata/每日工作.txt'
                a=self.textedit_work_show.toPlainText()
                #print(a)
                fp = open(r'D:\config\每日工作.txt', 'w+',encoding='UTF-8')
                fp.write(str(a))
                fp.close()

                #a=a.encode('UTF-8')
                fp = open(r'D:\config\每日工作.txt', 'rb')  # 以写模式在本地打开文件

                ftp.storbinary('STOR ' + file, fp, 95000000)

                ftp.set_debuglevel(0)  # 关闭调试
                ftp.quit()
                fp.close()
                self.Message_two('上传成功')

        except Exception:
            print_exc()





    #一个有一个选择的弹窗(弹出窗口的所说的文字)
    def Message_one(self, title):
        choice = QMessageBox.question(self, '确认', title, QMessageBox.Yes)
        return choice


    #一个有两个弹窗的(弹出窗口的所说的文字)
    def Message_two(self,title):
        choice = QMessageBox.warning(self, '是否操作', title, QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        return choice

    #窗口居中
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        #print('尺寸',qr.size())
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    #一个限制器(True or False)
    def testing_machine(self,expression):
        reg = QRegExp(expression)
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)

    #从一个日期减少/增加的天数,得到另外一个,日期加减(加减天数,一个时间戳)
    def Date_delete(self, day_ago,finally_datetime):  # 从现在（几天）得到几天前的时间

        now = datetime.strptime(finally_datetime, '%Y-%m-%d %H:%M:%S:000')

        delta = timedelta(days=day_ago)

        n_days = now - delta

        Seven_Day_Ago = str(n_days.strftime('%Y-%m-%d 00:00:00:000'))

        Year = int(Seven_Day_Ago[:4])
        Month = int(Seven_Day_Ago[5:7])
        Day = int(Seven_Day_Ago[8:10])
        # #print(Year,Month,Day)
        # #print(Seven_Day_Ago)

        return Seven_Day_Ago, Year, Month, Day

    #两个时间减得到一个相差的数(一个时间数,另一个时间数)
    def date_sub(self,finally_time,start_time):
        try:
            d1 = datetime.strptime(finally_time, '%Y-%m-%d %H:%M:%S')
            d2 = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')

            delta = d1 - d2

            #delta = timedelta(days=30)

            #print(delta)

            return delta
        except Exception:
            print_exc()


    #这是一个文件的导入function（一个删除的命令，一个是哪个界面的命令，一个是从excel中得到的多少行）
    def to_lend_function(self,delete_sql_order,order,read_column):

        self.cwd = os.getcwd()  # 获取当前程序文件位置

        try:
            fileName_choose, filetype = QFileDialog.getOpenFileName(self,"选取文件",self.cwd,"All Files (*);;Text Files (*.xls);;Text Files (*.xlsx)")  # 设置文件扩展名过滤,用双分号间隔

            if fileName_choose == "":
                #print("\n取消选择")
                return

            #print("\n你选择的文件为:")
            #print(fileName_choose)
            #print("文件筛选器类型: ", filetype)

            Connect = connect('172.17.130.106', 'sa', '123456', 'xueshengxinxi', login_timeout=1)  # 建立连接
            cursor = Connect.cursor()

            #这是一个删除指令
            cursor.execute(delete_sql_order)

            data = xlrd.open_workbook(fileName_choose)  # 打开xls文件
            table = data.sheets()[0]  # 打开第一张表
            nrows = table.nrows  # 获取表的行数

            #print(nrows)
            Y = 0

            for i in range(1,nrows):  # 循环逐行打印
                # #print(table.row_values(i)[:14])
                #这是得到excel中内容
                i = table.row_values(i)[:read_column]  # $$$$$

                #print('excel中的内容',i)

    #这是serson的导入
                if order == "Serson_Table":
                    sql_order="insert into Serson_Table(Serson_Name,Thing_Statius,Station,Work_Name,Address,CDT) values('%s','%s','%s','%s','%s','%s')"% (str(i[0]).replace('.0',''), str(i[1]).replace('.0',''), str(i[2]), i[3],i[4],Get_Now_Time())
    #这是machine_contrast导入

                elif order=="MACHINE_LH":
                    sql_order = "insert into MACHINE_LH(SIZE,MACHINES,SYSTEMS,JI_OR_SKD,MONDEL,BI,CTAG,BMA,IAS,AGIS,FFC,INV_POWER_WIRE,DRIVER_MARCH,DRIVER,POWER_WIRE,MACHINE_STATIUS) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
                                        % (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13],i[14],'True')

                elif order=="NC_KUCUN_LH":
                    sql_order = "insert into NC_KUCUN_LH(TYPEOF,TXM,WUPIN_NAME,LH,Thing_March) values('%s','%s','%s','%s','%s')"%(i[0],i[1],i[2],i[3],i[4])

                elif order =="NC_KUCUN_SUM":
                    sql_order = "insert into NC_KUCUN_SUMTEST(TYPEOF,TXM,WUPIN_NAME,QTY_OK,QTY_NG,QTY_BF,QTY_ONLINE,SECUREQTY,Location_OK,Location_NG,CDT) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                    i[0], i[1], i[2], i[3],i[4], i[5],i[6],i[7],i[8],i[9],Get_Now_Time())


                cursor.execute(sql_order)


            Connect.commit()
            self.Message_two('导入成功')
        except Exception:
            print_exc()



    #这是一个保存文件的(一个tablewidgetr的名称)
    def lend_function(self,tablewidget):
        self.cwd = os.getcwd()  # 获取当前程序文件位置
        fileName_choose, filetype = QFileDialog.getSaveFileName(self,
                                                                "文件保存",
                                                                self.cwd,  # 起始路径
                                                                "All Files (*);;Text Files (*.xls);;Text Files (*.xlm)")
        if fileName_choose == "":
            #print("\n取消选择")
            return

        #print("\n你选择要保存的文件为:")
        #print(fileName_choose)


    #创建一个文件
        #open(fileName_choose,'w')
        #print("文件筛选器类型: ", filetype)

        try:
            xls = xlwt.Workbook()
            sheet = xls.add_sheet('sheet 1')

            for i in range(tablewidget.columnCount()):
                #print(tablewidget.horizontalHeaderItem(i).text())
            # 这是一个把标题放进excel
                sheet.write(0, i, tablewidget.horizontalHeaderItem(i).text())

            for j in range(1,tablewidget.rowCount()):
                for i in range(tablewidget.columnCount()):
                    sheet.write(j, i, tablewidget.item(j - 1, i).text())


            xls.save(fileName_choose)

            if self.Message_two('已导出到D盘根目录,是否打开')==QMessageBox.Yes:
                #time.sleep(6)
                os.system(fileName_choose)



        except Exception:
            print_exc()

            # if self.Message_two('已导出到D盘根目录,是否打开') == QMessageBox.Yes:
            #     # time.sleep(6)
            #     os.system(file_name)


    #這是顯示時間用的
    def init_timer(self):
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.update_time)
    #这里的时间可以用来做一个定时执行


    #一个更新时间的function
    def update_time(self):
        # self.lcd_clock.display(time.strftime("%X", time.localtime()))

        #print('时间:',time.localtime())
        return time.localtime()


    #lineedit 自动补全的function (a lineedit widget,a ist)
    def init_lineedit(self,lineedit,items_list):
        # 增加自动补全
        self.completer = QCompleter(items_list)
        # 设置匹配模式  有三种： Qt.MatchStartsWith 开头匹配（默认）  Qt.MatchContains 内容匹配  Qt.MatchEndsWith 结尾匹配
        self.completer.setFilterMode(Qt.MatchContains)
        # 设置补全模式  有三种： QCompleter.PopupCompletion（默认）  QCompleter.InlineCompletion   QCompleter.UnfilteredPopupCompletion
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        # 给lineedit设置补全器
        lineedit.setCompleter(self.completer)

    #combobox 自动补全的function (a combobox widget ,a list)
    def init_combobox(self,combobox,items_list):
        # 增加选项元素
        for i in range(len(items_list)):
            combobox.addItem(items_list[i])
        combobox.setCurrentIndex(-1)

        # 增加自动补全
        self.completer = QCompleter(items_list)
        self.completer.setFilterMode(Qt.MatchContains)
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        combobox.setCompleter(self.completer)

    # 輸入一個數據,在表格中自動跳轉到時某個地方
    # tablewidget:控件的名稱
    # text:要尋找的數據
    def table_jump_address(self, tablewidget, text):
        try:
            text=text.upper()
            items = tablewidget.findItems(text, Qt.MatchExactly)
            item = items[0]

        except Exception:
            print_exc()
            text=text.lower()
            items = tablewidget.findItems(text, Qt.MatchExactly)
            item = items[0]
            # 选中单元格

        # print("test:",text)

        item.setSelected(True)
        # 设置单元格的背脊颜色为红
        # item.setForeground(QBrush(QColor(255, 0, 0)))

        row = item.row()
        # 通过鼠标滚轮定位，快速定位到第十一行
        tablewidget.verticalScrollBar().setSliderPosition(row - 8)




#这是窗口移动
class Windows_Move():

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        try:
            ##print("mouse_move",self.dragPosition)
            #print("event:",event)
            if event.buttons() == Qt.LeftButton:
                #print("窗口位置:",event.globalPos() - self.dragPosition)
                self.move(event.globalPos() - self.dragPosition)
                event.accept()
                #print("accept",event.accept())
        except Exception:
            print_exc(file=open('D://LOG//%s.txt'%Time_now,'a'))



#这是QSS设置
class CommonHelper:
    def __init__(self):
        pass

    @staticmethod
    def readQss(style):
        with open(style, 'r',encoding='UTF-8') as f:
            return f.read()


#继承相同的function
class All_Class_Common_Set(QMainWindow):
    def All_Class_Common_Set_Funcation(self):
        self.setWindowFlags(Qt.FramelessWindowHint)


class Common_Table(QMainWindow):

    #这是得到sql查找的值，然后显示到table中(一个sql的指令,tablewidget的名称,tablewidget的tf行数)
    def Set_Table(self,sql_order,table_name,table_cow):

        try:
            # All_lin_txm.clear()
            get_reslute = Execute_Sql_Get_Date(sql_order)

            ##print('201=%s' % get_reslute)
            table_name.setColumnCount(table_cow) # 设置table的列数
            table_name.setRowCount(len(get_reslute))

            for i in range(table_cow):
                for j in range(len(get_reslute)):
                    data = QTableWidgetItem(str(get_reslute[j][i]))  # 转换后可插入表格
                    table_name.setItem(j, i, data)

        except Exception:
            print_exc()



    #这是table点击得到table中的值(显示在框子上的lineedit的所有名称,tablewidget的名称,i是自带的函数)
    def Get_Table_Click_Data(self, widget_all,table_name,i):  # 这是一个通过触发table来得到它的值的函数
        get_result=[]
        p=0
        #print()
        for widget_son in widget_all:
            widget_son.setText(table_name.item(i, p).text())
            get_result.append(table_name.item(i, p).text())
            p += 1
        return get_result



    #输入一个数据然后查找,写入,table的sql的info(一个sql的指令,显示在框子上的lineedit的所有名称)
    def Seek_table_info(self,sql_order,widget_all):
        try:
            wire_info = Execute_Sql_Get_Date(sql_order)
            #print('26=%s' % wire_info)
            p=0
            for widget_son in widget_all:
                widget_son.setText(wire_info[0][p])
                p+=1
        except Exception:
            pass
            #print()


    #得到界面上的控件(lineedit所有的名称)
    def Get_Windows_Info(self,widget_all):
        Windows_Info=[]
        for widget_son in widget_all:
            Windows_Info.append(widget_son.text())

        return Windows_Info


    #确认更改table的(所有的table的lineedit的名称,一个combox的名称,sql表的名称,)
    def Confire_Change(self,widget_all,choice,sql_table_name,sql_fields,sql_valus):

        Now_Windows_Show_info = self.Get_Windows_Info(widget_all)

        # 把界面上显示的信息，有为空的进行附值
        for i in range(len(Now_Windows_Show_info)):
            if Now_Windows_Show_info[i] == '':
                Now_Windows_Show_info[i] = 'X'

        if choice == '增加':
            if self.Message_two('确认添加？') == QMessageBox.Yes:
                sql_order = "insert into sql_table_name(sql_fiedlds) values('%s','%s','%s','%s','%s','%s','%s','%s')" \
                            % (Now_Windows_Show_info[0], Now_Windows_Show_info[1], Now_Windows_Show_info[2],
                               Now_Windows_Show_info[3], Now_Windows_Show_info[4],
                               Now_Windows_Show_info[5], Now_Windows_Show_info[6], Get_Now_Time())


        elif choice == '删除':
            #print('85')
            if self.Message_two('确认删除？') == QMessageBox.Yes:
                sql_order = "delete from %s where USER_ID='%s'" % sql_table_name,self.lin_worker_id.text()

        elif choice == '修改':
            if self.Message_two("确认要修改吗？") == QMessageBox.Yes:

                sql_order = "update MFG_USER set USER_ID='%s', USER_NAME='%s' , CARD_ID='%s' , PHONE_ADDR='%s' , USER_BUMEN='%s' ,DAIMA='%s' , " \
                            "EMAIL='%s',CDT='%s' where USER_ID='%s'" \
                            % (Now_Windows_Show_info[0], Now_Windows_Show_info[1], Now_Windows_Show_info[2],
                               Now_Windows_Show_info[3], Now_Windows_Show_info[4],
                               Now_Windows_Show_info[5], Now_Windows_Show_info[6], Get_Now_Time(),
                               self.lin_worker_id.text())

        Execute_Sql_No_Get_Date(sql_order)
        #print('333')
        self.Clear_All()


#rewrite mouse event
#重写鼠标事件
class Windows_event(QMainWindow):

    def closeEvent(self, event):
        sender = self.sender()
        #print(sender)
        #print(sender.objectName())

        #print('有关闭的动作')

    def changeEvent(self, event):
        #     # 顶层窗口激活状态改变
        #     if event.type() == QEvent.ActivationChange:
        #         #print('顶层窗口变化')
        #         #self.repaint()
        #         #self.hide()
        #     else:
        #         #print('顶层窗口不变化')
        #         #self.hide()
        #
        #     #print(self.isMinimized())
        #
        #     #这是判断是否最小化的情况
        if self.isMinimized():
            pass
            # self.hide()
            #print('最小化')
    #     else:
    #         #print('窗口不是最小化')
    #
    #     ##print(self.windowState())
    #


#keyboard event rewrite
class Keyboard_event(QMainWindow):
    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        pass
        #print("这是键盘按下事件")

    def keyReleaseEvent(self, a0: QtGui.QKeyEvent) -> None:
        #print("这是键盘上升事件")
        pass


#mouse_event_rewrite
class Mouse_event(QMainWindow):
    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        #print("鼠标移动事件")
        pass

