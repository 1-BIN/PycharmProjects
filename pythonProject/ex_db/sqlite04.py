import sqlite3
#조회하기
#close 빠뜨릴거같으면 with로 엽시다
#with sqlite3.connect('mydb.db') as conn:
conn = sqlite3.connect('mydb.db')
sql = """
    SELECT *
    FROM stocks
"""
cur = conn.cursor()
cur.execute(sql)
rows = cur.fetchall()
for row in rows:
    print(row)
conn.close()    #close빠뜨리면 안됩니다.