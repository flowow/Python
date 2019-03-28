
#정규식(RE):주어진 문자열을 효과적으로 처리해서
#(수집 후 전처리 과정) 모델링하기 적합한 형태로 변환할 때 사용
#문제:개인정보 처리? ex)주민번호 뒷자리 모두 *로 치환

#스크래핑 해보기(stack 사이트 등 관심 분야)

#case: 정규식 모를 때 for문 이용 가능
jumin="""
h 190203-4749567
k 940226-9573854
"""
res=[]
for line in jumin.split("\n"): #해당 내용 기준으로 분리

    # print(line.split(" "))
    # print(line.count('h'))
    for word in line.split(" "):
        if len(word)==14:
            word=word[:6]+"-"+"*******"
            print(word)
        res.append(word)
    print(res)##################

#정규식 작성법
#re모듈 이용, match함수에 정규식 작성
#형식:re.match("패턴","문자열") ---> 문자열에 패턴이 존재하는지 물어보는 것
import re
print(re.match("hello","hello, world")) #--->문자열에 패턴이 존재하므로 Object로 나옴
print(re.match("hi","hello, world")) #---> none

jumin="""
h 190203-4749567
k 940226-9573854
"""
import re
pt=re.compile("(\d{6})[-]\d{7}") #메타문자:본래 문자의 의미가 아니라 특정하게 사용되는 문자
print(pt.sub("\g<1>-*******",jumin))
#( ) { } [대괄호] \ | ? + $ * ^ 등등
#1.[]: 대괄호 사이에 어떤 문자도 올 수 있다
#정규표현식: [asdf] ---> a,s,d,f 중 한 개의 문자와 매치
#"a", "all"는 정규표현식과 일치하는 any 문자가 있기에 match

#하이픈 기호 사용 시 시작과 끝 문자열을 지정하게 됨
#[^a-b]사용 시 여집합의 의미 ex)[^0-9]: 숫자를 제외한 나머지 모두
#[a-z]: 알파벳 소문자 모두
#\d: 숫자와 매치됨. [0-9]와 같은 의미 cf)\D는 숫자과 아닌 것과 매치됨. [^0-9]와 같은 의미
#\w:문자,숫자,_(언더바)와 매치됨, [a-zA-Z0-9]의미
#\W:문자,숫자, _ 가 아닌 문자와 매치됨,[^a-zA-Z0-9]
#\s: space 문자와 매치됨. [\t\n\r]의 의미
# \S: 바로 위가 아닌 문자와 매치 [^\t\n\r]

#^문자열: 문자열이 맨 앞에 오는지 판단
#문자열$: 문자열이 맨 뒤에 오는지 판단
#search함수가 사용됨
print(re.search("^hi","hello,hi")) #hi 문자열이 맨 앞에 오는지 판단-->none
print(re.search("^hi","hi hello")) #hi 문자열이 맨 앞에 오는지 판단
print(re.search("hi$","hello,hi")) #hi 문자열이 맨 뒤에 오는지 판단



# |(bar 기호)는 'or' 의미
print(re.match("hello|hi","he"))#hello 또는 hi가 포함--->none
print(re.match("hello|hi|good|how", "hi"))
print(re.match("hello|hi","hi"))#hello 또는 hi가 포함--->출력됨 span은 |기준으로 hi의 위치 의미 (0,2)

