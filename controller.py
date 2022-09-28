import crud
import data_note as dn
import os
import in_out as ino
from logging import log_save
from user_interface import ask_new_rec, ask_sel_rec, show_data

# menu пользователя
def menu() -> int:
    os.system('cls')
    for i in dn.menu_info.keys():
        print(f'{i} - {dn.menu_info[i]}')

    mn = ino.input_int('>')
    mn = 0 if mn not in dn.menu_info.keys() else mn
    return mn


def run_app():
    mnu = 1

    while mnu > 0:
        mnu = menu()
        match mnu:
            case 1:
                data = ask_new_rec()
                crud.insert_data(data)
                log_save('INSERT', data)
            case 2:
                ask = ask_sel_rec()
                data = crud.select_data(ask)
                log_save('SELECT', ask)
                show_data(data)
                print('1 - удалить, 2 - изменить, 0 - в меню ')
                mn = ino.input_int('>')
                if mn in (1,2):
                    val_id = ino.input_int('код: ')
                    if mn == 1:
                        crud.delete_data(val_id)
                        log_save('DELETE', val_id)
                    else:
                        upd_dat = ask_new_rec(val_id)
                        crud.update_date(upd_dat)
                        log_save('UPDATE', upd_dat)

        
    