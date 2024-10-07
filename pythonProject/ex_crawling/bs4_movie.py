import requests
import urllib.request as req
from bs4 import BeautifulSoup

url = "http://m.cine21.com/movie/boxoffice/history"
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")

div = soup.select_one('.lst_ranking_area')
lis = div.find_all('li')
print(lis)
arr = []
for li in lis:
    detail_url = li.select_one('.title a')['href']
    title = li.select_one('.title a').text
    score = li.select_one('.sub_info').text
    rating = li.select_one('.num').text
    print(detail_url, title, score, rating)
    print("=" * 100)
    arr.append([title, score, rating, detail_url])  #배열에 담습니다.
print(arr)
import csv
with open("./data/movie.csv", 'a', encoding = "utf-8", newline='') as f:    #csv 파일로 저장합니다.
    write = csv.writer(f, delimiter="|")    #delimiter: 구분자. 컬럼을 구분해줍니다. 텍스트에 없을만한거로 해야합니다.
    write.writerows(arr)        #rows: 여러개를 한번에 저장합니다.(row:한 줄만 저장합니다.)


