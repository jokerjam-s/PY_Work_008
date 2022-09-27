import crud
import data_note as dn
import os
import in_out as ino
from user_interface import show_data

# menu пользователя
def menu() -> int:
    os.system('cls')
    for i in dn.menu_info.keys():
        print(f'{i} - {dn.menu_info[i][0]}')

    mn = ino.input_int('>')
    mn = 0 if mn not in dn.menu_info.keys() else mn
    return mn


def run_app():
    mnu = 1

# clr.crud.insert_data({"id": "1", "sotrname":"Петр", "sotrfio":"Баширов", "oklad":"60000", "phones":"+7 855 436-90-15"})
    lst = [
        {"id": "1", "sotrname":"Иван", "sotrfio":"Иванов", "oklad":"60000", "phones":"+7 855 436-90-15"},
        {"id": "2", "sotrname":"Петр", "sotrfio":"Баширов", "oklad":"60000", "phones":"+7 855 436-90-15"},
        {"id": "3", "sotrname":"Елена", "sotrfio":"Сидорова", "oklad":"60000", "phones":"+7 855 436-90-15"}
    ]

    while mnu > 0:
        mnu = menu()
        match mnu:
            case 1:
                show_data(lst)
            case 2:
                print('pass')
            case 3:
                print('pass')
        
    