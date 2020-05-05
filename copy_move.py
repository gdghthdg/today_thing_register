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


def move_file_compile():
    """迁移文件的脚本"""
    #这是源文件
    file_head='C:\\Users\\Administrator\\Desktop\\today_thing_register\\'

    finally_address='C:\\Users\\Administrator\\Desktop\\2020506\\'

    #这是要拷贝的文件
    file_list=["Main_Window_Show.py","Admin_Resigner.py","Admin_Resigner_Monther.py","Bind_wire.py","Bind_Wire_monther.py","Common_Function.py","compile_all.py","Date_Analyse.py","Date_Analyse_monther.py","Get_Future_Three_Month.py","Get_Machine_Num_for_excel.py","history.py","history_monther.py","lend_registe.py","lend_registe_monther.py","Login.py","Login_monther.py",
               "Main_Window.py","put_in.py","random_question_register.py","SERSON.PY","SERSON_MONTHER.py","Set_Machine.py","set_machine_kitting.py","Set_Machine_monther.py","tetris.py","THING.py",
               "Thing_Check.py","Thing_Check_monther.py","Update.py","Update_Mother.py","wireandmachine_lh.py","wireandmachine_lh_monther.py","wire_images_rc.py","wire_ui.py","write_password.py","database_set.py"]

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
    # run_copy()
    move_file_compile()