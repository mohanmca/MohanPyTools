import sqlite3
import urllib.request
from urllib.request import urlopen, Request
import csv

urls = [r"https://people.sc.fsu.edu/~jburkardt/data/csv/oscar_age_male.csv", r"https://www.cmegroup.com/trading/interest-rates/files/mac-coupons-cusips-2023-09.csv", 'https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv']


req = Request(urls[0])
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0')


fileName = r"oscar_age_male.csv"

# req = urllib.request.Request(urls[0], method='GET')
# with urllib.request.urlopen(req) as r:
#     with open(fileName, 'wb') as fout:
#         fout.write(r.read())
# print("downloaded!")
result = []
with open(fileName, newline='') as csvfile:
    reader = csv.DictReader(csvfile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for row in reader:
        result.append(row)

columns = list(sorted(result[0].keys()))
print(columns)

connection = sqlite3.connect("current.db")



print(connection.total_changes)
print('\n'.join(sorted(dir(connection))))


