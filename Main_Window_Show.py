from PyQt5.QtCore import QEvent
import history_monther
import psutil
import random_question_register
import threading
import Bind_Wire_monther
import Set_Machine_monther
import wireandmachine_lh_monther
import Thing_Check_monther
import Date_Analyse_monther
import SERSON_MONTHER
import Update_Mother
import put_in
import write_password
from THING import wire_change_son
import lend_registe_monther
import Login_monther
#import set_machine_kitting
#from Tcp_Server import *
from Common_Function import *
from Main_Window import Ui_MainWindow
from Admin_Resigner_Monther import *
import subprocess,signal
import tetris

#文字闪烁的一个时间list
keep_time=[]


class mainwindow_common_function(Farther,QMainWindow):
    def common_to_lend(self,delete_sql_order,interface,column_num):
        try:
            #print('2341', admin_register_show.isHidden())

            if admin_register_show.isHidden() == True:
                #print('789')
                admin_register_show.show()
            else:
                admin_register_show.close()

            if admin_register_show.lineEdit.text() == '13579':
                try:
                    file_name = self.to_lend_function(delete_sql_order, interface, column_num)

                    admin_register_show.lineEdit.setText("")

                except Exception:
                    print_exc()



        except Exception:
            print_exc()


#这是一个写密码的界面
class write_password_class(write_password.Ui_Form,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.SubWindow | QtCore.Qt.WindowStaysOnTopHint)
        #
        # # 透明处理，移动需要拖动数字
        #
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)


    def confire(self):
        sender = self.sender()
        if serson_computer_register_show.isHidden()==False:
            serson_computer_register_show.to_lend()



#这是入库数量界面
class put_in_class(put_in.Ui_MainWindow, Farther,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lin_ok.setValidator(QtGui.QIntValidator())  # 设置只能输入int类型的数据
        self.lin_ng.setValidator(QtGui.QIntValidator())
        self.lin_new.setValidator(QtGui.QIntValidator())
        self.lin_maintain.setValidator(QtGui.QIntValidator())

        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.SubWindow | QtCore.Qt.WindowStaysOnTopHint)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

    def confire(self):
        try:

            thing_choice=[]
            thing_choice.append(self.lin_ok.text())
            thing_choice.append(self.lin_ng.text())
            thing_choice.append(self.lin_new.text())
            thing_choice.append(self.lin_maintain.text())

            for i in range(len(thing_choice)):
                if thing_choice[i] == '':
                    thing_choice[i]=0
                if int(thing_choice[i])>10000:
                    self.Message_two("物品数量超出限制")


            five_num = []
            five_num.append('OK退:'+self.lin_ok.text())
            five_num.append('NG退:'+self.lin_ng.text())
            five_num.append('新品:'+self.lin_new.text())
            five_num.append('維修:'+self.lin_maintain.text())


            for i in range(4):
                if five_num[i] in ['OK退:','NG退:','新品:','維修:']:
                    five_num[i]=five_num[i]+'0'
            #print('44=', five_num)
            five_num[1] = five_num[1] + ','


            five_num=replace_str(five_num,["[","]","'"])
            #print('46=', five_num)

            five_num=five_num.replace(',,','\n')
            five_num = five_num.replace(',', '  ')
            #print('46=',five_num)


            wire_registe_show.pushButton_5.setText(five_num)
            put_in_show.close()
        except Exception:
            print_exc()


