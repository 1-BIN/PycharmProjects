from datetime import timedelta, date, datetime
now = datetime.now()
print(now)
#timedelta() 로 기간에 대한 객체를 생성할 수 있다.
#오늘부터 일주일 뒤의 날짜를 구하고 싶다면 timedelta(weeks = 1) 혹은 timedelta(days = 7) 객체를 더해주면 된다.
#yesterday =

# today = date.today()
# one_week = timedelta(weeks = 1)
# one_week_later = today + one_week
# diff = one_week_later - today
# print(today)

#today = date.today()
# one_day = timedelta(days = 1)
# one_day_before = today - one_day
# print(one_day_before)

# date_string = "2024년 9월 24일 화요일"
# date = datetime.strptime(date_string[ :12], "%Y년 %m월 %d일").date()
# print(today, date)
#
# if today == date:
#     print("일치합니다")
# else:
#     print("다릅니다")