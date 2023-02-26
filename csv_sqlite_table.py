import sqlite3
import urllib.request
from urllib.request import urlopen, Request
import csv
import contextlib

'''Ref: https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3'''

urls = [r"https://people.sc.fsu.edu/~jburkardt/data/csv/oscar_age_male.csv",
        r"https://www.cmegroup.com/trading/interest-rates/files/mac-coupons-cusips-2023-09.csv",
        'https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv']

req = Request(urls[0])
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0')
fileName = r"oscar_age_male.csv"

req = urllib.request.Request(urls[0], method='GET')
with urllib.request.urlopen(req) as r:
    with open(fileName, 'wb') as fout:
        fout.write(r.read())
print("downloaded!")
result = []
with open(fileName, newline='') as csvfile:
    reader = csv.DictReader(csvfile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for row in reader:
        result.append(row)

columns = list(sorted(result[0].keys()))

col_def = ""
for i, column in enumerate(columns):
    col_def = col_def + column + " TEXT, "

col_def = col_def[:-2:]
table_name = fileName.replace(".", "_")

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
    for sql in sqls:
        cursor.execute(sql)
    connection.commit()
    rows = cursor.execute(f"SELECT * FROM {table_name} where Age='44'").fetchall()
    print(rows)

# print('\n'.join(sorted(dir(connection))))