#这是线材机种登记的界面
class wire_change_class(wire_change_son):
    def __init__(self):
        super().__init__()


    def return_mainwindow(self):
        wire_registe_show.close()
        main_window_show.show()
        main_window_show.move(self.x(),self.y())



    #这是一个重写的函数
    def change_two(self):
        self.com_method.clear()
        get_comboxdata = self.com_operation.currentText()

        if get_comboxdata == '入庫' and self.com_Thing_class.currentText() not in ['SERSON', '']:

            put_in_show.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

            self.com_method.addItems(['入庫'])
            self.stackedWidget.setCurrentIndex(0)


        elif get_comboxdata == '出庫':
            self.com_method.addItems(['加量需求', '外部借出', 'NG出庫', '報廢出庫'])
            # self.frm_thing_num.show()
            self.stackedWidget.setCurrentIndex(1)

        elif get_comboxdata == 'NG品更換':
            self.com_method.addItems(['NG品更換'])
            # self.frm_thing_num.show()
            self.stackedWidget.setCurrentIndex(1)

        elif get_comboxdata == '入庫' and self.com_Thing_class.currentText()=='SERSON':
            self.com_method.addItems(['OK退料', 'NG退料', '新品入庫', '維修入庫（OK）'])
            self.stackedWidget.setCurrentIndex(1)


        if get_comboxdata in ['出庫','NG品更換','']:
            #print('1111')
            self.stackedWidget.setCurrentIndex(1)
            self.pushButton_5.setText('')

            try:
                put_in_show.lin_maintain.clear()
                put_in_show.lin_ok.clear()
                put_in_show.lin_ng.clear()
                put_in_show.lin_new.clear()
            except Exception:
                print_exc()
    def set_thing_num_storang(self):
        storage=['OK退料','NG退料','新品入庫','維修入庫（OK）']
        s=0

        i=self.Insert_Oldserver_Data()
        #print('262',i)
        put_in_have_num=[]
        put_in_have_num.append(put_in_show.lin_ok.text())
        put_in_have_num.append(put_in_show.lin_ng.text())
        put_in_have_num.append(put_in_show.lin_new.text())
        put_in_have_num.append(put_in_show.lin_maintain.text())


        for j in put_in_have_num:

            if j!='':
                sql_order = "insert into NC_KUCUN_INOUT(TYPEOF,TXM,WUPIN_NAME,QTY,INOUT,STATUS,CDT,USERNAME,USERBUM,COMMENTS,ENG_NAME,USERPHONE,STATION,WUPIN_OK,WUPIN_NG) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
                            % (i[0], i[1], i[2], j, i[4], storage[s], Get_Now_Time(), i[6], i[7], i[8], i[9], i[10], i[11],
                               self.lin_OK_Serson.text(), self.lin_Ng_Serson.text())
                Execute_Sql_No_Get_Date(sql_order)

                if s==0:
                    #print('触发一次')
                    self.ok_ng_bf_online_num(int(put_in_have_num[0]), 0, 0, -(int(put_in_have_num[0])))
                if s==1:
                    #print('触发二次')
                    self.ok_ng_bf_online_num(0, int(put_in_have_num[1]), 0, -(int(put_in_have_num[1])))

                if s==2:
                    self.ok_ng_bf_online_num(int(put_in_have_num[2]), 0, 0, 0)
                    #print('触发三次')

                if s==3:
                    #print('触发四次')
                    self.ok_ng_bf_online_num(int(put_in_have_num[3]), -(int(put_in_have_num[3])), 0, 0)
            s+=1



    def put_in_show_function(self):
        put_in_show.show()


#这是盘点的类
class Thing_Change_class(Thing_Check_monther.thing_check_class,QMainWindow):
    def __init__(self):
        super().__init__()
        #self.move(self.x(),self.y())

#一个返回函数
    def return_mainwindow(self):
        thing_num_address_show.close()
        main_window_show.show()
        main_window_show.move(self.x(),self.y())

    def to_lend(self):
        if main_window_show.but_admin_info_show.text()=='HE':
            delete_sql_order = "delete NC_KUCUN_SUMTEST"
            common_function.common_to_lend(delete_sql_order,'NC_KUCUN_SUM',10)
        else:
            self.Message_two("此功能要特殊权限才可使用")


#這是繼承綁定線材的父類
class Bind_Wire_son(Bind_Wire_monther.Wirte_wireinfo,QMainWindow):  #
    def __init__(self):
        super().__init__()
        #self.move(self.x(),self.y())



    def Mian_Window_show(self):
        machine_lh_contrast_show.close()
        main_window_show.show()

        main_window_show.move(self.x(),self.y())


    def to_lend(self):
        delete_sql_order = "delete MACHINE_LHTEST1"
        common_function.common_to_lend(delete_sql_order,'MACHINE_LH', 17)



#這是繼承查詢耗損率的父類
class seek_thing_use_mary(Date_Analyse_monther.Choice_Condition, QMainWindow):
    def __init__(self):
        super().__init__()
        #self.move(self.x(),self.y())


    def return_mainwindow(self):
        date_analyze_show.close()
        main_window_show.show()
        main_window_show.move(self.x(),self.y())


#這是歷史記錄的繼承父類
class seek_history(history_monther.Thing_History, QMainWindow):

    def __init__(self):
        super().__init__()
        #self.move(self.x(),self.y())



    def return_mainwindow(self):
        main_window_show.show()
        history_show.close()
        main_window_show.move(self.x(),self.y())



#這是設置線材與料號綁定的地方
class wire_lh(wireandmachine_lh_monther.Wire_machine_lh):
    def __init__(self):
        super().__init__()
        #self.move(self.x(),self.y())


    def return_mainwindow(self):
        thing_lh_contrast_show.close()
        main_window_show.show()
        main_window_show.move(self.x(),self.y())


    def to_lend(self):
        delete_sql_order = "delete NC_KUCUN_LH"
        common_function.common_to_lend(delete_sql_order, 'NC_KUCUN_LH', 5)




