from shutil import copyfile
#src 源文件
#dst 最后位置

"""只是把文件从2018的ui文件转移到时todqy中"""

def run_copy():
    """迁移文件的脚本"""
    #这是源文件
    file_head='C:\\Users\\Administrator\\Desktop\\20190822\\'

    finally_address='C:\\Users\\Administrator\\Desktop\\today_thing_register\\'

    #这是文件要拷贝放在的地方
    file_list=['Main_Window.py','wire_ui.py','Bind_Wire.py','Date_Analyse.py',
               'Set_Machine.py', 'history.py','wire_images_rc.py', 'wireandmachine_lh.py',
               'SERSON.PY','Thing_Check.py','lend_registe.py','Update.py','Login.py','set_machine_kitting.py','put_in.py','database_set.py']

    for i in file_list:
        fp=open(file_head+i,'rb')
        all_data=fp.read()


        fp1=open(finally_address+i,'wb')
        fp1.write(all_data)


        fp.close()
        fp1.close()




        #copyfile(finally_address, finally_address)



    #copyfile('./test.txt', '/home/gaosiqi/tmp/test.txt')

if __name__ == '__main__':
    run_copy()