from datetime import datetime
from os import mkdir
from django.shortcuts import redirect
from django.contrib import messages

import sqlite3
import io, os


def backup(request):
    my_db = 'db.sqlite3'
    # sqlite3 my_db ".backup 'backup_file.sqlit3'"
    path = 'backups/'
    if not os.path.exists(path):
        mkdir('backups')
        conn = sqlite3.connect(my_db)
        with io.open('backups/backup_'+ datetime.now().strftime('%d-%m-%Y_%H-%M') + '_.sql', 'w') as f:
            for bk in conn.iterdump():
                f.write('%s\n' % bk)
        conn.close()
        messages.success(request, 'Create a directory and perform Backup successfully ... ')
    elif os.path.exists(path):
        conn = sqlite3.connect(my_db)
        with io.open('backups/backup_'+ datetime.now().strftime('%d-%m-%Y_%H-%M') + '_.sql', 'w') as f:
            for bk in conn.iterdump():
                f.write('%s\n' % bk)
        conn.close()
        messages.success(request, 'Backup Done Successfully ...@ ' + path)
    else:
        messages.success(request, 'Backup failed try again !!!! ')

        # conn = sqlite3.connect(my_db)
        # with io.open('backups/backup_'+ datetime.now().strftime('%d-%m-%Y_%H-%M') + '_.sql', 'w') as f:
        #     for bk in conn.iterdump():
        #         f.write('%s\n' % bk)
        # messages.success(request, 'Backup Done Successfully ... ')
    # print('Backup performed successfully.')
    # print('Saved as backup_dump.sql')
    # conn.close()
    return redirect('/')



def talk_with_reg(request):

    import winreg
    reg_connection = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)

    reg_key = winreg.OpenKey(reg_connection, r"SOFTWARE\Microsoft\\")

    winreg.CreateKey(reg_key, "New Key")

    # for key in range(3000):
    #     try:
    #         show_sub_keys = winreg.EnumKey(reg_key, key)
    #         print('done')
    #     except exceptions.WindosError:
    #         break

    new_key_value = winreg.OpenKey(reg_connection, r"SOFTWARE\Microsoft\New Key", 0, 
                                    winreg.KEY_SET_VALUE)
    winreg.SetValueEx(new_key_value, "New Value",0,winreg.REG_SZ, "This Value")
    winreg.CloseKey(new_key_value)

    return redirect('/')

