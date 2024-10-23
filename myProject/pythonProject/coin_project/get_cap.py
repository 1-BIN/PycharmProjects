import requests
from matplotlib.pyplot import title
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
url = "https://www.upbit.com/trends"
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get(url)
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="UpbitLayout"]/div[3]/div/div[1]/div[5]/div[1]/ul/li[2]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="UpbitLayout"]/div[3]/div/div[1]/div[5]/div[2]/div/a').click()
time.sleep(1)

while True:
    soup = BeautifulSoup(driver.page_source, "html.parser")
    break
#print(soup.prettify())

# 1. 수집할 내용은, 코인아이콘, 코인이름, 시가총액 + 거래대금(24H)(api로 가져오기)
logo_soup = soup.select('.BasicTable__Cell em')
title_soup = soup.select('.BasicTable__Cell a')
market_cab_soup = soup.select('.BasicTable__Cell--AlignRight')
# print(logo_soup)
# print(title_soup)
# print(market_cab_soup)
for strong_tag in title_soup:
    title = strong_tag.select_one('strong')
    if title:
        print(title.text)
for logo in logo_soup:
    logo = logo.get('style')
    logo = str(logo).split("\"")[1]
    print(logo)
for span_tag in market_cab_soup:
    market_cap = span_tag.select_one('.CryptNewsTable__Price')
    if market_cap:
        print(market_cap.text)