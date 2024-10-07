import os
import time
import urllib.request as req
from selenium import webdriver
from selenium.webdriver.common.by import By

from ex_util.file import file_path

option = webdriver.ChromeOptions()
option.add_argument('--headless=old')
def fn_search():
    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(3)
    query = entry.get()
    url = f"https://www.google.com/search?q={query}"
    driver.get(url)
    time.sleep(1)
    txt.insert(END, "=" * 50 + "\n")
    txt.insert(END, f"{query} 이미지" + "\n" + "수집을 시작합니다." + "\n")
    txt.insert(END, "=" * 50 + "\n")
    # 1.이미지 탭 클릭
    driver.find_element(By.XPATH, '//*[@id="hdtb-sc"]/div/div/div[1]/div/div[2]/a/div').click()
    # 2.페이지하단 높이 가져오기
    current_h = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script(f'window.scrollTo(0,{current_h});')
        time.sleep(1)
        new_h = driver.execute_script('return document.body.scrollHeight')
        # 높이가 같다면
        if current_h == new_h:
            break
        current_h = new_h   #같지 않다면
    body = driver.find_element(By.TAG_NAME, 'body')
    imgs = body.find_elements(By.TAG_NAME, 'img')
    img_set = set()
    for img in imgs:
        # selenium 엘리먼트에서 속성 가져오기: get_attribute()
        if img.get_attribute('src') != None:
            img_set.add(img.get_attribute('src'))
    #print(img_set)
    driver.close()

    #이미지 저장

    root = "./"
    img_dir = os.path.join(root, query)
    #검색 이미지 이름으로 폴더 확인 및 생성
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)
    for i, v in enumerate(img_set):
        file_path = os.path.join(img_dir, str(i) + '.png')
        try:
            req.urlretrieve(v, file_path)
        except Exception as e:
            print(str(e))
def fn_delete():
    img_dir = f"./{entry.get()}"
    count = 0
    for filename in os.listdir(img_dir):
        file_path = os.path.join(img_dir, filename)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            # 1KB 미만 파일을 지웁니다.
            if file_size < 1024:
                os.remove(file_path)
                count += 1
    print(count)
    txt.insert(END, "삭제한 이미지 수: " + count + "\n")
from tkinter import *
app = Tk()
app.title("이미지 검색 수집기")
entry = Entry(app, width = 100)
entry.pack()
btn = Button(app, text='수집', command=fn_search)
btn.pack()
txt = Text(app, width=100, height=50)
txt.pack()
app.mainloop()