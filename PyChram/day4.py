
#키워드 parameter(**):인수로 전달된 값을 딕셔너리로 변환
def myPrint(**info):
    print(info)
myPrint(x=100,y="hello")

def add_sub(x,y):
    return x+y, x-y
res1=add_sub(3,4) #return 여러 개 일 수 있는 파이썬 특징
res2,res3=add_sub(3,4)
print(res1)
print(res2)
print(res3)

def myPrint2(msg):
    if msg=="안녕":
        return #함수를 호출했던 곳으로 되돌아감. 아래 print로 안 가고 종료됨
    print("반갑습니다. %s" %msg)
myPrint2("안녕하세염")

def myPrint3(name, old, man=True): #초기값을 가지는 인수는 뒤쪽으로 넘겨 오류 피한다
    print("이름:%s"%name)
    print("age:%d" % old)
    if man:
        print("남자")
    else:
        print("여자")
myPrint3("홍길동",30,False)

#변수 scope, 함수 내에서 작성된 변수는 함수 내에서만 사용됨
x=1
def scopeTest(x):
    x=x+1
scopeTest(x)
print(x)

# def scopeTest2(y):
#     y=y+1
# scopeTest(5)
# print(y) #함수를 벗어난 지역변수 y는 기능ㄴㄴ

#함수 내에서 함수 외부에 있는 변수 변경
#1.리턴으로 해줘서 x에 값 넣어주기
x=1
def scopeTest3(a):
    a=a+1
    return a
x=scopeTest3(x)
print(x)
#2.global x 함수 이용: 함수 내부에서도 외부 변수 x 사용,but 메모리,유지 보수 번거로움으로 잘ㄴㄴ
x=1
def scopeTest4():
    global x
    x=x+1
scopeTest4()
print(x)

#람다(lamda)식: 함수를 간결하게 표현
#작성형식=>lamde 인수1, 인수2,..: 인수를 이용한 수식
mul=lambda x,y:x*y
res=mul(2,3)
print(res)
#def mul(x,y)
#   return x*y

pten=lambda x:x+10
print(pten(5))
#람다식의 이름=함수 이름
#map(적용하고자하는 함수, 함수에 적용되는 데이터(iterable-반복가능))
print(list(map(pten,[100,200,300]))) #map함수를 이용해 pten을 맵핑시켜라

#익명의 람다식을 이용해 함수호출 가능
print(list(map(lambda x:x+10,[100,200])))#익명의 람다식을

#예제:리스트 내에 저장된 값중에서 짝수만 문자열로 변환
#참인 경우 if 조건 else  거짓인 경우
#람다식에서 if문을 사용한 경우에는 반드시 else가 있어야 함
#식1 if 조건식1 else 식2 if 조건식2 else 식3(람다식은 elif사용x,
#조건식1x->조건식2로넘어가 ㅇ이면 식2 실행됨
x=[1,2,3,4,5]
print(list(map(lambda x:str(x) if x%2==0 else x,x)))
#print(str(3)+"1")#문자열 변환 함수 str(x), 실수 변환 함수 float(x)
print(list(map(lambda x: str(x) if x==1 else float(x) if x==2 else x+100 ,x )))

a=[1,2,3]
b=[4,5,6]
print(list(map(lambda x,y:x+y, a,b)))

def myFunc(x):
    return x>5 and x<10
print(myFunc(3))
myList=[7,3,10,0,9]
#filter: 반복가능한 객체에서 조건을 만족하는 요소만
#filter로 지정한 함수의 리턴값이 true인 경우만 필터링
print(list(filter(myFunc, myList)))#myFunc함수에 myList를 넣어
print(list(filter(lambda x: x>5 and x<10,myList)))

#num=input("입력하세요") #잘 쓸 일 없음
#print(num)
print("hi","hello") #컴마를 이용하면 띄어쓰기 또는
print("hi"+" "+"hello")

################파일 쓰기&읽기
#open():파일 작성 함수
#파일객체변수=open(파일명,파일열기모드)
#열기모드:r(읽기), w(쓰기), a(추가,append)
# myFile=open("newFile.txt","w")
# myFile.close()
# myFile2=open("newFile.txt","a")#여기선 역슬래시 아니라 슬래쉬
# for i in range(6,31):
#     msg="%d번째 라인입니다\n"% i
#     myFile2.write(msg)
# myFile2.close()
myFile3=open("newFile.txt","r")
while True:
    line=myFile3.readline() # 한 줄로 나옴
    print(line)
    if not line:break
    print(line)