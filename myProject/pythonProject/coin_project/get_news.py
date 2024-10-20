import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from datetime import date, timedelta, datetime
from datetime import datetime
import re
import cx_Oracle

today = date.today()
#db 연결
conn = cx_Oracle.connect("onebin", "BiNiBaMi", "127.0.0.1:1521/xe")
cur = conn.cursor()     # .cursor: db 작업을 가능하게 합니다.

#웹크롤링
url = "https://coinness.com/article"
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get(url)
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/main/div[2]/div[1]/button[2]').click()
time.sleep(1)
# 1. 오늘 날짜의 첫 기사가 나올 때까지 '더보기'버튼 클릭
    # (1) 페이지의 마지막 기사 날짜를 찾습니다.
while True:
    soup = BeautifulSoup(driver.page_source, "html.parser")
    page_last_article = soup.select_one('.kXHocr > a:last-child') #div class="kXHocr"의 마지막 자식 a태그
    article_date_str = page_last_article.select_one('.glLXQX').text[5:18]
    article_date = datetime.strptime(article_date_str, "%Y년 %m월 %d일").date() #today와 비교하기 위해 날짜형식으로 바꿉니다.
    # (2) 마지막 기사 날짜가 오늘 날짜와 같다면 더보기를 누릅니다.
    if article_date == today:
        driver.find_element(By.CLASS_NAME, 'bdXnLU').click()
    # (3) 마지막 기사의 날짜가 다르면 반복을 멈춥니다. 여기까지 완료!!!!!!!!!!!!
    else:
        break
# -- 이 시점의 soup에는 첫페이지부터, 마지막페이지까지 담겨있습니다.
#---------------------------------------------------------------------------------------------

# 2. 마지막 페이지에 있는 오늘의 첫 기사까지 수집합니다.
# (1) 수집할 내용은 고유번호, 날짜, 시간, 제목, 요약내용, 상세링크, 언론사
article = soup.select('.kXHocr a')
now = str(datetime.now())
today = date.today()
for dtl in reversed(article):
    # onum = int(re.sub("[^0-9]+", '', now)[:8] + str(count).zfill(4))
    article_dt = datetime.strptime(dtl.select_one('.glLXQX').text[5:18], "%Y년 %m월 %d일").date()  #날짜
    article_tm = dtl.select_one('.glLXQX span').text        #시간
    article_tt = dtl.select_one('.JpxIZ h3').text           #제목
    article_con = dtl.select_one('.JpxIZ p').text           #요약내용
    article_url = dtl.get('href')                           #링크
    article_jn = str(dtl.get('href')).split(".")[1]         #언론사(eng)

    old_news_url_sql = f"""
        SELECT article_url
        FROM news
    """
    cur.execute(old_news_url_sql)
    old_news_url_list = cur.fetchall()
    # 수집한 url이 데이터베이스에 없는 경우,
    for old_url in old_news_url_list:
        if old_url != article_url:
            latest_article_sql = """
                    SELECT onum, article_url, article_dt
                    FROM (
                        SELECT rownum, onum, article_url, article_dt
                        FROM news
                        ORDER BY 2 DESC
                        )
                    WHERE rownum = 1
                """
            cur.execute(latest_article_sql)
            latest_article = cur.fetchall()
            if list(latest_article[0])[2] == article_dt:
                onum = list(latest_article[0])[0] + 1
            elif today != list(latest_article[0])[2]:
                onum = int(re.sub("[^0-9]+", '', str(article_dt)) + str(1).zfill(4))
            # 새로운 기사 수집
            insert_data = """
                INSERT INTO news(onum
                                , article_dt
                                , article_tm
                                , article_tt
                                , article_con
                                , article_url
                                , article_jn )
                VALUES(:1, :2, :3, :4, :5, :6, :7)
            """
            cur.execute(insert_data, ( onum
                                       ,article_dt
                                       ,article_tm
                                       ,article_tt
                                       ,article_con
                                       ,article_url
                                       ,article_jn))
        conn.commit()
