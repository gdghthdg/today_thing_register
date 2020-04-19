import os
import copy_move
os.system(r'pyuic5 -o C:\Users\Administrator\Desktop\20190822\wire_ui.py C:\Users\Administrator\Desktop\20190822\wire_ui.ui')
os.system(r'pyuic5 -o C:\Users\Administrator\Desktop\20190822\Thing_Check.py C:\Users\Administrator\Desktop\20190822\Thing_Check.ui')
os.system(r'pyrcc5 -o C:\Users\Administrator\Desktop\20190822\wire_images_rc.py C:\Users\Administrator\Desktop\20190822\wire_images.qrc')
os.system(r'pyrcc5 -o C:\Users\Administrator\Desktop\20190822\IMAGES_QRC_rc.py C:\Users\Administrator\Desktop\20190822\IMAGES_QRC.qrc')
os.system(r'pyuic5 -o C:\Users\Administrator\Desktop\20190822\history.py C:\Users\Administrator\Desktop\20190822\history.ui')
os.system(r'pyuic5 -o C:\Users\Administrator\Desktop\20190822\Bind_wire.py C:\Users\Administrator\Desktop\20190822\Bind_wire.ui')
os.system(r'pyuic5 -o C:\Users\Administrator\Desktop\20190822\wireandmachine_lh.py C:\Users\Administrator\Desktop\20190822\wireandmachine_lh.ui')
os.system(r'pyuic5 -o C:\Users\Administrator\Desktop\20190822\Date_Analyse.py C:\Users\Administrator\Desktop\20190822\Date_Analyse.ui')
os.system(r'pyuic5 -o C:\Users\Administrator\Desktop\20190822\time_seek.py C:\Users\Administrator\Desktop\20190822\time_seek.ui')
os.system(r'pyuic5 -o C:\Users\Administrator\Desktop\20190822\SERSON.py C:\Users\Administrator\Desktop\20190822\SERSON.ui')
os.system(r'pyuic5 -o C:\Users\Administrator\Desktop\20190822\Set_Machine.py C:\Users\Administrator\Desktop\20190822\Set_Machine.ui')
os.system(r'pyuic5 -o C:\Users\Administrator\Desktop\20190822\set_machine_kitting.py C:\Users\Administrator\Desktop\20190822\Set_Machine_kitting.ui')
os.system(r'pyuic5 -o C:\Users\Administrator\Desktop\20190822\Main_Window.py C:\Users\Administrator\Desktop\20190822\MainWindow.ui')
os.system(r'pyuic5 -o C:\Users\Administrator\Desktop\20190822\lend_registe.py C:\Users\Administrator\Desktop\20190822\lend_registe.ui')
os.system(r'pyuic5 -o C:\Users\Administrator\Desktop\20190822\center_test.py C:\Users\Administrator\Desktop\20190822\center_test.ui')
# os.system(r'pyuic5 -o C:\Users\Administrator\Desktop\20190822\Update.py C:\Users\Administrator\Desktop\20190822\Update.ui')
# os.system(r'pyuic5 -o C:\Users\Administrator\Desktop\20190822\install.py C:\Users\Administrator\Desktop\20190822\install.ui')
# os.system(r'pyuic5 -o C:\Users\Administrator\Desktop\20190822\Admin_Resigner.py C:\Users\Administrator\Desktop\20190822\Admin_Resigner.ui')
os.system(r'pyuic5 -o C:\Users\Administrator\Desktop\20190822\Login.py C:\Users\Administrator\Desktop\20190822\LOGIN.ui')
os.system(r'pyuic5 -o C:\Users\Administrator\Desktop\20190822\put_in.py C:\Users\Administrator\Desktop\20190822\put_in.ui')
os.system(r'pyuic5 -o C:\Users\Administrator\Desktop\20190822\write_password.py C:\Users\Administrator\Desktop\20190822\write_password.ui')
os.system(r'pyuic5 -o C:\Users\Administrator\Desktop\20190822\gif.py C:\Users\Administrator\Desktop\20190822\gif.ui')
os.system(r'pyuic5 -o C:\Users\Administrator\Desktop\20190822\sound.py C:\Users\Administrator\Desktop\20190822\sound.ui')
# os.system(r'pyuic5 -o C:\Users\Administrator\Desktop\20190822\barcode.py C:\Users\Administrator\Desktop\20190822\barcode.ui')
# os.system(r'pyuic5 -o C:\Users\Administrator\Desktop\20190822\thing_keep_hint.py C:\Users\Administrator\Desktop\20190822\thing_keep_hint.ui')
# os.system(r'pyrcc5 -o C:\Users\Administrator\Desktop\20190822\IMAGES_QRC_rc.py C:\Users\Administrator\Desktop\20190822\IMAGES_QRC.qrc')

os.system(r'pyuic5 -o C:\Users\Administrator\Desktop\20190822\set_address_red.py C:\Users\Administrator\Desktop\20190822\set_address_red.ui')
os.system(r'pyuic5 -o C:\Users\Administrator\Desktop\20190822\set_shortcut.py C:\Users\Administrator\Desktop\20190822\set_shortcut.ui')


#一个移动的脚本
copy_move.run_copy()


print("操作完成")
#一个改名字的的方法,得到在某地的文件的大小
# os.rename("D:\\hblcmftp\\FD-flicker\\Main_Window_Show.down" ,"D:\\hblcmftp\\FD-flicker\\Main_Window_Show.exe")
# while True:
#     time.sleep(0.1)
#     a=os.path.getsize("D:\\hblcmftp\\FD-flicker\\Main_Window_Show.down")
#     print(a)