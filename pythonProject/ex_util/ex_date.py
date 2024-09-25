import datetime
# 현재 날짜와 시간
now = datetime.datetime.now()
print(now)
# 특정 날짜와 시간
dday = datetime.datetime(2025,1,17,17,50)
print(dday)
# 오늘 날짜
today = datetime.date.today()
print(today, '^~^')
# 날짜와 시간을 문자열로 반환
formatted = now.strftime('%Y%m%d %H:%M:%S')
print(formatted)
# 문자열을 날짜로
str_to_dt = datetime.datetime.strptime("2024-08-02","%Y-%m-%d")
print(str_to_dt)
# 날짜수 계산하기
st_date = datetime.date(2024,1,1)
end_date = datetime.date(2024,2,10)
delta = end_date - st_date
print(delta)
#요일 구하기
print('요일:',end_date.weekday()) #월:0, 화:1

import calendar
year = 2024
month = 9
first_weekday, num_days = calendar.monthrange(year, month)
print(f"{first_weekday}, {num_days}")
#for i in range(12):
# {i:2} <-- 2자리 차지하도록..
    #print(f"{i:2}", end=" ")    #<--옆으로 공백을 가지며 출력되도록..
print("일 월 화 수 목 금 토")
end_date_sep = datetime.date.month()
print(end_date_sep)
for i in range (int(f"{num_days}")):

    print(f"{i+1:2}", end=" ")