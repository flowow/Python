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
        print(True,end=' ')
    else:
        print(False,end=' ')

import re
p=re.compile("^[a-zA-Z+-.0-9]+@[a-zA-Z0-9-.]+\.["    @)
#계정@도메인.최상위도메인
for mail in emails:
    print(p.match(mail)!=None, end=" ")
