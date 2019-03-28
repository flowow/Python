#############################내장함수
# myFile=open("msg.txt","w")
# myFile.write("message")
# myFile.close()
#위의 코드와 동일한 의미
with open("msg.txt","w") as myFile:
    myFile.write("message")
############내장함수: import가 필요하지 않음
print(abs(-2))
print(abs(-2.1))
print(all([1,2,3,4,5]))#all함수는 모든 요소가 참이어야->True
print(all([1,2,0]))#0은 false임
print(any([1,2,0,4,5]))#하나라도 참이면 참,모두 거짓이어야 F

#chr:아스키 코드값 입력=>문자로 변환해주는 함수
#65:A~90:Z, 97:a, 122:z,48:'0', 57:'9' 외울 필요 없셈
print(chr(65))
#divmod:나누기, 나머지연산
print(divmod(10,3)) #몫:3, 나머지:1
print(10//3)
print(10%3)
#enumerate
for i in enumerate(['a','b','c']): #인덱스부여해 하나씩 나열한 tuple
    print(i)
for i,j in enumerate(['a','b','c']):
    print(i,j)
#eval
print(eval('10+20')) #실행가능한 문자열을 전달받아 실행해주는 함수
print(eval('divmod(10,3)'))#회귀때 쓸 일 있을 것

def pos(v):
    res=[]
    #전달받은 v에 저장된 값들 중 양수값만 추출 저장
    for i in v:
        if i>0:
            res.append(i)
    return res
print(pos([5,-2,7,-9,3]))

def pos2(v):
    return v>0
print(list(filter(pos2,[5,-2,7,-9,3])))

print(list(filter(lambda x:x>0 ,[5,-2,7,-9,3])))

print(hex(255))
print(int('3')+1)
print(int(3.14))
print(int('10001',2)) #2진수로
print(int('FF',16)) #16진수로

class Today:
    pass
t=Today()
print(t) #인스턴트 생성이란 객체를 만드는 것
#t가 Today클래스의 객체입니까?맞으면 true(is함수)
print(isinstance(t,Today))

print(len("kpc")) #문자열
print(len([10,20,30,40,50])) #리스트
print(len((1,'a'))) #tuple
print(list("hello"))
print(list([10,20,30]))

def myFunc(x):
    return x*3
print(list(map(myFunc,[10,20,30])))
#min, max
print(min([5,1,2]))
print(max([5,1,2]))

print(ord('0'))
print(ord('A'))
print(pow(2,5)) #제곱
print(range(1,10))#객체가 그대로 나옴
print(list(range(1,10,2)))
#print(list(range(1,10,0.1)))
for i in range(1,10):
    print(i*0.1)
#반올림
print(round(4.7))
print(round(4.1))
print(round(3.13423421,4))

x=[3,1,2]
print(sorted(x))
print(x) #자체적으로 정렬된 것x
print(sorted(['c','a','t']))
print(sorted("cat"))
print("hello".upper())
print(sum([2,3,4]))
print(sum((2,3,4)))
print(type("test"))
print(type([]))
print(type(open("aaa.txt","w")))
print(list(zip([1,3,5],[2,4,6],[7,8,9])))#######zip함수 유용
print(list(zip("abcd","efgh")))

#과제1
#print(list(map(lambda x:str(x) if x%2==0 else x,x)))

#x=[1,2,3,4,5]
#res=[i*2 for i in x if i%2!=0]
# def isEven(i):
#     i=int(input("숫자 입력고고"))
#
#     num= isEven(i)
#     for i in num
#         if i%2==0 :
#             isEven(i)="짝수입니다:"
#             print(isEven(i))
#         else :
#             isEven(i)="홀수입니다"
#             print(isEven(i))
#             return

#************sol
# def isEven(i): #초기값을 가지는 인수는 뒤쪽으로 넘겨 오류 피한다
#     i = int(input("숫자 입력고고: "))
#     if i%2==0:
#         print("짝수입니다")
#     else:
#         print("홀수입니다")
# isEven(i)

#과제2 ***********solllll
# def gugu(i):
#     i = int(input("몇 단?"))
#     for m in range(1,10):
#         print(i*m)
# gugu(i)
#??한줄로 어떻게?

#과제3

# for i = int(input("몇 단?")), m in range(1, 10):
# #     print(i * m)
while i<10
     append.//10
if i= ㅁ1+ㅁ2+...+ㄴ
x=range(1,5001)
a=x%10
sum=0
b=0
while x <10:
    i=x//10
    sum= sum + i
sum= sum + a
if x == sum:
    b= b+x
print()