from PyQt5.QtCore import QEvent

from wire_ui import Ui_MainWindow  #从登记的界面导出
import history_monther
import Bind_Wire_monther
import Set_Machine_monther
import wireandmachine_lh_monther
import Thing_Check_monther
import Date_Analyse_monther
import SERSON_MONTHER
import put_in
from Common_Function import *

#   from timeshow import LcdTime

list = []
My_Machine_Wire=[]  #保存人员选择的物品的LH
Confirm_Reslute=[]
lines = []  # 从config得到线体
sizes = []  # 得到新产品大小
input_windows = []  # 储存旧数据的数组
curruct_text = []  # 确认数据是否输入完全
new_input_window = []  # 储存新数据的数组
old_input_window=[]   #储存旧数据的东西
Set_machine = []    # 储存得到的机种
Get_pow_ff_dri = []
Set_size = []
#  #print('当前时间是%s'%time_now)
time_now=datetime.now()
Time_now=str(time_now)[:10]




class put_in_class(put_in.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def confire(self):
        try:

            put_in_show.close()

            #print('3r34r34r34')


        except Exception:
            print_exc()








class wire_change_son(Ui_MainWindow,Farther,QMainWindow):
    global list
    global lines
    global input_windows
    global curruct_text
    global new_input_window
    global Set_machine



    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.com_Thing_class.addItems(['', '測試線','電源線', '驅動板', 'FFC', 'SERSON', 'INV_電源線','整機線材','其他（机种不用选）'])
        self.com_lines.addItems(Read_load_info())
        self.com_size.addItems(Read_loadsize_info())

#        self.com_lines.addItem()
        #self.com_method.addItems(['新品入庫', '新品登记'])
        #self.setWindowFlags(Qt.FramelessWindowHint) #设置无边框
        self.lin_Thing_barcode.setFocus() #得到焦点
        #self.lab_Thing_truename.adjustSize()
        #self.center()   #窗口居中显示
        #self.center_test()
        self.wire_show_test.setAlignment(Qt.AlignCenter)
        self.lab_Thing_truename.setWordWrap(True)#设置label可以换行
        self.wire_show_test.setWordWrapMode(True)

        self.wire_show_test.moveCursor(QTextCursor.End)

        #self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
#        self.but_lookfor.pressed.connect(self.Date_Analyse_show)
#        self.but_new_data.pressed.connect(self.Serson_Set_Show)

        #这是一个时间的显示
        self.init_timer()

        self.Set_Comment_see()
        #禁止窗口关闭与放大
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowMaximizeButtonHint)



        #self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)



    # def showMinimized(self):
    #     super().showMinimized()
    #     self.close()

    # def changeEvent(self, event):
    #     # 顶层窗口激活状态改变
    #     if event.type() == QEvent.ActivationChange:
    #         #print('我是什么东村')
    #         self.showNormal()


#  通过備品人员输入的TXM得到它的LH

#        self.setCentralWidget(self.frame_main)

    #这是调动入库的界面的函数
    def put_in_show_function(self):
        put_in_show.show()


    #这是设置wyj焦点的函数
    def set_focus(self):
        self.lin_admin_password.setFocus()

        if self.com_method.currentText() in ['OK退料1']:
            self.lin_OK_Serson.setFocus()

        elif self.com_method.currentText() in ['NG退料1']:
            self.lin_NG_Serson.setFocus()



    def Get_Thing_Txm(self):
        try:
            IS_Complte=False
            Thing_Barcode=Determine_wire(self.lin_Thing_barcode.text())
            sql_order = "select LH from NC_KUCUN_LH where TXM='%s'"%Thing_Barcode
            GET_RESLUTE=Execute_Sql_Get_Date(sql_order)
            #print('173=%s'%My_Machine_Wire)
            #print('177=%s'%GET_RESLUTE)

            if GET_RESLUTE[0][len(GET_RESLUTE[0])-1] in My_Machine_Wire:
                IS_Complte=True
            else:
                IS_Complte=False
                self.Message_one('比对不正确')
            return IS_Complte

        except Exception:
            print_exc()
            self.lin_Thing_barcode.setFocus()



#  把数据录入旧的的保存位置
    def Insert_Oldserver_Data(self):
        input_windows.clear()
        Thing_name=Determine_wire(self.lin_Thing_barcode.text())
        # 得到物品的名称，条形码，全称
        sql_order1="select TYPEOF,TXM,WUPIN_NAME FROM NC_KUCUN_SUM where TXM='%s'" %Thing_name
        old_Thing=Execute_Sql_Get_Date(sql_order1)
        #print('old_Thing=%s'%old_Thing)
        # 得到换取人员的信息
        sql_order2= "select USER_NAME,USER_BUMEN,PHONE_ADDR from MFG_USER where USER_ID='%s'" %(self.lin_worker_num.text())
        old_worker=Execute_Sql_Get_Date(sql_order2)
        #print('old_worker=%s' %old_worker)
        input_windows.append(old_Thing[0][0])
        input_windows.append(old_Thing[0][1])
        input_windows.append(old_Thing[0][2])

        input_windows.append(self.lin_quantiy.text())


        input_windows.append(self.com_operation.currentText())
        input_windows.append(self.com_method.currentText())

        #input_windows.append(str(datetime.now()))
        input_windows.append(old_worker[0][0])
        input_windows.append(old_worker[0][1])

        input_windows.append(self.lin_comments.text())
        input_windows.append('張莉')
        input_windows.append(old_worker[0][2])

        input_windows.append(self.com_lines.currentText())
        return input_windows

#  把数据录入新的的保存位置
    def Insert_New_Data(self):

        new_input_window.clear()

        #new_input_window.append(self.com_Thing_class.currentText())#从桌面得到物品种类
        new_input_window.append(self.lab_Thing_truename.text())
        #new_input_window.append(self.com_Thing_class.currentText())
        new_input_window.append(self.com_Thing_class.currentText())
        new_input_window.append(self.com_machine.currentText())
        new_input_window.append(self.com_systems.currentText().split('(')[0])
        #print('170=%s'%Get_pow_ff_dri)

        # Thing_AllName=self.wire_show_test.toPlainText().split("\n    ")
        # #print('216=%s'%Thing_AllName[len(Thing_AllName)-1])
        # new_input_window.append(Thing_AllName[len(Thing_AllName)-1])

        new_input_window.append(self.lab_Thing_truename.text())

        #new_input_window.append(Get_pow_ff_dri[0])
        #new_input_window.append(self.wire_show_test.toPlainText().split("\n    ")[len(self.wire_show_test.toPlainText().split("\n    "))-1])
        #print('148=%s'%self.wire_show_test.toPlainText().split("\n    "))
        new_input_window.append(self.lin_quantiy.text())
        new_input_window.append(self.com_operation.currentText())
        new_input_window.append(self.com_method.currentText())
        new_input_window.append(self.lab_worker_name.text())
        new_input_window.append(self.lab_phone.text())
        new_input_window.append(self.lin_worker_num.text())
        new_input_window.append(self.com_lines.currentText())
        new_input_window.append(self.lin_comments.text())
        new_input_window.append(str(datetime.now())[:len(str(datetime.now()))-3])

        return new_input_window

