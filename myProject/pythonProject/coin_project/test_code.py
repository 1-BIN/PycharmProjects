
from datetime import date, timedelta, datetime

today = datetime.strptime(str(date.today()), "%Y-%m-%d")
today1 = date.today()
formatted = today.strftime('%Y년 %m월 %d일')
#formatted2 = today.strftime('%Y년 %m월 %d일 %HH시 %MM분 %ss초')
now = str(datetime.now())[:19]
now_date = datetime.strptime(now, '%Y-%m-%d %H:%M:%S').date()
print(today)
print(today1)
print(formatted)
print(type(now_date))
created_at = '2024-10-22T12:48:48+09:00'
date_created_at = datetime.strptime(created_at[:10], "%Y-%m-%d").date()
print(date_created_at)

price = '992 억원'
price = price[0:-3]+'00000000'
print(price)