import jwt
import hashlib
from datetime import date
import requests
import uuid
from urllib.parse import urlencode, unquote
import cx_Oracle
import re

conn = cx_Oracle.connect("onebin", "BiNiBaMi", "127.0.0.1:1521/xe")
cur = conn.cursor()

access_key = '7wyBZ596dAYxmILIIZhWO5OBLlBKgzDQILUniZ1r'
secret_key = 'r7kUzsQ7Sq3FRgldvnX46WunPxj4jiP7rJRdP4sw'
server_url = 'https://api.upbit.com'
order_uuid = '0b3828e5-df57-42d4-a25a-ba746a1abd16'
today = date.today()

select_uuid_sql = """
                SELECT uuid
                FROM tb_order
                WHERE uuid = :order_uuid
            """
cur.execute(select_uuid_sql, {'order_uuid': order_uuid})
ouuid = cur.fetchone()[0]

params = {
  'uuid': ouuid
}
query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

m = hashlib.sha512()
m.update(query_string)
query_hash = m.hexdigest()

payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
    'query_hash': query_hash,
    'query_hash_alg': 'SHA512',
}

jwt_token = jwt.encode(payload, secret_key)
authorization = 'Bearer {}'.format(jwt_token)
headers = {
  'Authorization': authorization,
}

res = requests.delete(server_url + '/v1/order', params=params, headers=headers)
res.json()
print(res.json())
data = res.json()

time_in_force=""
uuid = data['uuid']
side = data['side']
ord_type = data['ord_type']
price = data['price']
state = 'cancle'
market = data['market']
created_dt = data['created_at'][:10]
created_tm = data['created_at'][11:19]
volume = data['volume']
remaining_volume = data['remaining_volume']
reserved_fee = data['reserved_fee']
remaining_fee = data['remaining_fee']
paid_fee = data['paid_fee']
locked = data['locked']
executed_volume = data['executed_volume']
trades_count = data['trades_count']

latest_order_sql = """
                        SELECT MAX(onum)
                        FROM tb_order
                        WHERE created_dt = :today
                    """
cur.execute(latest_order_sql, {'today': today})
db_today_max_onum = cur.fetchone()

if db_today_max_onum[0] is None:
    onum = int(re.sub("[^0-9]+", '', created_dt[:10]) + str(1).zfill(5))
else:
    onum = db_today_max_onum[0] + 1

if "time_in_force" in data:
    print(data['time_in_force'])
    time_in_force = data['time_in_force']
else:
    print("없음")


insert_order_sql = """
                INSERT INTO tb_order
                VALUES(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17, :18)
                """
cur.execute(insert_order_sql,(onum, uuid, side, ord_type, price, state, market
                              ,created_dt, created_tm, volume, remaining_volume, reserved_fee, remaining_fee
                              , paid_fee, locked, executed_volume, trades_count, time_in_force))
conn.commit()