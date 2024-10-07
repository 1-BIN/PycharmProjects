#bs4_movie에서 저장한 csv파일에서 movie_detial정보 읽어오기
import csv
import re
import requests
from bs4 import BeautifulSoup

url = "http://m.cine21.com"

#csv 파일 읽기
with open("./data/movie.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter="|")
    data = list(reader)
    for row in data:
        #상세페이지 url 열기
        detail_url = url + row[3]
        #print(detail_url)
        res = requests.get(detail_url)
        title = re.sub(r'[^a-zA-Z0-9가-힣\s]','',row[0])
        soup = BeautifulSoup(res.content, "html.parser")
        ul = soup.select_one('.review_writer')
        lis = ul.find_all('li')
        arr=[]
        for li in lis:
            writer = li.select_one('.name a').text
            score = li.select_one('.rating_area span').text
            review = li.select_one('.review_txt').text
            arr.append([writer, score, review])
        print(arr)
        with open(f"./data/{title}.csv", 'a', encoding="utf-8", newline='') as g:
            write = csv.writer(g, delimiter="|")
            write.writerows(arr)


#         res = requests.get(detail_url)
#         soup = BeautifulSoup(res.content, 'html.parser')
#         print(soup.prettify())
# #각 영화 이름으로('./data/폴더에) csv 파일 만들고
# #평론가이름|평점|관람평 을 저장하세요

