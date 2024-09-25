#pip install bs4
from bs4 import BeautifulSoup
#html 파일로 열어서 가져오는 방법
with open('./data/test.html', 'r', encoding="utf-8") as file:   #'r':read (a:append, w:write)
    html_doc = file.read()

soup = BeautifulSoup(html_doc, 'html.parser')   # 앞의 파라미터를, html형식으로 parsing 합니다.
print(soup) #문서를 parsing한 객체가 soup에 담깁니다.
#구조화된 모습으로 출력하기(.prettify())
print(soup.prettify())
a_tag = soup.a
print(a_tag.name)       #a태그의 이름
print(a_tag.text)       #a태그로 감싸져있는 텍스트 내용
print(a_tag['href'])    #속성명으로
print(a_tag.get('id')) #get함수로 해당 속성 찾기
#find: 1개 (여러 개 있다면, 첫번째 등장하는 것)
#find_all: 모두
a_all = soup.find_all('a')
for a in a_all:
    print(a.text)

a_all2 = soup.find_all('a', string=True)    #text가 있는 a 태그만
print('텍스트 포함: ', len(a_all2))
import re
#re: 정규표현식 관련 라이브러리
a_han = soup.find_all('a', string=re.compile(r'[가-힝]')) #한글이 있는 태그만
print('한글 포함: ', len(a_han))

#select: 여러 건 css selector 사용
#select_one: 한 건에 사용
link1 = soup.select_one('#link1')   # (#)id
print(link1)
cls = soup.select('.sister')        # (.)class
print(cls)





