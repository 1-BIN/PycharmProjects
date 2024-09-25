import sqlite3
conn = sqlite3.connect("mydb.db")
cur = conn.cursor()
# 1. insert 문자열로
# cur.execute("INSERT INTO stocks VALUES('T', '테스트', 'TEXT')")

# 2. array
#cur.execute("INSERT INTO stocks VALUES(?,?,?)",['T2', '테스트2', 'TEST2'])
#cur.execute("INSERT INTO stocks VALUES(:1,:2,:3)",['T3', '테스트3', 'TEST3'])

# 3. dict
data = {'code':'T4', 'kr_nm':'테스트4', 'en_nm':'TEST4'}
cur.execute("INSERT INTO stocks VALUES(:code, :kr_nm, :en_nm)", data)
conn.commit()
conn.close()