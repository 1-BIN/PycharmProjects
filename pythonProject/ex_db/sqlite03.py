import sqlite3
import requests
import json
conn = sqlite3.connect("mydb.db")
cur = conn.cursor()
sql = """
    INSERT INTO stocks
    VALUES(:1, :2, :3)
"""
res = requests.get("https://api.upbit.com/v1/market/all")
if res.status_code == 200:
    markets = res.json()
    for market in markets:
        print(market['market'])
        cur.execute(sql, [market['market']
                        , market['korean_name']
                        , market['english_name']])
    conn.commit()
conn.close()