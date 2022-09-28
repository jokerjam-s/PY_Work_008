# crud операции к БД
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
        cur.execute("SELECT id FROM sotrudnik WHERE id = last_insert_rowid();")
        cur.close()
        con.close()

    except Exception as ex:
        print(ex)


# удаление информации
def delete_data(val_id: int):
    try:
        con = sql3.connect(dn.connection_str)
        cur = con.cursor()
        cmd = f'DELETE FROM sotrudnik WHERE id = {val_id};'
        cur.execute(cmd)
        cur.execute('COMMIT')
        cur.close()
        con.close()

    except Exception as ex:
        print(ex)


# поиск отображение / информации
def select_data(condition: dict) -> list:
    fields = ''
    k = ''
    cnd = ''

    if condition.keys():
        k = list(condition.keys())[0]
        cnd = ' WHERE '

    if condition[k][0] == 'T':
        cnd += f' {k} LIKE "%{condition[k][1]}%";'
    else:
        cnd += f' {k} = {condition[k][1]}'

    result = []
    try:
        for k in dn.data_struct.keys():
            fields += f'{k},'
            
        con = sql3.connect(dn.connection_str)
        cur = con.cursor()
        cmd = f'SELECT {fields[:-1]} FROM sotrudnik' + cnd

        records = cur.execute(cmd)

        keys = list(dn.data_struct.keys())
        for row in records:
            tmp = {} 
            for k in range(len(keys)):
                tmp[keys[k]] = row[k]
            result.append(tmp) 

        cur.close()
        con.close()
    except Exception as ex:
        print(ex)

    return result
