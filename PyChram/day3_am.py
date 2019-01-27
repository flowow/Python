
#################"리스트 복사(y=x)","is"
x=[1,2]
print(id(x))#리스트의 메모리 주소가 출력
y=x
print(id(y))#x,y주소 동일->메모리에 [1,2]리스트는 하나 있고 두 변수가 동일한 리스트를 가리킴
#변수들이 동일한 주소를 가지는지 확인하는 함수 is
print(x is y)
x[0]=9
print(x)
print(y)

#################다른 주소 할당 방법: [:], copy 이용
i=[1,2]
j=i[:]#전체 영역 의미
print(i is j)
print(i)
print(j)
print(id(i))
print(id(j))
i[0]=10
print(i)
print(j)

k=[1,2]
from copy import copy #copy 모듈(py확장자 가진 파일들 즉 파이썬파일)에서 copy 함수 가져와라
c=copy(k)
print(id(c))
print(id(k))

###################초기화
x=y="hello" #오른쪽에서 왼쪽으로 이동(y->x) 초기화됨
print(x)
print(y)
[x,y]=["hi","hello"] #보통 이렇게 하지는 않지만 이렇게도 초기화 가능
print(x)
print(y)
x=10
y=20
# z=y
# y=x
# x=z
x,y=y,x #z라는 새로운 변수를 설정해서 값을 바꿀 수도 있지만 파이썬에서는 이렇게 간단히
print(x)
print(y)

#####################제어문과 반복문(for,while)
AI=True
if AI: #조건문 다음에는 반드시 콜론 사용으로 분리해줄것
    print("data scientist") #들여쓰기는 Tab이용
else :
    print("data analyst")
score=50
lic = True
if score>=60 or lic: #and 사용시 "불합격"출력
#    if #조건이 많으면 이렇게 아래에 나눠서 해도 됨
    print("합격")
else:
    print("불합격")

#a in 리스트, 문자열, 튜플 -> 그 안에 a 존재하는가?
print('a' in 'abc')
print('a' in ['a','b','c'])
print(1 not in [0,1,2])
print('a' in ('a','b','c'))
spec=['python','ML']
if 'ML' in spec:
    pass #pass: 조건문에서 아무 작업도 x
else :
    print("keep it up")
spec=['Cloud','Design']
langPy=True
if 'Cloud' in spec:
    print("클라우드 엔지니어")
else:
    if langPy:
        print("파이썬 개발자")
    else:
        print("추가공부 필요")
#위를 좀 더 간단히 elif
if 'Cloud' in spec: print("클라우드 엔지니어") #단문은 한 줄로 표현도 가능
elif langPy: #spec에 'Cloud'는 없지만(if 만족x) langpy가 참이면
    print("파이썬 개발자")
else: #위 두 조건 모두 만족하지 않으면
    print("추가공부 필요")
#파이썬에서는 이렇게도 표현 가능, 관심있는 결과부터 먼저
#조건이 참인 경우 if 조건문 else 조건문이 거짓
score=100
res="합격" if score>=60 else "불합격"
# if score>=90: res="합격"
# else: res="불합격"
print(res)
#*********반복문
#while문: 조건을 만족하는 동안 반복하라(무한루프 주의)
coffeept=0
while coffeept<10:
    coffeept=coffeept+1
    print("커피 %d잔째" % coffeept)
    if coffeept==10:
        print("You get free cup of coffee!")
#줄바꿈을 하고 싶으면 겹따옴표 3개 or \n!
# command="""
# 1. 입력
# 2. 검색
# 3. 출력
# 4. 종료
#
# 숫자를 입력하세요:
# """
# 입력받는 함수 input, 문자가 아닌 숫자로 입력받기 위해 int 필요
# print(command)
# number=0
# while number!=4:
#     print(command)
#     number=int(input())
#1~100까지 수 중 5의 배수 합
#!답(sum)을 먼저 설정함
#속성은 명료하게!(5의 배수면, 더해라)

a=5
sum=0
while a<=100:
    sum+=a
    a = a + 5
print(sum)
# sum=초기값
# if i%5==0: sum+=i
# 5의 배수면 더해라
#  100까지

#sol
# i=0
# sum=0
# while(i<=100):
#     if i%5==0:
#         sum+=i
#     i=i+1
# print(sum)