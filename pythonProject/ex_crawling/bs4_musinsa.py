import requests
from bs4 import BeautifulSoup
import re
url = "https://www.musinsa.com/mz/community-info?sort=uid&orderby=desc&p=1"
#403오류가 납니다. 잘못된 접근. 브라우저로 접근하지 않았기 때문.
#개발자툴 > 네트워크 > header > ~info > user agent가 나의 접근 브라우저.
#헤더에 포함시켜주면 되기도 합니다.
headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}
res = requests.get(url, headers = headers)
if res.status_code == 200:
    soup = BeautifulSoup(res.content, 'html.parser')
    #print(soup.prettify())
    divs = soup.select('.listPost')
    for div in divs:
        #info = div.select_one('.info')
        info = div.select('.info span')  #info 하위의 span이 필요할 때
        print(info[0])
        print(info[1])
        print(info[2])
        print(info[3])
        print(info[3].text) #태그의 텍스트만 필요할 때
        print(re.sub(r'\D','',info[0].text))    #정규 표현식 사용하여 숫자가 아닌 모든 것 제거
        print(re.sub(r'\D','',info[1].text))
else:
    print(res.text)