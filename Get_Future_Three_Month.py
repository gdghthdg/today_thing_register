import xlrd
from Common_Function import *
import numpy as np


Dist_Wire_Machine={}
Dist_Machine_Three_NUM={}
Dist_XY={}
All_Dist={}
h0 = [0]
h1 = [0]
h2 = [0]
data = xlrd.open_workbook('D:\\config\\LCMHB1_W1927.03(MFG).xls',encoding_override='utf8') # 打开xls文件
table = data.sheets()[0] # 打开第一张表


nrows = table.nrows      # 获取表的行数
print('%s=nrows'%nrows)

ncols = table.ncols
#print(ncols)


#得到所有线材有使用的机种

def Get_All_Thing_Use_Machine(Machine_name_num):
    try:
        WUPIN_NAME_LH = {}
        sql_order="select WUPIN_NAME,LH from NC_KUCUN_LH"
        get_relute=Execute_Sql_Get_Date(sql_order)


        for xy in get_relute:
            WUPIN_NAME_LH[xy[0]]=[xy[1]]
        #print('24=%s'%WUPIN_NAME_LH)
        #print(len(list(WUPIN_NAME_LH.keys())))



        # 通过料号得到机种
        for lh in list(WUPIN_NAME_LH.keys()):
            h0[0] = 0
            h1[0] = 0
            h2[0] = 0

            Have_Thing=[]
            machine = []
            # #print('物品的LH%s'%lh)

            if WUPIN_NAME_LH[lh] != '/':
                sql_order = "select distinct MACHINES from MACHINE_LH where JI_OR_SKD='%s' or MONDEL='%s' or BI='%s' or CTAG='%s' or IAS='%s' or AGIS='%s' or " \
                            "FFC='%s' or INV_POWER_WIRE='%s' or DRIVER='%s' or DRIVER_MARCH='%s' or POWER_WIRE='%s' or BMA='%s'" % (
                            WUPIN_NAME_LH[lh][0], WUPIN_NAME_LH[lh][0], WUPIN_NAME_LH[lh][0], WUPIN_NAME_LH[lh][0], WUPIN_NAME_LH[lh][0], WUPIN_NAME_LH[lh][0], WUPIN_NAME_LH[lh][0], WUPIN_NAME_LH[lh][0], WUPIN_NAME_LH[lh][0], WUPIN_NAME_LH[lh][0], WUPIN_NAME_LH[lh][0], WUPIN_NAME_LH[lh][0])

                get_reslute = Execute_Sql_Get_Date(sql_order)


                print(lh)
                print('使用此种线材所用的机种=%s'%get_reslute)

                if len(get_relute)!=0:
                    for xy in get_reslute:
                        if xy[0]!='':
                            machine.append(xy[0])  # 得到这个料号的机种有多少个从SQL中


                    Have_Thing = list(set(machine).intersection(set(list(Machine_name_num.keys()))))

                    print('相同的机种%s'%Have_Thing)
                    Dist_Wire_Machine[lh]=Have_Thing


                if len(Have_Thing) != 0:
                    for ht in Have_Thing:
                        print('Machine_name_num%s'%Machine_name_num[ht])
                        a = int(h0[0]) + int(Machine_name_num[ht][0])
                        b=int(h1[0]) + int(Machine_name_num[ht][1])
                        c=int(h2[0]) + int(Machine_name_num[ht][2])

                        h0[0]=a
                        h1[0]=b
                        h2[0]=c
                        print('00的线材使用机种数量%s%s%s' % (h0, h1, h2))
                else:
                    h0[0] = 0
                    h1[0] = 0
                    h2[0] = 0
            else:
                h0[0] = 0
                h1[0] = 0
                h2[0] = 0

            WUPIN_NAME_LH[lh].append(np.sum(h0))
            WUPIN_NAME_LH[lh].append(np.sum(h1))
            WUPIN_NAME_LH[lh].append(np.sum(h2))
            print('当前的线材使用机种数量%s%s%s'%(h0,h1,h2))

        print('71=%s'%WUPIN_NAME_LH)
        return WUPIN_NAME_LH
    except Exception:
        print_exc()

def Get_Future_three_wire_sum():
    try:
        Machine_name_num = {}
        for i in range(nrows):
            if table.cell_value(i, 0)=='   Table Name : LCM Prod ID Input Plan ':
                for j in range(nrows):
                    h=j+65
                    #得到前七个的字母
                    machine_name=table.cell_value(h, 2)
                    machine_name = machine_name[:len(machine_name) - 7]
                    print("101=%s"%machine_name)



                    #这是显示excel一整行的数据
                    print("一行的数据%s"%table.row_values(h))
                    rows=table.row_values(h)[9:len(table.row_values(h))-5]
                    for o in range(len(rows)):
                       if rows[o]=='':
                           rows[o]=0
                    Dist_Machine_Three_NUM[machine_name+str(h)]=rows
                    print(table.row_values(h)[9:])



                    sum1=table.cell_value(h, 162)
                    if sum1=='':
                        sum1=0
                    sum2=table.cell_value(h, 163)
                    if sum2=='':
                        sum2=0
                    sum3=table.cell_value(h, 164)
                    if sum3=='':
                        sum3=0

                    #print('lll=[%s] [%s] [%s] [%s]' % (machine_name,sum1,sum2,sum3))

                    if machine_name in list(Machine_name_num.keys()):
                        sum_all=Machine_name_num[machine_name]
                        Machine_name_num[machine_name]=[str(int(sum1)+int(sum_all[0])),str(int(sum2)+int(sum_all[1])),str(int(sum3)+int(sum_all[2]))]

                    else:
                        Machine_name_num[machine_name]=[sum1,sum2,sum3]

                    if table.cell_value(h, 0)=='   Table Name : LCM Prod Input Plan - fab distribution ':
                        break

        #从拿到的三个月的机种名与三个个月的数量，把当前线材使用的机种数量进行相加
        #得到一个包含线材KEY,VALUES(三个月使用这种线材的总数量进行相加的值)

        WUPIN_NAME_LH=Get_All_Thing_Use_Machine(Machine_name_num)


        print('wupin_name_NUM=%s' % Machine_name_num)
        print('wupin_name_lh=%s' % WUPIN_NAME_LH)

        #print(len(list(WUPIN_NAME_LH.keys())))



        return WUPIN_NAME_LH
    except Exception:
        print_exc()



