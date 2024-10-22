import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from datetime import date, datetime
import re
import cx_Oracle

today = date.today()
conn = cx_Oracle.connect("onebin", "BiNiBaMi", "127.0.0.1:1521/xe")
cur = conn.cursor()

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
for dtl in reversed(article):
    article_dt = datetime.strptime(dtl.select_one('.glLXQX').text[5:18], "%Y년 %m월 %d일").date()  #날짜
    article_tm = dtl.select_one('.glLXQX span').text        #시간
    article_tt = dtl.select_one('.JpxIZ h3').text           #제목
    article_con = dtl.select_one('.JpxIZ p').text           #요약내용
    article_url = dtl.get('href')                           #링크
    article_jn = str(dtl.get('href')).split(".")[1]         #언론사(eng)
    #수집한 url이 db에 존재하는지 확인
    url_check_sql = """
                    SELECT count(*)
                    FROM news
                    WHERE article_url = :article_url
                """
    cur.execute(url_check_sql, {'article_url' :article_url})
    url_exists = cur.fetchone()[0]
    #db에 수집한 url과 동일한 url이 있다면 다음 기사로 진행하기
    if url_exists > 0:
        continue
    #동일한 url이 없다면 수집하기
    #전에, 고유넘버링 위해 db에 존재하는 동일날짜 기사의 가장 큰 고유넘버 불러오기
    latest_article_sql = """
                        SELECT MAX(onum)
                        FROM news
                        WHERE article_dt = :article_dt
                    """
    cur.execute(latest_article_sql, {'article_dt': article_dt})
    db_max_onum = cur.fetchone()
    #완전히 새로운 날짜의 기사라면 기사날짜+0001~ 넘버링 해줍니다
    if db_max_onum[0] is None:
        onum = int(re.sub("[^0-9]+", '', str(article_dt)) + str(1).zfill(4))
    #동일 날짜의 기사가 존재한다면 기존 고유넘버에 +1 해줍니다
    else:
        onum = db_max_onum[0] + 1
    #기사를 insert 합니다
    insert_data = """
                    INSERT INTO news(onum, article_dt, article_tm, article_tt
                                    , article_con, article_url, article_jn )
                    VALUES(:1, :2, :3, :4, :5, :6, :7)
                """
    cur.execute(insert_data, (onum, article_dt, article_tm
                                  , article_tt, article_con, article_url, article_jn))
    conn.commit()




