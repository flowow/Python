# 함수 기본 형식
# def functionname(arguments):
#     sentences   들여쓰기 꼭
#     ...

def add(x,y):
    return x+y
res=add(6,9)
print(res)
#인수 없는 함수
def msg():
    return "hello"
var=msg()
print(var)
#return문이 없는 함수
def mul(x,y):
    print("%d와 %d의 곱은 %d입니다" % (x,y,x*y))
mul(3,4)
#res = mul(3,4) 리턴없어서 assign불가 출력결과 print(res)는 None
def add(x,y):
    print( x+y)
add(6,9)
def mul2(x,y):
    print(x) #매개변수를 호출해서 수행 가능
    print(y)
    return x*y
res=mul2(y=3,x=4) #함수는 이렇게 반드시 호출되어야 실행됨 그전에는 ㄴㄴ
print(res)
#매개변수 값이 일정치 않을 때, 즉 번거로운 수정을 줄여주기 위해
#def factorial(x1,x2,x3):
def total(*num): #total함수로 전달된 모든 값의 합 *num:임의의 개수를 가진 인수들을 리스트 전달받는다
    sum=0 #for문 안에 있으면 매번 초기화 되므로 주의
    for i in num:
        sum=sum+i #변수는 assign(~ = ~)시 초기화가 필요하다
    return sum
print(total(1,2,3,4,5))

# def add_sub(op,*num):
#     res=0
#
#         res = [res+i for i in num if op=add
#         res - i for i in num if op = sub]
    # else op=="sub":
    #     res=res-i
    # return res
# res=add_sub("add",1,3,5)
# print(res)
# res=add_sub("sub",1,3,5)
# print(res)

#리스트 내부

#과제1-1 일반for문
score=[70,20,50]
res=[]
for i in score:
    res.append(i*3)
print(res)

#과제1-2
score=[70,20,50]
res=[i*3 for i in score]
print(res)

#과제2 60점 이상 점수평균
score=[75,50,90,30,100,85]
sum=0
i=0
for num in score:
    if num>=60:
        i=i+1
        sum = sum+num
print(sum/i)

#과제3-1
for num in range(1,4):
    if num>0:
        print("*"*(num))

#과제3-2
for num in range(1,4):
    if num>0:
        print((len(range(1, 4)) - 1*num)*" ",end="")
        print("*"*(2*num-1))