#  从NC_KUCUN_KUMTEST得到ok的数量，NG的数量，报废的数量，在线上的数量
    def Get_kucun_num(self):
        #  修改
        sql_order = "select QTY_OK,QTY_NG,QTY_BF,QTY_ONLINE from NC_KUCUN_SUM where TXM='%s'" % (
            Determine_wire(self.lin_Thing_barcode.text()))
        #print('160=%s' % sql_order)

        get_reslut = Execute_Sql_Get_Date(sql_order)
        return get_reslut


# ok的ng的BF的数量有一些是空白的，所以把空白置0
    def ok_ng_bf_online_num(self,ok_num,ng_num,bf_num,on_num):
        get_ok_ng_online = self.Get_kucun_num()
        #print('167=%s'%get_ok_ng_online)
        ok=get_ok_ng_online[0][0]
        if ok=='':
            ok=0
        ng = get_ok_ng_online[0][1]
        if ng == '':
            ng = 0
        bf = get_ok_ng_online[0][2]
        if bf == '':
            bf = 0
        online = get_ok_ng_online[0][3]
        if online == '':
            online = 0
        ok_kucun = int(ok) + ok_num
        ng_kucun = int(ng) + ng_num
        bf_kucun = int(bf) + bf_num
        online_kucun = int(online) + on_num
        #print('ok=%d ng=%d bf=%d online=%d' %(ok_kucun,ng_kucun,bf_kucun,online_kucun))
        # 把得到的数量进行加减，然后录入数据库
        sql_order1 = "update NC_KUCUN_SUM set QTY_OK=%s,QTY_NG=%s,QTY_BF=%s,QTY_ONLINE=%s where TXM='%s'" % (
            str(ok_kucun), str(ng_kucun), str(bf_kucun), str(online_kucun), Determine_wire(self.lin_Thing_barcode.text()))
        Execute_Sql_No_Get_Date(sql_order1)


#  根据人员选择的（入库，出库）把得到的物品数量进行加减
    def Set_think_num(self,thing_operat):
        thing_num=int(self.lin_quantiy.text())
        if thing_operat == '出庫':
            if self.com_method.currentText()=='報廢出庫':
                self.ok_ng_bf_online_num(0, -(thing_num), thing_num, 0)
            elif self.com_method.currentText()=='NG出庫':
                self.ok_ng_bf_online_num(0, -(thing_num), thing_num, 0)
            else:
                self.ok_ng_bf_online_num(-(thing_num), 0, 0, thing_num)

        elif thing_operat=='入庫':
            if self.com_method.currentText()=='新品入庫':
                self.ok_ng_bf_online_num(thing_num, 0, 0, 0)
            elif self.com_method.currentText()=='維修入庫（OK）':
                self.ok_ng_bf_online_num(thing_num,-(thing_num),0,0)
            elif self.com_method.currentText()=='OK退料':
                self.ok_ng_bf_online_num(thing_num,0, 0, -(thing_num))
            elif self.com_method.currentText()=='NG退料':
                self.ok_ng_bf_online_num(0,thing_num, 0, -(thing_num))

        elif thing_operat=='NG品更換':
            self.ok_ng_bf_online_num(-(thing_num), thing_num, 0, 0)

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








