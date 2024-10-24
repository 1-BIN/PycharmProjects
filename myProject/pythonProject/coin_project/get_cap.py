from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from datetime import  datetime
import cx_Oracle

now = str(datetime.now())[:19]
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

logo_soup = soup.select('.BasicTable__Cell em')
title_soup = soup.select('.BasicTable__Cell a')
market_cab_soup = soup.select('.BasicTable__Cell--AlignRight')
# print(logo_soup)
# print(title_soup)
# print(market_cab_soup)
title_list = []
logo_list = []
cap_list = []
for strong_tag in title_soup:
    title = strong_tag.select_one('strong')
    if title:
        title_list.append(title.text)
for span_tag in market_cab_soup:
    market_cap = span_tag.select_one('.CryptNewsTable__Price')
    if market_cap:
        cap_list.append((str(market_cap.text)[0:-3]+'00000000').replace(',',''))
cap_list = cap_list[0::2]
for logo in logo_soup:
    logo = logo.get('style')
    logo = str(logo).split("\"")[1]
    logo_list.append(logo)

dict_list = [{'title_list': v1, 'logo_list': v2, 'cap_list': v3} for v1, v2, v3 in zip(title_list, logo_list, cap_list)]

def insert_market_cap():
    for i in range(len(dict_list)):
        title = dict_list[i]['title_list']
        logo = dict_list[i]['logo_list']
        cap = dict_list[i]['cap_list']
        i += 1

        insert_market_cap_sql = """
            INSERT INTO market_cap(kor_name, logo_url, cap, update_dt)
            VALUES (:1, :2, :3, :4)
        """
        cur.execute(insert_market_cap_sql, (title, logo, int(cap), now))
    conn.commit()
def update_market_cap():
    for i in range(len(dict_list)):
        title = dict_list[i]['title_list']
        cap = dict_list[i]['cap_list']
        i += 1

        insert_market_cap_sql = """
            UPDATE market_cap
            SET  cap = :1
                ,update_dt = :2
            WHERE kor_name = :kor_name
        """
        cur.execute(insert_market_cap_sql, (int(cap), now, title))
    conn.commit()

if __name__ == '__main__':
    update_market_cap()