#这是SERSON的界面的父类继承
class Serson_Set_Son(SERSON_MONTHER.SET_MACHINE_USE,QMainWindow):
    def __init__(self):
        super().__init__()
        #self.move(self.x(),self.y())


    def return_mainwindow(self):
        main_window_show.show()
        serson_computer_register_show.close()
        main_window_show.move(self.x(),self.y())


    def to_lend(self):
        delete_sql_order = "delete Serson_Table where Serson_Name not like 'LS-%'"
        common_function.common_to_lend(delete_sql_order, 'Serson_Table', 5)


#这是一个set_machine_kitting的类
class set_machine_kitting_class(Set_Machine_monther.kitting_show_class,QMainWindow):
    def __init__(self):
        super().__init__()
        #self.move(self.x(),self.y())

    def confire(self):
        try:
            get_kitting_address_false_true = []
            get_kitting_address_false_true.append(kitting_show.checkBox1300.isChecked())
            get_kitting_address_false_true.append(kitting_show.checkBox1450.isChecked())
            get_kitting_address_false_true.append(kitting_show.checkBox1600.isChecked())

            #print('douxeu:', get_kitting_address_false_true)

            kitting_data = []
            address_list = [1300, 1450, 1600]
            for i in range(3):
                if get_kitting_address_false_true[i] == True:
                    kitting_data.append(address_list[i])

            #print(kitting_data)


            if kitting_data==[]:
                kitting_data='無'

            #print("gggg",kitting_data)

            data1 = QTableWidgetItem(str(kitting_data))  # 转换后可插入表格
            set_machine_use_show.tableWidget.setItem(int(kitting_show.lab_table_rows.text()), 2, data1)

            kitting_show.close()


        except Exception:
            print_exc()



#这是机种是否使用界面的父类继承
class set_machine_use_son(Set_Machine_monther.SET_MACHINE_USE,QMainWindow):
    def __init__(self):
        super().__init__()
        #self.move(self.x(),self.y())



    def return_mainwindow(self):

        if self.Message_two('是否保存?')==QMessageBox.Yes:
            self.save_data()

        main_window_show.show()
        set_machine_use_show.close()
        main_window_show.move(self.x(),self.y())

    #得试试重载
    def TEST(self, i, j):
        try:

            # 判断是否点击在选择kitting
            if j == 2:

                kitting_show.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
                kitting_show.showNormal()

                # 把一个表格的列放在kitting_show上
                kitting_show.lab_table_rows.setText(str(i))


            else:
                #print(i, j)
                #print('test')
                #print(self.tableWidget.item(i, j).text())
                self.lin_machine.setText(self.tableWidget.item(i, 0).text())
                # self.com_machine_use.setText(self.tableWidget.item(i, 1).text())
        except Exception:
            print_exc()


#这是物品借用登记界面的父类继承
class lend_thing_son(lend_registe_monther.lend_registe_son,QMainWindow):
    def __init__(self):
        super().__init__()
        #self.move(self.x(),self.y())


    def return_mainwindow(self):
        main_window_show.show()
        lend_thing_show.close()

        main_window_show.move(lend_thing_show.x(),lend_thing_show.y())



#这是自动更新的父类
class update_class(Update_Mother.update_son,Windows_Move,QMainWindow):
    def __init__(self):
        super().__init__()
        #self.move(self.x(),self.y())

    def Close_Show(self):
        update_show.close()


