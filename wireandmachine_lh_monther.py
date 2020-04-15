from wireandmachine_lh import Ui_MainWindow
from Common_Function import *


All_Machine=[]
All_Machine_Dist={}

#在这里用了继承
class Wire_machine_lh(Ui_MainWindow,Farther,No_Main_Window,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Set_Table()

        self.action_to_lend.triggered.connect(self.to_lend)
        self.action_lend.triggered.connect(self.lend)

        #self.lin_machine_use.setMaxLength(4)#

        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)

        #self.lin_machine_use.setValidator(testing_machine('True|False'))
    def return_mainwindow(self):
        #print('this is return mainwindow')
        pass


    def Set_Table(self):#
        All_Machine.clear()
        All_Machine_Dist.clear()


        #sql_order="select WUPIN_NAME,TYPEOF,TXM,LH from NC_KUCUN_LHTEST"
        #备份的
        sql_order = "select WUPIN_NAME,TYPEOF,TXM,LH,Thing_March from NC_KUCUN_LH order by WUPIN_NAME"

        get_reslute=Execute_Sql_Get_Date(sql_order)
        #print('22=%s'%get_reslute)


        #print(get_reslute)
        #print(len(get_reslute))

        for xy in get_reslute:
            All_Machine.append(xy[0])

            All_Machine_Dist[xy[0]]=[xy[1]]
            All_Machine_Dist[xy[0]].append(xy[2])
            All_Machine_Dist[xy[0]].append(xy[3])
            All_Machine_Dist[xy[0]].append(xy[4])

        All_Machine_Dist_Keys=list(All_Machine_Dist.keys())

        #print('33=%s'%All_Machine_Dist_Keys)
        #print(All_Machine_Dist)

        self.tableWidget.setRowCount(len(get_reslute))

        for j in range(len(get_reslute)):
            for i in range(5):
                data = QTableWidgetItem(get_reslute[j][i])  # 转换后可插入表格
                self.tableWidget.setItem(j, i, data)

# 从table得到数值，并且设置在界面的lineedit
    def Get_Table_Date(self,i,j):
        try:
            #print(i,j)
            #print('test')
            #print(self.tableWidget.item(i, j).text())
            self.lin_WUPIN_NAME.setText(self.tableWidget.item(i, 0).text())
            self.lin_TYPEOF.setText(self.tableWidget.item(i, 1).text())
            self.lin_TXM.setText(self.tableWidget.item(i, 2).text())
            self.lin_THING_LH.setText(self.tableWidget.item(i, 3).text())
            self.lin_thing_march.setText(self.tableWidget.item(i, 4).text())
        except Exception:
            print_exc()

    def confire_reslute(self):
        try:
            #print('89=%s'%All_Machine)
            if self.lin_WUPIN_NAME.text() in All_Machine:
                if self.Message_two('确认要更改？') == QMessageBox.Yes:
                    #print("更改")
                    sql_order="update NC_KUCUN_LH set TYPEOF='%s',TXM='%s',LH='%s',Thing_March='%s' where WUPIN_NAME='%s'"%(self.lin_TYPEOF.text(),self.lin_TXM.text(),self.lin_THING_LH.text(),self.lin_thing_march.text(),self.lin_WUPIN_NAME.text())

            else:
                #print("添加")
                if self.Message_two('是否添加此机种')==QMessageBox.Yes:
                    sql_order = "insert into NC_KUCUN_LH(WUPIN_NAME,TYPEOF,TXM,LH,Thing_March) values('%s','%s','%s','%s','%s')"% (self.lin_WUPIN_NAME.text(),self.lin_TYPEOF.text(),self.lin_TXM.text(),self.lin_THING_LH.text(),self.lin_thing_march.text())

            #print('85=%s'%sql_order)
            Execute_Sql_No_Get_Date(sql_order)

            self.Clear_All()
        except Exception:
            print_exc()

    def Seek_Info(self):
        try:
            sender_one=self.sender()

            #print('95=',sender_one.objectName())

            if sender_one.objectName()=='lin_TXM':
                sql_order="select TXM,TYPEOF,WUPIN_NAME,LH,Thing_March from NC_KUCUN_LH where TXM='%s'"%self.lin_TXM.text()

            else:
                sql_order="select TXM,TYPEOF,WUPIN_NAME,LH,Thing_March from NC_KUCUN_LH where LH='%s'"%self.lin_THING_LH.text()

            relute = Execute_Sql_Get_Date(sql_order)
            #print(relute)

            self.lin_TXM.setText(relute[0][0])
            self.lin_TYPEOF.setText(relute[0][1])
            self.lin_WUPIN_NAME.setText(relute[0][2])
            self.lin_THING_LH.setText(relute[0][3])
            self.lin_thing_march.setText(relute[0][4])

            self.table_jump_address(self.tableWidget,self.lin_TXM.text())

        except Exception:
            print_exc()
            self.Message_two('没有此物品')


    def Clear_All(self):
        All_Machine.clear()
        All_Machine_Dist.clear()
        self.Set_Table()
        self.lin_TYPEOF.setText('')
        self.lin_WUPIN_NAME.setText('')
        self.lin_TXM.setText('')
        self.lin_THING_LH.setText('')
        self.lin_thing_march.setText('')



    def delete(self):
        sql_order="delete NC_KUCUN_LH WHERE WUPIN_NAME='%s' and LH='%s'"%(self.lin_WUPIN_NAME.text(),self.lin_THING_LH.text())
        Execute_Sql_No_Get_Date(sql_order)
        self.Clear_All()


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



if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    ui = Wire_machine_lh()
    ui.show()
    exit(app.exec_())