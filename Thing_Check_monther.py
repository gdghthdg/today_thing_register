from Common_Function import *
from Thing_Check import Ui_MainWindow
from Bind_Wire_monther import Wirte_wireinfo


#  执行SQL语句并且有获取数据的要求
Button_Statius = []
Ago_Now_Windows_Show_info = []
Get_reslute_all = []
lin_txm_all=[]
#這是一個tabwidget顯示的第幾個界面，默認第一
tabwidget_int=0



class thing_check_class(Ui_MainWindow,Farther,QMainWindow):


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Set_Table()

        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)

        self.action_to_lend.triggered.connect(self.to_lend)
        self.action_lend.triggered.connect(self.lend)



    def return_mainwindow(self):
        #print('this is return mainwindow')
        pass

    #查找物品在table中的位置
    def Seek_wireinfo(self):
        try:
            sql_order = "select WUPIN_NAME,TYPEOF,QTY_OK,QTY_NG,QTY_ONLINE,QTY_BF,SECUREQTY,Location_OK,Location_NG from NC_KUCUN_SUM where TXM='%s'" % (
                self.lin_txm.text())
            wire_info = Execute_Sql_Get_Date(sql_order)

            #print('26=%s' % wire_info)
            self.lin_typeof.setText(wire_info[0][0])
            self.lin_thing_truename.setText(wire_info[0][1])
            self.lin_ok.setText(wire_info[0][2])
            self.lin_ng.setText(wire_info[0][3])
            self.lin_online.setText(wire_info[0][4])
            self.lin_bf.setText(wire_info[0][5])
            self.lin_secureqty.setText(wire_info[0][6])
            self.lin_ok_address.setText(wire_info[0][7])
            self.lin_ng_address.setText(wire_info[0][8])

            get_reslute = self.Get_Windows_Statius()

            for xy in get_reslute:
                Ago_Now_Windows_Show_info.append(xy)

            for x in range(len(lin_txm_all)):
                if lin_txm_all[x] == self.lin_txm.text():
                    self.lab_lh_address.setText(str(x))

            self.table_jump_address(self.tab_thing_all,self.lin_txm.text())

        except Exception:
            #print()
            print_exc()



    #提到界面上的信息
    def Get_Windows_Statius(self):
        try:
            Now_Windows_Show_info = []
            Now_Windows_Show_info.append(self.lin_txm.text())
            Now_Windows_Show_info.append(self.lin_thing_truename.text())
            Now_Windows_Show_info.append(self.lin_typeof.text())
            Now_Windows_Show_info.append(self.lin_ok.text())
            Now_Windows_Show_info.append(self.lin_ng.text())
            Now_Windows_Show_info.append(self.lin_online.text())
            Now_Windows_Show_info.append(self.lin_bf.text())
            Now_Windows_Show_info.append(self.lin_secureqty.text())
            Now_Windows_Show_info.append(self.lin_ok_address.text())
            Now_Windows_Show_info.append(self.lin_ng_address.text())

            #print('All_Window%s' % Now_Windows_Show_info)

            return Now_Windows_Show_info
        except Exception:
            print_exc()

    def confire_reslute(self):
        try:
            if tabwidget_int==0:
                Now_Windows_Show_info = self.Get_Windows_Statius()

                # 把界面上显示的信息，有为空的进行附值
                for i in range(len(Now_Windows_Show_info)):
                    if Now_Windows_Show_info[i] == '':
                        Now_Windows_Show_info[i] = 'X'


                if self.com_desc.currentText() == '增加':

                    if self.Message_two('确认添加？') == QMessageBox.Yes:
                        sql_order = "insert into NC_KUCUN_SUM(TXM,WUPIN_NAME,TYPEOF,QTY_OK,QTY_NG,QTY_ONLINE,QTY_BF,SECUREQTY,Location_OK,Location_NG) " \
                                    "values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
                                    % (Now_Windows_Show_info[0], Now_Windows_Show_info[1], Now_Windows_Show_info[2], Now_Windows_Show_info[3], Now_Windows_Show_info[4],
                                       Now_Windows_Show_info[5], Now_Windows_Show_info[6], Now_Windows_Show_info[7], Now_Windows_Show_info[8], Now_Windows_Show_info[9])


                elif self.com_desc.currentText()=='删除':
                    #print('85')
                    if self.Message_two('确认删除？') == QMessageBox.Yes:
                        sql_order = "delete from NC_KUCUN_SUM where TXM='%s'"%self.lin_txm.text()



                elif self.com_desc.currentText() == '修改':
                    if self.Message_two("确认要修改吗？") == QMessageBox.Yes:
                        #print('102=%s' % Now_Windows_Show_info)
                        #print('103=%s' % Ago_Now_Windows_Show_info)
                        sql_order = "update NC_KUCUN_SUM set TXM='%s', WUPIN_NAME='%s' , TYPEOF='%s' , QTY_OK='%s' , QTY_NG='%s' ,QTY_ONLINE='%s' , " \
                                    "QTY_BF='%s' , SECUREQTY='%s' , Location_OK='%s' , Location_NG='%s' where TXM='%s'" \
                                    % (Now_Windows_Show_info[0], Now_Windows_Show_info[1], Now_Windows_Show_info[2], Now_Windows_Show_info[3], Now_Windows_Show_info[4],
                                       Now_Windows_Show_info[5],Now_Windows_Show_info[6], Now_Windows_Show_info[7], Now_Windows_Show_info[8], Now_Windows_Show_info[9],
                                       self.lin_txm.text())

                Execute_Sql_No_Get_Date(sql_order)
                #print('333')


            else:
                if self.Message_two('確認盤點？')==QMessageBox.Yes:
                    if self.com_ok_ng_on_bf.currentText() == 'OK品盤點':
                        sql_order="update NC_KUCUN_SUM set QTY_OK='%s' where TXM='%s'"% (self.lin_tab_peidiao.text(),self.lin_tab_txm.text())
                    if self.com_ok_ng_on_bf.currentText() == 'NG品盤點':
                        sql_order = "update NC_KUCUN_SUM set QTY_NG='%s' where TXM='%s'" % (self.lin_tab_peidiao.text(),self.lin_tab_txm.text())
                    if self.com_ok_ng_on_bf.currentText() == '在線品盤點':
                        sql_order = "update NC_KUCUN_SUM set QTY_ONLINE='%s' where TXM='%s'" % (self.lin_tab_peidiao.text(),self.lin_tab_txm.text())
                    if self.com_ok_ng_on_bf.currentText() == '報廢品盤點':
                        sql_order = "update NC_KUCUN_SUM set QTY_BF='%s' where TXM='%s'" % (self.lin_tab_peidiao.text(),self.lin_tab_txm.text())
                    Execute_Sql_No_Get_Date(sql_order)

                    time=str(datetime.now())[:len(str(datetime.now()))-3]
                    sql_order="insert into NC_KUCUN_INOUTTEST(TXM,WUPIN_NAME,QTY,INOUT,STATUS,CDT,USERNAME,WUPIN_OK) " \
                              "values('%s','%s','%s','%s','%s','%s','%s','%s')"\
                              %(self.lin_tab_txm.text(),self.lab_tab_thingname.text(),self.lin_tab_peidiao.text(),'盤點',
                                self.com_ok_ng_on_bf.currentText(),time,'administrator',self.lab_tab_thingnum.text())
                    Execute_Sql_No_Get_Date(sql_order)


            self.Clean_All()

        except Exception:
            print_exc()


    #設置人員選擇回車顯示物品盤點
    def thing_showinfo(self):
        try:
            sql_order = "select WUPIN_NAME,QTY_OK,QTY_NG,QTY_ONLINE,QTY_BF from NC_KUCUN_SUM WHERE TXM='%s' " % self.lin_tab_txm.text()
            get_reslute = Execute_Sql_Get_Date(sql_order)
            #print('115=%s' % get_reslute)
            self.lab_tab_thingname.setText(get_reslute[0][0])
            #print(self.com_desc.currentText())
            if self.com_ok_ng_on_bf.currentText()=='OK品盤點':
                self.lab_tab_thingnum.setText(get_reslute[0][1])
            if self.com_ok_ng_on_bf.currentText()=='NG品盤點':
                self.lab_tab_thingnum.setText(get_reslute[0][2])
            if self.com_ok_ng_on_bf.currentText()=='在線品盤點':
                self.lab_tab_thingnum.setText(get_reslute[0][3])
            if self.com_ok_ng_on_bf.currentText()=='報廢品盤點':
                self.lab_tab_thingnum.setText(get_reslute[0][4])
            return get_reslute

        except Exception:
            print_exc()

    #得到tabwidget的tab的界面
    def get_tabwidget_int(self,num):
        global tabwidget_int
        tabwidget_int=num



    def Clean_All(self):
        try:
            self.lin_txm.setText('')
            self.lin_thing_truename.setText('')
            self.lin_typeof.setText('')
            self.lin_ok.setText('')
            self.lin_ng.setText('')
            self.lin_online.setText('')
            self.lin_bf.setText('')
            self.lin_secureqty.setText('')
            self.lin_ok_address.setText('')
            self.lin_ng_address.setText('')
            self.Set_Table()
            Get_reslute_all.clear()
            #這是清除tehk盤點的數據的
            self.lin_tab_peidiao.clear()
            self.lin_tab_txm.clear()
            self.lab_tab_thingname.clear()
            self.lab_tab_thingnum.clear()
        except Exception:
            print_exc()


    def Set_Table(self):
        # All_lin_txm.clear()
        lin_txm_all.clear()

        sql_order = "select TXM,WUPIN_NAME,TYPEOF,QTY_OK,QTY_NG,QTY_ONLINE,QTY_BF,SECUREQTY,Location_OK,Location_NG from NC_KUCUN_SUM order by TYPEOF"
        get_reslute = Execute_Sql_Get_Date(sql_order)

        #print('201=%s' % get_reslute)
        self.tab_thing_all.setRowCount(len(get_reslute))  # 设置table的列数

        for i in range(10):
            for j in range(len(get_reslute)):
                data = QTableWidgetItem(str(get_reslute[j][i]))  # 转换后可插入表格
                self.tab_thing_all.setItem(j, i, data)

        for lin_txm in get_reslute:
            lin_txm_all.append(lin_txm[0])

    def TEST(self, i, j):  # 这是一个通过触发table来得到它的值的函数
        #print('167')
        try:
            if tabwidget_int==0:
                #print(i, j)
                #print('test')

                self.lab_lh_address.setText(str(i))

                #print(self.tab_thing_all.item(i, j).text())
                self.lin_txm.setText(self.tab_thing_all.item(i, 0).text())
                self.lin_thing_truename.setText(self.tab_thing_all.item(i, 1).text())
                self.lin_typeof.setText(self.tab_thing_all.item(i, 2).text())
                self.lin_ok.setText(self.tab_thing_all.item(i, 3).text())
                self.lin_ng.setText(self.tab_thing_all.item(i, 4).text())
                self.lin_online.setText(self.tab_thing_all.item(i, 5).text())
                self.lin_bf.setText(self.tab_thing_all.item(i, 6).text())
                self.lin_secureqty.setText(self.tab_thing_all.item(i, 7).text())
                self.lin_ok_address.setText(self.tab_thing_all.item(i, 8).text())
                self.lin_ng_address.setText(self.tab_thing_all.item(i, 9).text())


                get_reslute = self.Get_Windows_Statius()

                for xy in get_reslute:
                    Ago_Now_Windows_Show_info.append(xy)

        except Exception:
            print_exc()



    def to_lend(self):
        try:
            delete_sql_order = "delete Serson_TableTEST"
            file_name = self.to_lend_function(delete_sql_order, 'Serson_TableTEST', 5)
            #print('38', file_name)

        except Exception:
            print_exc()



    def lend(self):
        save_file_name = self.lend_function(self.tab_thing_all)
        #print('44', save_file_name)







if __name__=="__main__":
    app = QtWidgets.QApplication(argv)
    MainWindow = QtWidgets.QMainWindow()

    thing_check_son = thing_check_class()
    thing_check_son.show()


    exit(app.exec_())