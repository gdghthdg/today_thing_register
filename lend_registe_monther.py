from lend_registe import Ui_MainWindow
from Common_Function import *

Insert_Info={}
Get_Table_Click_varlues=[]

class lend_registe_son(Ui_MainWindow,Farther,QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.com_address.addItems(Read_load_info())
        self.com_return_line.addItems(Read_load_info())
        self.center()
        styleFile = r'd:\config\blue_style.qss'
        qssStyle = CommonHelper.readQss(styleFile)
        self.setStyleSheet(qssStyle)

        self.dat_time.setDateTime(QDateTime.addSecs(QDateTime.currentDateTime(),18000))

        # print('时间',QDateTime.currentDateTime())
        print(QDateTime.currentDateTime())

        print('55',QDateTime.addSecs(QDateTime.currentDateTime(),18000))

        self.stackedWidget.setCurrentIndex(1)

        self.check_thing_is_return()


        self.Set_Table()
        self.get_user_for_sql()
        self.init_timer()
        self.return_set_table()


    #确认登录借出, 这是一个什么东
    def Confire_Lend(self):
        try:
            result=True

            if self.stackedWidget.currentIndex()==1:
                result=self.Seek_User_Info()

            if self.lin_lend_password.text()=='1' and result==True:
                if self.Message_two('确认借出')==QMessageBox.Yes:
                    time_clock=self.dat_time.text()
                    if self.com_is_not_have_limits.currentText()=='厂内人员':
                        sql_order="insert into Lend_Registe(Thing_Name,Lend_Num,User_Name,User_Phone,User_bumun,Use_Address,Lend_time,Return_time,Lend_Statius)" \
                                  " values('%s','%s','%s','%s','%s','%s','%s','%s','%s') "%(self.lin_thing_name.text(),self.lin_lend_num.text(),Insert_Info['lend_user'],Insert_Info['lend_phone'],Insert_Info['lend_bumun'],self.com_address.currentText(),Get_Now_Time(),str(time_clock)+'.000','借用中')
                    else:
                        sql_order="insert into Lend_Registe(Thing_Name,Lend_Num,User_Name,User_Phone,Use_Address,Lend_time,Return_time,Lend_Statius)" \
                                  " values('%s','%s','%s','%s','%s','%s','%s','%s') "%(self.lin_thing_name.text(),self.lin_lend_num.text(),self.lin_lend_user_name.text(),self.lin_lend_user_phone.text(),self.com_address.currentText(),Get_Now_Time(),str(time_clock)+'.000','借用中')


                    print(sql_order)
                    Execute_Sql_No_Get_Date(sql_order)

                    self.test_uer_info.appendPlainText(
                        '\n' + '物品:' + self.lin_thing_name.text() + '数量:' + self.lin_lend_num.text() + '已成功被借用')


                    self.clear_all()
                    self.get_user_for_sql()
                    self.test_uer_info.clear()

            else:
                self.Message_two("密码错误")

        except Exception:
            print_exc()


    def Return_Confire(self):
        # self.Seek_Thing_Info()

        try:
            if self.lin_password.text()=="1" and self.lab_lend_time.text()!='':
                if int(self.lab_thing_num.text())-int(self.lin_return_lend_num.text())==0:
                    print(self.lab_lend_time.text())
                    sql_order="update Lend_Registe set Lend_Statius='已歸還',Return_time='%s' where Lend_time = '%s'"%(Get_Now_Time(),self.lab_lend_time.text()[:len(self.lab_lend_time.text())-3])
                    Execute_Sql_No_Get_Date(sql_order)

                    print("已经归还")

                    self.return_set_table()
                    self.clear_label()
                    self.get_user_for_sql()

                else:
                    self.Message_two("归还数量不足或其他")
            # 一个捕获异常的函数

            else:
                self.Message_two("密码错误")
                self.lin_lend_password.clear()


        except Exception:
            print_exc()


    def Seek_Thing_Info(self):
        try:
            sender = self.sender()
            self.statusBar().showMessage(sender.text() + ' was pressed')


            sql_order="select WUPIN_NAME,QTY_OK FROM NC_KUCUN_SUM WHERE TXM='%s'"%sender.text()
            get_reslute=Execute_Sql_Get_Date(sql_order)
            print(get_reslute)

            self.lin_thing_name.setText(get_reslute[0][0])
            Insert_Info['thing_name']=get_reslute[0][0]
            #self.test_uer_info.setPlainText('\n'+str(get_reslute))

            if self.tabWidget.currentIndex()==0:
                #self.lin_thing_name.setText(get_reslute[0][0])
                self.test_uer_info.appendPlainText('\n'+str(get_reslute))


        except Exception:
            print_exc()


    def seek_no_limeit_user_name(self):

        sql_order = "select Thing_Name,Lend_Num,Lend_time,Return_time,Lend_Statius from Lend_Registe WHERE User_Name='%s'" % self.lin_lend_user_name.text()
        get_result = Execute_Sql_Get_Date(sql_order)
        print('114',sql_order)

        if len(get_result) > 0:
            # print('有借用未归还')
            # print(get_result)
            # Common_Table.Set_Table(self,sql_order,self.tableWidget,4)

            self.tableWidget.setRowCount(len(get_result))
            self.tableWidget.setColumnCount(5)
            for j in range(len(get_result)):
                for i in range(5):
                    data = QTableWidgetItem(str(get_result[j][i]))  # 转换后可插入表格
                    self.tableWidget.setItem(j, i, data)  # version(),Name
            self.Message_two("你有未归还的东西")

    # 一个使用者的函数
    def Seek_User_Info(self):
        try:

            sql_order = "select USER_NAME,PHONE_ADDR,USER_BUMEN FROM MFG_USER WHERE USER_ID='%s'" % self.lin_user_number.text()
            get_reslute = Execute_Sql_Get_Date(sql_order)
            print(get_reslute)
            Insert_Info['lend_user'] = get_reslute[0][0]
            Insert_Info['lend_phone'] = get_reslute[0][1]
            Insert_Info['lend_bumun'] = get_reslute[0][2]


            sql_order="select Thing_Name,Lend_Num,Lend_time,Return_time,Lend_Statius from Lend_Registe where User_Name='%s' and Lend_Statius='%s'"%(Insert_Info['lend_user'],'未歸還')
            get_result=Execute_Sql_Get_Date(sql_order)
            print(sql_order)

            if len(get_result)>0:
                # print('有借用未归还')
                # print(get_result)
                # Common_Table.Set_Table(self,sql_order,self.tableWidget,4)

                self.tableWidget.setRowCount(len(get_result))
                self.tableWidget.setColumnCount(5)
                for j in range(len(get_result)):
                    for i in range(5):
                        data = QTableWidgetItem(str(get_result[j][i]))  # 转换后可插入表格
                        self.tableWidget.setItem(j, i, data)  # version(),Name
                self.Message_two("你有未归还的东西")

            #这是判断显示在哪个Plaintextedit
            if self.tabWidget.currentIndex()==0:
                #self.lin_user_number.setText(get_reslute[0][0])
                self.test_uer_info.appendPlainText('\n'+str(get_reslute))

            elif self.tabWidget.currentIndex()==2:
                self.lin_return_lend_num.setText(get_reslute[0][0])
                self.test_uer_info_2.appendPlainText('\n'+str(get_reslute))

            return True

        except Exception:
            self.Message_two("此账号没有权限，请选择厂外人员")
            self.lin_user_number.clear()
            print_exc()
            return False

    #这一个列表的设置函数
    def Set_Table(self):#
        All_Machine=[]
        All_Machine_Dist={}
        All_Machine.clear()

        sql_order="select Thing_Name,Lend_Num,User_Name,User_Phone,Use_Address,Lend_time,Return_time,Lend_Statius from Lend_Registe where Lend_Statius = '%s' order by Lend_time"%self.com_thing_statius.currentText()
        get_reslute=Execute_Sql_Get_Date(sql_order)
        print('22=%s'%get_reslute)

        self.table_lend_register.setRowCount(len(get_reslute))
        self.table_lend_register.setColumnCount(8)
        for j in range(len(get_reslute)):
            for i in range(8):
                data = QTableWidgetItem(str(get_reslute[j][i]))  # 转换后可插入表格
                self.table_lend_register.setItem(j, i, data)  # version(),Name

    #这是一个获得列表中数据
    def return_set_table(self):

        if self.com_return_line.currentText()!='\ufeff':
            address_order="and Use_Address ='%s'"%self.com_return_line.currentText()
        else:
            address_order="and Use_Address !=''"

        if self.com_return_name.currentText()!='':
            user_order="and User_Name ='%s'"%self.com_return_name.currentText()
        else:
            user_order="and User_Name !=''"

        print('175',address_order,user_order)

        sql_order = "select Thing_Name,Lend_Num,User_Name,User_Phone,Use_Address,Lend_time,Return_time,Lend_Statius from Lend_Registe where Lend_Statius != '已歸還' %s %s order by Lend_time desc"%\
                    (address_order,user_order)

        print(sql_order)

        self.table_lend_data.setHorizontalHeaderLabels(['物品名称', '数量', '人員','手機','位置','借用时间', '归还时间', '状态'])
        Common_Table.Set_Table(self,sql_order,self.table_lend_data,8)

    #從table點點擊得到數據
    def get_return_table(self,i,j):
        try:
            Get_Table_Click_varlues.clear()
            Label_All_Widget=[self.lab_thing_name,self.lab_thing_num,self.lab_user_name,self.lab_phone,self.lab_address,self.lab_lend_time,self.lab_return_time,self.lab_is_not_return]
            thing_name=['编码:','数量:','姓名:','手机:','位置:','借用时间:','开始时间:','结束时间:','状态:']


            text=[]
            widget_all=[]
            Common_Table.Get_Table_Click_Data(self,widget_all,self.table_lend_data,i)

            for j in range(8):
                text.append(thing_name[j]+self.table_lend_data.item(i,j).text())
                Get_Table_Click_varlues.append(self.table_lend_data.item(i,j).text())
                Label_All_Widget[j].setText(self.table_lend_data.item(i,j).text())


            print(text)
            # self.test_uer_info_2.appendPlainText('\n' + replace_str(str(text),['[',"]","'"]).replace(',','\n'))
            self.but_is_no_select.setStyleSheet('*{background:#31ff1a;}')

        except Exception:
            print_exc()


    def Get_Table_Info(self,i,j):
        print(i,j)

    def return_mainwindow(self):
        pass


    def check_thing_is_return(self):
        sql_order = "update Lend_Registe set Lend_Statius='未歸還' where Return_time < '%s' and Lend_Statius='借用中' " % Get_Now_Time()
        Execute_Sql_No_Get_Date(sql_order)



    def update_time(self):

        # self.lcd_clock.display(time.strftime("%X", time.localtime()))

        #print('时间:', time.localtime())
        #return time.localtime()
        #print(Get_Now_Time()[11:19])

        time_now=Get_Now_Time()[11:19]
        if time_now in ['20:00:00','08:00:00','12:00:00',"00:00:00",'09:27:00']:
            print('545')
            sql_order="update Lend_Registe set Lend_Statius='未歸還' where Return_time < '%s' and Lend_Statius='借用中' "%Get_Now_Time()
            Execute_Sql_No_Get_Date(sql_order)


    def get_user_for_sql(self):
        sql_order="select distinct User_Name from Lend_Registe where Lend_Statius!='已歸還'"
        get_result=Execute_Sql_Get_Date(sql_order)

        self.com_return_name.clear()
        self.com_return_name.addItem('')
        for i in get_result:
            self.com_return_name.addItem(i[0])


    def clear_all(self):
        self.lin_lend_num.clear()
        self.lin_user_number.clear()
        self.lin_thing_name.clear()
        self.com_address.setEditText('')
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(['物品名称', '数量', '借用时间', '归还时间','状态'])
#这是一个设置
        self.dat_time.setDateTime(QDateTime.addSecs(QDateTime.currentDateTime(),18000))

        self.lin_lend_user_name.clear()
        self.lin_lend_user_phone.clear()
        self.lin_lend_password.clear()



    def clear_label(self):
        Label_All_Widget=[self.lab_thing_name,self.lab_thing_num,self.lab_user_name,self.lab_phone,self.lab_address,self.lab_lend_time,self.lab_return_time,self.lab_is_not_return]
        for i in Label_All_Widget:
            i.clear()
        self.lin_return_lend_num.clear()
        self.lin_password.clear()
        self.lin_lend_user_name.clear()
        self.but_is_no_select.setStyleSheet('*{background:red;}')

    def interface_chioce(self,str):
        print(str)
        if str=='厂内人员':
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.stackedWidget.setCurrentIndex(0)


if __name__ == '__main__':
    app=QApplication(argv)
    lend_registe=lend_registe_son()
    lend_registe.show()
    exit(app.exec())
