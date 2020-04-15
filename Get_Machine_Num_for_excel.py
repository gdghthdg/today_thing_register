import pandas as pd
import numpy as np
import re
from traceback import print_exc
import matplotlib.pyplot as plt
from datetime import datetime,timedelta

plt.rcParams['font.sans-serif'] = ['SimHei']
Dist_All = {}
X_All_Data = []
Y_Data_All = []

def find_english(file):
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    english = re.sub(pattern, '', file)
    return english



class Get_Excel_AllMachine_Num():
    def ischinese(self,s):
        for c in s:
            if '\u4e00' <= c <='\u9fa5':
                return  True
        return False


    def Date_Subtract(self,start_datetime,finally_datetime):


        d2 = datetime.strptime(start_datetime, '%Y-%m-%d')
        d1 = datetime.strptime(finally_datetime, '%Y-%m-%d')
        delta = d1 - d2
        #print('相差的时间：')
        #print(delta.days)
        return delta.days
    
    def Date_delete(self,q,start_datetime):


        now = datetime.strptime(start_datetime, '%Y-%m-%d')

        delta = timedelta(days=q)
        
        n_days = now + delta
        year_month_day=str(n_days.strftime('%Y-%m-%d'))
        
        Year=int(year_month_day[:4])
        Month=int(year_month_day[5:7])
        Day=int(year_month_day[8:10])

        return year_month_day,Year,Month,Day

    #这个函数有两个参数，一个是人自己选择的开始时间，琴人选择的结束时间
    def set_up(self,starttime,finallytime):
        global X_All_Data
        Dist_All.clear()
        X_All_Data.clear()

        #方法三：通过表单索引来指定要访问的表单，0表示第一个表单
        #也可以采用表单名和索引的双重方式来定位表单
        #也可以同时定位多个表单，方式都罗列如下所示
        #print('5555')
        df=pd.read_excel('D:\\config\\HB每週生產計劃.xls',sheet_name='每周-CD檢')#可以通过表单名同时指定多个
        # df=pd.read_excel('lemon.xlsx',sheet_name=0)#可以通过表单索引来指定读取的表单
        # df=pd.read_excel('lemon.xlsx',sheet_name=['python',1])#可以混合的方式来指定
        # df=pd.read_excel('lemon.xlsx',sheet_name=[1,2])#可以通过索引 同时指定多个

        data=df.values#获取所有的数据，注意这里不能用head()方法哦~
        #print("获取到所有的值:\n{0}".format(data[0]))#格式化输出
        #print("输出列标题",df.columns.values[3])
        ##print("输出值\n",df[datetime(2019, 5, 3, 0, 0)].values)
        j=1
        y=0
        a=0
        # Start_Time=input('请输入开始时间比如2018-1-1:')
        # Finally_Time=input('请输入结束时间比如2018-1-2:')
        #print(starttime,finallytime)
        sf_day=self.Date_Subtract(starttime,finallytime)


        for q in range(sf_day+1):
            (year_month_day,Year,Month,Day)=self.Date_delete(q,starttime)
            #print((year_month_day,Year,Month,Day))
            All_Data = df[datetime(2019, Month, Day, 0, 0)].values  # 获取列数据


            #All_Data=df[datetime(2019, sf_month,day_start, 0, 0)].values #获取列数据

            i=1
            j=3
            try:
                for a in range(int(len(All_Data)/2)):
                   # #print(Dist_All)
                    data=All_Data[i:j]
                    try:
                       # data[0]=find_english(str(data[0]))
                       ggg=str(data[0]).split('\n')
                       for ddd in ggg:
                           if len(ddd)==13:
                               data[0]=ddd

                    except Exception:

                       #print('data[0]没有、n')
                       pass

                    if data[0] in Dist_All.keys() and pd.isnull(data[1])!=True:
                        Haved_Data=int(Dist_All[data[0]])
                        Dist_All[data[0]]=int(data[1])+Haved_Data
                    else:
                        if data[0] != 'X' and pd.isnull(data[0])!=True and str(data[0]).isdigit()==False and pd.isnull(data[1])!=True: # isnull判断nan
                            try:
                                Dist_All[data[0]] = int(data[1])
                            except Exception:
                                #print('错误')
                                print_exc()
                    i+=2
                    j+=2
            except Exception:
                #print('错误22')
                print_exc()

        X_All_Data=list(Dist_All.keys())

        for i in X_All_Data:

            Y_Data_All.append(Dist_All[i])

        return X_All_Data,Dist_All   #返回X_all_date是机种的名称，后面一个字典包括机种名与数量


if __name__=='__main__':

    XY_All_Date=[]

    NEW=Get_Excel_AllMachine_Num()
    NEW.set_up(1,2)
    plt.figure(figsize=(10,8),dpi=120)
    plt.subplot(111)
    #print(X_All_Data)
    #print(Y_Data_All)
    for i in range(len(X_All_Data)):
        XY_All_Date.append('%s(%s)' % (X_All_Data[i], Y_Data_All[i]))
    l1=plt.bar(X_All_Data, Y_Data_All, alpha=0.5, width=0.3, edgecolor='red', lw=1)
    plt.xticks(X_All_Data, size='small', rotation=55)
    for x, y in enumerate(Y_Data_All):
        plt.text(x, y, '%s' % y, ha='center', va='bottom',fontsize=7)
    plt.legend(l1,XY_All_Date,loc='best',fontsize='small',ncol=4,title="物品总数%d"%np.sum(Y_Data_All),prop = {'size':6})
    #print(np.sum(Y_Data_All))
    plt.show()
