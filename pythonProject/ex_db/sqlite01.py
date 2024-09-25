import sqlite3

# 경량 db, 파일형태
# conn = sqlite3.connect(":memory") #일회성 사용
conn = sqlite3.connect("mydb.db")
# 동적 타입
# NULL, INTEGER, REAL, TEXT, BLOB
print(sqlite3.version)
sql="""
    CREATE TABLE stocks(
        stock_code VARCHAR2 (20)
        ,stock_kr VARCHAR2 (100)
        ,stock_en VARCHAR2 (100)
    )
"""
cur = conn.cursor()
cur.execute(sql)
conn.close()