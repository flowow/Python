a="Hello World, How are you?"
print(a[0]) #인덱스지정추출!
print(a[len(a)-4])
print(a[-2])#마이너스를 붙이면 뒤에서부터
#일부만 추출할 때
b=a[6]+a[7]+a[8]
print(b)
b=a[6:11]#slicing(시작위치:(마지막 위치는 미포함이기에)끝위치+1)
print(b)
print(a[11:])#11번째 위치부터~마지막까지 추출
print(a[:11])#첨부터 10번째까지
print(a[:])#전체 추출
print(a[3:-1])#3번째~뒤에서 5번째 전까지-1은 맨 마지막 문자열
day="20181231Sunny"
print(day[:8])#처음 시작은 1번째가 아니라 0번째
print(day[:-5])
print(day[-5:])
a="hallo"
print(a[1])
#a[1]='e''#문자열의 특정 요소값은 변경될 수 없다
#슬라이싱으로 해결 가능
print(a[:1]+'e'+a[2:])
a=a[:1]+'e'+a[2:]
print(a)

#######################문자열 형식 지정하기
lunch="I eat %d cookies." %5 #또는 %s % "five"
print(lunch)
lunch="I eat %d cookies. so I was %s " %(5, "sick") #두 개 이상 나열 시에는 소괄호로 묶을 것
print(lunch)
number=5
day="sick"
lunch="I eat %s cookies. 100%% so I was %s " %(number, "sick")
print(lunch) #퍼센트 출력은 %하나가 아니라 %% 두 개로!
#%s는 모든 자료가 변환되어 출력가능
print("%s" % "python") # %기준으로 왼쪽 형식에 맞춰 오른쪽을 출력 그냥 "파이썬"해도 출력 가능
print("%20s" % "python")
#20칸 확보 후 오른쪽 정렬로 문자열 출력
print("%-20sjava" % "python")
print("%20.5f" % 3.141592)#소수 이하 다섯째 자리까지 출력하라
print("I eat {0} cookies".format(5))
print("I eat {1} cookies " 
      "so I was sick for {0} days".format(5,"three"))#중괄호 0자리에 5넣어라 {#}에서 #는 format메서드 안에 인수 위치
print("I eat {number} cookies" 
      " so I was sick for {day} days".format(number=5,day=3))
print("I eat {0} cookies" 
      " so I was sick for {day} days".format(5,day=3))

print("{0}".format("hello"))
print("{0:<5}".format("hello"))#왼쪽 정렬, (5자리를 확보  후 출력
print("{0:>67}".format("hello"))#오른쪽 정렬, 67자리로 맞춰 출력
print("{0:^10}".format("hello"))#가운데 정렬, 10자리로 맞춰 출력

#공백 대체 출력
print("{0:=<10}".format("hello"))
print("{0:=>10}".format("hello"))
print("{0:=^10}".format("hello"))

x=3.123284
print("{0}".format(x))
print("{0:0.4f}".format(x)) #소수 이하 넷째자리까지(반올림)
print("{0:10.4f}".format(x)) #전체 10자리를 확보한 후 넷째자리까지
#format함수에서는 {, }기호를 나타낼 때 2개를 작성
print("{{ {0} and {1} }}".format("You","I"))

##################join,count,find,딕셔너리,대문자출력(upper),소문자출력(lower)
age=25
print(f'나는 {age+1}살이 된다') #파이썬 3.6버전부터 f포매팅 지원됨
myDict={'name':'이순신', 'age':30}
print(f'내 이름은 {myDict["name"]}') #key(name등)는 대괄호([) 내에
a="hello"
print(a.count('l')) #몇개 있는지
print(a.find('l')) #몇번째 위치?, 찾지 못하면 -1출력
print("%".join("abcd"))
print(",".join("abcd"))
print(a.upper())
print(a.lower())

#################공백제거, 치환
a="         deep learning     "
print(a.lstrip()) #왼쪽 공백제거
print(a.rstrip()) #오른쪽//
print(a.strip()) #양쪽//
print(a.replace("deep", "machine"))
#print(a= a.replace("deep", "machine")) #갱신하고 싶으면

a="How, are you" #문자열 3개 아니라 1개임
print(a.split()) #공백문자를 기준으로 분리 여기서는 3개
print(a.split("o"))
#[]:리스트 자료구조

#과제1
a="190101-1234567"
print(a[:6])
print(a[7:])
#과제2
if a[7] == "1": print("남")
else: print("여")
#과제3
b="x^y^z"
print(b.replace("^","!"))
#과제4
c = b.split("^")
print("!".join(c))
