from Common_Function import *
from thing_keep_hint import Ui_MainWindow



class thing_keep_class(Ui_MainWindow,Farther,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        print(self.Date_delete(-90,Get_Now_Time_have_zero()))
        self.init_timer()
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        self.tableWidget.setWordWrap(True)
        self.dat_hint_time.setDateTime(QDateTime.addSecs(QDateTime.currentDateTime(), 30*60*60*24))
        self.set_table()


    def update_time(self):
        pass
        # self.lcd_clock.display(time.strftime("%X", time.localtime()))
        #print('时间:')

    def test(self):
        #self.date_sub()
        self.check_date()

    def ok_off(self):
        print("这是一个测试功能")

    def confir_result(self):
        try:
            self.set_hint_time()
            widget_all = [self.lin_thing_name,  self.lin_hint_time]
            if self.com_choice.currentText()=='增加':
                sql_order="insert into thing_hint(thing_txm,thing_name,CDT,expire_time) values('%s','%s','%s','%s')"%(self.lin_thing_txm.text(),self.lin_thing_name.text(),Get_Now_Time(),self.dat_hint_time.text())
                print(sql_order)

            elif self.com_choice.currentText()=='修改':
                pass

            Execute_Sql_No_Get_Date(sql_order)

        except Exception:
            print_exc()


    #设置一个隐藏时间,自动进行更新
    def set_hint_time(self):
        try:
            get_time=self.Date_delete(int(self.lin_hint_time.text()),Get_Now_Time_have_zero())
            #self.dat_hint_time.setDateTime(get_time[0])
            secs=int(self.lin_hint_time.text())*60*60*24
            print(secs)
            self.dat_hint_time.setDateTime(QDateTime.addSecs(QDateTime.currentDateTime(), secs))
            print(get_time)

        except Exception:
            print_exc()


    #设置table显示
    def set_table(self):
        sql_order="select * from thing_hint"
        table_name=self.tableWidget
        table_cow=4
        Common_Table.Set_Table(self,sql_order,table_name,5)


    #得到table_显示
    def get_table_data(self,i,j):
        try:
            widget_all=self.class_comment()
            Common_Table.Get_Table_Click_Data(self,widget_all,self.tableWidget,i)
        except Exception:
            print_exc()


    #一个检查的数据的函数
    def check_date(self):
        try:
            sql_order="select * from thing_hint"
            get_result=Execute_Sql_Get_Date(sql_order)
            print(get_result)
            for i in range(len(get_result)):
                print(get_result[i][3],get_result[i][2])
                day=get_result[i][3]-get_result[i][2]
                print(day)

                sql_order="update thing_hint set surplus_time='%s' where thing_txm='%s'"%(day,get_result[i][0])
                Execute_Sql_No_Get_Date(sql_order)

                #self.date_sub()
                self.set_table()
        except Exception:
            print_exc()


    #一个界面控件的总称,应该可以放在一个类属性中
    def class_comment(self):
        widget_all=[self.lin_thing_txm,self.lin_thing_name,self.lin_hint_time]
        return widget_all


    #清除所有界面数据
    def clear_all(self):
        widget_all=self.class_comment()
        for i in widget_all:
            i.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    ui = thing_keep_class()
    ui.show()
    exit(app.exec_())





