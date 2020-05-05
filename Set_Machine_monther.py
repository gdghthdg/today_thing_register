from Set_Machine import Ui_Form
from Common_Function import *
import set_machine_kitting

All_Machine=[]
All_Machine_Dist={}
All_Machine_sort=[]



class kitting_show_class(set_machine_kitting.Ui_Form,Farther, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def confire(self):
        try:
            get_kitting_address_false_true = []
            get_kitting_address_false_true.append(kitting_show.checkBox1300.isChecked())
            get_kitting_address_false_true.append(kitting_show.checkBox1370.isChecked())
            get_kitting_address_false_true.append(kitting_show.checkBox1450.isChecked())
            get_kitting_address_false_true.append(kitting_show.checkBox1600.isChecked())

            #print('douxeu:',get_kitting_address_false_true)

            kitting_data = []
            address_list=[1300,1370,1450,1600]

            for i in range(4):
                if get_kitting_address_false_true[i]==True:
                    kitting_data.append(address_list[i])

            #print(kitting_data)

            if kitting_data==[]:
                kitting_data='无'

            #print("gggg",kitting_data)

            data1 = QTableWidgetItem(str(kitting_data))  # 转换后可插入表格
            ui.tableWidget.setItem(int(kitting_show.lab_table_rows.text()), 2, data1)

            kitting_show.close()


            #print('3r34r34r34',get_kitting_address_false_true)


        except Exception:
            print_exc()




#在这里用了继承
class SET_MACHINE_USE(Ui_Form,Farther,No_Main_Window,QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupUi(self)
        self.Set_Table()
        #self.com_machine_use.setMaxLength(4)#
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.com_machine_use.setValidator(testing_machine('True|False'))

        self.tableWidget.horizontalHeader().setStretchLastSection(True)

    def return_mainwindow(self):
        if self.Message_two('是否保存?')==QMessageBox.Yes:
            self.save_data()

        #print('this is return mainwindow')

        #添加一个返回是否保存的提示


    def Set_Table(self):#

        try:
            All_Machine.clear()
            sql_order="select MACHINES,MACHINE_STATIUS,KITTING_STATION from MACHINE_LH order by MACHINES"
            get_reslute=Execute_Sql_Get_Date(sql_order)
            #print('22=%s'%get_reslute)

            get_reslute=list(set(get_reslute))  #去重

            #print(get_reslute)
            #print(len(get_reslute))

            for xy in get_reslute:
                All_Machine.append(xy[0])
                All_Machine_Dist[xy[0]]=[xy[1]]
                All_Machine_Dist[xy[0]].append(xy[2])

            All_Machine_Dist_Keys=sorted(list(All_Machine_Dist.keys()))
            for i in All_Machine_Dist_Keys:
                All_Machine_sort.append(i)



            #print('33=%s'%All_Machine_Dist_Keys)
            #print('33=%s' % All_Machine_Dist)

            self.tableWidget.setRowCount(len(get_reslute))

            for j in range(len(All_Machine_Dist_Keys)):
                data = QTableWidgetItem(All_Machine_Dist_Keys[j])  # 转换后可插入表格
                self.tableWidget.setItem(j, 0, data)

                data1 = QTableWidgetItem(All_Machine_Dist[All_Machine_Dist_Keys[j]][0])  # 转换后可插入表格
                self.tableWidget.setItem(j, 1, data1)


                data2 = QTableWidgetItem(All_Machine_Dist[All_Machine_Dist_Keys[j]][1])  # 转换后可插入表格
                self.tableWidget.setItem(j, 2, data2)

            #
            # for i in range(2):
            #     for j in range(len(get_reslute)):
            #         data = QTableWidgetItem(str(get_reslute[j][i]))  # 转换后可插入表格
            #         self.tableWidget.setItem(j, i, data)
            #
        except Exception:
            print_exc()

    def kitting_window_is_no_show(self,i):

        kitting_show.showNormal()

        #把一个表格的列放在kitting_show上
        kitting_show.lab_table_rows.setText(str(i))



# 从table得到数值，并且设置在界面的lineedit
    def TEST(self,i,j):

        #判断是否点击在选择kitting
        if j==2:
            kitting_show.showNormal()

            #把一个表格的列放在kitting_show上
            kitting_show.lab_table_rows.setText(str(i))


        else:
            #print(i,j)
            #print('test')
            #print(self.tableWidget.item(i, j).text())
            self.lin_machine.setText(self.tableWidget.item(i, 0).text())
            #self.com_machine_use.setText(self.tableWidget.item(i, 1).text())


    def confire_reslute(self):
        #print('62=%s'%All_Machine)
        if self.lin_machine.text() in All_Machine:
            if self.Message_two('确认要更改？') == QMessageBox.Yes:
                sql_order="update MACHINE_LH set MACHINE_STATIUS='%s'where MACHINES='%s'"%(self.com_machine_use.currentText(),self.lin_machine.text())

            else:
                #print('no change')
                pass

        else:
            if self.Message_two('是否添加此机种')==QMessageBox.Yes:
                #sql_order = "insert into MACHINE_LHTEST(MACHINE_STATIUS,MACHINES) values('%s','%s')"% (self.com_machine_use.currentText(),self.lin_machine.text())


                sql_order = "insert into MACHINE_LH(MACHINE_STATIUS,MACHINES,SIZE,SYSTEMS,JI_OR_SKD,MONDEL,BI,CTAG,IAS,AGIS,FFC,INV_POWER_WIRE,DRIVER,DRIVER_MARCH,POWER_WIRE) " \
                            "values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
                            %(self.com_machine_use.currentText(),self.lin_machine.text(),'X','X','X','X','X','X','X','X','X','X','X','X','X')
            else:
                #print('no incree')
                pass

        try:
            Execute_Sql_No_Get_Date(sql_order)
        except Exception:
            print_exc()

        self.Clean_All()


    #保存更改kitting的站点,上传至sql server
    def save_data(self):
            for i in range(self.tableWidget.rowCount()):
                try:
                    if self.tableWidget.item(i,2).text()!='':
                ##print(self.tableWidget.item(0,0).text(),'kkkkkk',self.tableWidget.columnCount(),self.tableWidget.rowCount())
                        sql_order="update MACHINE_LH set KITTING_STATION='%s' where MACHINES='%s'"%(self.tableWidget.item(i,2).text(),self.tableWidget.item(i,0).text())
                        #print(self.tableWidget.item(i,0).text(),self.tableWidget.item(i,2).text())
                        Execute_Sql_No_Get_Date(sql_order)
                except Exception:
                    print_exc()


    #輸入機種名稱,得到位置,並且自動跳轉在指定頁面
    # item = self.tableWidget.findItems(text, QtCore.Qt.MatchExactly)＃遍历表查找对应的item
    # row = item[0].row()                                            ＃获取其行号
    # self.tableWidget.verticalScrollBar().setSliderPosition(row)  ＃滚轮定位过去，搞定
    def seek_machine_address(self):
        try:
            # #print("得到機種的名稱",self.lin_machine.text(),All_Machine_sort)
            #
            # #print(All_Machine_sort.index(self.lin_machine.text()))
            # #self.tableWidget.SelectRows(10)
            #
            # self.tableWidget.verticalScrollBar().setSliderPosition(All_Machine_sort.index(self.lin_machine.text())-5)

            # 遍历表格查找对应项
            self.table_jump_address(self.tableWidget,self.lin_machine.text())

        except Exception:
            print_exc()



    def Clean_All(self):
        try:
            self.Set_Table()
            self.lin_machine.setText('')
            All_Machine.clear()
            All_Machine_Dist.clear()
            self.Set_Table()
        except Exception:
            print_exc()


#一个是主函数,只是在这个py中都会执行,如果要有一个被引用的话,大概要以怎样的形式表达
#如果是一个函数形式来表达的话,模块化的
if __name__ == "__main__":
    set_server_ip_admin_password_database('172.17.130.106:5900','sa','123456','xueshengxinxi')
    app = QtWidgets.QApplication(argv)
    ui = SET_MACHINE_USE()
    kitting_show=kitting_show_class()
    ui.show()
    exit(app.exec_())