#登录的父类
class Admin_Resigter_class(Login_monther.Login_class,QMainWindow):
    def __init__(self):
        super().__init__()


    #一个退出的按钮的函数
    def Exit(self):
        #print("主窗口是触发的",main_window_show.isHidden())
        if main_window_show.isHidden()==False:
            admin_register_show.close()
        else:
            #print("exit login")
            exit()


    #这是登录的界面的,输入不同的账号,得到不一样的选择
    def Login_Reslute(self):
        try:
            user_dist={}
            sql_order = "select user_id,password from nc_user"
            get_result=Execute_Sql_Get_Date(sql_order)
            #print('365',get_result)
            for user in get_result:
                user_id=str(user[0]).replace(' ','')
                password=str(user[1]).replace(' ','')

                #print(user_id,password)

                user_dist[user_id]=password

            #print(user_dist)

            #print(self.lineEdit.text() in list(user_dist.keys()))

            ##print(user_dist[self.lineEdit.text()])
            #这是一个检测已经注册过的人员,是否可以登录
            if self.lineEdit.text() in list(user_dist.keys()):
                if user_dist[self.lineEdit.text()] == self.lineEdit_2.text():
                    #print('有这个账号')
                    main_window_show.show()
                    main_window_show.move(self.x(),self.y())
                    admin_register_show.close()
                else:
                    self.Message_two('账号或密码错误')


            #没有输入账号也可以自己进行登录
            elif self.lineEdit.text() == '':

                get_num,get_sum=random_question_register.random_produce_funcation()
                #print("得到的数字",get_num,get_sum)

                QMessageBox.question(self, 'dhdfh', 'title', QMessageBox.Yes)

                main_window_show.show()
                admin_register_show.close()


            #一个自己的账号HE
            elif self.lineEdit.text()=='HE':
                main_window_show.but_admin_info_show.setText('HE')
                admin_register_show.close()
                self.Message_one('登录成功')


            #这是一个俄罗斯方块
            elif self.lineEdit.text()=='HJWZL':
                main_window_show.but_admin_info_show.setText('补天裂')
                admin_register_show.close()
                tetris.main()

            #这是登录主界面的验证
            elif self.lineEdit.text() == '24680':
                main_window_show.show()
                admin_register_show.close()

            #这些是检测导入数据是要输入密码()
            #也就是在有导入功能界面下,输入密码的界面才可以进行显示

            elif serson_computer_register_show.isHidden() == False:
                serson_computer_register_show.to_lend()



            elif machine_lh_contrast_show.isHidden()==False:
                machine_lh_contrast_show.to_lend()

            elif thing_lh_contrast_show.isHidden()==False:
                thing_lh_contrast_show.to_lend()

            elif thing_num_address_show.isHidden()==False:
                thing_num_address_show.to_lend()
            
            else:
                self.Message_two('没有账号或权限')
                self.lineEdit.setText('')
                self.lineEdit_2.setText('')


        except Exception:
            print_exc()