#  确认正式录入数据
    def Confirm_Reslut(self):
        self.Thing_Showinfo()
        try:
            curruct_text.append(self.com_Thing_class.currentText())
            if self.com_operation.currentText()!='入庫':
                curruct_text.append(self.lin_quantiy.text())
            curruct_text.append(self.com_operation.currentText())

            #curruct_text.append(self.lin_worker_num.text())
            curruct_text.append(self.lab_worker_name.text())
            curruct_text.append(self.com_lines.currentText())

            #curruct_text.append(self.lin_Thing_barcode.text())
            curruct_text.append(self.lab_wire_name.text())

            ##print('167=%s' % self.wire_show_test.toPlainText().split("\n    ")[2])
            #print(type(self.wire_show_test.toPlainText()))

            if self.com_Thing_class.currentText() == '其他（机种不用选）' or self.com_Thing_class.currentText()=='' and self.com_operation.currentText()=='入庫':

                if Determine_wire(self.lin_Thing_barcode.text())=='LS-000':
                    #curruct_text.append(self.lin_OK_Serson.text())
                    pass

            # 检验是否完全输入数据
            # 三个隐藏输入框是否要检查
            if self.com_Thing_class.currentText() not in  ['其他（机种不用选）','','SERSON'] and (self.com_method.currentText() == '加量需求' or self.com_operation.currentText() == 'NG品更換') \
                    and self.com_lines.currentText()[:2] in ['SK', 'FT', 'JI', 'BM', 'IA', 'AG','BI','CT','FQ','IN','OQ','RP']:

                curruct_text.append(self.com_size.currentText())
                curruct_text.append(self.com_machine.currentText())
                curruct_text.append(self.com_systems.currentText().split('(')[0])
                #curruct_text.append(self.wire_show_test.toPlainText().split("\n    ")[len(self.wire_show_test.toPlainText().split("\n    "))-1])

            #print('236=%s'%curruct_text)
        except Exception:
            print_exc()
            #print_exc()

        try:
            #print('182=%s'%curruct_text)
            #self.Message_two(str(curruct_text))
            if '' not in curruct_text and '此系统没有这种線材' not in curruct_text:
        # 这是确认密码
                if self.lin_admin_password.text()=='admin123':
        #检查物品数量是否足够
                    if self.Check_Thing_Is_Zero()==True:
        # 确认是否录入,还有检查物品是否有库存
                        if self.Message_two('确认录入') == QMessageBox.Yes:
        # 分别是存入有机种的新数据还是旧数据
        # 这是没有选择机种的历史记录


        #这是判断数据是要在这存入新数据库中
                            if self.com_Thing_class.currentText() not in  ['其他（机种不用选）','','SERSON'] \
                                    and (self.com_method.currentText() == '加量需求' or self.com_operation.currentText() == 'NG品更換') \
                                    and self.com_lines.currentText()[:2] in ['SK', 'FT', 'JI', 'BM', 'IA', 'AG','BI','CT','IN','FQ','OQ','RP']:



        ##print('旧数据是',old_input_window.append(curruct_text))
        # 修改
                                j = self.Insert_New_Data()
                                #print('195=%s' % j)
                                sql_order="insert into New_History(worker_choice_wire,TYPEOF,machine_name,systems,wire_name,wire_barcode,inout_num,INOUT," \
                                          "STATUS,worker_name,worker_num,worker_phone,STATION,comments,CDT) values" \
                                          "('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
                                          %(j[0],j[1],j[2],j[3],j[4],self.lin_Thing_barcode.text(),j[5],j[6],j[7],j[8],j[9],j[10],j[11],j[12],j[13])
                                Execute_Sql_No_Get_Date(sql_order)


                            # 这是存入旧数据中
                            #else:

                            i=[]
                            i=self.Insert_Oldserver_Data()
                            #print('309=%s'%i)

        #这是一个SERSON的数量设置为1
                            if self.lin_Thing_barcode.text()[:2] in ['LS','UP']:
                                i[3]=1

                            if self.com_operation.currentText() != '入庫' or self.com_Thing_class.currentText()=='SERSON':
                                sql_order = "insert into NC_KUCUN_INOUT(TYPEOF,TXM,WUPIN_NAME,QTY,INOUT,STATUS,CDT,USERNAME,USERBUM,COMMENTS,ENG_NAME,USERPHONE,STATION,WUPIN_OK,WUPIN_NG) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
                                          %(i[0],i[1],i[2],i[3],i[4],i[5],Get_Now_Time(),i[6],i[7],i[8],i[9],i[10],i[11],self.lin_OK_Serson.text(),self.lin_Ng_Serson.text())
                                Execute_Sql_No_Get_Date(sql_order)

        # 把得到的物品进行加减，存入数据库中，库存
                                thing_number = self.com_operation.currentText()
                                if self.com_Thing_class.currentText()=='SERSON':
                                    thing_number =1

                                self.Set_think_num(thing_number)

                            else:
                                self.set_thing_num_storang()

        #  把物品的變化情況進行記錄
        #  這是得到物品的數量
                            sql_order = "select QTY_OK,QTY_NG,QTY_BF,QTY_ONLINE from NC_KUCUN_SUM where WUPIN_NAME='%s'" % (
                                self.lab_Thing_truename.text())
                            Get_Thing_Online_Num = Execute_Sql_Get_Date(sql_order)
                            #print('348=%s' % sql_order)
                            #print(Get_Thing_Online_Num)

                            sql_order = "insert into History_Thing_Num(Thing_Name,QTY_OK,QTY_NG,QTY_BF,QTY_ONLINE,People_Method,People_input_num,CDT) values('%s','%s','%s','%s','%s','%s','%s','%s')" % (self.lab_Thing_truename.text(), Get_Thing_Online_Num[0][0], Get_Thing_Online_Num[0][1], Get_Thing_Online_Num[0][2], Get_Thing_Online_Num[0][3],self.com_method.currentText(),self.lin_quantiy.text(),Get_Now_Time())
                            #print('352=%s' % sql_order)
                            Execute_Sql_No_Get_Date(sql_order)


                            if self.com_operation.currentText()!='入庫' or self.com_Thing_class.currentText()=='SERSON':
                                round_num = int(self.lin_quantiy.text())  # 这是得到换线人输入的数量信息
                            else:
                                round_num=0

    #Serson状态更改
                            self.Serson_Statius_Change()

    # 这是SERSON数量的多次使用，登记完之后输入的信息不会消失
                            if self.lin_Thing_barcode.text()[:3] in ['LS-'] and int(self.lin_quantiy.text()) >0:
                                round_num -= 1
                                self.lin_quantiy.setText(str(round_num))
                                self.lin_Ng_Serson.setText('')
                                self.lin_OK_Serson.setText('')
                                self.lin_OK_Serson.setFocus()


                            if self.lin_Thing_barcode.text()[:3] not in  ['LS-'] or self.lin_quantiy.text() == '0':
                                    self.Clear_all()
                                    self.Clear_Thinginfo()

                            #print('录入成功')
                            #print(i)
                    else:
                        self.Message_two('物品数量不足')
                else:

                    #winsound.Beep(32767, 152212)
                    self.Message_one('密码错误')
                    self.lin_admin_password.setText('')
                    #self.Clear_all()
            else:
                self.Message_one('数据未完成')
                #self.Message_two(str(old_input_window))

        except Exception:
            print_exc()
            #print('录入数据%s'%Exception)
        curruct_text.clear()

