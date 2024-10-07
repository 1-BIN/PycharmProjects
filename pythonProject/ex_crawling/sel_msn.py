#pip install selenium
#pip install chromedriver_autoinstaller
import chromedriver_autoinstaller
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 브라우저 드라이버 설치
chromedriver_autoinstaller.install(True)
# 브라우저 오픈
driver = webdriver.Chrome()
driver.implicitly_wait(3)   #브라우저가 켜질 때까지 최대(3)초 대기합니다. 컴퓨터마다 켜지는게 다르니까..
url = "https://www.msn.com/ko-kr/news/techandscience"
# url 페이지로 이동
driver.get(url)
time.sleep(1)   #1초 멈춤. driver.get(url)로 로드되는데 시간이 걸리기도 하니까..
# find_element <- 단일 엘리먼트 찾기 (By.   id,class, tag_name, xpath(절대경로)....)
body = driver.find_element(By.TAG_NAME, 'body')
pagedown = 1
cnt = 10
while pagedown < cnt:
    body.send_keys(Keys.PAGE_DOWN)  #스크롤 내리기
    time.sleep(0.5)
    pagedown +=1
soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup.prettify())
# driver.close()  #브라우저 종료

driver.close()  #브라우저 종료