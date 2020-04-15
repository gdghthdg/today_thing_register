'''這里的功能主要包括，线体的各种线材的查询，物品的破损率的查询的功能
还有未来的线材的损耗的查询'''


# -*- coding: utf-8 -*-
from Get_Machine_Num_for_excel import Get_Excel_AllMachine_Num
from PyQt5.QtCore import QDate, QTime
from PyQt5.QtWidgets import *
from datetime import datetime, timedelta
from matplotlib.ticker import FuncFormatter

from Date_Analyse import Ui_MainWindow
from Get_Future_Three_Month import *
from matplotlib.pyplot import MultipleLocator

import numpy as np
import matplotlib.pyplot as plt
from Common_Function import *

plt.rcParams['font.sans-serif'] = ['SimHei']
Can_Fei = ['電源線', '測試線', '驅動板', 'FFC']

show_noshow = [1]
lines = []
X_All = []
Y_All = []
All_Future = {}
XY_DIST = {}
X_Y_Dist = {}
X_Y_Dist1 = {}
Two_Legend = {}
Peraration_A_ll = []
Ago_All_Dist = {}
Have_LH = []
All_Dist = {}
LH_PCDF_MACHINE_NUM = []
Execute_Class = 0  # 要执行什么的功能
Excetu_One = []
Determine_User_Choise = []
Aces_excuext_one = []
Color_All = [
    '#FAEBD7',
    '#00FFFF',
    '#7FFFD4',
    '#F0FFFF',
    '#F5F5DC',
    '#FFE4C4',
    '#000000',
    '#FFEBCD',
    '#0000FF',
    '#8A2BE2',
    '#A52A2A',
    '#DEB887',
    '#5F9EA0',
    '#7FFF00',
    '#D2691E',
    '#FF7F50',
    '#6495ED',
    '#FFF8DC',
    '#DC143C',
    '#00FFFF',
    '#00008B',
    '#008B8B',
    '#B8860B',
    '#A9A9A9',
    '#006400',
    '#BDB76B',
    '#8B008B',
    '#556B2F',
    '#FFA500',
    '#DA70D6',
    '#FFF5EE',
    '#A0522D',
    '#FF6347',
    '#40E0D0',
    '#EE82EE',
    '#F5DEB3',
    '#FFFFFF',
    '#F5F5F5',
    '#FFFF00',
    '#9ACD32'
]
Color_All_Two = [
    '#E0FFFF',
    '#FAF0E6',
    '#FF00FF',
    '#800000',
    '#66CDAA',
    '#0000CD',
    '#BA55D3',
    '#9370DB',
    '#3CB371',
    '#7B68EE',
    '#00FA9A',
    '#48D1CC',
    '#C71585',
    '#191970',
    '#F5FFFA',
    '#FFE4E1',
    '#FFE4B5',
    '#FFDEAD',
    '#000080',
    '#FDF5E6',
    '#808000',
    '#6B8E23',
]

Common_Thing = []
Common_Thing_Num = 0
All_Thing_Class = ['']
All_Thing_Class_son = ['']
STATUS_ALL = ['NG退料', 'NG品更換']


def Read_load_Config_Lines_info():
    line_place = open('D:\\config\\line.txt', 'r', encoding='utf8')
    for file in line_place.readlines():
        file = file[:len(file) - 1]
        if file != '\ufeff':
            lines.append(file)
    return lines




def to_percent(temp, position):
    return '%3.3f' % (1 * temp) + '%'