#  人员进行操作选择时，如入库就把'OK退料','NG退料','新品入庫','維修入庫（OK）'在另一个显示出来
    def change_two(self):
        self.com_method.clear()
        get_comboxdata=self.com_operation.currentText()

        if get_comboxdata=='入庫' and self.com_Thing_class.currentText() not in ['SERSON','']:

            put_in_show.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            #put_in_show.show()
            #put_in_show.setWindowModality(Qt.ApplicationModal)

            #print('这入库的有触发')
            #self.com_method.addItems(['OK退料','NG退料','新品入庫','維修入庫（OK）'])

            self.com_method.addItems(['入庫'])
            #self.lin_quantiy.setEnabled(False)
            #self.lin_quantiy.setStyleSheet("*{background:#00000000;color:#00000000;border:none;}")
            #self.frm_thing_num.close()
            self.stackedWidget.setCurrentIndex(0)

        elif get_comboxdata=='出庫':
            self.com_method.addItems(['加量需求','外部借出','NG出庫','報廢出庫'])
            #self.frm_thing_num.show()
            self.stackedWidget.setCurrentIndex(1)
        elif get_comboxdata=='NG品更換':
            self.com_method.addItems(['NG品更換'])
            #self.frm_thing_num.show()
            self.stackedWidget.setCurrentIndex(1)

        elif get_comboxdata!='':
            self.com_method.addItems(['OK退料', 'NG退料', '新品入庫', '維修入庫（OK）'])

            self.stackedWidget.setCurrentIndex(1)


    #  Serson状态更改
    def Serson_Statius_Change(self):
        # 把serson信息进行更改位置与NG与OK
        if self.lin_Thing_barcode.text()[:3] in ['LS-']:
            #print('378')
            try:
                # 把得到的SERSON名字放在Get_SERSON_allName中
                Get_Serson_AllName = []
                sql_order = "select Serson_Name from Serson_Table order by Serson_Name"
                get_reslute = Execute_Sql_Get_Date(sql_order)
                for i in get_reslute:
                    Get_Serson_AllName.append(i[0])
                #print('410=%s' % Get_Serson_AllName)

                # 把NG的serson出库，位置从产线变成備品房
                if self.com_method.currentText() in ['NG品更換']:
                    if self.lin_Ng_Serson.text() in Get_Serson_AllName:
                        sql_order = "update Serson_Table set Station='%s',Address='%s',Work_Name='%s' where Serson_Name='%s'" % (
                            'NG', '備品房', self.lab_worker_name.text(), self.lin_Ng_Serson.text())
                        Execute_Sql_No_Get_Date(sql_order)
                        #print('376=%s' % sql_order)

                    else:
                        sql_order = "insert into Serson_Table(Serson_Name,Station,Work_Name,Address) values('%s','%s','%s','%s')" % (
                        self.lin_Ng_Serson.text(), 'NG', self.lab_worker_name.text(), '備品房')
                        Execute_Sql_No_Get_Date(sql_order)

                    # 把好的serson出库，位置从備品房变成产线
                    if self.lin_OK_Serson.text() in Get_Serson_AllName:
                        sql_order = "update Serson_Table set Address='%s',Work_Name='%s' where Serson_Name='%s'" % (
                            self.com_lines.currentText(), self.lab_worker_name.text(), self.lin_OK_Serson.text())
                        Execute_Sql_No_Get_Date(sql_order)

                    else:
                        sql_order = "insert into Serson_Table(Serson_Name,Station,Work_Name,Address) values('%s','%s','%s','%s')" % (
                            self.lin_OK_Serson.text(), 'OK', self.lab_worker_name.text(), self.com_lines.currentText())
                        Execute_Sql_No_Get_Date(sql_order)

                    #print('383=%s' % sql_order)


                elif self.com_method.currentText() in ['OK退料']:
                    if self.lin_OK_Serson.text() in Get_Serson_AllName:
                        sql_order = "update Serson_Table set Station='%s',Address='%s',Work_Name='%s' where Serson_Name='%s'" % (
                            'OK', '備品房', self.lab_worker_name.text(), self.lin_OK_Serson.text())
                        Execute_Sql_No_Get_Date(sql_order)

                    else:
                        sql_order = "insert into Serson_Table(Serson_Name,Station,Work_Name,Address) values('%s','%s','%s','%s')" % (
                            self.lin_OK_Serson.text(), 'OK', self.lab_worker_name.text(),'備品房')
                        Execute_Sql_No_Get_Date(sql_order)


                elif self.com_method.currentText() in ['NG退料']:
                    if self.lin_Ng_Serson.text() in Get_Serson_AllName:
                        sql_order = "update Serson_Table set Station='%s',Address='%s',Work_Name='%s' where Serson_Name='%s'" % (
                            'NG', '備品房', self.lab_worker_name.text(), self.lin_Ng_Serson.text())
                        Execute_Sql_No_Get_Date(sql_order)

                    else:
                        sql_order = "insert into Serson_Table(Serson_Name,Station,Work_Name,Address) values('%s','%s','%s','%s')" % (
                            self.lin_Ng_Serson.text(), 'NG', self.lab_worker_name.text(), '備品房')

                        Execute_Sql_No_Get_Date(sql_order)


                elif self.com_method.currentText() in ['加量需求']:
                    #print('加量')
                    #print(self.lin_OK_Serson)
                    #print(Get_Serson_AllName)
                    if self.lin_OK_Serson.text() in Get_Serson_AllName:
                        #print('加量')
                        sql_order = "update Serson_Table set Station='%s',Address='%s',Work_Name='%s' where Serson_Name='%s'" % (
                            'OK', self.com_lines.currentText(), self.lab_worker_name.text(), self.lin_OK_Serson.text())
                        #print('423=%s' % sql_order)
                        Execute_Sql_No_Get_Date(sql_order)

            except Exception:
                print_exc()



    #  根据人员选择的物品种类（测试线，电源线）把拥有此物品的机种拿出来（物品种类，）
    def set_class_change_machine(self,thing_class,sql_class):#驱动板
        if self.com_Thing_class.currentText() == thing_class and self.com_size.currentText()!='':
            Set_machine.clear()
            self.com_machine.clear()
            #@sql_order = "select MACHINES from WIRE_TEST where %s!='/' and MACHINES!='/' and SIZE='%s'" % (thing_class,self.com_size.currentText())
            sql_order = "select distinct MACHINES from MACHINE_LHTEST1 where %s!='/' and %s!='X'  and MACHINES!='/' and MACHINES!='X' and SIZE='%s' and MACHINE_STATIUS='True'" % (sql_class, sql_class,self.com_size.currentText())
            #print('228=%s'%sql_order)
            get_reslut = Execute_Sql_Get_Date(sql_order)
            get_reslut = set(get_reslut)
            #print('get_reslut%s' % get_reslut)
            Set_machine.append('')
            for i in get_reslut:#
                Set_machine.append(i[0])
            Set_machines=set(Set_machine)
            #print('Set_machine%s' % Set_machine)
            #print('Set_machine=%d'%len(Set_machine))
            Set_machines = sorted(Set_machines)
            if len(Set_machines) == 1 and Set_machines[0] == '':
                Set_machines.append('没有对应机种')
            self.com_machine.addItems(Set_machines)

#  根据人员选择的线体筛选机种，这一个子函数
    def Line_Wire_Change_Maching_one(self,line_term,sql_line):
        try:
            if self.com_lines.currentText()[:2] == line_term and self.com_size.currentText()!='':
                #print('242=%s'%line_term)
                self.com_machine.clear()
                #@sql_order = "select MACHINES from WIRE_TEST where %s!='/' and MACHINES!='/' and SIZE='%s'" % (sql_line,self.com_size.currentText())
                sql_order = "select MACHINES from MACHINE_LHTEST1 where %s!='/' and %s!='X' and MACHINES!='/' and MACHINES!='X' and SIZE='%s' and MACHINE_STATIUS='True'" % (sql_line,sql_line, self.com_size.currentText())


                #print("243=%s"%sql_order)
                get_reslute = Execute_Sql_Get_Date(sql_order)
                Set_machine.append('')
                for i in get_reslute:
                    Set_machine.append(i[0])
                Set_machines=set(Set_machine)
                Set_machines = sorted(Set_machines)
                #print('247=%d'%len(Set_machines))
                #print('401=%s'%Set_machines)

                if len(Set_machines)==1 and Set_machines[0]=='':
                    Set_machines.append('没有对应机种')

                #print('404=%s' % Set_machines)
                self.com_machine.addItems(Set_machines)

        except Exception:
            print_exc()

    def Line_Wire_Change_Maching(self):
        try:
            if self.com_Thing_class.currentText()== '測試線' and self.com_lines.currentText()!='':
                Set_machine.clear()
                self.com_machine.clear()
                self.Line_Wire_Change_Maching_one("FT",'MONDEL')
                self.Line_Wire_Change_Maching_one("FQ", 'MONDEL')
                self.Line_Wire_Change_Maching_one("OQ", 'MONDEL')
                self.Line_Wire_Change_Maching_one("IN", 'MONDEL')
                self.Line_Wire_Change_Maching_one("RP", 'MONDEL')

                self.Line_Wire_Change_Maching_one("BM", 'BMA')

                #如果要加BMA的測試線，那就只要在EXCEL中加入BMA段的測試線
                #self.Line_Wire_Change_Maching_one("BM", 'BMA')
                self.Line_Wire_Change_Maching_one('JI','JI_OR_SKD')
                self.Line_Wire_Change_Maching_one('BI','BI')
                self.Line_Wire_Change_Maching_one('CT','CTAG')
                self.Line_Wire_Change_Maching_one('IA','IAS')
                self.Line_Wire_Change_Maching_one('SK','JI_OR_SKD')
                self.Line_Wire_Change_Maching_one('AG', 'AGIS')
                #print('421yyyyyy')
        except Exception:
            print_exc()

