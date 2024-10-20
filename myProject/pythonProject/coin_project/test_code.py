
from datetime import date, timedelta, datetime

today = datetime.strptime(str(date.today()), "%Y-%m-%d")
today1 = date.today()
formatted = today.strftime('%Y년 %m월 %d일')
now = str(datetime.now())
print(today)
print(today1)
print(formatted)
print(now)

