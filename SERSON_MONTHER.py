from SERSON import Ui_MainWindow
from Common_Function import *


All_Machine=[]
All_Machine_Dist={}
Worker_All=[]
Address_All=[]


#在这里用了继承
class SET_MACHINE_USE(Ui_MainWindow,Farther,No_Main_Window,QMainWindow):
    def __init__(self):
        try:
            super().__init__()
            self.setupUi(self)
            self.Set_Table()
            self.action_SERSON.triggered.connect(self.Reset_Serson_Num)
            self.action_to_lend.triggered.connect(self.to_lend)
            self.action_lend.triggered.connect(self.lend)

            styleFile = r'd:\config\blue_style.qss'
            qssStyle = CommonHelper.readQss(styleFile)
            self.setStyleSheet(qssStyle)


            self.com_Address.addItems(Read_load_info())
            self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)

            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
            self.tableWidget.setWordWrap(True)


        except Exception:
            print_exc()
        #self.lin_machine_use.setMaxLength(4)#

        #self.lin_machine_use.setValidator(testing_machine('True|False'))

    def to_lend(self):
        try:
            delete_sql_order="delete Serson_TableTEST"
            file_name=self.to_lend_function(delete_sql_order,'Serson_TableTEST',5)
            #print('38',file_name)

        except Exception:
            print_exc()


    def lend(self):
        save_file_name=self.lend_function(self.tableWidget)
        #print('44',save_file_name)



    def Reset_Serson_Num(self):
        try:
            sql_order="select count(*) from Serson_Table where Station='OK' and Serson_Name like 'LS-%' and Address='測試備品房'"
            Serson_NUM_OK=Execute_Sql_Get_Date(sql_order)
            #print(Serson_NUM_OK)
            sql_order="update NC_KUCUN_SUM set QTY_OK='%s' where WUPIN_NAME='%s'"%(Serson_NUM_OK[0][0],'Light Sensor')
            Execute_Sql_No_Get_Date(sql_order)

            sql_order = "select count(*) from Serson_Table where Station='NG' and Address='測試備品房' and Serson_Name like 'LS-%'"
            Serson_NUM_NG = Execute_Sql_Get_Date(sql_order)
            #print(Serson_NUM_NG)
            sql_order = "update NC_KUCUN_SUM set QTY_NG='%s' where WUPIN_NAME='%s'" % (Serson_NUM_NG[0][0], 'Light Sensor')
            Execute_Sql_No_Get_Date(sql_order)

            sql_order = "select count(*) from Serson_Table where Station='OK' and Address!='測試備品房' and Serson_Name like 'LS-%'"
            Serson_NUM_ONLINE=Execute_Sql_Get_Date(sql_order)

            sql_order = "update NC_KUCUN_SUM set QTY_ONLINE='%s' where WUPIN_NAME='%s'" % (
            Serson_NUM_ONLINE[0][0], 'Light Sensor')
            Execute_Sql_No_Get_Date(sql_order)

            print('73',Serson_NUM_OK)


        except Exception:
            print_exc()



    def Set_Table(self):#
        All_Machine.clear()
        All_Machine_Dist.clear()
        Worker_All.clear()
        Address_All.clear()

        #这是选择显示电脑还是SERSON，STATIUS
        try:
            if  self.com_chioce_comp_or_ser.currentText()=='SERSON':
                if self.com_Choice.currentText()=='所有' :
                    sql_order = "select Serson_Name,Thing_Statius,Station,Work_Name,Address,CDT from Serson_Table where Serson_Name like 'LS-%' order by Serson_Name"
                else:
                    sql_order="select Serson_Name,Thing_Statius,Station,Work_Name,Address,CDT from Serson_Table where Station='%s' and Serson_Name like '%s' order by Serson_Name"%(self.com_Choice.currentText(),'LS-%')

            else:
                #print('this is computer')
                if self.com_Choice.currentText()=='所有' :
                    sql_order = "select Serson_Name,Thing_Statius,Station,Work_Name,Address,CDT from Serson_Table where Serson_Name not like 'LS-%' order by Serson_Name"
                else:
                    sql_order="select Serson_Name,Thing_Statius,Station,Work_Name,Address,CDT from Serson_Table where Station='%s' and Serson_Name not like '%s' order by Serson_Name"%(self.com_Choice.currentText(),'LS-%')

            get_reslute=Execute_Sql_Get_Date(sql_order)
            #print('23=%s'%sql_order)

            #print('22=%s'%get_reslute)

            #get_reslute=list(set(get_reslute))  #去重

            for xy in get_reslute:
                All_Machine.append(xy[0])
                All_Machine_Dist[xy[0]]=xy[1]

                Worker_All.append(xy[2])
                Address_All.append(xy[3])


            #print('ALL_Machine=%s'%All_Machine_Dist)
            #print(Worker_All)

            All_Machine_Dist_Keys=list(All_Machine_Dist.keys())

            #print('33=%s'%All_Machine_Dist_Keys)

            self.tableWidget.setRowCount(len(get_reslute))
            self.tableWidget.setColumnCount(6)

            for j in range(len(get_reslute)):
                for i in range(6):
                    data = QTableWidgetItem(str(get_reslute[j][i]))  # 转换后可插入表格
                    self.tableWidget.setItem(j, i, data)
        except Exception:
            print_exc()

    # 从table得到数值，并且设置在界面的lineedit
    def TEST(self,i,j):
        try:
            #print(i,j)
            #print('test')
            #print(self.tableWidget.item(i, j).text())
            #self.com_Station.setText(self.tableWidget.item(i, 0).text())
            self.lin_Num.setText(self.tableWidget.item(i, 0).text())

            self.com_thing_status_info.setEditText(self.tableWidget.item(i, 1).text())
            self.com_Station.setEditText(self.tableWidget.item(i,2).text())
            self.lin_Worker.setText(self.tableWidget.item(i,3).text())
            self.com_Address.setEditText(self.tableWidget.item(i,4).text())

            self.dat_hint_time.setDateTime(self.tableWidget.item(i,5).text())

            self.lin_delete.setText(self.tableWidget.item(i, 0).text())

        except Exception:
            print_exc()


    #确定一个结果的确认
    def confire_reslute(self):
        try:
            #print('62=%s'%All_Machine)
            if self.lin_Num.text() in All_Machine:
                if self.Message_two('确认要更改？') == QMessageBox.Yes:
                    sql_order="update Serson_Table set Thing_Statius='%s',Station='%s',Address='%s',Work_Name='%s',CDT='%s' where Serson_Name='%s'"%(self.com_thing_status_info.currentText(),self.com_Station.currentText(),self.com_Address.currentText(),get_uaer_name(self.lin_Worker.text(),self.lin_Worker.text()),Get_Now_Time(),self.lin_Num.text())
            else:
                if self.Message_two('是否添加此物品')==QMessageBox.Yes:
                    sql_order = "insert into Serson_Table(Thing_Statius,Serson_Name,Station,Work_Name,Address,CDT) values('%s','%s','%s','%s','%s','%s')"%(self.com_chioce_comp_or_ser.currentText(),self.lin_Num.text(),self.com_Station.currentText(),self.lin_Worker.text(),self.com_Address.currentText(),Get_Now_Time())

            if self.com_Station.currentText()=='OK':
                sql_order="update Serson_Table set CDT='%s' where Serson_Name='%s'"%(Get_Now_Time(),self.lin_Num.text())

            #print(sql_order)
            Execute_Sql_No_Get_Date(sql_order)
            self.Clean_All()


        except Exception:
            print_exc()


    #删除函数
    def delete(self):
        sql_order = "delete from Serson_Table where Serson_Name='%s'"%self.lin_delete.text()
        Execute_Sql_No_Get_Date(sql_order)
        self.Set_Table()


    #清除所有的东西,这是一个测试东西
    def Clean_All(self):
        try:
            self.tableWidget.clear()
            self.com_Station.clear()
            self.com_Address.clear()
            self.com_Station.addItems(['','OK','NG','BF'])
            #self.com_Address.addItems(['','產線','測試備品房'])
            self.com_Address.addItems(Read_load_info())

            self.lin_Num.setText('')
            self.lin_Worker.setText('')

            All_Machine.clear()
            All_Machine_Dist.clear()
            Worker_All.clear()
            Address_All.clear()

            self.lin_Worker.setText("黃林燦")
            self.tableWidget.setHorizontalHeaderLabels(['物品编码','保存情况','物品状态','操作人员','物品位置','维护时间'])
            self.Set_Table()

        except Exception:
            print_exc()


    #一个返回函数
    def return_mainwindow(self):
        #print('this is a serson return main window')
        pass

    #設置人員選擇回車顯示物品盤點,查找的函數
    def thing_showinfo(self):
        try:
            sql_order = "select Serson_Name,Thing_Statius,Station,Address,Work_Name from Serson_Table WHERE Serson_Name='%s' " % self.lin_Num.text()
            get_reslute = Execute_Sql_Get_Date(sql_order)
            #print('115=%s' % get_reslute)

            #self.lin_Num.setText(get_reslute[0][0])
            self.com_Station.setEditText(get_reslute[0][2])
            self.lin_Worker.setText(get_reslute[0][4])

            self.com_thing_status_info.setEditText(get_reslute[0][1])
            self.com_Address.setEditText(get_reslute[0][3])
            #self.com_thing_status_info.setEditText(get_resuit)

            self.table_jump_address(self.tableWidget,self.lin_Num.text())

            return get_reslute

        except Exception:
            print_exc()



if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    ui = SET_MACHINE_USE()
    ui.show()
    exit(app.exec_())

