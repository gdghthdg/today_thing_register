import xlwt
import traceback
from PyQt5.QtCore import QDate

from Common_Function import *
from history import Ui_MainWindow

Get_data_num=[]
#All_name = ['TYPEOF', 'TXM', 'WUPIN_NAME', 'CDT', 'WUPIN_OK', 'WUPIN_NG', 'COMMENTS', 'QTY', 'INOUT', 'STATUS','USERNAME', 'USERBUM', 'USERPHONE', 'STATION', 'ENG_NAME']
All_name = ["操作时间","名称","条形码","物品全称","数量","出入库类型","出入库方式","所用站点","更换人","领用课别","联系方式","ENG人员","ok编码","ng编码","备注"]
New_All_name=['时间','人员选择','名称','机种','系统','物品全称','条形码','数量','出入库类型','出入库方式','更换人','联系方式','更换人工号','所用站点','备注']


class Thing_History(Ui_MainWindow,Farther,No_Main_Window,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Seek_sql_data()
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.center()
        self.com_lines.addItems(Read_load_info())
        self.set_check()

        self.action_to_lend.triggered.connect(self.to_lend)
        self.action_lend.triggered.connect(self.lend)


    #一个返回函数
    def return_mainwindow(self):
        print('this is thing history seek')



    def clear(self):
        self.tableWidget.clear()
        if self.History_chioce.currentText()=='旧记录':
            self.tableWidget.setHorizontalHeaderLabels(All_name)
        else:
            self.tableWidget.setHorizontalHeaderLabels(New_All_name)

    def Choice_operation(self,Choice):
        try:

            start_datetime = self.dat_start.text() + ' ' + self.tim_start.text() + ':000'
            fiannly_datetime = self.dat_finally.text() + ' ' + self.tim_finally.text() + ':000'
            if self.History_chioce.currentText() == '旧记录':
                while_num=15
                sql_order = "select CDT,TYPEOF,TXM,WUPIN_NAME,QTY,INOUT,STATUS,STATION,USERNAME,USERBUM,USERPHONE,ENG_NAME,WUPIN_OK,WUPIN_NG,COMMENTS from NC_KUCUN_INOUT where CDT between '%s' and '%s' %s order by CDT desc" % (start_datetime, fiannly_datetime,Choice)
            elif self.History_chioce.currentText() == '新记录':
                while_num=15
                sql_order = "select CDT,worker_choice_wire,TYPEOF,machine_name,systems,wire_name,wire_barcode,inout_num,INOUT,STATUS,worker_name,worker_num,worker_phone,STATION,comments from New_History where CDT between '%s' and '%s' %s order by CDT desc" % (start_datetime, fiannly_datetime, Choice)

            print("HISTORY:",sql_order)
            get_sql_alldata = Execute_Sql_Get_Date(sql_order)
            #print(get_sql_alldata)
            Get_data_num.append(len(get_sql_alldata))

            self.tableWidget.setRowCount(len(get_sql_alldata))   #设置有多少行

            for j in range(len(get_sql_alldata)):
                for i in range(while_num):
                    #print(get_sql_alldata[j][i])
                    try:
                        data = QTableWidgetItem(str(get_sql_alldata[j][i]))  # 转换后可插入表格
                        self.tableWidget.setItem(j, i, data)#version(),Name
                    except Exception:
                        traceback.print_exc()

        except Exception:
            self.Message_two('条件不全或无此条件搜索结果')
            print_exc()



    def seek(self):
        try:
            Get_data_num.clear()
            self.tableWidget.clear()

        #设置列表的标头
            if self.History_chioce.currentText() == '旧记录':
                self.tableWidget.setHorizontalHeaderLabels(All_name)
            else:
                self.tableWidget.setHorizontalHeaderLabels(New_All_name)



            print('选中的线体', self.Get_Line_Check_Name(self.com_class))
            print('选中的操作', self.Get_Line_Check_Name(self.com_lines))

        #得到标记的选择：
            get_status_data=self.Get_Line_Check_Name(self.com_class)

            get_line_data=self.Get_Line_Check_Name(self.com_lines)

            get_thing_class_data=self.Get_Line_Check_Name(self.com_thing_class)



            if len(get_status_data) == 1:
                get_status_data=str(get_status_data).replace(',','')


            if len(get_line_data) == 1:
                get_line_data = str(get_line_data).replace(',', '')

            if len(get_thing_class_data) == 1:
                get_thing_class_data = str(get_thing_class_data).replace(',', '')

            if self.com_thing_class.currentText()=='全选':
                thing_class_chioce=" and TYPEOF not in ('')"

            elif self.com_thing_class.currentText()=='其他':
                thing_class_chioce=" and TYPEOF not in ('測試線', '電源線', '驅動板', 'FFC', 'Sensor', 'INV_電源線')"

            else:
                thing_class_chioce = ' and TYPEOF in ' + str(get_thing_class_data)



            ggg='and STATUS in ' + str(get_status_data) + ' and STATION in ' + str(get_line_data) + thing_class_chioce


            print('555555555',ggg)

            self.Choice_operation(ggg)


            # if self.com_class.currentText()=='进出品查询':
            #     self.Choice_operation('')
            # elif self.com_class.currentText()=='ng品查询':
            #     self.Choice_operation("and (STATUS='NG品更換' or STATUS='NG退料')")
            # elif self.com_class.currentText()=='借用记录':
            #     self.Choice_operation("and STATUS='外單位借用'")
            # elif self.com_class.currentText() == 'ng出库':
            #     self.Choice_operation("and STATUS='NG出庫'")
            # elif self.com_class.currentText() == 'ng报废':
            #     self.Choice_operation("and STATUS='報廢出庫'")
            # elif self.com_class.currentText()=='盤點記錄':
            #     self.Choice_operation("and INOUT='盤點'")
            #


        except Exception:
            traceback.print_exc()




    def Seek_sql_data(self):
        self.dat_finally.setDate(QDate.currentDate())
        self.dat_start.setDate(QDate.currentDate())
        self.dat_start.setCalendarPopup(True)
        self.dat_finally.setCalendarPopup(True)


    def set_check(self):
        for j in range(3,len(Read_load_info())):
            self.com_lines.model().item(j).setCheckState(QtCore.Qt.Unchecked)

        for j in range(3,self.com_class.count()):
            self.com_class.model().item(j).setCheckState(QtCore.Qt.Unchecked)

        for j in range(3,self.com_thing_class.count()):
            self.com_thing_class.model().item(j).setCheckState(QtCore.Qt.Unchecked)

    def Get_Line_Index(self,i):
        try:

            sender=self.sender()
            count_line=self.com_lines.count()
            print('129',count_line)
            #这是一个复选框的使用
            #self.com_lines.addItems(['gggg'])
            print(i)

            if i not in [0,1,2]:
                if sender.model().item(i).checkState() == QtCore.Qt.Unchecked:
                    sender.model().item(i).setCheckState(QtCore.Qt.Checked)
                else:
                    sender.model().item(i).setCheckState(QtCore.Qt.Unchecked)


            print('选中的线体',self.Get_Line_Check_Name(sender))

            if sender.itemText(i)=='全选':
                for j in range(3,sender.count()):
                    sender.model().item(j).setCheckState(QtCore.Qt.Checked)

            elif sender.itemText(i)=='清除':
                for j in range(3,sender.count()):
                    sender.model().item(j).setCheckState(QtCore.Qt.Unchecked)

            self.statusBar().showMessage(str(list(self.Get_Line_Check_Name(self.com_lines)))+str(list(self.Get_Line_Check_Name(self.com_class))))


        except Exception:
            print_exc()


    def Get_Line_Check_Name(self,sender):

        Line_Name=[]
        for i in range(3,sender.count()):
            if sender.model().item(i).checkState() == QtCore.Qt.Checked:
                Line_Name.append(sender.itemText(i))

        print('187',Line_Name)
        print(tuple(Line_Name))

        return tuple(Line_Name)


    def to_lend(self):
        try:
            # delete_sql_order="delete Serson_TableTEST"
            # file_name=self.to_lend_function(delete_sql_order,'Serson_TableTEST',5)
            # print('38',file_name)
            pass
        except Exception:
            print_exc()


    def lend(self):
        save_file_name=self.lend_function(self.tableWidget)
        print('44',save_file_name)



if __name__=="__main__":
    app = QtWidgets.QApplication(argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Thing_History()

    ui.show()
    exit(app.exec_())
