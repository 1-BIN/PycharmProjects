
from datetime import date, timedelta, datetime

today = datetime.strptime(str(date.today()), "%Y-%m-%d")
today1 = date.today()
formatted = today.strftime('%Y년 %m월 %d일')
now = str(datetime.now())
print(today)
print(today1)
print(formatted)
print(now)

created_at = '2024-10-22T12:48:48+09:00'
date_created_at = datetime.strptime(created_at[:10], "%Y-%m-%d").date()
print(date_created_at)