#这是主界面的导航继承的类
class Main_Window_class(Ui_MainWindow,Farther,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.move(self.x(),self.y())

        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        #这是设置默认为蓝色
        self.but_blue_interface.setChecked(True)
        #self.but_black_interface.setChecked(True)

        #print('160=%s'%self.but_blue_interface.isChecked())

        self.Choose_Interface()

        self.init_timer()

        self.tabWidget.setCurrentIndex(5)
        self.toolBox_navigation.setCurrentIndex(2)
        # self.Monitor_Process()

        #这是更新功能显示的
        self.Download_File()

        self.Show_Hanf_Year_No_Use_Thing()
        self.thing_security_ont_enough()

        self.set_gif(":/images/dou4.gif",self.label_8)
        self.set_gif(":/images/dou3.gif",self.lab_version_gif)




        #self.set_system_stock(":/images/77.ico")

    # def set_gif(self):
    #     self.gif=QMovie(":/images/dou1.gif")
    #     self.gif.setScaledSize(self.label_8.size())
    #     #self.gif.setScaledSize(QSize(150, 150))
    #     self.label_8.setMovie(self.gif)
    #     self.gif.start()
    #
    #     self.gif1=QMovie(":/images/dou4.gif")
    #     self.gif1.setScaledSize(self.lab_version_gif.size())
    #     #self.gif.setScaledSize(QSize(150, 150))
    #     self.lab_version_gif.setMovie(self.gif1)
    #     self.gif1.start()
    #

    #这是主界面,功能选择后显示的界面,这是一个,可以
    def eng2_2_funcation_choice(self):
        sender = self.sender()
        choice_function=sender.objectName()

        #物品登记

        if choice_function=="but_thing_resigner":
            wire_registe_show.show()
            wire_registe_show.move(self.x(),self.y())

            #print('431',wire_registe_show.isHidden())
            if wire_registe_show.isHidden()==False:

                self.tcp_test()

        #机种料号绑定
        elif choice_function=="but_wire_machine_bind":
            machine_lh_contrast_show.show()
            #machine_lh_contrast_show.move(self.x(),self.y())

            machine_lh_contrast_show.move(self.x(),self.y())
            print('123==',machine_lh_contrast_show.geometry())

        #serson与computer的登记
        elif choice_function=="but_serson_computer_resigner":
            serson_computer_register_show.show()
            serson_computer_register_show.move(self.x(),self.y())
        #这是耗损查询
        elif choice_function=="but_lost_seek":
            date_analyze_show.show()
            date_analyze_show.move(self.x(),self.y())
        #历史记录查询
        elif choice_function=="but_history":
            history_show.show()
            history_show.move(self.x(),self.y())
        #物品数量与位置，盘点
        elif choice_function=="but_newthing_registe":
            thing_num_address_show.show()
            thing_num_address_show.move(self.x(),self.y())
        #机种是否使用
        elif choice_function=="but_machine_use":
            set_machine_use_show.show()
            set_machine_use_show.move(self.x(),self.y())
        #借用登记
        elif choice_function=="but_lend_registe":
            lend_thing_show.show()
            lend_thing_show.move(self.x(),self.y())
        #物品料号与价格
        elif choice_function=="but_thing_lh":
            thing_lh_contrast_show.show()
            thing_lh_contrast_show.move(self.x(),self.y())
        #tcp的使用
        elif choice_function=="but_tcp_show":
            self.tcp_test()
        #更新界面
        elif choice_function=="but_check_update":
            update_show.raise_()
            update_show.showNormal()
            update_show.show()


        #这是一个测试功能
        if choice_function not in ["but_tcp_show","but_check_update"]:
            main_window_show.close()


    def Admin_Change(self):
        pass

    def Navigation_Num(self,num):
        #print(num)
        pass


    #tcp连接,大概有
    def tcp_server_main(self):
        try:
            #print('tcp有触发')
            # 1.创建套接字
            tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # 2.绑定端口
            addr = ("", 8866)
            tcp_server_socket.bind(addr)

            # 3.监听链接
            tcp_server_socket.listen(128)

            # 4.接收别人的连接
            client_socket, client_addr = tcp_server_socket.accept()

            for i in range(50):
                # client_socket用来为这个客户端服务

                # 5.接收对方发送的数据
                recv_data = client_socket.recv(10240)

                #print("接收到的数据：%s" % recv_data.decode("utf-8"))



                #self.but_tcp_text.setText(recv_data.decode("utf-8"))
                #self.but_tcp_text.setStyleSheet("*{border-radius: 10px;font-size: 15px;color:red;}")
                wire_registe_show.lab_tcp_show.setText(recv_data.decode("utf-8"))
                #self.tabWidget.setCurrentIndex(9)
                #update_show.show()
                #self.Message_one(recv_data.decode("utf-8"))

                # 6.给对方发送数据
                client_socket.send("OK rec".encode("utf-8"))

                # 7.关闭套接字

                if recv_data.decode('utf-8')=='close':
                    client_socket.close()
                    tcp_server_socket.close()
                    wire_registe_show.lab_tcp_show.setText('')


        except Exception:
            print_exc()


    def tcp_test(self):
        try:
            t1=threading.Thread(target=self.tcp_server_main)
            t1.start()

            #进入物品登记后,主界面的颜色自动变成黑色
            # self.but_black_interface.setChecked(True)
            # self.Choose_Interface()


            # if self.but_admin_info_show.text()=='HE':
            #     self.Message_one('测试成功')
            # else:
            #     self.Message_one('没有权限')
            #self.but_thing_resigner.setCursor()
        except Exception:
            print_exc()


    #这是导航选择显示出什么界面
    def Set_Natigation_Window(self):
        sender = self.sender()
        #print('选择的界面',sender.text())

        if sender.text()=='界面样式':
            #print('界面9')
            self.tabWidget.setCurrentIndex(9)

        #这是ENG2-1的主界面
        elif sender.text()=='主界面 ':
            self.tabWidget.setCurrentIndex(4)

        elif sender.text()=='主界面':
            self.tabWidget.setCurrentIndex(5)

        elif sender.text()=='功能介绍':
            self.tabWidget.setCurrentIndex(1)

        elif sender.text()=='线体尺寸管理':
            self.tabWidget.setCurrentIndex(2)
            self.Line_and_Size_Show()

        elif sender.text()=='更改':
            self.tabWidget.setCurrentIndex(3)
            self.table_show()

        elif sender.text()=='版本':
            self.tabWidget.setCurrentIndex(8)
            #print('版本11')


        elif sender.objectName()=='but_admin_register' or sender.objectName()=='but_admin_info_show':
            admin_register_show.show()
            admin_register_show.move(self.x(),self.y())
            admin_register_show.lineEdit.clear()
            admin_register_show.lineEdit_2.clear()

        elif sender.text()=='server ip':
            print("gggggggggggg")
            self.tabWidget.setCurrentIndex(6)


    #这是得到了所有正在运行的PID号
    # def Monitor_Process(self):
    #     processname = 'python.exe'
    #     pl = psutil.pids()
    #
    #     Process = {}
    #
    #     for pid in pl:
    #         Process[psutil.Process(pid).name()]=pid
    #
    #     #print("213=%s" % Process)
    #     #print(len(Process))
    #
    #     if processname not in list(Process.keys()):
    #         #main_window_show.show()
    #         #print("没有两个程序")
    #
    #     else:
    #         if self.Message_two("程序已重复打开\n是否关闭正在运行的程序\n重新打开")==QMessageBox.Yes:
    #
    #             cmd ="taskkill /pid %d -f"% int(Process['python.exe'])
    #             #print(cmd)
    #             rc = os.system(cmd)
    #             exit()




    #这是更换界面的函数
    def Choose_Interface(self):
        try:
            styleFile=""
            mainstyleFile=""
            if self.but_white_interface.isChecked()==True:
                styleFile = r'd:\config\white_style.qss'
            elif self.but_black_interface.isChecked()==True:
                styleFile = r'd:\config\black_style.qss'
            elif self.but_blue_interface.isChecked()==True:
                styleFile = r'd:\config\blue_style.qss'
                mainstyleFile=r'd:\config\Main_Window_style.qss'

            qssStyle = CommonHelper.readQss(styleFile)

            if self.but_blue_interface.isChecked()==True:
                mainqssStyle = CommonHelper.readQss(mainstyleFile)
                self.setStyleSheet(mainqssStyle)
            else:
                self.setStyleSheet(qssStyle)


            history_show.setStyleSheet(qssStyle)
            machine_lh_contrast_show.setStyleSheet(qssStyle)
            set_machine_use_show.setStyleSheet(qssStyle)
            date_analyze_show.setStyleSheet(qssStyle)
            thing_lh_contrast_show.setStyleSheet(qssStyle)
            lend_thing_show.setStyleSheet(qssStyle)
            thing_num_address_show.setStyleSheet(qssStyle)
            serson_computer_register_show.setStyleSheet(qssStyle)

        except Exception:
            print_exc()



    #这是线体与尺寸的管理
    def Line_and_Size_Show(self):
        try:
            sql_order="select Line_Name,Line_Use from Line_Size_All WHERE Line_Name!=''"
            Common_Table.Set_Table(self,sql_order,self.tab_line,2)

            sql_order="select Size_Name,Size_Use from Line_Size_All where Size_Name!=''"

            Common_Table.Set_Table(self,sql_order, self.tab_size, 2)
        except Exception:
            print_exc()

    #线体双击得到数据,显示在lineedit上
    def Line_Size_Get_Double_Click_Data(self,i,j):
        try:
            sender=self.sender()

            if sender.objectName()=='tab_line':
                widget_all=[self.lin_line,self.lin_line_use]
                Common_Table.Get_Table_Click_Data(self,widget_all,self.tab_line,i)
            else:
                widget_all = [self.lin_size, self.lin_size_use]
                Common_Table.Get_Table_Click_Data(self, widget_all, self.tab_size, i)
        except Exception:
            print_exc()


        #判断窗口是否打开
        # wire_registe_show.isWindow()

    #这是体更改Ok
    def Line_Size_Confire(self):
        try:
            sender=self.sender()
            if sender.objectName()=='but_line_confire':
                 widget_all = [self.lin_line, self.lin_line_use]
                 table_fields=['Line_Name','Line_Use','Line_Time']
                 choice=self.com_line_choice
            else:
                widget_all = [self.lin_size, self.lin_size_use]
                table_fields = ['Size_Name', 'Size_Use','Size_Time']
                choice = self.com_size_choice

            Now_Windows_Show_info = Common_Table.Get_Windows_Info(self, widget_all)

            # 把界面上显示的信息，有为空的进行附值
            for i in range(len(Now_Windows_Show_info)):
                if Now_Windows_Show_info[i] == '':
                    Now_Windows_Show_info[i] = 'X'

            if choice.currentText() == '增加':
                if self.Message_two('确认添加？') == QMessageBox.Yes:
                    sql_order = "insert into Line_Size_All(%s,%s,%s) values('%s','%s','%s')"% (table_fields[0],table_fields[1],table_fields[2],Now_Windows_Show_info[0], Now_Windows_Show_info[1],Get_Now_Time())

            elif choice.currentText() == '删除':
                if self.Message_two('确认删除？') == QMessageBox.Yes:
                    sql_order = "delete from Line_Size_All where %s='%s'" % (table_fields[0],widget_all[0].text())

            elif choice.currentText() == '修改':
                if self.Message_two("确认要修改吗？") == QMessageBox.Yes:
                    sql_order = "update Line_Size_All set %s='%s', %s='%s' where %s='%s'" \
                                % (table_fields[0],Now_Windows_Show_info[0], table_fields[1],Now_Windows_Show_info[1],table_fields[0], widget_all[0].text())

            ##print(sql_order)
            Execute_Sql_No_Get_Date(sql_order)
            ##print('333')
            self.Line_and_Size_Show()
            self.Clear_All()
        except Exception:
            print_exc()

    #显示安全库存不足的物品
    def thing_security_ont_enough(self):
        sql_ordr="select WUPIN_NAME FROM NC_KUCUN_SUM where convert(int,QTY_OK)<convert(int,SECUREQTY)"
        get_result=Execute_Sql_Get_Date(sql_ordr)
        ##print('739',get_result)

        i = 1
        for x in get_result:
            self.text_thing_enough_show.moveCursor(QTextCursor.End)
            self.text_thing_enough_show.insertPlainText(str(i) + '.' + x[0] + '\n')
            i += 1


    #这是显示警示区半年未使用物品
    def Show_Hanf_Year_No_Use_Thing(self):
        try:
            All_One_Year_Use =[]
            All_Thing=[]

            now_time = str(datetime.now())[:len(str(datetime.now())) - 7]+':000'
            aaa = self.Date_delete(182, now_time)
            #print(aaa)

            sql_order="select distinct WUPIN_NAME from NC_KUCUN_INOUT where CDT between '%s' and '%s' order by WUPIN_NAME desc"%(aaa[0],now_time)
            get_reslute=Execute_Sql_Get_Date(sql_order)
            for x in get_reslute:
                All_One_Year_Use.append(x[0])

            #print(sql_order)
            ##print(get_reslute)
            ##print(len(get_reslute))

            sql_order="select distinct WUPIN_NAME from NC_KUCUN_LH"
            get_reslute = Execute_Sql_Get_Date(sql_order)
            for x in get_reslute:
                All_Thing.append(x[0])

            #Have_Thing = list(set(All_One_Year_Use).intersection(set(All_Thing)))

            difference_Thing = list(set(All_Thing).difference(set(All_One_Year_Use)))
            #print(set(All_Thing))
            #print('sh相同的东西=%s'%difference_Thing)
            #print(len(difference_Thing))

            i=1
            for x in difference_Thing:
                self.text_warning.moveCursor(QTextCursor.End)
                self.text_warning.insertPlainText(str(i)+','+x+'\n')
                i+=1
            self.text_warning.moveCursor(QTextCursor.Start)
        except Exception:
            print_exc()

    #是否有物品没有归还
    def thing_is_not_return(self):

        time_now = Get_Now_Time()[11:19]
        if time_now in ['20:00:00', '08:00:00', '12:00:00', "00:00:00", '09:27:00']:
            sql_order = "select * from Lend_Registe where Lend_Statius='未歸還'"
            get_result = Execute_Sql_Get_Date(sql_order)
            if len(get_result)>0:
                return True




    #时间显示,更新一个时间
    def update_time(self):
        self.lcd_clock.display(time.strftime("%X", time.localtime()))

        if len(keep_time) == 1:
            self.pushButton_39.setStyleSheet('*{color:red;}')
            self.lab_version.setStyleSheet('*{color:red;}')
        elif len(keep_time) == 2:
            self.pushButton_39.setStyleSheet('*{color:white;}')
            self.lab_version.setStyleSheet('*{color:white;}')
            keep_time.clear()

        keep_time.append(1)
        ##print('时间:',time.localtime())



    #这是改变警示区显示的
    def Change_Warning_Show(self):
        try:

            sender = self.sender()
            #print('444=', sender)
            ggg=sender.objectName()

            #print('431',ggg)

            starck_warning_index=self.starck_warning.currentIndex()
            #print(starck_warning_index)
            if sender.text()=='左边' and starck_warning_index>0:
                self.starck_warning.setCurrentIndex(starck_warning_index-1)

            if sender.text()=='右边' and starck_warning_index<3:
                self.starck_warning.setCurrentIndex(starck_warning_index+1)
            #print(sender.text())
        except Exception:
            print_exc()

    def Exit(self):
        os._exit(0)


    #下载every_day_work,
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

    # 上传every_day_work,上传ftp的东西在10.178.1.98
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


    #确认人员账号的更改
    def confire_admin_reslute(self):
        try:
            widget_all = [self.lin_worker_id, self.lin_worker_name, self.lin_card_id, self.lin_phone,
                          self.lin_bumen_name, self.lin_bumen_id, self.lin_email]

            Now_Windows_Show_info = Common_Table.Get_Windows_Info(self,widget_all)

            # 把界面上显示的信息，有为空的进行附值
            for i in range(len(Now_Windows_Show_info)):
                if Now_Windows_Show_info[i] == '':
                    Now_Windows_Show_info[i] = 'X'

            if self.com_adnim_choice.currentText() == '增加':
                if self.Message_two('确认添加？') == QMessageBox.Yes:
                    sql_order = "insert into MFG_USER(USER_ID,USER_NAME,CARD_ID,PHONE_ADDR,USER_BUMEN,DAIMA,EMAIL,CDT) " \
                                "values('%s','%s','%s','%s','%s','%s','%s','%s')" \
                                % (Now_Windows_Show_info[0], Now_Windows_Show_info[1], Now_Windows_Show_info[2],
                                   Now_Windows_Show_info[3], Now_Windows_Show_info[4],
                                   Now_Windows_Show_info[5], Now_Windows_Show_info[6], Get_Now_Time())

            elif self.com_adnim_choice.currentText() == '删除':
                #print('85')
                if self.Message_two('确认删除？') == QMessageBox.Yes:
                    sql_order = "delete from MFG_USER where USER_ID='%s'" % self.lin_worker_id.text()


            elif self.com_adnim_choice.currentText() == '修改':
                if self.Message_two("确认要修改吗？") == QMessageBox.Yes:
                    #print('102=%s' % Now_Windows_Show_info)
                    #print('103=%s' % Ago_Now_Windows_Show_info)
                    sql_order = "update MFG_USER set USER_ID='%s', USER_NAME='%s' , CARD_ID='%s' , PHONE_ADDR='%s' , USER_BUMEN='%s' ,DAIMA='%s' , " \
                                "EMAIL='%s',CDT='%s' where USER_ID='%s'" \
                                % (Now_Windows_Show_info[0], Now_Windows_Show_info[1], Now_Windows_Show_info[2],
                                   Now_Windows_Show_info[3], Now_Windows_Show_info[4],
                                   Now_Windows_Show_info[5], Now_Windows_Show_info[6], Get_Now_Time(),
                                   self.lin_worker_id.text())

            Execute_Sql_No_Get_Date(sql_order)
            #print('333')
            self.Clear_All()

        except Exception:
            print_exc()

    # 确认人员账号的显示
    def table_show(self):
        sql_order = "select USER_ID,USER_NAME,CARD_ID,PHONE_ADDR,USER_BUMEN,DAIMA,EMAIL,CDT from MFG_USER ORDER BY CDT DESC"
        Common_Table.Set_Table(self,sql_order,self.tab_user_all,8)

    # 确认人员账号的显示
    def admin_double_click(self,i,j):
        widget_all=[self.lin_worker_id,self.lin_worker_name,self.lin_card_id,self.lin_phone,self.lin_bumen_name,self.lin_bumen_id,self.lin_email]
        Common_Table.Get_Table_Click_Data(self, widget_all,self.tab_user_all,i)

    # 确认人员账号的显示
    def Seek_User_Info(self):
        sql_order = "select USER_NAME,CARD_ID,PHONE_ADDR,USER_BUMEN,DAIMA,EMAIL from MFG_USER where USER_ID='%s'" % (
            self.lin_worker_id.text())

        widget_all = [self.lin_worker_name, self.lin_card_id, self.lin_phone, self.lin_bumen_name,
                      self.lin_bumen_id, self.lin_email]

        Common_Table.Seek_table_info(self,sql_order,widget_all)


    def closeEvent(self, event):
        try:
            sender = self.sender()
            #print('触发的东西',sender.event())
            #print(sender.objectName())
            print(event)

            print('有关闭的动作')
            #os._exit(0)
        except Exception:
            print_exc()


    # 确认人员账号的显示
    def Clear_All(self):
    #这是人员工号的清除
        self.lin_worker_id.setText('')
        self.lin_worker_name.setText('')
        self.lin_card_id.setText('')
        self.lin_phone.setText('')
        self.lin_bumen_name.setText('')
        self.lin_bumen_id.setText('')
        self.lin_email.setText('')
        self.table_show()

    #这是线体与尺寸的清除
        self.lin_size_use.clear()
        self.lin_size.clear()
        self.lin_line.clear()
        self.lin_line_use.clear()





if __name__ == '__main__':


    #怎样从主界面得到ip还有password

    app = QApplication(argv)

    common_function=mainwindow_common_function()

    # print('得到一个数值',Main_Window_class.lin_server_ip.text())

    set_server_ip_admin_password_database('127.0.0.1', 'sa', '123456', 'management')

    #这是入库的数量输入界面
    put_in_show=put_in_class()

    #这是线材登记的界面
    wire_registe_show=wire_change_class()

    #这是查询历史界面
    history_show= seek_history()

    #这是设置机种所胡使用的线材
    machine_lh_contrast_show = Bind_Wire_son()

    #这是输入1300,1450界面的窗口
    kitting_show=set_machine_kitting_class()


    #这是人员选择机种是否出现
    set_machine_use_show = set_machine_use_son()  #机种是否使用界面

    #这是查询耗损的界面
    date_analyze_show=seek_thing_use_mary()

    #这是物品与料号的对应界面
    thing_lh_contrast_show=wire_lh()

    #这是物品借用的界面
    lend_thing_show=lend_thing_son()

    #这是盘点的界面
    thing_num_address_show = Thing_Change_class()

    #这是Serson界面
    serson_computer_register_show=Serson_Set_Son()

    #这是自动更新的父类
    update_show=update_class()

    #账号登录
    admin_register_show=Admin_Resigter_class()
    admin_register_show.show()

    write_password_show=write_password_class()
    # mytimeshow= time_show()
    # mytimeshow.show()

    # 主界面
    main_window_show = Main_Window_class()

    #main_window_show.show()

    exit(app.exec())