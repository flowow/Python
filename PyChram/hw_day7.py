from urllib.request import urlopen
from bs4 import BeautifulSoup

#정보를 구하기 어려울 때 직접 스크래핑으로 얻는다
#경로가 유일하면 다 쓸 필요 없다
#가격과 주행거리 추출 관계성?
# 지식인 모든 질문들 한번에 가져올 수 있다
# ex)konlpy(형태소분석기)=>명사/동사/
# 텍스트마이닝,감성분석, 광고/비광고 햄/스팸 등 분류기 만들 때
#질문 경향의 변화라든가 환율변동과 뉴스사이의 관계
#for i in range(20101213, 2018818) -뉴스 등!!!!!!!@!@!@!@!@!@!@!@@@@@
"""
https://search.naver.com/search.naver?where=kin&sm=tab_jum&query=%ED%95%9C%EA%B5%AD%EC%83%9D%EC%82%B0%EC%84%B1%EB%B3%B8%EB%B6%80
https://kin.naver.com/qna/detail.nhn?d1id=4&dirId=406&docId=316423667&qb=7ZWc6rWt7IOd7IKw7ISx67O467aA&enc=utf8&section=kin&rank=1&search_sort=0&spq=0
https://kin.naver.com/qna/detail.nhn?d1id=4&dirId=406&docId=312224313&qb=7ZWc6rWt7IOd7IKw7ISx67O467aA&enc=utf8&section=kin&rank=2&search_sort=0&spq=0
https://search.naver.com/search.naver?where=kin&kin_display=10&qt=&title=0&&answer=0&grade=0&choice=0&sec=0&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&query=%ED%95%9C%EA%B5%AD%EC%83%9D%EC%82%B0%EC%84%B1%EB%B3%B8%EB%B6%80&c_id=&c_name=&sm=tab_pge&kin_start=1
https://search.naver.com/search.naver?where=kin&kin_display=10&qt=&title=0&&answer=0&grade=0&choice=0&sec=0&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&query=%ED%95%9C%EA%B5%AD%EC%83%9D%EC%82%B0%EC%84%B1%EB%B3%B8%EB%B6%80&c_id=&c_name=&sm=tab_pge&kin_start=11
"""
#차량별로 가격,km 보배드림 사이트 이용
#listCont > div.wrap-thumb-list > ul > li:nth-child(1) > div > div.mode-cell.price > b > em
#listCont > div.wrap-thumb-list > ul > li:nth-child(2) > div > div.mode-cell.price > b > em
page=urlopen("http://www.bobaedream.co.kr/cyber/CyberCar.php?gubun=K")
doc=page.read()
soup=BeautifulSoup(doc,'html.parser')
ext=soup.find_all(class_="cr")
for e in ext:
    print(e.get_text(),end=" ")

check=soup.select("dd:nth-child(6)") #find_all로 했을 때는 오류났는데 왜 select로는 되지?
print(check)
for c in check:
    print(c.get_text(),end=" ")




