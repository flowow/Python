"""
match(): 문자열 처음부터 정규식과 매치되는지 확인
search(): 문자열 전체
fildall(): 정규식과 매칭되는 문자열을 리스트로 리턴
filditer(): 정규식과 매칭되는 문자열을 iterator로 리턴
"""
import re
p=re.compile('[a-z]+')
res=p.match("kpc")
print(res)
res2=p.match("2019 kpc")
print(res2)
res3=p.search("kpc.or.kr")
if res3: #res3에 객체가 들어가 있으면 참
    print("매칭 됨", res3.group()) #a.group(): 매칭된 부분 출력
else:
    print("매칭ㄴㄴ")

res5=p.match("2019 how are you")
print(res5)
res6=p.search("2019 how are you")
print(res6)
res7=p.findall("2019 how are you")
print(res7)
res8=p.finditer("how are you")
print(res8)
for r in res8:
    print(r)
    print(r.group()) #모든 매칭되는 대상들이 iterator(반복가능한 객체로 리턴)
res9=p.match("today is")
print(res9.group()) #매칭 문자열 리턴
print(res9.start()) #매칭 문자열 시작위치
print(res9.end()) #매칭 문자열 끝 위치
print(res9.span()) #매칭 문자열 위치 튜플로

res10=p.search("2019 today is")
print(res10.group())
print(res10.end())
print(res10.span())

            #2가지 표현 방식
a1=re.match('[a-z]','today') #축약형
pat=re.compile('[a-z]+') #기본형 (여러번할때 편리)
a2=pat.match('today')