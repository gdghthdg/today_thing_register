from Common_Function import *
from Main_Window import Ui_MainWindow

#  执行SQL语句并且有获取数据的要求
Button_Statius = []
Ago_Now_Windows_Show_info = []
Get_reslute_all = []
lin_txm_all=[]
#這是一個tabwidget顯示的第幾個界面，默認第一
tabwidget_int=0



class admin_change(Farther,QMainWindow):


    def Seek_wireinfo(self):
        try:
            sql_order = "select USER_NAME,CARD_ID,PHONE_ADDR,USER_BUMEN,DAIMA,EMAIL from MFG_USER where USER_ID='%s'" % (
                self.lin_worker_id.text())
            wire_info = Execute_Sql_Get_Date(sql_order)

            print('26=%s' % wire_info)
            self.lin_worker_name.setText(wire_info[0][0])
            self.lin_card_id.setText(wire_info[0][1])
            self.lin_phone.setText(wire_info[0][2])
            self.lin_bumen_name.setText(wire_info[0][3])
            self.lin_bumen_id.setText(wire_info[0][4])
            self.lin_email.setText(wire_info[0][5])


            get_reslute = self.Get_Windows_Statius()

            for xy in get_reslute:
                Ago_Now_Windows_Show_info.append(xy)

            for x in range(len(lin_txm_all)):
                if lin_txm_all[x] == self.lin_txm.text():
                    self.lab_lh_address.setText(str(x))

        except Exception:
            print()



    #得到界面上的信息
    def Get_Windows_Statius(self):
        try:
            Now_Windows_Show_info = []
            Now_Windows_Show_info.append(self.lin_worker_id.text())
            Now_Windows_Show_info.append(self.lin_worker_name.text())
            Now_Windows_Show_info.append(self.lin_card_id.text())
            Now_Windows_Show_info.append(self.lin_phone.text())
            Now_Windows_Show_info.append(self.lin_bumen_name.text())
            Now_Windows_Show_info.append(self.lin_bumen_id.text())
            Now_Windows_Show_info.append(self.lin_email.text())


            print('All_Window%s' % Now_Windows_Show_info)

            return Now_Windows_Show_info
        except Exception:
            print_exc()

    def confire_admin_reslute(self):
        try:
            time_now = str(datetime.now())[:len(str(datetime.now())) - 3]

            Now_Windows_Show_info = self.Get_Windows_Statius()

            # 把界面上显示的信息，有为空的进行附值
            for i in range(len(Now_Windows_Show_info)):
                if Now_Windows_Show_info[i] == '':
                    Now_Windows_Show_info[i] = 'X'


            if self.com_desc.currentText() == '增加':

                if self.Message_two('确认添加？') == QMessageBox.Yes:
                    sql_order = "insert into MFG_USER(USER_ID,USER_NAME,CARD_ID,PHONE_ADDR,USER_BUMEN,DAIMA,EMAIL,CDT) " \
                                "values('%s','%s','%s','%s','%s','%s','%s','%s')" \
                                % (Now_Windows_Show_info[0], Now_Windows_Show_info[1], Now_Windows_Show_info[2], Now_Windows_Show_info[3], Now_Windows_Show_info[4],
                                   Now_Windows_Show_info[5], Now_Windows_Show_info[6],time_now)


            elif self.com_desc.currentText()=='删除':
                print('85')
                if self.Message_two('确认删除？') == QMessageBox.Yes:
                    sql_order = "delete from MFG_USER where USER_ID='%s'"%self.lin_worker_id.text()



            elif self.com_desc.currentText() == '修改':
                if self.Message_two("确认要修改吗？") == QMessageBox.Yes:
                    print('102=%s' % Now_Windows_Show_info)
                    print('103=%s' % Ago_Now_Windows_Show_info)
                    sql_order = "update MFG_USER set USER_ID='%s', USER_NAME='%s' , CARD_ID='%s' , PHONE_ADDR='%s' , USER_NUMEN='%s' ,DAIMA='%s' , " \
                                "EMAIL='%s',CDT='%s' where USER_ID='%s'" \
                                % (Now_Windows_Show_info[0], Now_Windows_Show_info[1], Now_Windows_Show_info[2], Now_Windows_Show_info[3], Now_Windows_Show_info[4],
                                   Now_Windows_Show_info[5],Now_Windows_Show_info[6], time_now,self.lin_worker_id.text())

            Execute_Sql_No_Get_Date(sql_order)
            print('333')

            self.Clean_All()

        except Exception:
            print_exc()




    #得到tabwidget的tab的界面
    def get_tabwidget_int(self,num):
        global tabwidget_int
        tabwidget_int=num



    def Clean_All(self):
        try:
            self.lin_worker_id.setText('')
            self.lin_worker_name.setText('')
            self.lin_card_id.setText('')
            self.lin_phone.setText('')
            self.lin_bumen_name.setText('')
            self.lin_bumen_id.setText('')
            self.lin_email.setText('')
            self.Set_Table()
            Get_reslute_all.clear()

        except Exception:
            print_exc()


    def Set_Table(self):
        # All_lin_txm.clear()
        lin_txm_all.clear()

        sql_order = "select USER_ID,USER_NAME,CARD_ID,PHONE_ADDR,USER_BUMEN,DAIMA,EMAIL,CDT from MFG_USER ORDER BY CDT DESC"
        get_reslute = Execute_Sql_Get_Date(sql_order)

        print('201=%s' % get_reslute)
        self.tab_thing_all.setRowCount(len(get_reslute))  # 设置table的列数

        for i in range(8):
            for j in range(len(get_reslute)):
                data = QTableWidgetItem(str(get_reslute[j][i]))  # 转换后可插入表格
                self.tab_thing_all.setItem(j, i, data)

        for lin_txm in get_reslute:
            lin_txm_all.append(lin_txm[0])



    def TEST(self, i, j):  # 这是一个通过触发table来得到它的值的函数
        print('167')
        try:
            if tabwidget_int==0:
                print(i, j)
                print('test')

                self.lab_lh_address.setText(str(i))

                print(self.tab_thing_all.item(i, j).text())

                self.lin_worker_id.setText(self.tab_thing_all.item(i, 0).text())
                self.lin_worker_name.setText(self.tab_thing_all.item(i, 1).text())
                self.lin_card_id.setText(self.tab_thing_all.item(i, 2).text())
                self.lin_phone.setText(self.tab_thing_all.item(i, 3).text())
                self.lin_bumen_name.setText(self.tab_thing_all.item(i, 4).text())
                self.lin_bumen_id.setText(self.tab_thing_all.item(i, 5).text())
                self.lin_email.setText(self.tab_thing_all.item(i, 6).text())


                get_reslute = self.Get_Windows_Statius()

                for xy in get_reslute:
                    Ago_Now_Windows_Show_info.append(xy)

        except Exception:
            print_exc()






if __name__=="__main__":
    app = QtWidgets.QApplication(argv)
    MainWindow = QtWidgets.QMainWindow()

    admin_change_son = admin_change()
    admin_change_son.show()


    exit(app.exec_())