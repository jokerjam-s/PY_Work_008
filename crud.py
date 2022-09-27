# crud операции к БД
from logging import exception
import data_note as dn
import sqlite3 as sql3

# добавленеи информации
def insert_data(data):
    fields = ''
    values = ''

    try:
        for k in dn.data_struct.keys():
            if dn.data_struct[k][0] != 'I':    # пропустить ИД (автоинк)
                fields += f'{k},'
                if dn.data_struct[k][0] == 'T':
                    values += f'"{data[k]}",'
                else:
                    values += f'{data[k]},'
        
        con = sql3.connect(dn.connection_str)
        cur = con.cursor()
        cmd = f'INSERT INTO sotrudnik ({fields[:-1]}) VALUES ({values[:-1]});'
        cur.execute(cmd)
        cur.execute('COMMIT')
        records = cur.execute("SELECT id FROM sotrudnik WHERE id = last_insert_rowid();")
        cur.close()
        con.close()

        for row in records:
            data[id] = row[0]

    except Exception as ex:
        print(ex)

    return data


# обновление информации
def update_date(data):
    fields = ''
    values = ''

    try:
        for k in dn.data_struct.keys():
            if dn.data_struct[k][0] != 'I':    # пропустить ИД (автоинк)
                fields += f'{k} = '
                if dn.data_struct[k][0] == 'T':
                    fields += f'"{data[k]}",'
                else:
                    fields += f'{data[k]},'
        
        con = sql3.connect(dn.connection_str)
        cur = con.cursor()
        cmd = f'UPDATE sotrudnik SET {fields[:-1]} WHERE id =({data["id"]});'
        cur.execute(cmd)
        cur.execute('COMMIT')
        records = cur.execute("SELECT id FROM sotrudnik WHERE id = last_insert_rowid();")
        cur.close()
        con.close()

        for row in records:
            data[id] = row[0]

    except Exception as ex:
        print(ex)

    return data



# удаление информации
def delete_data(data):
    try:
        con = sql3.connect(dn.connection_str)
        cur = con.cursor()
        cmd = f'DELETE FROM sotrudnik WHERE id = {data["id"]};'
        cur.execute(cmd)
        cur.execute('COMMIT')
        cur.close()
        con.close()

    except Exception as ex:
        print(ex)


# поиск отображение / информации
def select_data(value):
    pass

