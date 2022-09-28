# пользовательский интерфейс
from data_note import data_struct as ds
from in_out import *

# запрос новых данных
def ask_new_rec(id : int = -1) -> dict:
    data = {}
    for k in ds.keys():
        if ds[k][0] == 'T':
            data[k] = input_str(f'введите {ds[k][1]}: ')
        elif ds[k][0] == 'N':
            data[k] = input_float(f'введите {ds[k][1]}: ')
        elif ds[k][0] == 'I':
            data[k] = id

    return data

# запрос информации для CRUD или отображения
def ask_sel_rec()-> dict:
    print('поле для поиска:')
    i = 0

    for k in ds.keys():
        i += 1
        print(f'{i} - {ds[k][1]}')
    
    fld_no = input_int('>')-1

    if fld_no not in range(1, i):
        return {}

    k = list(ds.keys())[fld_no]

    if ds[k][0] == 'T':
        val = input_str('Значение: ')
    else:
        val = input_int('Значение: ')
    lst = [ds[k][0], val]
    
    return {k: lst}



# отображение данных
def show_data(data: list):
    dkeys = ds.keys()

    header = ''
    head_line = ''
    for d in dkeys:
        if ds[d][0] == 'T':
            header += str(ds[d][1]).ljust(ds[d][2], ' ') + '  '
        else:
            header += str(ds[d][1]).rjust(ds[d][2], ' ') + '  '
        head_line += ''.rjust(ds[d][2], '-') + '  '

    print(head_line)
    print(header)
    print(head_line)

    for row in data:
        line = ''
        for k in dkeys:
            if ds[k][0] == 'T':
                line += str(row[k]).ljust(ds[k][2], ' ') + '  '
            else:
                line += str(row[k]).rjust(ds[k][2], ' ') + '  '
        print(line)

    print(head_line)
        
        
