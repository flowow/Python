# #######커피머신 제작
# coffee=5
# while True:
#     money=int(input("give me money"))
#     if money==150:
#         print("커피 곧 나옴")
#         coffee=coffee-1
#     elif money>150:
#         print("change:%d,커피나옴" % (money-150))
#         #출력지정자%d나 %s에 들어갈 수식의 결과는 괄호로 묶어줘야함
#         coffee=coffee-1
#     else:
#         print("돈 부족")
#         print("남은 커피 %d 잔 가능" % coffee)
#     if coffee==0:
#         print("재료 부족")
#         break

x=0
while x<10:
    x=x+1
    if x%2==0:continue
    print(x)

################for문
myList=[10,20,30]
for x in myList:
    print(x)
myList2=[(10,20),(30,40)] #tuple
for x in myList2:
    print(x)
myList3=[(10,20),(30,40)] #tuple의 구성요소 불러오기
for (x1,x2) in myList3:
    print(x1)
    print(x2)
    print(x1-x2)

score=[90,50,70,40,80]
for x in score:
    if x>60:
        print(score.index(x))
        print("번 학생 합격")

    else :
        print(score.index(x))
        print("번 학생 합격")

#성적처리 프로그램 작성
#결과 예시
score=[90,50,70,40,80]
num=0
for x in score :
    num=num+1
    if x<60:
        continue
    print("%d번 합격" % num)
#범위함수 range ->리스트 생성
x=range(5) #0이상 i미만
print(x)
x=range(1,11)
for i in range(1,11): #range(1,11) == [1,2,3,...,10]
    print(i)

score=[90,50,70,40,80]
for num in range(len(score)):
    if score[num]<60:
        continue
    print("%d번 ㅊㅋ"%(num+1))
####################줄바꿈 없이 연결
print(1, end="@")
print(2)
print(3)
#리스트 내포(comprehension): 리스트 내부에 for문 포함->간결
x=[10,20,30]
res=[] #빈 리스트
for su in x: #일반적 for문
    res.append(su*2)
    print(res)

x=[10,20,30] #원본리스트
res=[num*2 for num in x]#target list->x리스트의 요소값을 2배로 한 리스트
#[저장하고자 하는 값 for 변수 in 원본리스트]
res=[num/10 for num in x]
print(res)

x=[1,2,3,4,5] #홀수값[1,3,5]만 2배로 출력
#일반적 for문
res=[]
for i in x:
    if i%2!=0:
        res.append(i*2)
print(res)
#리스트내포
x=[1,2,3,4,5]
res=[i*2 for i in x if i%2!=0] #형식:[표현식 for 항목 in 반복대상객체 if 조건문
#                                           for 항목2 in 반복대상객체 if 조건문2
#                                                          ...                ]
print(res)

res=[a+b for a in range(1,5) #바깥 for문처럼 볼 수 있다
         for b in range(1,3)]
print(res)
#java의 이중for문과 비교
# for(int i=1;i<3;i++){
#     for(int j=1;i<3;j++){
#     }
# }
