# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Main_Window_Show.py', 'Admin_Resigner.py', 'Admin_Resigner_Monther.py', 'Bind_wire.py', 'Bind_Wire_monther.py', 'Common_Function.py', 'compile_all.py', 'Date_Analyse.py', 'Date_Analyse_monther.py', 'Get_Future_Three_Month.py', 'Get_Machine_Num_for_excel.py', 'history.py', 'history_monther.py', 'lend_registe.py', 'lend_registe_monther.py', 'Login.py', 'Login_monther.py', 'Main_Window.py', 'put_in.py', 'random_question_register.py', 'SERSON.PY', 'SERSON_MONTHER.py', 'Set_Machine.py', 'set_machine_kitting.py', 'Set_Machine_monther.py', 'tetris.py', 'THING.py', 'Thing_Check.py', 'Thing_Check_monther.py', 'Update.py', 'Update_Mother.py', 'wireandmachine_lh.py', 'wireandmachine_lh_monther.py', 'wire_images_rc.py', 'wire_ui.py', 'write_password.py'],
             pathex=['C:\\Users\\Administrator\\Desktop\\compile'],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Main_Window_Show',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='77.ico')
