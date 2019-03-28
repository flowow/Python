#question-summary-54103294 > div.summary > h3 > a
"""

url=https://stackoverflow.com/questions/tagged/python
res=rep.urlopen(url)
soup=BeatifulSoup(res, 'html.parser')
result=soup.select_one("#question-summary-54103294 > div.summary > h3 > a").string
"""
            #불러오는 또다른 방법
from urllib.request import urlopen #----------------(1) 필수파트. 동일
from bs4 import BeautifulSoup

page=urlopen("https://stackoverflow.com/questions/tagged/python")
doc=page.read()
#print(doc)

soup=BeautifulSoup(doc, 'html.parser') #이 구문이 있어야 제대로 줄바꿈 돼서 출력되는구나 잼따ㅎㅎ
print(soup)

questions=soup.find(id='questions')
print(questions)
#추출하고자 하는 범위의 태그를 찾아낸다
#qlist=questions.find_all(class_="question-hyperlink") #why not just 'class'?
qlist=questions.find_all(class_="excerpt")
#print(qlist) #리스트로 나오니까 for문으로  .get_text()!!!!
for que in qlist:
    print(que.get_text()) #wow 감동,,,,,결과 원하는대로 잘 나온다
    #get을 이용해 특정 속성값을 가져올 수 있다
    #<a href= 질문을 클릭하면 연결되는 링크> 질문</a> get_text find_all이 get_text보다 나중에 개발됨
    print('http://https://stackoverflow.com'+que.get('href'))
"""
영화 순위 뽑아내기
"""
url="https://www.rottentomatoes.com"
page=urlopen(url)
source=page.read()
soup=BeautifulSoup(source, 'html.parser')
#print(soup)
table=soup.find(id="Top-Box-Office")
#print(table)
movies=table.find_all(class_="middle_col")
print(movies)
for movie in movies:
    title=movie.get_text()
    print(title)
    link=movie.a.get('href') #href가 어디있는지 모르니까 a로 명시해준 것
    # print(, end=" ")
    url="https://www.rottentomatoes.com"+link
    print(url)