#  根据人员的选择把选择机种的UI显示或者不显示
    def Set_MACorSYS_See(self):
        try:
            self.com_systems.clear()
            self.com_machine.clear()
            self.wire_show_test.setText('')

            #  显示出隐藏的三个框
            if self.com_Thing_class.currentText() not in ['其他（机种不用选）','','SERSON'] and (self.com_method.currentText()=='加量需求' or  self.com_operation.currentText() == 'NG品更換') \
                and self.com_lines.currentText()[:2] in ['SK','FT','JI','BM','IA','AG','BI','CT','FQ','IN','OQ','RP']:

                #self.com_machine.setEditable(True)


                #self.lin_Thing_barcode.setEnabled(False)

                self.Fra_mac_sys.setEnabled(True)
                #print('317set=%s'%self.com_Thing_class.currentText())

                #self.com_machine.addItems(list)
                self.com_systems.addItems(['','无电脑','Chroma(白电脑)', 'JC(黑色电脑)', 'PCBase','整機'])
                self.com_size.setStyleSheet("*{border-radius:9px;background:rgb(255, 255, 127);color:green;font-size:19px;border: 2px solid rgb(100, 100, 100);}QComboBox QAbstractItemView{background:#aaaa7f;}QComboBox::down-arrow {image: url(:/images/triangle_down_16px_1189852_easyicon.net.ico);}")
                self.com_machine.setStyleSheet("*{border-radius:9px;background:rgb(255, 255, 127);color:green;font-size:19px;border: 2px solid rgb(100, 100, 100);}QComboBox QAbstractItemView{background:#aaaa7f;}QComboBox::down-arrow {image: url(:/images/triangle_down_16px_1189852_easyicon.net.ico);}")
                self.com_systems.setStyleSheet("*{border-radius:9px;background:rgb(255, 255, 127);color:green;font-size:19px;border: 2px solid rgb(100, 100, 100);}QComboBox QAbstractItemView{background:#aaaa7f;}QComboBox::down-arrow {image: url(:/images/triangle_down_16px_1189852_easyicon.net.ico);}")
                #self.Fra_thing_show.setStyleSheet("*{background:#00000000;color:#00000000;}")

                self.wire_show_test.setStyleSheet("*{background:rgb(255, 255, 127);border-radius:40px;color:red;font-size:20px;border: 2px solid rgb(100, 100, 100);}")
                self.lab_wire_info.setStyleSheet("*{background:none;color:black;}")
                self.lab_size.setStyleSheet("QLabel {border-radius: 10px;font-size: 20px;color:black;}")
                self.lab_machine.setStyleSheet("QLabel {border-radius: 10px;font-size: 20px;color:black;}")
                self.lab_systems.setStyleSheet("QLabel {border-radius: 10px;font-size: 20px;color:black;}")
                #self.pushButton.setStyleSheet("*{border-radius: 15px;font-size: 20px;color:rgb(179, 179, 179);}")
                self.Fra_mac_sys.setStyleSheet("QComboBox::drop-down{width:20px;background:rgb(255,255,255,30);border-left-width:2px;border-left-style:solid;border-left-color:gray;}")

            else:#Thing_Class触发 画面默认的stylesheet会首先执行 这些是隐藏的三个Qcombox的QSS
                self.com_machine.setEditable(False)
                self.com_systems.setEditable(False)
                #self.lin_Thing_barcode.setEnabled(True)
                self.Fra_mac_sys.setEnabled(False)
                #self.com_machine.setStyleSheet("*{border-radius:10px;background:rgb(72,72,73,50%);}")
                #self.com_systems.setStyleSheet("*{border-radius:10px;background:rgb(72,72, 73,50%);}")
                self.Fra_thing_show.setStyleSheet("QLabel{background:rgb(255, 255, 127);}")
                self.wire_show_test.setStyleSheet("*{background:#00000000;border-radius:40px}")
                self.lab_wire_info.setStyleSheet("*{background:#00000000;color:#00000000;}")
                self.lab_machine.setStyleSheet("*{background:#00000000;color:#00000000;}")
                self.lab_systems.setStyleSheet("*{background:#00000000;color:#00000000;}")
                self.lab_size.setStyleSheet("*{background:#00000000;color:#00000000;}")
                self.com_size.setStyleSheet("*{background:#00000000;color:#00000000;}")
                self.com_machine.setStyleSheet("*{background:#00000000;color:#00000000;}")
                self.com_systems.setStyleSheet("*{background:#00000000;color:#00000000;}")
                #self.pushButton.setStyleSheet("*{background:#00000000;color:#00000000;}")



                self.Fra_mac_sys.setStyleSheet("QComboBox::drop-down{background:#00000000;border-left-width:0px;border-left-style:solid;border-left-color:gray;}")

                if self.com_Thing_class.currentText()!='SERSON':
                    self.Serson_close()

                self.com_size.clear()
                self.com_size.addItems(Read_loadsize_info())

        except Exception:
            print_exc()



    def Set_Comment_see(self):

        if self.lin_comments.isHidden() == False:
            self.lin_comments.close()
            self.lab_comment.setStyleSheet("*{background:#00000000;color:#00000000;}")
        else:
            self.lin_comments.show()
            self.lab_comment.setStyleSheet("*{background:none;color:black;}")


    def Clear_Workerinfo(self):
        self.lab_worker_name.setText('')
        self.lab_frim.setText('')
        self.lab_phone.setText('')

        #self.table_user_history.clear()


    def Clear_Thinginfo(self):
        self.lab_wire_name.setText('')
        self.lab_surplus_num.setText('')
        self.lab_Thing_truename.setText('')
        self.lab_ok_place.setText('')
        self.lab_ng_place.setText('')
    def Clear_all(self):
        try:
            self.Clear_Workerinfo()
            self.Clear_Thinginfo()
            self.com_Thing_class.clear()
            self.com_Thing_class.addItems(['','測試線','電源線','驅動板','FFC','SERSON','INV_電源線','整機線材','其他（机种不用选）'])
            self.com_operation.clear()
            self.com_operation.addItems(['','入庫','出庫','NG品更換'])
            self.com_method.clear()
            self.lin_worker_num.setText('')
            self.lin_quantiy.setText('')
            self.lin_comments.setText('')
            self.com_lines.clear()
            self.com_lines.addItems(Read_load_info())
            self.lin_Thing_barcode.setText('')
            self.lin_admin_password.setText('')
            self.lin_OK_Serson.setText('')
            self.lin_Ng_Serson.setText('')
            self.Serson_close()
            self.wire_show_test.clear()
            self.com_size.clear()
            self.com_size.addItems(Read_loadsize_info())
            self.lab_Thing_truename.clear()
            Set_machine.clear()
            curruct_text.clear()
            input_windows.clear()
            new_input_window.clear()
            Get_pow_ff_dri.clear()
            My_Machine_Wire.clear()
            self.Clear_Thinginfo()
            self.stackedWidget.setCurrentIndex(1)

            put_in_show.lin_maintain.clear()
            put_in_show.lin_ok.clear()
            put_in_show.lin_ng.clear()
            put_in_show.lin_new.clear()


            #print('清除执行成功')
        except Exception:
            print_exc()




    #這得到有線材的物品的機種
    def power_ff_input_machine(self):
        try:
            if self.com_Thing_class.currentText() != '測試線':
                self.set_class_change_machine('INV_電源線', 'INV_POWER_WIRE')
                self.set_class_change_machine('電源線', 'POWER_WIRE')
                self.set_class_change_machine('FFC', 'FFC')
                self.set_class_change_machine('驅動板', 'DRIVER')
                self.set_class_change_machine('整機線材','CLASS')

        except Exception:
            print_exc()


