#pip install cx_Oracle
import cx_Oracle
conn = cx_Oracle.connect("member", "member", "localhost:1521/xe")
print(conn.version)
sql = """
    SELECT *
    FROM stocks
    WHERE mem_name LIKE '%' || :word || '%'
"""
while True:
    nm = input("검색하고 싶은 고객명 입력(종료q): ")
    if nm == 'q':
        break
    d = {"word": nm}
    with conn:
        cur = conn.cursor()
        rows = cur.execute(sql, d)
        for row in rows:
            print(row)