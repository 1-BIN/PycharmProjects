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
today = date.today()

params = {
  'market': 'KRW-SHIB'
  ,'side': 'bid'        # bid: 매수, ask: 매도
  ,'ord_type': 'limit'  # 주문타입. limit: 지정가 주문, price: 시장가 주문(매수), market: 시장가 주문(매도), best: 최유리 주문
  ,'price': '0.02'     # 주문가격. limit, price 시 필수.
  ,'volume': '250000'     # 주문량
}
# 파라미터를 url인코딩을 하고, 그걸 다시 읽을 수 있는 형태로 unquote하고,
# 데이터 전송을 위해 utf-8로 인코딩합니다
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

res = requests.post(server_url + '/v1/orders', json=params, headers=headers)
print(res.json())
data = res.json()

time_in_force=""
uuid = data['uuid']
side = data['side']
ord_type = data['ord_type']
price = data['price']
state = data['state']
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