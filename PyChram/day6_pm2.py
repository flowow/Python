#크롬->ko.wikipedia.org으로 이동
#mw-content-text > div > div:nth-child(80) > table > tbody > tr > td > ul > li:nth-child(1) > a
#mw-content-text > div > ul:nth-child(8) > li:nth-child(42)
#스크래핑하고자하는 사이트 이동>F12> 맨 위 네모박스커서아이콘 눌러서 오른쪽 클릭>copy>copy selector
from bs4 import BeautifulSoup
import urllib.request as req
url="https://ko.wikipedia.org/wiki/%ED%94%BC%ED%84%B0_%EB%93%9C%EB%9F%AC%EC%BB%A4#%EC%A0%80%EC%84%9C" #한글이 인코딩된 주소
res=req.urlopen(url)
soup=BeautifulSoup(res,'html.parser')
print(soup)
#프로페셔널의 조건의 경로---> #(이#은 태그와 아이디를 구분하는#)mw-content-text
#                               > div > ul:nth-child(8) (8번째 child,n에 8 들어가는 구조)> li:nth-child(42)
#p=select_one(soup,req) ㄴㄴ
alist=soup.select("#mw-content-text > div > ul:nth-child(8) > li")
#mw-content-text > div > ul:nth-child(8) > li:nth-child(40)
for a in alist:
    print(a.string)

#mw-content-text > div > ul:nth-child(8) > li:nth-child(1)