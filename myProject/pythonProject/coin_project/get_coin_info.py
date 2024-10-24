import requests
import cx_Oracle
from datetime import datetime

conn = cx_Oracle.connect("onebin", "BiNiBaMi", "127.0.0.1:1521/xe")
cur = conn.cursor()
# 종목 정보 조회
url = "https://api.upbit.com/v1/market/all"
url2 = "https://api.upbit.com/v1/market/all?is_details=true"
headers = {"accept": "application/json"}
res = requests.get(url, headers=headers)
data = res.json()
res2 = requests.get(url2, headers=headers)
detail_data = res2.json()
#print(data)
#print(detail_data)
def insert_coin_info():
    count = 1
    for info in data:
        coin_onum = "C" + str(count).zfill(3)
        market = info['market']
        kor_name = info['korean_name']
        eng_name = info['english_name']
        coin_info_insert_sql = """
                    INSERT INTO coin_info
                    VALUES (:1, :2, :3, :4)
                """
        cur.execute(coin_info_insert_sql, (coin_onum, market, kor_name, eng_name))
        count += 1
    conn.commit()

# 전체 종목 시세 조회
server_url = "https://api.upbit.com"

markets_list = []
for market in data:
    markets = market['market']
    markets_list.append(markets)

markets_str = ','.join(markets_list)
params = {
    "markets": f"{markets_str}"
}
res3 = requests.get(server_url + "/v1/ticker", params=params)
price_data = res3.json()
#print(price_data)

# 가격 정보 인서트
def insert_price_info():
    for info in price_data:
        market = info['market']
        opening_price = info['opening_price']
        high_price = info['high_price']
        low_price = info['low_price']
        trade_price = info['trade_price']
        prev_closing_price = info['prev_closing_price']
        acc_trade_price = info['acc_trade_price']
        acc_trade_price_24h = info['acc_trade_price_24h']
        acc_trade_volume = info['acc_trade_volume']
        acc_trade_volume_24h = info['acc_trade_volume_24h']
        price_info_insert_sql = """
                        INSERT INTO price_info
                        VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10)
                        """
        cur.execute(price_info_insert_sql, (market, opening_price,
                                            high_price, low_price,
                                            trade_price, prev_closing_price,
                                            acc_trade_price, acc_trade_price_24h,
                                            acc_trade_volume, acc_trade_volume_24h))
    conn.commit()

# 가격 정보 업데이트
def update_price_info():
    for info in price_data:
        market = info['market']
        opening_price = info['opening_price']
        high_price = info['high_price']
        low_price = info['low_price']
        trade_price = info['trade_price']
        prev_closing_price = info['prev_closing_price']
        acc_trade_price = info['acc_trade_price']
        acc_trade_price_24h = info['acc_trade_price_24h']
        acc_trade_volume = info['acc_trade_volume']
        acc_trade_volume_24h = info['acc_trade_volume_24h']
        price_info_update_sql = """
                                UPDATE price_info
                                SET opening_price = :1
                                    ,high_price = :2
                                    ,low_price = :3
                                    ,trade_price = :4
                                    ,prev_closing_price = :5
                                    ,acc_trade_price = :6
                                    ,acc_trade_price_24h = :7
                                    ,acc_trade_volume = :8
                                    ,acc_trade_volume_24h = :9
                                WHERE market = :market
                                """
        cur.execute(price_info_update_sql, (opening_price, high_price,
                                            low_price, trade_price,
                                            prev_closing_price, acc_trade_price,
                                            acc_trade_price_24h, acc_trade_volume,
                                            acc_trade_volume_24h, market))
        conn.commit()

if __name__ == '__main__':
    #insert_coin_info()
    #insert_price_info()
    update_price_info()