#  这是测试线的信息包括LH
    def Get_Line_Machine_Wire_Info(self):
        self.wire_show_test.clear()
        Get_pow_ff_dri.clear()
        My_Machine_Wire.clear()
        try:
            thing_class=self.com_Thing_class.currentText()  #@
            line=self.com_lines.currentText()
            if line[:2]=='JI' or line[:2]=='SK':
                line='JI_OR_SKD'
            elif line[:2] == 'CT':
                line = 'CTAG'
            elif line[:2] == 'BI':
                line = 'BI'
            elif line[:2] == 'IA':
                line = 'IAS'
            elif line[:2] == 'AG':
                line = 'AGIS'
            elif line[:2] in ['FT','OQ','FQ','IN','RP']:
                line = 'MONDEL'

            elif line[:2] in ['BM']:
                line = 'BMA'

            machine=self.com_machine.currentText()
            systems=self.com_systems.currentText().split('(')[0]
            #print('machine=%s,thing_class=%s,line=%s,systems=%s'%(machine,thing_class,line,systems))
            if thing_class=='測試線' and self.com_machine.currentText()!='':
                #@sql_order="select %s from WIRE_TEST where MACHINES='%s' and SYSTEMS='%s'" %(line,machine,systems)
                #if self.com_lines.currentText()[:2] in ['FT','SK','AG','IA'] and self.com_systems.currentText().split('(')[0] in ['','Chroma', 'JC', 'PCBase']:



                if self.com_lines.currentText()[:2] in ['CT','BI'] and self.com_systems.currentText().split('(')[0]=='无电脑':
                    sql_order = "select distinct %s from MACHINE_LHTEST1 where MACHINES='%s' and %s!='X'" % (line, machine, self.com_lines.currentText())
                      #人员选择得到的线材料号，
                else:
                    sql_order = "select distinct %s from MACHINE_LHTEST1 where MACHINES='%s' and SYSTEMS='%s'" % (line, machine, systems)

                #print('344=%s'%sql_order)
                Get_reslut=Execute_Sql_Get_Date(sql_order)
                #print('329=%s'%Get_reslut)

                if  len(Get_reslut)==0:
                    self.wire_show_test.setPlainText('\n机种:' + self.com_machine.currentText() + '\n系统:' + self.com_systems.currentText() + '\n物品:' + 'None')

                elif Get_reslut[0][len(Get_reslut[0])-1] in ['/','X','']:
                    self.wire_show_test.setPlainText('\n机种:' + self.com_machine.currentText() + '\n系统:' + self.com_systems.currentText() + '\n物品:' + 'None')

                else:  #[(1,2,3)]
                    LH_ALL = ['*','*','*','*','*']
                    for i in range(len(Get_reslut)):
                        LH_ALL[i]=Get_reslut[i][0]
                    #print('612=%s'%LH_ALL)
                    try:
                        sql_order = "select WUPIN_NAME from NC_KUCUN_LH where LH='%s' or LH='%s' or LH='%s' or LH='%s' or LH='%s'" %(LH_ALL[0],LH_ALL[1],LH_ALL[2],LH_ALL[3],LH_ALL[4])


                        #print('557=%s' % sql_order)

                        relute = Execute_Sql_Get_Date(sql_order)
                        #print('620=%s'%relute)

                        CU_SHI_NAME_ALL = ['*', '*', '*', '*', '*','*', '*', '*', '*', '*']
                        for i in range(len(relute)):
                            CU_SHI_NAME_ALL[i] = relute[i][0]

                        # 得到物品的位置
                        sql_order = "select Location_OK,Location_NG from NC_KUCUN_SUM where WUPIN_NAME='%s' or WUPIN_NAME='%s' or WUPIN_NAME='%s' or WUPIN_NAME='%s' or WUPIN_NAME='%s'" % (
                        CU_SHI_NAME_ALL[0], CU_SHI_NAME_ALL[1], CU_SHI_NAME_ALL[2], CU_SHI_NAME_ALL[3],
                        CU_SHI_NAME_ALL[4])

                        Thing_Address = Execute_Sql_Get_Date(sql_order)
                        #print('642=%s'%sql_order)
                        #print('641=%s' % Thing_Address)

                    except Exception:
                        print_exc()

                    Get_pow_ff_dri.append(Get_reslut[0][0])
                    #print('481=%s'%Get_pow_ff_dri)
                    self.wire_show_test.setPlainText('\n机种:' +self.com_machine.currentText()+'\n系统:' +self.com_systems.currentText()+'\n物品:'+ replace_str(relute,["[('","',)]"])+'\n位置:'+str(Thing_Address))

                    for xy in Get_reslut:
                        My_Machine_Wire.append(xy[0])

        except Exception:
            print_exc()
            #print('498=%s'%Exception)


    def seek_dri_pow_ff(self):
        My_Machine_Wire.clear()
        try:
            machine = self.com_machine.currentText()
            systems = self.com_systems.currentText().split('(')[0]
            thing_class = self.com_Thing_class.currentText()

            if machine not in ['','X','/'] and systems not in ['','121','/'] and thing_class not in ['','X','/']:
                if thing_class=='驅動板':
                    thing_class='DRIVER,DRIVER_MARCH'
                elif thing_class=='電源線':
                    thing_class='POWER_WIRE'
                elif thing_class=='INV_電源線':
                    thing_class='INV_POWER_WIRE'
                elif thing_class == '整機線材':
                    thing_class = 'CLASS'

                #@sql_order="select %s from WIRE_TEST where MACHINES='%s' and SYSTEMS='%s'" %(thing_class,machine,systems)
                #  判斷線體在BMA，或在BI中，
                if self.com_lines.currentText()[:2] in ['BM','BI','CT'] and self.com_systems.currentText().split('(')[0]=='无电脑':
                    sql_order = "select %s from MACHINE_LHTEST1 where MACHINES='%s' and %s!='X'" % (
                    thing_class, machine, thing_class.split(',')[0])

                else:
                    sql_order = "select distinct %s from MACHINE_LHTEST1 where MACHINES='%s' and SYSTEMS='%s'" % (thing_class, machine, systems)

                Get_reslut=Execute_Sql_Get_Date(sql_order)

                #print('628=%s'%sql_order)
                #print('343Get_reslut=%s'%Get_reslut)

                POW_FFC_LH_ALL = ['*', '*', '*', '*', '*','*', '*', '*', '*', '*','*','*','*','*','*']
                for i in range(len(Get_reslut)):
                    POW_FFC_LH_ALL[i] = Get_reslut[i][0]

                try:
                    if len(Get_reslut)!=0:
                        sql_order = "select WUPIN_NAME from NC_KUCUN_LH where LH='%s' or LH='%s' or LH='%s' or LH='%s' or LH='%s'" % (POW_FFC_LH_ALL[0],POW_FFC_LH_ALL[1],POW_FFC_LH_ALL[2],POW_FFC_LH_ALL[3],POW_FFC_LH_ALL[4])
                        #print('618=%s'%sql_order)
                        relute = Execute_Sql_Get_Date(sql_order)
                        #print('599%s' % relute)

                        b = str(relute).replace('[', '').replace(']', '').replace("'", '').replace(',', '')
                        #print(b)
                        c = b.replace(") (", ")\n(")
                        #print(c)


                        #  得到選擇出的物品的位置
                        POW_FFC_NAME_ALL = ['*', '*', '*', '*', '*','*', '*', '*', '*', '*']
                        for i in range(len(relute)):
                            POW_FFC_NAME_ALL[i] = relute[i][0]

                        sql_order="select Location_OK,Location_NG from NC_KUCUN_SUM where WUPIN_NAME='%s' or WUPIN_NAME='%s' or WUPIN_NAME='%s' or WUPIN_NAME='%s' or WUPIN_NAME='%s'"%(POW_FFC_NAME_ALL[0],POW_FFC_NAME_ALL[1],POW_FFC_NAME_ALL[2],POW_FFC_NAME_ALL[3],POW_FFC_NAME_ALL[4])
                        Thing_Address=Execute_Sql_Get_Date(sql_order)

                        #print('695=%s'%Thing_Address)
                        e = str(Thing_Address).replace('[', '').replace(']', '').replace("'", '').replace(',', '')
                        #print(e)
                        f = e.replace(") (", ")\n(")


                except:
                    print_exc()

                if len(Get_reslut)==0 or POW_FFC_LH_ALL in ['/','X','']:
                    #print('629')
                    self.wire_show_test.setPlainText('\n机种:' + self.com_machine.currentText() + '\n系统:' + self.com_systems.currentText() + '\n物品:' + 'None')

                elif thing_class=='DRIVER,DRIVER_MARCH':
                    POW_FFC_LH_ALL_MARCH=['','','','','']
                    for i in range(len(Get_reslut)):
                        POW_FFC_LH_ALL_MARCH[i] = Get_reslut[i][1]
                    for i in POW_FFC_LH_ALL_MARCH:
                        if i=='':
                            POW_FFC_LH_ALL_MARCH.remove('')

                    Get_pow_ff_dri.append(Get_reslut[0][0]+Get_reslut[0][1])
                    self.wire_show_test.setPlainText('\n机种:' + self.com_machine.currentText() + '\n系统:' + self.com_systems.currentText() +'\n电流:' +str(POW_FFC_LH_ALL_MARCH)+'\n物品:' + str(c)+'\n位置:'+str(f))

                    #self.wire_show_test.setPlainText('\n    '+self.com_machine.currentText()+'\n    '+self.com_systems.currentText().split('(')[0]+Get_reslut[0][1]+'\n    '+Get_reslut[0][0])
                    for xy in Get_reslut:#
                        My_Machine_Wire.append(xy[0])
                    #print('639=%s'%My_Machine_Wire)

                # 这是电源线,FFC，测试线的显示函数
                else:
                    #print('622')
                    Get_pow_ff_dri.append(Get_reslut[0][0])
                    self.wire_show_test.setPlainText('\n机种:'+self.com_machine.currentText()+'\n系统:'+ self.com_systems.currentText()+'\n物品:'+str(c)+'\n位置:'+str(f))
                    for xy in Get_reslut:#
                        My_Machine_Wire.append(xy[0])
                    #My_Machine_Wire.append(Get_reslut[0][len(Get_reslut[0])-1])
                    #print('646=%s'%My_Machine_Wire)

        except Exception:
            print_exc()

    def Worker_Showinfo(self):
        Worker_Num = self.lin_worker_num.text()
        #print('WOKER_NUM=%s'%Worker_Num)
        #curruct_text.append(Worker_Num)
        sql_order = "select USER_NAME,USER_BUMEN,PHONE_ADDR from MFG_USER where USER_ID='%s'" % (Worker_Num)
        #print(sql_order)
        try:
            get_Thing_reslut = Execute_Sql_Get_Date(sql_order)
            #print('get_Thing_reslut=$s'%get_Thing_reslut)

            self.lab_worker_name.setText(get_Thing_reslut[0][0])
            self.lab_frim.setText(get_Thing_reslut[0][1])
            self.lab_phone.setText(get_Thing_reslut[0][2])

            #self.User_Thing_History()

        except Exception as e:
            if self.lin_worker_num.text()!='':
                self.Message_one('账号没有权限')
            self.lin_worker_num.setText('')
            self.Clear_Workerinfo()
            #print('Woker_showinfo=%s'%e)

    #这是一个物品的信息的显示
    def Thing_Showinfo(self):

        #if self.com_Thing_class.currentText()=='其他（机种不用选）':
        if self.lin_Thing_barcode.text()!='':
            self.Serson_close()
            Thing_Barcode = self.lin_Thing_barcode.text()
            #print('547=%s'%Thing_Barcode)
            Thing_Barcode=Determine_wire(Thing_Barcode)
            #print('549=%s'%Thing_Barcode)
            sql_order = "select TYPEOF,WUPIN_NAME,QTY_OK,Location_OK,Location_NG from NC_KUCUN_SUM where TXM='%s'" %(Thing_Barcode)
            #print('551=%s'%sql_order)

            try:
                getworker_reslut=Execute_Sql_Get_Date(sql_order)
                #print(getworker_reslut)
                # 设置查找的物品中的信息
                self.lab_wire_name.setText(getworker_reslut[0][0])
                self.lab_Thing_truename.setText(getworker_reslut[0][1])
                self.lab_surplus_num.setText(getworker_reslut[0][2])
                self.lab_ok_place.setText(getworker_reslut[0][3])
                self.lab_ng_place.setText(getworker_reslut[0][4])

            except Exception as e:
                if self.lin_Thing_barcode.text()!='':
                    self.Message_one('没有此类物品')
                self.lin_Thing_barcode.setText('')
                print_exc()
                self.Clear_Thinginfo()

            self.Serson_show(Thing_Barcode)

            # 如果是SERSON的话焦点就固定在OK

        # 分為測試線與電源線與驅動板
        if self.com_Thing_class.currentText()=='測試線' and self.com_lines.currentText()!='':
            #self.Line_Wire_Change_Maching()
            self.Get_Line_Machine_Wire_Info()
        else:
            self.seek_dri_pow_ff()

        #  設置焦點
        #print(self.lin_Thing_barcode.text())
        if self.lin_Thing_barcode.text()!='':
            self.lin_admin_password.setFocus()
        else:
            self.lin_Thing_barcode.setFocus()
            #print('773')

        if self.lin_Thing_barcode.text()[:2] in ['LS', 'UP']:
            self.lin_OK_Serson.setFocus()

        # 人員一掃條碼就判斷比對是否一致

        if self.lab_Thing_truename.text()!='' and self.lab_worker_name.text()!='':
            if self.com_Thing_class.currentText() not in ['其他（机种不用选）','','SERSON','整機線材'] and (self.com_method.currentText() == '加量需求' or self.com_operation.currentText() == 'NG品更換') \
                    and self.com_lines.currentText()[:2] in ['SK', 'FT', 'JI', 'BM', 'IA', 'AG', 'BI', 'CT','RP','IN','FQ','OQ']:
                if self.Get_Thing_Txm() == False:
                    self.lin_Thing_barcode.setFocus()
                    self.lin_Thing_barcode.setText('')



    def Serson_show(self,Thing_Barcode):
        if (Thing_Barcode[:2] in ['LS','UP']) and self.com_Thing_class.currentText()=='SERSON':
            self.lin_OK_Serson.setStyleSheet("QLineEdit {font-size: 14px;color: green;height: 25px;border: "
                                             "1px solid rgb(100, 100, 100);border-radius: 10px;background: rgb(72, 72, 73, 10%);}")
            self.lab_okserson.setStyleSheet("QLabel {border-radius: 10px;font-size: 20px;color:black;}")
           # self.Fra_mac_sys.close()
            self.lin_OK_Serson.setEnabled(True)

            self.lin_Ng_Serson.setStyleSheet("QLineEdit {font-size: 14px;color: red;height: 25px;border: "
                                             "1px solid rgb(100, 100, 100);border-radius: 10px;background: rgb(72, 72, 73, 10%);}")
            self.lab_ngserson.setStyleSheet("QLabel {border-radius: 10px;font-size: 20px;color:black;}")
            # self.Fra_mac_sys.close()
            self.lin_Ng_Serson.setEnabled(True)
            #print('serson=true')
            #self.lin_comments.setEnabled(True)


    def Serson_close(self):
        self.lin_OK_Serson.setStyleSheet("QLineEdit{background:#00000000;color:#717072;border:none;font-size:25px;}")#
        self.lab_okserson.setStyleSheet("QLabel{color:#00000000;}")
        #self.Fra_mac_sys.show()
        self.lin_OK_Serson.setEnabled(False)

        self.lin_Ng_Serson.setStyleSheet("QLineEdit{background:#00000000;color:#717072;border:none;font-size:25px;}")  #
        self.lab_ngserson.setStyleSheet("QLabel{color:#00000000;}")
        # self.Fra_mac_sys.show()
        self.lin_Ng_Serson.setEnabled(False)
        ##print('serson=false')

    def Serson_is_use(self):
        try:
            sql_order="select Station from Serson_Table where Serson_name='%s'"%self.lin_OK_Serson.text()
            serson_use_statius=Execute_Sql_Get_Date(sql_order)
            #print('937=%s'%serson_use_statius)

            if serson_use_statius[0][0]=='NG':
                self.Message_one('NG品不准出库或者此SERSON不存在')
                self.lin_OK_Serson.setText('')
                self.lin_OK_Serson.setFocus()
            else:
                if self.com_operation.currentText() in ['NG品更換']:
                    self.lin_Ng_Serson.setFocus()

        except Exception:
            print_exc()
            self.lin_Ng_Serson.setFocus()

        return serson_use_statius

    #这是test，自动输入BARCODE
    def Set_Thing_Barcode_Me(self):

        try:
            all_list=[]
            #print('1019')
            all_list.append(self.wire_show_test.toPlainText())
            #print(all_list)

            h=str(self.wire_show_test.toPlainText())
            for i in ["[('","',)]","(",")","\n"]:
                h=h.replace(i,"")

            regex = r'物品:([\s\S]*)位置:'
            matches = re.findall(regex, h)
            for match in matches:
                #print('match',match)
                pass

            #print(h)

            sql_order="select TXM from NC_KUCUN_LH where WUPIN_NAME='%s'"%match
            get_reslute=Execute_Sql_Get_Date(sql_order)
            self.lin_Thing_barcode.setText(get_reslute[0][0])

            self.Thing_Showinfo()
        except Exception:
            print_exc()

    #這是顯示時間用的
    def init_timer(self):
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.update_time)

    def update_time(self):
        self.lcd_clock.display(time.strftime("%X", time.localtime()))

    def shutcut(self):
        self.lin_Thing_barcode.setFocus()

    def return_mainwindow(self):
        #print('this is thing_registe return window')
        pass

    #检查物品输入数量
    def Check_Thing_Num(self):
        try:
            if int(self.lin_quantiy.text())>1000:
                self.Message_two('你确认输入的物品\n数字是正确的？')
        except Exception:
            print_exc()

    def Check_Thing_Is_Zero(self):
        try:
            if self.com_operation.currentText()!='入庫':
                result=False
                sql_order="select QTY_OK from NC_KUCUN_SUM where WUPIN_NAME='%s'"%self.lab_Thing_truename.text()
                get_result=Execute_Sql_Get_Date(sql_order)
                #print(sql_order)
                #print('1044=',get_result)
                if int(get_result[0][0])-int(self.lin_quantiy.text())>0:
                    #print('物品库存还有大于零的数')
                    result=True
                return result
            else:
                return True
        except Exception:
            print_exc()


    def rewrite(self):
        #print('旧数据',old_input_window)
        pass
    # #显示人物一个月领用物品
    # def User_Thing_History(self):
    #     try:
    #
    #         sql_order="select WUPIN_NAME,QTY,STATUS,CDT from NC_KUCUN_INOUT where USERNAME='%s' order by CDT desc"%self.lab_worker_name.text()
    #         get_reslute=Execute_Sql_Get_Date(sql_order)
    #
    #         self.table_user_history.setRowCount(20)
    #         #print('1041=',get_reslute)
    #         for j in range(len(get_reslute)):
    #             for i in range(4):
    #                 data = QTableWidgetItem(str(get_reslute[j][i]))  # 转换后可插入表格
    #                 self.table_user_history.setItem(j, i, data)
    #     except Exception:
    #         print_exc()


    # def changeEvent(self, event):
    #     try:
    #         if self.isMaximized():
    #             #print('这是变大了的')
    #             self.lin_quantiy.setGeometry(QtCore.QRect(10, 70, 141, 41))
    #             #self.setCentralWidget(self.lin_quantiy)
    #             #self.setCentralWidget(self.frame_main)
    #     except Exception:
    #         print_exc()
    #
    #
    # def center_test(self):
    #     screen = QDesktopWidget().screenGeometry()
    #     size = self.geometry()
    #     self.move((screen.width() - size.width()) / 2,
    #               (screen.height() - size.height()) / 2)
    #
    def reset_function(self):
        self.lab_tcp_show.setText('')




if __name__ == '__main__':
    app = QApplication(argv)
    put_in_show = put_in_class()

    mywindow1 = wire_change_son() #主界面

    mywindow1.show()

    exit(app.exec())
