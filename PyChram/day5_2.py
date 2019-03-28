import re
            #a{3}: a가 3개 있는가(aaa로 시작하는가)?
print(re.match("a{3}","aaabbbccc"))
print(re.match("a{3}","bbbaaaccc"))
print(re.match("a{3}","aaaaaccc"))
            #\d{6} ---> 0-9의 숫자 6개

print(re.match("hellohi","hello")) #none
print(re.match("hihi","hi")) #none
print(re.match("(hi){2}","hihi7"))
print(re.match("(hi){2}","hihi7"))

print(re.match("[0-9]{2}", "010"))
print(re.match("[0-9]{2}-", "010-"))
print(re.match("[0-9]{3}-", "010-"))
            #span이 중요한 게 아니라 매치가 됐느냐 안됐느냐?의 여부
#           none이 아니면 True if문과 연결됨

tel1="010-7445-0094"
tel2="032-272-0986"
tel3="010-23-12345" #이 경우에도 올바른 형식으로 나옴 따라서 오류수정 필요

#ex)숫자3-숫4-숫4인 경우메나 올바른 전화번호 형식
#res=re.match("\d{3}-\d{4}-\d{4}", tel1)
res= re.match("[0-9]{3}-[0-9]{4}-[0-9]{4}", tel1)
#            [0-9]{2,3}: 숫자가 2개 이상 3개 이하
res2= re.match("[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}", tel3) #--->None
#res=re.match("\d{3}-\d{4}-\d{4}", tel2)
if res2==None:
    print("잘못된 형식")
else:
    print("올바른 전화번호 형식")

print(re.match("[a-z]","hellohi1234"))
print(re.match("[a-z]*","hellohi1234"))
print(re.match("[a-z]+","heLlohi1234"))
print(re.match("[a-zA-Z]+","heLlohi1234"))
print(re.match("[a-zA-Z]+","heLlo7hi1234"))
print(re.match("[a-zA-Z0-9]+","heLlo7hi1234")) #영문대소문자와 숫자포함

print(re.match("[가-힣]", "안녕")) #모든 글자 포함
print(re.match("[가-힣]+", "안녕")) # + 는 한 글자 이상
print(re.match("[가-힣]", "안녕. 뭐해?")) #온점은 ㄴㄴ
print(re.match("[가-힣]", "안녕ㅋㄷ")) #자모음도 ㄴㄴ
print(re.match("[A-Z]+","Hello"))
print(re.match("[^A-Z]+","Hello"))#None
print(re.match("[^A-Z]+","888Hello"))
            # ^가 []내에 있을시: 'not'을 의미.
            # ^   []바깥       : '~로 시작'(하는지 여부 알고싶을 때)
print(re.match("^[A-Z]+","Hello"))
            # $: '~로 끝'(나는지 여부)
print(re.search("[0-9]+$","asdf3455"))
            # 특수문자가 패턴의 대상 자체로 삼고 싶으면 re.search("*+"~~))
            # 특수 문자 앞에 \(역슬래시) 추가
print(re.search("\*+","3**8")) #3**8:3의 8제곱
            #search가 전체 인덱스에서 match를 찾음 그에 비해 match는 1st index 탐색
print(re.match("\*+","3**8"))
print(pow(3,8))
print(re.match("\d+","12a3"))
print(re.match("\D+","12a3")) #숫자가 아닌 것
print(re.match("\D+","a12a3"))
print(re.match("\w+","hello_123")) #문자,숫자,_(언더바)
print(re.match("\W+","hello_123")) #제외한 게 한 글자 이상==[^\w]
print(re.match("\W+","(#:)"))
print(re.match("[a-zA-Z0-9]+","hi hello kpc 1234"))
print(re.match("[a-z A-Z0-9]+","hi hello kpc 1234")) #공백match방법1-대괄호 내에 공백문자 포함(위치상관ㄴ)
print(re.match("[a-zA-Z0-9\s]+","hi hello kpc 1234")) # \s: 스페이스
            #동일한 패턴이 반복될 경우 정규식을 저장해놓고 사용하는 게 효율적
print(re.match("[0-9]+","234abd456"))
            #패턴 저장
p=re.compile("[0-9]")
p.match("123")
p.match("987")
print(p.match("4abd45"))

print(re.match("do{3}g","dog"))#None
print(re.match("do{3}g","dooog"))
print(re.match("do{2,4}g","dog"))
print(re.match("do{2,4}g","doog"))
print(re.match("do{2,4}","dooooog"))

print(re.match("k.c", "kpc")) #매치됨
print(re.match("k[.]c","kpc")) #none: [.]는 실제점을 의미
print(re.match("kp?c","kpc"))# ?:앞의 p문자가 있어도 되고 없어도 됨
print(re.match("kp?c","kc"))
###########################그룹 관련 정규식: 패턴 내부 정규식을
#                           괄호로 묶어주면 괄호로 묶인 부분이 그룹이 됨
g=re.match("([0-9]+) ([0-9]+)","100 200")#그룹 2개
print(g)
g5=re.match("([0-9]+) ([0-9]+)","100 200")#그룹 2개
print(g5)
print(g5.group())#print(g5.group(0))과 동일 --->100 200
print(g5.group(1))#--->100
print(g5.group(2))
print(g5.groups()) #tuple로 출력 --->('100', '200')
            #그룹 이름: 그룹을 구분하기 위해 사용
#           그룹 이름 형식: (?P<그룹이름>)
g=re.match("(?P<func>[a-z][a-zA-Z0-9_]+)"   #그룹1
           "\((?P<arg>\w+)\)","hello(123)") #그룹1 \(->소괄호인 (표현을 위해
print(g.group('func'))
print(g.group('arg'))

#re.findall("패턴식", "문자열") :패턴에 매칭된 모든 문자열을 리스트로 반환
print(re.findall("[0-9]+","100 200 thr 300"))

            #문자열 데이터를 바꾸기
            #대화 data('대한민국'을 '한국'으로 치환)
            #챗봇을 제작해야하는 상황에서 데이터(대화) 치환 #데이터 다다익선
            #만약 '토지' 소설 데이터 챗봇과 '어린왕자' 소설 데이터가 대화 나눈다면?
            # 컴퓨터는 영화 이해ㄴㄴ 0,1만
            #같은 의미를 가지는 모든 텍스트들을 일관되게 바꿔줘야 한다(동의어 처리)
re.sub("패턴","대체해 들어가는 new 문자열","문자열") #:문자열이 패턴에 매칭되면 바꿀문자열로 바꿔라
print(re.sub("kpc|ml|dl","301","kpc ai dl ml"))





