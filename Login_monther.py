from Login import Ui_Form
from Common_Function import *


class Login_class(Ui_Form,Farther,Windows_Move,QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.center()
        # 透明处理，移动需要拖动数字
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.SubWindow | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        self.lineEdit.setFocus()

        self.set_gif(':/images/dou5.gif',self.lab_background)
        #self.set_gif(':/images/yunye.gif', self.lab_background)

        # my_list = ['1','2','3']
        # my_str,ok = QInputDialog.getItem(self,"下拉框",'提示',my_list)
        # print(my_str,ok)

    #界面的退出按钮
    def Exit(self):
        os._exit(0)
        # exit(1)
        # return


    #一个确认的按钮的函数
    def Login_Reslute(self):

        text, ok = QInputDialog.getText(self, "title", "User name:", QLineEdit.Normal, '>>>:')

        # if self.lineEdit.text()=='123':
        #     return '管理员账号'
        # else:
        #     image_file, _ = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\',
        #                                                 'Image files (*.jpg *.gif *.png *.jpeg)')


if __name__=="__main__":
    app = QtWidgets.QApplication(argv)
    MainWindow = QtWidgets.QMainWindow()

    Login_son = Login_class()
    Login_son.show()

    exit(app.exec_())