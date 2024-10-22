import requests
# 종목 정보 조회
url = "https://api.upbit.com/v1/market/all?is_details=true"
headers = {"accept": "application/json"}
res = requests.get(url, headers=headers)
#print(res.json())

# 시세 조회
server_url = "https://api.upbit.com"
params = {
    "markets": "KRW-BTC,KRW-ETH"
}
res2 = requests.get(server_url + "/v1/ticker", params=params)
print(res2.json())