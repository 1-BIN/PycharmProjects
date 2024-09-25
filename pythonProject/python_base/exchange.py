import requests
# 현재 환율 api
# USD 1달러 기준 각 국가의 환율 정보 json으로 리턴

url = "http://open.er-api.com/v6/latest/USD"
res = requests.get(url)
data = res.json()
#print(data)

# 달러 to 원화 함수를 작성해주세요
# input: 달러 금액 (ex:10)
# output: 원화 금액 (ex: 13421.04544)
def fn_to_krw(usd):
    krw_exc = data['rates']['KRW']
    to_krw = usd * krw_exc
    return usd, to_krw
print("%d 달러는 원화로 %.2f"% (fn_to_krw(220.91)))