if __name__=="__main__":
    Get_Future_three_wire_sum()
    print("153=%s"%Dist_Machine_Three_NUM)

    # for i in list(Dist_Machine_Three_NUM.keys()):
    #     print(i)
    #     print(sorted(Dist_Machine_Three_NUM[i],reverse = True))

    #这是机种对应三个月的每天的产品量
    print("机种对应三个月的每天的产品量%s"%Dist_Machine_Three_NUM)

    #未来的线材有使用的机种
    for wupin_mane in list(Dist_Wire_Machine.keys()):
        if Dist_Wire_Machine[wupin_mane]==[]:
            Dist_Wire_Machine.pop(wupin_mane)
            print(wupin_mane)
    print("DIST_WIRE_MACHINE=%s"%Dist_Wire_Machine)
    print(list(Dist_Wire_Machine.keys()))
    print(len(list(Dist_Wire_Machine.keys())))
#这里面会得到比较多线材，跟以前的预测的有不同是因为，以前的预测是以使用过线材来选定的，只有以前使用过的，才有耗损率
    Dist_Size={'315':[],'195':[],'231':[],'236':[],'240':[],'290':[],'320':[],'350':[],'400':[],'850':[],'A00':[]}

    #得到三个月所有机种的名称
    machine_three_all=list(Dist_Machine_Three_NUM.keys())

    for i in range(len(Dist_Machine_Three_NUM[machine_three_all[0]])):
        num=0
        num1 = 0
        num2 = 0
        num3 = 0
        num4 = 0
        num5 = 0
        num6 = 0
        num7 = 0
        num8 = 0
        num9 = 0

        for machine in list(Dist_Machine_Three_NUM.keys()):
            if machine[:2]!='2V':
                if machine[2:5]=='195':
                    num=Dist_Machine_Three_NUM[machine][i]+num

                if machine[2:5]=='231':
                    num1=Dist_Machine_Three_NUM[machine][i]+num1
                if machine[2:5]=='236':
                    num2=Dist_Machine_Three_NUM[machine][i]+num2

                if machine[2:5]=='240':
                    num3=Dist_Machine_Three_NUM[machine][i]+num3
                if machine[2:5]=='290':
                    num4=Dist_Machine_Three_NUM[machine][i]+num4
                if machine[2:5]=='320':
                    num5=Dist_Machine_Three_NUM[machine][i]+num5
                if machine[2:5]=='350':
                    num6=Dist_Machine_Three_NUM[machine][i]+num6
                if machine[2:5]=='400':
                    num7=Dist_Machine_Three_NUM[machine][i]+num7
                if machine[2:5]=='850':
                    num8=Dist_Machine_Three_NUM[machine][i]+num8
                if machine[2:5]=='A00':
                    num9=Dist_Machine_Three_NUM[machine][i]+num9

        #这是把三个月中每天每个尺寸的总数放在一个字
        Dist_Size['195'].append(num/2)
        Dist_Size['231'].append(num1)
        Dist_Size['236'].append(num2/2)
        Dist_Size['240'].append(num3)
        Dist_Size['290'].append(num4)
        Dist_Size['320'].append(num5)
        Dist_Size['350'].append(num6)
        Dist_Size['400'].append(num7)
        Dist_Size['850'].append(num8)
        Dist_Size['A00'].append(num9)



    print(Dist_Size)
    print(list(Dist_Machine_Three_NUM.keys()))
    for i in list(Dist_Size.keys()):
        print(i)
        print(len(Dist_Size[i]))

    #这是得到了尺寸中三个月中每个尺寸的最大值
    Dist_Size_Max = {}
    for i in list(Dist_Size.keys()):
        if Dist_Size[i] != []:
            Dist_Size_Max[i] = max(Dist_Size[i])

    print('这是未来尺寸机种要生产的总数%s'%Dist_Size_Max)
    print('这是未来某种线材的有使用的机种=%s'%Dist_Wire_Machine)

# (Excel_Machine, Dist_XY) = Get_Excel_AllMachine()
#
# ave_Thing = list(set(machine).intersection(set(Excel_Machine)))

# for i in range(nrows):  # 循环逐行打印
#     ##print(table.row_va lues(i)[:14])
#     i=table.row_values(i)[:166] #$$$$$
#
#     #print('16=%s' % i)