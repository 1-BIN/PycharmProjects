from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import urllib.request as req
from ex_util.file import file_path
query = "수달"
url = f"https://www.google.com/search?q={query}"
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)
time.sleep(1)
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
print(img_set)
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