import re
print(re.match("[0-9]","7"))
print(re.match("[0-9]","7dfdgh"))#문자열의 맨앞글자만 고려
# *: 0개 이상 있는지 판단
print(re.match("[0-9]*","asdf"))#none이 아니라 0개로 인식
print(re.match("[0-9]*","78asdf"))
print(re.match("[0-9]*","a7sdf"))#맨 앞문자가 아니라 여전히 0개
print(re.match("[a-z]*","asdf"))#a가 아니라 asdf로 인식yo
# +: 1개 이상 있는지 판단(*와 다르게 0개 있으면 none)
#           맨 앞부분이 특정 단어로 시작하는 데이터를 찾고 싶을 때 등 유용!
print(re.match("[a-b]+","데이버뉴스기사"))
print(re.match("[0-9]+","abc"))
#           a가 0개 이상 있으면 패턴 매칭됨
print(re.match("a*b","aaaaab")) #(패턴,문자열) span은 매치된 범위(aaaaab)를 뜻함
print(re.match("a*","aaaaab")) #(패턴,문자열) /match='aaaaa'
print(re.match("a+b","aaaabbcc")) # a한 개 이상, 다음, b 1개(단수)
print(re.match("a+b+","aaaabbcc")) # a한 개 이상, 다음, b 1개 이상(복수)
print(re.match("a+b*","aaaabbcc")) # a한 개 이상, 다음, b 0개 이상(복수)
#           문자가 한 개만 있는지 판단: ? 또는 .(온점) 사용
#           ?는 문자 0개 또는 1개, (.)는 문자 1개 (* , +) (? , .)
print(re.match('h?','h'))
print(re.match('h?','hello')) # h(범위)
print(re.match('h.','h')) #--->none
print(re.match('h.','hello')) # he(범위)
#           a.b: 'a'+모든 문자+ 'b'
print(re.match('a.b','aab'))
print(re.match('a.b','akb'))
print(re.match('a.b','ab')) #--->none
print(re.match('a.b','a0b'))
print(re.match('a.b','akdsdb')) #--->none

print(re.match('c*t', 'ctctct')) #ct
print(re.match('ca*t', 'ct')) #---->I don't get why it has " match='ct' " though it doesn't have 'ca'?
print(re.match('ca*t', 'caaaaatdog')) #caaaaat
print(re.match('ca*t', 'cttttt')) #ct

print(re.match('ca*', 'oottttt')) #'[a-z]*'가 아니라 단순 문자열 'ca*'에서 *는 바로앞문자 a의 0개 이상을 의미함
print(re.match('ca', 'coottttt')) #None, *없으면 'ca'를 찾음
print(re.match('ca*t+', 'cttttt')) #cttttt

print(re.search("hi","hello,hi")) #span=(6, 8), match='hi'
print(re.search("hi*","hello,hi")) #span=(0, 1), match='h'
print(re.search("hi*o","hello,hi"))
print(re.search("hl*o","heo,hi")) #


print(re.search("^[-com]","java@example-com"))
print(True)
print(re.match("[a-z]+\@[a-z]+\.[a-z]+\.com", "java@mail.example.com"))
print(re.match("[\+\.\-\w]+\@[a-z]+[\.\-a-z]*[a-z]+\.com", "java@mail.example.com"))
print(re.match("[\+\.\-\w]+\@[a-z]+[\.\-a-z]*[a-z]+\.+[info]+|[co\.kr]+", "java@example.info"))
print(re.search("\.+[infocomco\.kr]+$", "java@example.."))
#Q.세 조건 중 하나는 반드시 만족하는 식은 정규식에 어떻게 표현하나요?(ex뒤에 info 또는 com 또는 co.kr로 끝나도록)
#Q.문자열이 맨 뒤에 오는지 판단할 때 $는 *처럼 바로 앞 문자열만 적용되나요? 아니면 전체문자열인가요? 일부라면대괄호로 [123[abc]*]$와 같이 표현 가능한가요?

import re
emails=[
'java@mail.example.com',        # 올바른 형식
'java+kr@example.com',          # 올바른 형식
'java-jsp@example.co.kr',       # 올바른 형식
'java_10@example.info',         # 올바른 형식
'java.jsp@e-xample.com',        # 올바른 형식
'@example.com',   # 잘못된 형식
'java@example',   # 잘못된 형식
'java@example-com',
       '추가1as@-.',
'추가2java@aaa.']

for e in emails:
    ans = re.match("[\+\.\-\w]+\@[a-z]+[\.\-a-z]*[a-z]+", e)
    ans2 =re.search("\.+[infocomco\.kr]+$", e)
    if ans !=None and ans2 !=None:
        print(True)
    else:
        print(False)



