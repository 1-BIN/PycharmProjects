import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from datetime import date, timedelta, datetime
from datetime import datetime
import re

today = date.today()
#db 연결
# conn = cx_Oracle.connect("member", "member", "127.0.0.1:1521/xe")
# cur = conn.cursor()     # .cursor: db 작업을 가능하게 합니다.

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
article = soup.select('.kXHocr > a')
print(article)
# -고유번호 만들기 수집시간날짜시간
now = str(datetime.now())
onum = int(re.sub("[^0-9]+", '', now))
print(onum)
# 날짜
soup = BeautifulSoup(driver.page_source, "html.parser")
article = soup.select_one('.kXHocr > a')
article_date_str = page_last_article.select_one('.glLXQX').text[5:18]
article_date = datetime.strptime(article_date_str, "%Y년 %m월 %d일").date()
# 시간

# 제목

# 요약내용

# 상세링크

# 언론사



# (2) 고유번호 생성
# (3) 링크가 중복된다면 수집하지 않습니다

