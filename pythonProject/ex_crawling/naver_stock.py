import cx_Oracle
import csv

conn = cx_Oracle.connect("member", "member", "127.0.0.1:1521/xe")
dict_list = []

with open('./data/kospi_list.csv', 'r', encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        dict_list.append(row)
print(dict_list)
insert_sql="""
    INSERT INTO stock(code, name, market, marcap, stocks)
    VALUES (:1, :2, :3, :4, :5)
"""
cursor = conn.cursor()
for item in dict_list:
    cursor.execute(insert_sql
                  , [item['Code'], item['Name'], item['Market'], item['Marcap'], item['Stocks']])
conn.commit()
conn.close()