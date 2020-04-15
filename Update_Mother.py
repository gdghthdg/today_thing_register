from Update import Ui_MainWindow
from Common_Function import *
import threading
from multiprocessing import Process
from ftplib import *
import os

import time
File_Size=[0]
file = '/hblcmftp/AllType/Personal Files/何健文/更新/Main_Window_Show.exe'



class update_son(Ui_MainWindow,Farther,QMainWindow):


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.SubWindow | QtCore.Qt.WindowStaysOnTopHint)

        # 透明处理，移动需要拖动数字

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

    def Get_Load_Ftp_File_Size(self):
        print("进度开始")

        ftp = Ftp()
        file_size = ftp.size(file)

        print('文件大小=%s' % file_size)
        a = os.path.getsize("D:\\config\\Main_Window_Show.exe")

        update_have_on=(a==file_size)
        ftp.close()
        return (a,file_size)

    def Show_File_Down(self):
        print("进度开始")

        (a,file_size)=self.Get_Load_Ftp_File_Size()

        if a==file_size:
            self.lab_show.setText("这已是最新版本，不需更新")

        else:
            self.progressBar.setMaximum(file_size)
            a=0
            while True:
                try:
                    if a == file_size:
                        break

                    time.sleep(0.2)
                    a=os.path.getsize("D:\\config\\Main_Window_Show.down")
                    print(a)

                    QApplication.processEvents()
                    self.progressBar.setValue(a)

                    print('进度有触发')

                except Exception:
                    print_exc()


            print('循环结束')

            try:
                os.rename("D:\\config\\Main_Window_Show.exe", "D:\\config\\Main_Window_Show.backup")
                os.rename("D:\\config\\Main_Window_Show.down" ,"D:\\config\\Main_Window_Show.exe")
                #os.system("del D:\\config\\Main_Window_Show.exe")

            except FileNotFoundError:
                print('没有这个文件')
                os.rename("D:\\config\\Main_Window_Show.down",
                          "D:\\config\\Main_Window_Show.exe")

            except FileExistsError:
                print('文件已经存在')
                os.remove("D:\\config\\Main_Window_Show.backup")

                os.rename("D:\\config\\Main_Window_Show.exe",
                          "D:\\config\\Main_Window_Show.backup")

                os.rename("D:\\config\\Main_Window_Show.down",
                          "D:\\config\\Main_Window_Show.exe")


            self.lab_show.setText('更新成功，请重新打开软件')




         # try:
            #     for i in range(100):
            #         time.sleep(1)
            #         # self.progressBar
            #         print(i)
            #         QApplication.processEvents()
            #         self.progressBar.setValue(i)
            #
            # except Exception:
            #     print_exc()
            #     # 使用多线程？多进程？



    def Download_Ftp_file(self):
        (a,file_size)=self.Get_Load_Ftp_File_Size()
        if a!=file_size:
            try:
                ftp = Ftp()

                fp = open('D:\config\Main_Window_Show.down', 'wb')  # 以写模式在本地打开文件

                #设置进度条的大小

                ftp.retrbinary('RETR %s' % file, fp.write, 90240000)  # 接收服务器上文件并写入本地文件

                ftp.set_debuglevel(0)  # 关闭调试
                ftp.quit()
                fp.close()

            except Exception:
                print_exc()


            #把名字更改后就行一个检验程序是否最新的

            #self.Message_one("更新完成，请重新打开软件")
            #self.Message_one("更新完成，")


    def start(self):

        #self.Show_File_Down()

        try:
            t1 = threading.Thread(target=self.Download_Ftp_file)
            t2=threading.Thread(target=self.Show_File_Down)
            t1.start()
            t2.start()



        # mt1=Process(target=self.Download_Ftp_file)
            # mt2 = Process(target=self.Show_File_Down)
            # mt1.start()
            # mt2.start()


        except Exception:
            print_exc()



    def start_two(self):

        try:
            self.Download_Ftp_file()
        except Exception:
            print_exc()

    def Close_Show(self):
        update_show.close()



if __name__ == '__main__':
    app=QApplication(argv)
    update_show=update_son()
    update_show.show()

    exit(app.exec())