# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Main_Window_Show.py', 'Main_Window.py', 'THING.py', 'wire_ui.py', 'Bind_Wire_monther.py', 'Bind_Wire.py', 'Common_Function.py', 'Date_Analyse.py', 'Date_Analyse_monther.py', 'Get_Machine_Num_for_excel.py', 'Get_Future_Three_Month.py', 'Set_Machine_monther.py', 'Set_Machine.py', 'history.py', 'history_monther.py', 'wire_images_rc.py', 'wireandmachine_lh_monther.py', 'wireandmachine_lh.py', 'SERSON.PY', 'SERSON_MONTHER.PY', 'Thing_Check.py', 'Thing_Check_monther.py', 'lend_registe.py', 'lend_registe_monther.py', 'Update.py', 'Update_Mother.py', 'Login_monther.py', 'Login.py', 'set_machine_kitting.py'],
             pathex=['C:\\Users\\Administrator\\Desktop\\today_thing_register'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Main_Window_Show',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='77.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Main_Window_Show')
