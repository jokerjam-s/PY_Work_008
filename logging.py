# логирование
import csv
import time

def log_save(operation: str, info):

    row = [time.ctime(), operation, info]

    with open('application.log', 'a', encoding='utf-8', newline='') as log:
        cwr = csv.writer(log, dialect='excel', delimiter='\t')
        cwr.writerow(row)
