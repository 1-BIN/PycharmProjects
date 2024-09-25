from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
url = "https://www.hanatour.com/package/international"
# 백그라운드에서 실행되도록
option = webdriver.ChromeOptions()
option.add_argument('--headless=old')

def fn_search():
    driver = webdriver.Chrome(options=option)
    driver.get(url)
    time.sleep(1)
    input_search = driver.find_element(By.ID, 'input_keyword')
    input_search.send_keys(entry.get())   #tkinter의 entry에 입력한 값을 받아옵니다.
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
            txt.insert(END, title + ":" + price + "\n") #tkinter에 출력합니다.
        except Exception as e:
            print(str(e))
from tkinter import *
app = Tk()
app.title("tour search")
entry = Entry(app, width = 100)
entry.pack()
btn = Button(app, text='search', command=fn_search)
btn.pack()
txt = Text(app, width=100, height=50)
txt.pack()
app.mainloop()


