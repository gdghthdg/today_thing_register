from Bind_wire import Ui_MainWindow
import wireandmachine_lh_monther
from Common_Function import *
import Set_Machine_monther


#  执行SQL语句并且有获取数据的要求
Button_Statius = []
Ago_All_Windows = []
Get_reslute_all = []
machine_all=[]





class Wirte_wireinfo(Ui_MainWindow, Farther, No_Main_Window,QMainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.Clean_All()
        self.change.setChecked(True)

        self.Set_Table()

        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)

        self.action_to_lend.triggered.connect(self.to_lend)

        self.action_lend.triggered.connect(self.lend)




    def Seek_wireinfo(self):
        try:
            sql_order="select MACHINES,SIZE,SYSTEMS,JI_OR_SKD,MONDEL,BI,CTAG,BMA,IAS,AGIS,FFC,INV_POWER_WIRE,DRIVER,DRIVER_MARCH,POWER_WIRE from MACHINE_LH where MACHINES='%s'"%(self.machine.text())
            wire_info=Execute_Sql_Get_Date(sql_order)
            #print('26=%s'%wire_info)

            self.size.setText(wire_info[0][1])
            self.systems.setText(wire_info[0][2])
            self.ji_or_skd.setText(wire_info[0][3])
            self.mondel.setText(wire_info[0][4])
            self.bi.setText(wire_info[0][5])
            self.ctag.setText(wire_info[0][6])
            self.bma.setText(wire_info[0][7])
            self.ias.setText(wire_info[0][8])
            self.agis.setText(wire_info[0][9])
            self.ffc.setText(wire_info[0][10])
            self.inv.setText(wire_info[0][11])
            self.power_march.setText(wire_info[0][12])
            self.dirver.setText(wire_info[0][13])
            self.power_wire.setText(wire_info[0][14])


            get_reslute = self.Get_Windows_Statius()

            for xy in get_reslute:
                Ago_All_Windows.append(xy)

            for x in range(len(machine_all)):
                if machine_all[x]==self.machine.text():
                    self.lab_lh_address.setText(str(x))

            #跳轉到時指定的地方
            self.table_jump_address(self.tab_machine_lh,self.machine.text())


        except Exception:
            #print()
            print_exc()


    def Set_Machine_Statius(self):
        set_machine_statius.show()


    def Set_Wire_Machine_Lh(self):
        set_wire_machine_lh.show()


    def Change_thing_num_address(self):
        #ui.hide()
        #change_thing_num_address.show()
        #print('66666')
        pass



    def Button_Statius_funaction(self):
        Button_Statius.clear()
        Button_Statius.append(self.add.isChecked())
        Button_Statius.append(self.delete_2.isChecked())
        Button_Statius.append(self.change.isChecked())
        #print('Button_Statius%s' % Button_Statius)



    def Get_Windows_Statius(self):
        try:
            All_Windows = []
            self.Button_Statius_funaction()
            All_Windows.append(self.machine.text())
            All_Windows.append(self.size.text())
            All_Windows.append(self.systems.text())
            All_Windows.append(self.ji_or_skd.text())
            All_Windows.append(self.mondel.text())
            All_Windows.append(self.bi.text())
            All_Windows.append(self.ctag.text())
            All_Windows.append(self.bma.text())
            All_Windows.append(self.ias.text())
            All_Windows.append(self.agis.text())
            All_Windows.append(self.ffc.text())
            All_Windows.append(self.inv.text())
            All_Windows.append(self.power_march.text())
            All_Windows.append(self.dirver.text())
            All_Windows.append(self.power_wire.text())

            #print('All_Window%s' % All_Windows)



            return All_Windows
        except Exception:
            print_exc()

    def confire_reslute(self):

        All_Windows = self.Get_Windows_Statius()


        #把
        for i in range(len(All_Windows)):
           if All_Windows[i]=='':
               All_Windows[i]='X'


        #if Button_Statius[0] == True:

        if Button_Statius[0] == True:
            try:
                if self.Message_two('确认添加？') == QMessageBox.Yes:
                    sql_order = "insert into MACHINE_LH(MACHINES,SIZE,SYSTEMS,JI_OR_SKD,MONDEL,BI,CTAG,BMA,IAS,AGIS,FFC,INV_POWER_WIRE,DRIVER,DRIVER_MARCH,POWER_WIRE,MACHINE_STATIUS) " \
                                "values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
                                % (All_Windows[0], All_Windows[1], All_Windows[2], All_Windows[3], All_Windows[4],
                                   All_Windows[5],All_Windows[6], All_Windows[7], All_Windows[8], All_Windows[9],
                                   All_Windows[10],All_Windows[11],All_Windows[12], All_Windows[13],All_Windows[14],'True')
                else:
                    pass
            except Exception:
                print_exc()

        elif Button_Statius[1] == True:
            try:
                #print('85')
                if self.Message_two('确认删除？') == QMessageBox.Yes:
                    get_reslute = self.Get_Windows_Statius()
                    sql_order = "delete from MACHINE_LH where MACHINES='%s' and SIZE='%s' and SYSTEMS='%s' and JI_OR_SKD='%s' and MONDEL='%s' and BI='%s' and " \
                                "CTAG='%s' and BMA='%s' and IAS='%s' and AGIS='%s' and FFC='%s' and INV_POWER_WIRE='%s' and DRIVER='%s' and DRIVER_MARCH='%s' and POWER_WIRE='%s'" \
                                % (get_reslute[0], get_reslute[1], get_reslute[2], get_reslute[3],
                                   get_reslute[4]
                                   , get_reslute[5], get_reslute[6], get_reslute[7], get_reslute[8],
                                   get_reslute[9],
                                   get_reslute[10], get_reslute[11], get_reslute[12], get_reslute[13],get_reslute[14])
                else:
                    pass
            except Exception:
                print_exc()


        elif Button_Statius[2] == True:
            try:
                if self.Message_two("确认要修改吗？") == QMessageBox.Yes:
                    #print('102=%s'%All_Windows)
                    #print('103=%s'%Ago_All_Windows)
                    sql_order = "update MACHINE_LH set MACHINES='%s' , SIZE='%s' , SYSTEMS='%s' , JI_OR_SKD='%s' , MONDEL='%s' , BI='%s' , " \
                                "CTAG='%s' , BMA='%s' , IAS='%s' , AGIS='%s' , FFC='%s' , INV_POWER_WIRE='%s' , DRIVER='%s' , DRIVER_MARCH='%s' , POWER_WIRE='%s'" \
                                " where MACHINES='%s' and SIZE='%s' and SYSTEMS='%s' and JI_OR_SKD='%s' and MONDEL='%s' and BI='%s' and " \
                                "CTAG='%s' and BMA='%s'and IAS='%s' and AGIS='%s' and FFC='%s' and INV_POWER_WIRE='%s' and DRIVER='%s' and DRIVER_MARCH='%s' and POWER_WIRE='%s'" \
                                % (All_Windows[0], All_Windows[1], All_Windows[2], All_Windows[3], All_Windows[4],
                                   All_Windows[5],
                                   All_Windows[6], All_Windows[7], All_Windows[8], All_Windows[9], All_Windows[10],
                                   All_Windows[11],
                                   All_Windows[12], All_Windows[13],All_Windows[14], Ago_All_Windows[0], Ago_All_Windows[1],
                                   Ago_All_Windows[2], Ago_All_Windows[3], Ago_All_Windows[4], Ago_All_Windows[5],
                                   Ago_All_Windows[6], Ago_All_Windows[7], Ago_All_Windows[8], Ago_All_Windows[9],
                                   Ago_All_Windows[10], Ago_All_Windows[11],
                                   Ago_All_Windows[12], Ago_All_Windows[13], Ago_All_Windows[14])
                else:
                    #print('gggg')
                    pass
                #print('111111')
            except Exception:
                print_exc()
        #print('2222')
        ##print(sql_order)
        #print('333')
        try:
            Execute_Sql_No_Get_Date(sql_order)
            #print('333')
            self.Clean_All()
        except Exception:
            print_exc()



    def Mian_Window_show(self):
        #print('')
        print_exc()


    def Set_Table(self):
        # All_Machine.clear()
        machine_all.clear()

        sql_order="select MACHINES,SIZE,SYSTEMS,JI_OR_SKD,MONDEL,BI,CTAG,BMA,IAS,AGIS,FFC,INV_POWER_WIRE,DRIVER,DRIVER_MARCH,POWER_WIRE from MACHINE_LH where MACHINE_STATIUS='True' order by SIZE"
        get_reslute=Execute_Sql_Get_Date(sql_order)
        #get_reslute=sorted(list(set(get_reslute)))
        #print('201=%s'%get_reslute)
        self.tab_machine_lh.setRowCount(len(get_reslute))  #设置table的列数

        for i in range(15):
            for j in range(len(get_reslute)):
                data = QTableWidgetItem(str(get_reslute[j][i]))  # 转换后可插入表格
                self.tab_machine_lh.setItem(j, i, data)

        for machine in get_reslute:
            machine_all.append(machine[0])

    def TEST(self,i,j): #这是一个通过触发table来得到它的值的函数
        #print(i,j)
        #print('test')
        try:
            self.lab_lh_address.setText(str(i))
        except Exception:
            print_exc()
        try:
            #print(self.tab_machine_lh.item(i, j).text())
            self.machine.setText(self.tab_machine_lh.item(i, 0).text())
            self.size.setText(self.tab_machine_lh.item(i, 1).text())
            self.systems.setText(self.tab_machine_lh.item(i, 2).text())
            self.ji_or_skd.setText(self.tab_machine_lh.item(i, 3).text())
            self.mondel.setText(self.tab_machine_lh.item(i, 4).text())
            self.bi.setText(self.tab_machine_lh.item(i, 5).text())
            self.ctag.setText(self.tab_machine_lh.item(i, 6).text())
            self.bma.setText(self.tab_machine_lh.item(i,7).text())
            self.ias.setText(self.tab_machine_lh.item(i, 8).text())
            self.agis.setText(self.tab_machine_lh.item(i, 9).text())
            self.ffc.setText(self.tab_machine_lh.item(i, 10).text())
            self.inv.setText(self.tab_machine_lh.item(i, 11).text())
            self.power_march.setText(self.tab_machine_lh.item(i, 12).text())
            self.dirver.setText(self.tab_machine_lh.item(i, 13).text())
            self.power_wire.setText(self.tab_machine_lh.item(i, 14).text())

            get_reslute=self.Get_Windows_Statius()

            for xy in get_reslute:
                Ago_All_Windows.append(xy)

            def Mian_Window_show():
                #print('這是用來顯示主界面的')
                pass




        except Exception:
            print_exc()

    def to_lend(self):
        self.cwd = os.getcwd()  # 获取当前程序文件位置

        try:

            fileName_choose, filetype = QFileDialog.getOpenFileName(self,"选取文件",self.cwd,"All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,用双分号间隔

            if fileName_choose == "":
                #print("\n取消选择")
                return

            #print("\n你选择的文件为:")
            #print(fileName_choose)
            #print("文件筛选器类型: ", filetype)

        except Exception:
            print_exc()



        #這是一個要保存的文件選項
        # fileName_choose, filetype = QFileDialog.getSaveFileName(self,
        #                                                         "文件保存",
        #                                                         self.cwd,  # 起始路径
        #                                                         "All Files (*);;Text Files (*.txt);;Text Files (*.jpg)")
        #
        #
        # if fileName_choose == "":
        #     #print("\n取消选择")
        #     return
        #
        # #print("\n你选择要保存的文件为:")
        # #print(fileName_choose)
        # #print("文件筛选器类型: ", filetype)



    def lend(self):
        save_file_name=self.lend_function(self.tab_machine_lh)
        #print('44',save_file_name)


    def Clean_All(self):
        global i

        self.machine.setText('')
        self.size.setText('')
        self.systems.setText('')
        self.ji_or_skd.setText('')
        self.mondel.setText('')
        self.bi.setText('')
        self.ctag.setText('')
        self.ias.setText('')
        self.agis.setText('')
        self.ffc.setText('')
        self.inv.setText('')
        self.power_march.setText('')
        self.dirver.setText('')
        self.power_wire.setText('')
        self.bma.setText('')
        Ago_All_Windows.clear()

        self.Set_Table()

        Get_reslute_all.clear()

        # my_list = ['1', '2', '3']
        # my_str, ok = QInputDialog.getItem(self, "下拉框", '輸入密碼', my_list)
        # #print(my_str, ok)


if __name__ == "__main__":
    import Thing_Check_monther
    app = QtWidgets.QApplication(argv)
    ui = Wirte_wireinfo()
    ui.show()
    set_machine_statius = Set_Machine_monther.SET_MACHINE_USE()
    set_wire_machine_lh= wireandmachine_lh_monther.Wire_machine_lh()



    change_thing_num_address=Thing_Check_monther.thing_check_class()
    exit(app.exec_())

