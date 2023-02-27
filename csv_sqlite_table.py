import sqlite3

import csv
import contextlib
from tools import download_and_save

'''Ref: https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3'''

urls = [r"https://people.sc.fsu.edu/~jburkardt/data/csv/oscar_age_male.csv",
        r"https://www.cmegroup.com/trading/interest-rates/files/mac-coupons-cusips-2023-09.csv",
        'https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv']

fileName = urls[0].split("/")[-1]
table_name = fileName.replace(".", "_")
download_and_save(urls[0], fileName)

print("downloaded!")

result = []
with open(fileName, newline='') as csvfile:
    reader = csv.DictReader(csvfile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for row in reader:
        result.append(row)

columns = list(sorted(result[0].keys()))

col_def = " TEXT, ".join(columns) + " TEXT"
col_def = col_def.replace("Index", "_Index")

table_def = f"CREATE TABLE  IF NOT EXISTS {table_name} ( {col_def} )"
print(table_def)

connection = sqlite3.connect("current.db")

sqls = []
for record in result:
    insert_def = ''
    for column in columns:
        value = record[column].strip().replace("'", "_")
        insert_def = insert_def + f"'{value}', "
    except_last_2_char = slice(0, -2)
    values = insert_def[except_last_2_char]
    insert_def = f"insert into {table_name} VALUES ( {values} )"
    sqls.append(insert_def)

# print(sqls)

with contextlib.closing(connection.cursor()) as cursor:  # auto-closes
    cursor.execute(table_def)
    for sql in sqls:
        cursor.execute(sql)
    connection.commit()
    rows = cursor.execute(f"SELECT * FROM {table_name} where Age='44'").fetchall()
    print(rows)

# print('\n'.join(sorted(dir(connection))))
