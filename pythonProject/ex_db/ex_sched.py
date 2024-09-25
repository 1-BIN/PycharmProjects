from datetime import datetime
import pytz
seoul = pytz.timezone("Asia/Seoul")
from apscheduler.schedulers.blocking import BlockingScheduler
# interval 반복적으로 실행
# cron :원하는 시간, 다양한 시간에 실행
def fn_interval():
    print("interval")
    print(datetime.now())
def fn_cron():
    print("cron")
    print(datetime.now())

sched=BlockingScheduler()
sched.add_job(fn_interval, 'interval', seconds=2, timezone=seoul)
sched.add_job(fn_cron, 'cron', day_of_week = 'mon-fri', hour='16', minute='12', timezone=seoul)
                    #매주 월~금 16시 12분 호출
sched.start()
# sched.shutdown() 스케줄러 종료