class Choice_Condition(Ui_MainWindow,Farther,No_Main_Window, QMainWindow):
    try:
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.Config_info()
            # 菜单的信号
            self.act_shuhu.triggered.connect(self.Get_All_LH_Sql)
            self.act_future.triggered.connect(self.Fture_Wire_Sum)
            self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)


        def return_mainwindow(self):
            print('this is return mainwindows')

        #  这是从以前物品的损耗率，然后得到未来三个月的总产量，计算出一个未来的损耗数
        def Fture_Wire_Sum(self):
            try:
                Legend_name = []
                show_noshow.clear()
                show_noshow.append(0)
                Future_Thing_Num = {}

                self.Get_All_LH_Sql()

                # V23.6非三星---BI(30-30)': ['R377B000NM000', 0.0, 0.0, 0.0],{'Light
                # Sensor': 0, '10-6電源線': 0.27684616844902865}.

                #这是从一个py中得到三个月后物品的数量
                Future_Machine_Num = Get_Future_three_wire_sum()

                # print('all_future=%s' % All_Future)
                # print('future_machine_num=%s'%Future_Machine_Num)

                for i in list(All_Future.keys()):
                    SH = float(All_Future[i])
                    SUM = int(Future_Machine_Num[i][1]) * SH
                    SUM1 = int(Future_Machine_Num[i][2]) * SH
                    SUM2 = int(Future_Machine_Num[i][3]) * SH

                    print('i=%s' % i)
                    print(SH,SUM,SUM1,SUM2)

                    if int(SUM) + int(SUM1) + int(SUM2) > 0:
                        Future_Thing_Num[i] = [int(SUM), int(SUM1), int(SUM2)]
                        Legend_name.append(
                            "%s[%s,%s,%s]" %
                            (i, int(SUM), int(SUM1), int(SUM2)))

                t1 = [Future_Thing_Num[i][0] for i in list(Future_Thing_Num.keys())]
                t2 = [Future_Thing_Num[i][1] for i in list(Future_Thing_Num.keys())]
                t3 = [Future_Thing_Num[i][2] for i in list(Future_Thing_Num.keys())]

                fig = plt.figure(8, dpi=150)

                ax1 = fig.add_subplot(111)
                plt.title('三个月后的物品需求')
                plt.xticks(
                    np.arange(
                        len(Future_Thing_Num)),
                    list(
                        Future_Thing_Num.keys()),
                    rotation=90,
                    size='xx-small')

                ax2 = ax1.twinx()
                b2 = ax1.bar(
                    np.arange(
                        len(Future_Thing_Num)) +
                    0.3,
                    t1,
                    alpha=0.5,
                    width=0.3,
                    color=Color_All,
                    edgecolor='red',
                    lw=1)
                b1 = ax1.bar(
                    np.arange(
                        len(Future_Thing_Num)),
                    t2,
                    alpha=0.5,
                    width=0.3,
                    color=Color_All,
                    edgecolor='red',
                    lw=1)
                b3 = ax1.bar(
                    np.arange(
                        len(Future_Thing_Num)) -
                    0.3,
                    t3,
                    alpha=0.5,
                    width=0.3,
                    color=Color_All,
                    edgecolor='red',
                    lw=1)

                plt.legend(b1, Legend_name, loc='best', ncol=2, prop={'size': 3})

                for x, y in enumerate(t1):
                    ax1.text(
                        x +
                        0.3,
                        y,
                        '%s' %
                        y,
                        ha='center',
                        va='bottom',
                        fontsize=7)
                for x, y in enumerate(t2):
                    ax1.text(x, y, '%s' % y, ha='center', va='bottom', fontsize=7)
                for x, y in enumerate(t3):
                    ax1.text(
                        x -
                        0.3,
                        y,
                        '%s' %
                        y,
                        ha='center',
                        va='bottom',
                        fontsize=7)

                plt.show()
            except Exception:
                print_exc()


        def Get_sql_Set_config(self, sql_order, All_Thing):
            # print('88')
            # print(sql_order)
            get_reslute = Execute_Sql_Get_Date(sql_order)
            for i in get_reslute:
                All_Thing.append(i[0])

        def Config_info(self):
            self.dat_finally.setDate(QDate.currentDate())
            (Seven_Day, Year, Month, Day) = self.Date_delete(30)  # get 七天前的日期设置默认
            self.dat_start.setDate(QDate(Year, Month, Day))
            Now_time = str(datetime.now())[11:19].split(':')
            self.tim_finally.setTime(
                QTime(int(Now_time[0]), int(Now_time[1]), int(Now_time[2])))
            self.dat_start.setCalendarPopup(True)
            self.dat_finally.setCalendarPopup(True)
            self.com_lines_son.addItems(Read_load_Config_Lines_info())
            # self.Get_sql_Set_config('select distinct TYPEOF from NC_KUCUN_INOUT group by TYPEOF',All_Thing_Class)
            self.com_thing_class.addItems(All_Thing_Class)
            Class_All = "select distinct WUPIN_NAME from NC_KUCUN_INOUT where CDT between '2018-01-16 00:00:00:000' and '%s' group by WUPIN_NAME " % str(
                datetime.now())[:23]
            # print(Class_All)
            self.Get_sql_Set_config(Class_All, All_Thing_Class_son)
            self.com_thing_class_son.addItems(All_Thing_Class_son)

        def Qmassage_Show(self, title):
            choice = QMessageBox.question(self, '确认', title, QMessageBox.Yes)
            return choice

        def Get_Window_Data_son(self, windows):
            if windows != '':
                Determine_User_Choise.append(1)
            else:
                Determine_User_Choise.append(0)

        def Get_Window_Data(self):
            Determine_User_Choise.clear()
            self.Get_Window_Data_son(self.com_lines.currentText())
            self.Get_Window_Data_son(self.com_lines_son.currentText())
            self.Get_Window_Data_son(self.com_thing_class.currentText())
            self.Get_Window_Data_son(self.com_thing_class_son.currentText())
            # print('Determine_User_Choise=%s'%Determine_User_Choise)
            return Determine_User_Choise

        def Matplotlib_Son(self, sql_order, s, titles):
            self.Get_Sql_Data_In_XY(sql_order)
            plt.subplot(s)
            plt.title(titles, fontsize=10)
            # print('211@@@@@')

            l1 = plt.bar([i for i in list(All_Dist.keys())], [All_Dist[i][0] for i in list(
                All_Dist.keys())], alpha=0.5, width=0.3, color=Color_All, edgecolor='red', lw=1)
            plt.xticks(np.arange(len(list(All_Dist.keys()))), [
                i for i in list(All_Dist.keys())], rotation=65, size='xx-small')

            for x, y in enumerate([All_Dist[i][0] for i in list(All_Dist.keys())]):
                plt.text(x, y, '%s' % y, ha='center', va='bottom')

            plt.legend(l1,
                       [All_Dist[i][2] for i in list(All_Dist.keys())],
                       loc='best',
                       fontsize='xx-small',
                       ncol=2,
                       title="物品总数%d" % np.sum([All_Dist[i][0] for i in list(All_Dist.keys())]),
                       prop={'size': 3})

        def Matplotlib_Add_Aces(
                self,
                sql_order,
                radius_size,
                ago_start_time,
                ago_finally_time):
            global X_Y_Dist
            global X_Y_Dist1
            global Color_All
            global Two_Legend
            global Ago_All_Dist
            (start_time, finally_time) = self.Date_Choice()  # 从界面上得到现在的时间差
            try:
                XY_Reslute = self.Get_Sql_Data_In_XY(sql_order)
                if XY_Reslute == 0:
                    return 0
                X_All = Peraration_A_ll

                if len(Aces_excuext_one) == 0:
                    for i in list(All_Dist.keys()):
                        Ago_All_Dist[i] = All_Dist[i]

                else:
                    p = 0
                    for i in list(All_Dist.keys()):  # 把以前的颜色换给现在的All_Dist
                        if i in list(Ago_All_Dist.keys()):
                            All_Dist[i][0] = (Ago_All_Dist[i][0])
                        else:
                            All_Dist[i][0] = (Color_All_Two[p])
                            p += 1

                    # print(Ago_All_Dist)
                    # print(All_Dist)

                if len(Aces_excuext_one) == 0:
                    l1 = plt.pie(
                        [
                            All_Dist[i][1] for i in list(
                            All_Dist.keys())],
                        textprops={
                            'fontsize': 7,
                            'color': 'black'},
                        radius=radius_size,
                        autopct='%3.2f%%',
                        pctdistance=0.9,
                        colors=[
                            All_Dist[i][3] for i in list(
                                All_Dist.keys())],
                        wedgeprops=dict(
                            linewidth=2,
                            width=0.4,
                            edgecolor='w'),
                        rotatelabels=True)  # 图例

                    Aces_excuext_one.append(1)
                    first_legend = plt.legend([All_Dist[i][2] for i in list(All_Dist.keys())],
                                              fontsize='xx-small',
                                              ncol=1,
                                              title="%s到%s物品总数%s(内圆)" % (start_time[5:9],
                                                                         finally_time[5:9],
                                                                         np.sum([All_Dist[i][0] for i in
                                                                                 list(All_Dist.keys())])),
                                              loc='upper right')
                    plt.gca().add_artist(first_legend)
                    # print('第一个图例')

                else:
                    l1 = plt.pie(
                        [
                            All_Dist[i][1] for i in list(
                            All_Dist.keys())],
                        textprops={
                            'fontsize': 7,
                            'color': 'black'},
                        radius=radius_size,
                        autopct='%3.2f%%',
                        pctdistance=0.8,
                        colors=[
                            All_Dist[i][3] for i in list(
                                All_Dist.keys())],
                        wedgeprops=dict(
                            linewidth=3,
                            width=0.4,
                            edgecolor='w'),
                        rotatelabels=True,
                        labels=[
                            All_Dist[i][2] for i in list(
                                All_Dist.keys())],
                        labeldistance=10)  # 图例

                    legend_two = plt.legend(fontsize='xx-small',
                                            ncol=1,
                                            title="%s到%s物品总数%s(外圆)" % (ago_start_time[5:10],
                                                                       ago_finally_time[5:10],
                                                                       np.sum(Y_All)),
                                            loc='upper left')  # 设置图例标题、位置bbox_to_anchor=(1,1)

                    # print('第二个图例')

                # plt.annotate('gg', xy=(-1, 0.4), xytext=(legend_two), arrowprops=dict(facecolor='blue', shrink=-1))

                plt.title(r'各物品占总数情况环形图', fontsize=15)
                plt.axis('equal')  # 设置坐标轴比例以显示为圆形

            except Exception:
                print_exc()

        def Matplotlib_New(self):
            global Execute_Class
            Execute_Class = 1
            Have_LH.clear()
            try:
                Have_Thing = []
                plt.close()
                self.Clean_ALL()

                Get_Reslute = self.Get_Window_Data()

                (start_time, finally_time) = self.Date_Choice()

                TIME_STATUS = "and (STATUS='NG品更換' or STATUS='NG退料') and CDT between '%s' and '%s'" % self.Date_Choice(
                )
                # TIME_STATUS = "and (STATUS='NG品更換' or STATUS='NG退料')"
                time_titles = '%s到%s' % (start_time[:9], finally_time[:9])
                fig = plt.figure(figsize=(8, 6), dpi=150)

                fig.tight_layout()
                if Get_Reslute == [0, 0, 0, 0]:
                    Sort_Requirment = "TYPEOF!='%s' %s" % ('1', TIME_STATUS)
                    sql_order = "select TYPEOF,QTY from NC_KUCUN_INOUT where %s" % (
                        Sort_Requirment)
                    titles = '%s' % (time_titles)

                elif Get_Reslute in [[1, 1, 0, 0], [0, 1, 0, 0]]:
                    Sort_Requirment = "STATION='%s' %s" % (
                        self.com_lines_son.currentText(), TIME_STATUS)
                    # print(Sort_Requirment)
                    sql_order = "select TYPEOF,QTY from NC_KUCUN_INOUT where %s" % (
                        Sort_Requirment)
                    # print('184=%s'%sql_order)
                    titles = '%s%s所用物品情况' % (
                        time_titles, self.com_lines_son.currentText())
                    # fig.tight_layout()  # 调整整体空白
                    # plt.subplots_adjust(wspace=0.5, hspace=0.5)  # 调整子图间距

                elif Get_Reslute == [1, 0, 0, 0]:
                    Sort_Requirment = "STATION like '%s' %s" % (
                        self.com_lines.currentText() + '%', TIME_STATUS)
                    sql_order = "select TYPEOF,QTY from NC_KUCUN_INOUT where %s" % (
                        Sort_Requirment)

                    titles = '%s%s所用物品情况' % (
                        time_titles, self.com_lines.currentText())

                elif Get_Reslute == [0, 0, 1, 0]:
                    Sort_Requirment = "TYPEOF='%s' %s" % (
                        self.com_thing_class.currentText(), TIME_STATUS)
                    # sql_order = "select WUPIN_NAME,count(*) from NC_KUCUN_INOUT where %s  group by WUPIN_NAME" % (Sort_Requirment)
                    sql_order = "select STATION,QTY from NC_KUCUN_INOUT where %s" % (
                        Sort_Requirment)
                    titles = '%s%s在各线使用情况' % (
                        time_titles, self.com_thing_class.currentText())

                elif Get_Reslute == [0, 1, 1, 0]:
                    Sort_Requirment = "STATION='%s' and TYPEOF='%s' %s" % (
                        self.com_lines_son.currentText(), self.com_thing_class.currentText(), TIME_STATUS)
                    sql_order = "select WUPIN_NAME,QTY from NC_KUCUN_INOUT where %s" \
                                % (Sort_Requirment)
                    titles = '%s在%s中%s使用情况' % (time_titles,
                                               self.com_lines_son.currentText(),
                                               self.com_thing_class.currentText())

                elif Get_Reslute == [0, 0, 0, 1]:
                    Sort_Requirment = "WUPIN_NAME='%s' %s" % (
                        self.com_thing_class_son.currentText(), TIME_STATUS)
                    sql_order = "select STATION,QTY from NC_KUCUN_INOUT where %s" \
                                % (Sort_Requirment)
                    titles = '%s%s在各线体的使用情况' % (
                        time_titles, self.com_thing_class_son.currentText())

                elif Get_Reslute == [0, 1, 0, 1]:
                    Sort_Requirment = "STATION='%s' and WUPIN_NAME='%s' %s" % (
                        self.com_lines_son.currentText(), self.com_thing_class_son, TIME_STATUS)
                    sql_order = "select WUPIN_NAME,QTY from NC_KUCUN_INOUT where %s" \
                                % (Sort_Requirment)
                    titles = '%s%s在%s的使用情况' % (time_titles,
                                               self.com_thing_class_son.currentText(),
                                               self.com_lines_son.currentText())

                elif Get_Reslute == [1, 0, 0, 1]:
                    Sort_Requirment = "STATION like '%s' and WUPIN_NAME='%s' %s" % (
                        self.com_lines.currentText() + '%', self.com_thing_class_son.currentText(), TIME_STATUS)
                    sql_order = "select WUPIN_NAME,QTY from NC_KUCUN_INOUT where %s" \
                                % (Sort_Requirment)
                    titles = '%s%s在%s段的使用情况' % (time_titles,
                                                self.com_thing_class_son.currentText(),
                                                self.com_lines.currentText())

                elif Get_Reslute == [1, 0, 1, 0]:
                    Sort_Requirment = "STATION like '%s' and TYPEOF='%s' %s" % (
                        self.com_lines.currentText() + '%', self.com_thing_class.currentText(), TIME_STATUS)
                    sql_order = "select WUPIN_NAME,QTY from NC_KUCUN_INOUT where %s" \
                                % (Sort_Requirment)

                    titles = '%s%s在%s段的使用情况' % (
                        time_titles, self.com_thing_class.currentText(), self.com_lines.currentText())

                self.Matplotlib_Son(sql_order, 111, titles)  # 主界面

                if X_All == []:
                    return 0

                Have_Thing = list(set(Can_Fei).intersection(
                    set([i for i in list(All_Dist.keys())])))

                # print('219=%s'%sql_order)
                # print('220=%s'%Have_Thing)
                # print('224=%s'%Sort_Requirment)

                if len(Have_Thing) != 0:  # 如果有测试线之类的就拆开
                    fig = plt.figure(figsize=(7, 6), dpi=150)
                    self.Son_Matplotlib(Have_Thing, Sort_Requirment)

                fig.tight_layout()

                Figure = plt.figure(figsize=(10, 6), dpi=150)
                self.Matplotlib_Add_Aces(sql_order, 0.6, '', '')

                Time_Subtract = self.Date_Subtract()

                # print(Time_Subtract)
                (Seven_Day, Year, Month, Day) = self.Date_delete(
                    Time_Subtract * 2)  # 现在的三十天前

                sql_order = sql_order.replace(str(start_time), str(Seven_Day))
                sql_order = sql_order.replace(str(finally_time), str(start_time))

                self.Matplotlib_Add_Aces(
                    sql_order, 1, str(Seven_Day), str(start_time))
                plt.show()

            except Exception:
                print_exc()
            Aces_excuext_one.clear()

        def Son_Matplotlib(self, Have_Thing, Sort_Requirment):  # 拆开的函数
            i = len(Have_Thing)
            if i == 1:
                s = 111
            elif i == 2:
                s = 121
            elif i == 3:
                s = 221
            elif i == 4:
                s = 221
            # 111,121,122,223,224
            for sql_order_son in Have_Thing:
                self.Clean_ALL()
                # print('72=%s'%sql_order_son)
                sql_order = "select WUPIN_NAME,QTY from NC_KUCUN_INOUT where %s and TYPEOF='%s'" % (
                    Sort_Requirment, sql_order_son)
                titles = '%s在%s的使用情况' % (
                    sql_order_son, self.com_lines_son.currentText())
                self.Matplotlib_Son(sql_order, s, titles)
                s += 1

        def Date_Choice(self):  # 得到user选择的天数
            start_datetime = self.dat_start.text() + ' ' + self.tim_start.text() + ':000'
            finally_datetime = self.dat_finally.text() + ' ' + self.tim_finally.text() + ':000'
            return (start_datetime, finally_datetime)

        def Date_Subtract(self):  # 得到从现在到开始相差的天数
            (start_datetime, finally_datetime) = self.Date_Choice()
            d2 = datetime.strptime(start_datetime, '%Y-%m-%d %H:%M:%S:000')
            d1 = datetime.strptime(finally_datetime, '%Y-%m-%d %H:%M:%S:000')
            delta = d1 - d2
            # print('329')
            # print(delta.days)
            return delta.days

        def Date_delete(self, day_ago):  # 从现在（几天）得到几天前的时间
            (start_datetime, finally_datetime) = self.Date_Choice()

            now = datetime.strptime(finally_datetime, '%Y-%m-%d %H:%M:%S:000')
            delta = timedelta(days=day_ago)
            n_days = now - delta
            Seven_Day_Ago = str(n_days.strftime('%Y-%m-%d 00:00:00:000'))
            Year = int(Seven_Day_Ago[:4])
            Month = int(Seven_Day_Ago[5:7])
            Day = int(Seven_Day_Ago[8:10])
            # print(Year,Month,Day)
            # print(Seven_Day_Ago)
            return Seven_Day_Ago, Year, Month, Day

        # 从SQL得到料号这是MAIN
        def Get_All_LH_Sql(self):
            global Execute_Class
            All_Dist.clear()
            Have_LH.clear()  # 清除
            LH_PCDF_MACHINE_NUM.clear()  # 清除驱动板测试线电源线FFC的所占机种的多少
            Execute_Class = 2
            Have_LH.append('1')
            # print('478')
            # print(All_Dist,Have_LH,LH_PCDF_MACHINE_NUM)

            TIME_STATUS = "and (STATUS='NG品更換' or STATUS='NG退料') and CDT between '%s' and '%s'" % self.Date_Choice()
            Sort_Requirment = "COMMENTS!='%s' %s" % ('1', TIME_STATUS)
            sql_order = "select WUPIN_NAME,QTY from NC_KUCUN_INOUT where %s" % (
                Sort_Requirment)  # 得到以前的物品的名称与数量
            self.Get_Sql_Data_In_XY(sql_order)
            print('487=%s'%All_Dist)

            for wupin_name in list(All_Dist.keys()):
                sql_order = "select LH,TYPEOF from NC_KUCUN_LH WHERE WUPIN_NAME='%s'" % wupin_name  # 得到物品的LH与种类
                get_reslute = Execute_Sql_Get_Date(sql_order)
                print('649=%s'%sql_order)
                print('637=%s'%get_reslute)
                print(All_Dist)
                try:
                    if get_reslute!=[]:
                        # ALL_DIST={(WUOIN_NAME,LH):[QTY,TYPEOF,MACHINE_NUM]}
                        print('653%s'%get_reslute)
                        All_Dist[wupin_name].append(get_reslute[0][1])
                        # print('ALL_DIST.append()%s'%All_Dist)
                        All_Dist[(wupin_name, get_reslute[0][0])] = All_Dist.pop(wupin_name)

                    else:
                        del All_Dist[wupin_name]

                except Exception:
                    print_exc()

            print('645=%s'%All_Dist)

            self.LH_Get_Machine_Num()  # 得到物品所拥有的机种数量

            # self.All_Dist_funtion() #绑定150=所有的参数在字典中
            self.HS_Statistics_table()

            # print('440')

            # print(All_Dist)
            if show_noshow[0] == 1:
                plt.show()
            else:
                plt.close('all')
                show_noshow.clear()
                show_noshow.append(1)
                return 0

        def LH_Get_Machine_Num(self):  # 由料号得到这种物品一共有多少机种数量
            LH_POWER_ALL = []
            LH_CESHI_ALL = []
            LH_DIRVER_ALL = []
            LH_FFC_ALL = []
            try:

                (Excel_Machine, Dist_XY) = self.Get_Excel_AllMachine_Num()
                # print('从excel得到的机种%s'%Excel_Machine)
                # print('从excel得到的机种与数量字%s'%Dist_XY)

                for lh in list(All_Dist.keys()):  # 通过料号得到机种
                    hh = [0]
                    machine = []
                    # #print('物品的LH%s'%lh)

                    if lh[1] != '':
                        sql_order = "select distinct MACHINES from MACHINE_LH where JI_OR_SKD='%s' or MONDEL='%s' or BI='%s' or CTAG='%s' or IAS='%s' or AGIS='%s' or " \
                                    "FFC='%s' or INV_POWER_WIRE='%s' or DRIVER='%s' or DRIVER_MARCH='%s' or POWER_WIRE='%s'" % (
                                        lh[1], lh[1], lh[1], lh[1], lh[1], lh[1], lh[1], lh[1], lh[1], lh[1], lh[1])
                        get_reslute = Execute_Sql_Get_Date(sql_order)
                        for xy in get_reslute:
                            machine.append(xy[0])  # 得到这个料号的机种有多少个从SQL中
                            if All_Dist[lh][1] == '電源線':
                                LH_POWER_ALL.append(xy[0])
                            if All_Dist[lh][1] == '測試線':
                                LH_CESHI_ALL.append(xy[0])
                            if All_Dist[lh][1] == '驅動板':
                                LH_DIRVER_ALL.append(xy[0])
                            if All_Dist[lh][1] == 'FFC':
                                LH_FFC_ALL.append(xy[0])

                        # print('通过LH从SQL得到的MACHINE=%s'%machine)

                        Have_Thing = list(
                            set(machine).intersection(
                                set(Excel_Machine)))
                        # print('相同的机种=%s' % Have_Thing)
                        if len(Have_Thing) != 0:
                            for ht in Have_Thing:
                                # print('绑定的机种与数量execl %s'%Dist_XY[ht])
                                a = int(hh[0]) + int(Dist_XY[ht])
                                hh.append(a)
                        else:
                            hh.append(0)
                    else:
                        hh.append(0)
                    All_Dist[lh].append(
                        np.sum(hh) / 1000)  # 把从execl表拿到的机种数量放进ALL_D

                for i in [LH_POWER_ALL, LH_CESHI_ALL, LH_DIRVER_ALL, LH_FFC_ALL]:
                    hh = [0]
                    if len(i) != 0:
                        Have_Thing = list(set(i).intersection(set(Excel_Machine)))
                        # print('相同的机种=%s' % Have_Thing)
                        if len(Have_Thing) != 0:
                            for ht in Have_Thing:
                                # print('绑定的机种与数量execl%s'%Dist_XY[ht])
                                a = int(hh[0]) + int(Dist_XY[ht])
                                hh.append(a)
                        else:
                            hh.append(0)
                    else:
                        hh.append(0)
                    LH_PCDF_MACHINE_NUM.append(np.sum(hh) / 1000)

                # print('712')
                # print(LH_POWER_ALL,LH_CESHI_ALL,LH_DIRVER_ALL,LH_FFC_ALL)
                # print(LH_PCDF_MACHINE_NUM)
                # print('All_Dist%s'%All_Dist)

            except Exception:
                print_exc()

        # 所有物品的耗损率的总表
        def HS_Statistics_table(self):
            SH = []
            Legend_name = []
            All_Future.clear()
            print("560=%s"%All_Dist)
            try:
                for i in list(All_Dist.keys()):
                    try:
                        if All_Dist[i][2] != 0:
                            a = int(All_Dist[i][0]) / (int(All_Dist[i][2] * 1000))
                            SH.append(a * 100)
                        else:
                            SH.append(0)

                        Legend_name.append('%s(%3.2f%s)' %
                                           (i[0], SH[len(SH) - 1], '%'))
                        All_Future[i[0]] = SH[len(SH) - 1] / 100
                    except Exception:
                        print_exc()
                fig = plt.figure(figsize=(10, 8), dpi=150)

                self.Two_Y_Twin(
                    fig, 111, [
                        i[0] for i in list(
                            All_Dist.keys())], [
                        All_Dist[i][0] for i in list(
                            All_Dist.keys())], [
                        All_Dist[i][2] for i in list(
                            All_Dist.keys())], SH, Legend_name,
                    '所有物品的耗损情况')  # 所有的物品的耗损情况{('Light Sensor', 'R372B000KJ300'): [66, 'Sensor', 0.0]}

                # print('540=%s%d'%(All_Dist,len(All_Dist)))
                # print('541=%s%d'%(SH,len(SH)))
                # print('544=%s'%All_Future)

                self.Power_Ceshi_Dirver_FFC()

                j = 221
                Have_Thing = list(set(['電源線', '測試線', '驅動板', 'FFC']).intersection(
                    set([All_Dist[i][1] for i in list(All_Dist.keys())])))

                fig1 = plt.figure(figsize=(7, 5), dpi=150)


                #这是电源线与驱动板与测试线分开的显示（耗损率的查询）
                for thing_class_name in Have_Thing:
                    self.PCDF_SON(fig1, j, thing_class_name)
                    j += 1


                #  让子图可以自动调整距离pad=0.4, w_pad=1.0, h_pad=1.0
                fig1.tight_layout()

            except Exception:
                print_exc()
                # print('627')


        #这是耗损的查询
        def Power_Ceshi_Dirver_FFC(self):
            Legend_name = []
            X_PCDF = ['電源線', '測試線', '驅動板', 'FFC']
            Y_PCDF = [0, 0, 0, 0]
            PCDF_SH = []
            # print(Y_PCDF,PCDF_SH)
            for i in list(All_Dist.keys()):  # 得到电源线测试线的数量
                if All_Dist[i][1] == '電源線':
                    Y_PCDF[0] = All_Dist[i][0] + Y_PCDF[0]
                if All_Dist[i][1] == '測試線':
                    Y_PCDF[1] = All_Dist[i][0] + Y_PCDF[1]
                if All_Dist[i][1] == '驅動板':
                    Y_PCDF[2] = All_Dist[i][0] + Y_PCDF[2]
                if All_Dist[i][1] == 'FFC':
                    Y_PCDF[3] = All_Dist[i][0] + Y_PCDF[3]

            for i in range(4):
                if LH_PCDF_MACHINE_NUM[i] != 0:
                    PCDF_SH.append(Y_PCDF[i] / (LH_PCDF_MACHINE_NUM[i] * 1000))
                else:
                    PCDF_SH.append(0)
                PCDF_SH[i] = PCDF_SH[i] * 100

            fig = plt.figure(5, figsize=(6, 5), dpi=150)
            self.Two_Y_Twin(
                fig,
                111,
                X_PCDF,
                Y_PCDF,
                LH_PCDF_MACHINE_NUM,
                PCDF_SH,
                Legend_name,
                "('電源線','測試線','驅動板','FFC')耗损情况")


            print('829')
            #fig = plt.figure(10, figsize=(6, 5), dpi=150)


        def Shuxu(self):
            pass

        def PCDF_SON(self, fig, iii, thing_class_name):  # 这是一个拆分的子图
            x_pcdf_son = []
            Legend_name = []
            y_pcdf_son = []
            xy_pcdf_machine_son = []
            xy_hs = []
            j = 0
            for i in list(All_Dist.keys()):
                if All_Dist[i][1] == thing_class_name:
                    x_pcdf_son.append(i[0])
                    y_pcdf_son.append(All_Dist[i][0])
                    xy_pcdf_machine_son.append(All_Dist[i][2])

                    if All_Dist[i][2] != 0:
                        xy_hs.append(All_Dist[i][0] / (All_Dist[i][2] * 10))
                    else:
                        xy_hs.append(0)


            self.Two_Y_Twin(
                fig,
                iii,
                x_pcdf_son,
                y_pcdf_son,
                xy_pcdf_machine_son,
                xy_hs,
                Legend_name,
                thing_class_name)


        #这是查询得到Y轴对照表
        def Two_Y_Twin(self, fig, iii, X, Y, XY, SH, Legend_name, title_name):
            for i in range(len(SH)):
                Legend_name.append('%s(%3.2f%s)' % (X[i], SH[i], '%'))

            ax1 = fig.add_subplot(iii)
            plt.title(title_name)

            plt.xticks(np.arange(len(Y)), X, rotation=70, size='xx-small')
            ax2 = ax1.twinx()
            plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))

            b2 = ax1.bar(
                np.arange(
                    len(Y)) + 0.15,
                XY,
                alpha=0.5,
                width=0.3,
                color=Color_All,
                edgecolor='red',
                lw=1)

            b1 = ax1.bar(
                np.arange(
                    len(Y)) - 0.15,
                Y,
                alpha=0.5,
                width=0.3,
                color=Color_All,
                edgecolor='red',
                lw=1)



            #这是一个折线的统计图
            p1 = ax2.plot(np.arange(len(Y)), SH)
            s1 = ax2.scatter(np.arange(len(Y)), SH)



            print('910=%s'%SH)
            print(X)#这是线材用的产量
            print(XY)
            print(Legend_name)



            #这是耗损的legend
            plt.legend(b1, Legend_name, loc='best', ncol=2, prop={'size': 3})

            for x, y in enumerate(Y):
                ax1.text(
                    x -
                    0.15,
                    y,
                    '%s' %
                    y,
                    ha='center',
                    va='bottom',
                    fontsize=7)
            for x, y in enumerate(XY):
                ax1.text(
                    x +
                    0.15,
                    y,
                    '%s' %
                    y,
                    ha='center',
                    va='bottom',
                    fontsize=7)
            for x, y in enumerate(SH):
                ax2.text(x, y + 0.02, '%3.2f%s' %
                         (y, '%'), ha='center', va='bottom', fontsize=5,color='red')


        def Get_Excel_AllMachine_Num(self):  # 从excel得到机种与数量
            NEW = Get_Excel_AllMachine_Num()
            (Excel_Machine, Dist_XY) = NEW.set_up(
                self.dat_start.text(), self.dat_finally.text())
            return (Excel_Machine, Dist_XY)



        def Get_Sql_Data_In_XY(self, sql_order):
            global Peraration_A_ll
            All_Dist.clear()
            XY_DIST.clear()
            X_All.clear()
            Y_All.clear()
            # print('187=%s'%sql_order)
            try:
                get_reslute = Execute_Sql_Get_Date(sql_order)
                if len(get_reslute) == 0:
                    self.Qmassage_Show('None information')
                    # plt.close()
                    return 0
                for xy in get_reslute:
                    if xy[0] in All_Dist.keys():
                        # print(All_Dist)
                        Haved_Data = All_Dist[xy[0]][0]
                        All_Dist[xy[0]] = [int(xy[1]) + Haved_Data]
                    else:
                        All_Dist[xy[0]] = [int(xy[1])]

                # d_order = sorted(All_Dist.items(), key=lambda x: x[1], reverse=False)#由大到小的排顺序
                # #print(d_order)
                # for g in d_order:
                #     X_All.append(g[0])
                #     Y_All.append(int(g[1][0]))

                # '測試線': [899, 0.43367100820067533, '測試線(899)', '#FAEBD7']
                # ('V23.6非三星--JC 測試線', 'R377B0012B000'): [136, '測試線', 622.119]
                p = 0
                ALL_THING_NUM = np.sum([All_Dist[i][0]
                                        for i in list(All_Dist.keys())])
                for i in list(All_Dist.keys()):
                    if Execute_Class == 1:
                        # print('有执行添加颜色')
                        All_Dist[i].append(
                            All_Dist[i][0] / ALL_THING_NUM)  # 添加个件所占总数的比例
                        All_Dist[i].append(
                            '%s(%s)' %
                            (i, All_Dist[i][0]))  # 添加标题legend
                        All_Dist[i].append(Color_All[p])  # 添加颜色
                        p += 1

                    X_All.append(i)
                    Y_All.append(All_Dist[i][0])

            except Exception:
                print_exc()


        def Clean_ALL(self):
            Peraration_A_ll.clear()
            lines.clear()
            X_All.clear()
            Y_All.clear()
            X_Y_Dist.clear()
            X_Y_Dist1.clear()
            Two_Legend.clear()
            Excetu_One.clear()
            Determine_User_Choise.clear()
            Aces_excuext_one.clear()
            XY_DIST.clear()

        def Close_plot(self):
            plt.close()
            plt.close()
            plt.close()

    except Exception:
        print_exc()

if __name__ == '__main__':
    app = QApplication(argv)
    mywindow = Choice_Condition()
    mywindow.show()

    exit(app.exec())
