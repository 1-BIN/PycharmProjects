import requests
from matplotlib import pyplot as plt

url = "https://api.upbit.com/v1/candles/minutes/1"
params = {
    'market': 'KRW-BTC',
    'count':30 ,
    'to': '2024-10-01 00:00:00' #마지막 캔들 시각, 비우면 가장 최근 캔들
}
headers = {"accept": "application/json"}
response = requests.get(url, params=params, headers=headers)
data = response.json()
data.reverse()
for i in range(len(data)):
    time = data[i]['candle_date_time_kst']
    print(time)