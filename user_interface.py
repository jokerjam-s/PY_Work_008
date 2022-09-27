# пользовательский интерфейс
from data_note import data_struct as ds
from in_out import *

# запрос нового сотрудника
def ask_new_rec() -> dict:
    data = {}
    for k in ds.keys():
        if ds[k][0] == 'T':
            data[k] = input_str(f'введите {ds[k][1]}: ')
        elif ds[k][0] == 'N':
            data[k] = input_float(f'введите {ds[k][1]}: ')
        elif ds[k][0] == 'I':
            data[k] = 0

    return data

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
    os.system('pause')
