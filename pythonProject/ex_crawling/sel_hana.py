import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.hanatour.com/package/international"
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get(url)
time.sleep(1)
input_search = driver.find_element(By.ID, 'input_keyword')
input_search.send_keys("하와이")   #input 입력값
driver.find_element(By.CSS_SELECTOR, 'button.btn_search').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="contents"]/div[3]/div[2]/div[1]/a').click()
time.sleep(1)
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

arr = soup.select('.prod_list li')
for li in arr:
    try:
        title = li.select_one('.txt_info .tit').text
        price = li.select_one('.price_info strong').text
        print("제목: "+title, "금액: "+price)
        print("=" * 80)
    except Exception as e:
        print(str(e))

driver.quit()

