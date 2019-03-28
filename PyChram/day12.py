import pandas as pd
import numpy as np
            #데이터 읽어들일 때 옵션들
df=pd.read_csv("sample1.csv")
print(df) #column index c1~c3까지 존재
df=pd.read_csv("sample2.csv", names=['c1','c2','c3'])
print(df) # 열인덱스 사라졌지만 첫 행이 인덱스가 됨->names로 재정의
        #특정 열인덱스를 인덱스로 가지고 올 때->index_col
df=pd.read_csv("sample1.csv", index_col='c1')
print(df)

df=pd.read_csv("sample3.txt")
print(df)
# print(df['c1']) #print(df['c1']) #->csv가 아닌 파일들은 sep속성을 사용해 구분자 지정
# ->csv가 아닌 파일들은 sep속성을 사용해 구분자 지정
# read_table():txt파일을 읽을 때 사용
#sep='\s+' 공백문자가 1개 이상을 의미
df=pd.read_table("sample3.txt",sep='\s+')
print(df)
df=pd.read_table("sample4.txt",sep='\s+')
print(df)#NaN이 생긴 이유? 공백을 기준으로 5개의 컬럼으로 인식해서.
df=pd.read_table("sample4.txt",sep='\s+',skiprows=2) #두 줄 건너 뛰어라!!!!!!!!skiprows=2
print(df)
df=pd.read_csv("sample5.csv") # #로 시작해서 주석문으로 처리할 수 있음
print(df)
############################################na_values=['없음']
df=pd.read_csv("sample5.csv", na_values=['없음'])
############################################파일 생성
df.to_csv('sample6.csv')
df=pd.read_csv("sample6.csv") #컴마를 기준으로 읽는다, 데이터를 읽어들일 때마다 인덱스 생성됨 저장 시 고려!
print(df)
df.to_csv('sample7.txt',sep="|")
print("="*50)
df=pd.read_csv("sample1.csv")
print(df)
df.index=['a','b','c']
print(df)
df.to_csv('sanple9.csv',index=False, header=False)

#넷상에 존재하는 csv는 주소를 불러오면 된다
#titanic.csv 검색해서 raw 클릭 후 주소 복사, 구분자 파악해서 보기 좋게 정리
df=pd.read_csv("https://gist.githubusercontent.com/michhar/2dfd2de0d4f8727f873422c5d959fff5/"
               "raw/ff414a1bcfcba32481e4d4e8db578e55872a2ca1/titanic.csv",sep="\t")
#set_option 이용해서 큰 데이터->앞 뒤로 총 10개씩만 표현 가능
pd.set_option("display.max_rows",10)
print(df)
print(df.head(7)) #상위 7개(default는 5개)
print(df.tail()) #하위 5개만

print(df[['Survived', 'Fare']])
#추출 저장도 가능!
df2=df[['Survived']]
print(df2)

#데이터프레임 인덱서(인덱싱 하는 것)
#인덱싱이랑 내가 원하는 데이터만 선택 추출하는 것
# iloc, loc, at lat (pd에 있는 4 인덴서)
# iloc: 순서 기반 2차원 인덱싱
# loc: 라벨 기반 //
# at: 라벨값 기반 // 스칼라값 1개
# iat: 순서 기반 // //

################## 1. loc인덱서
df=pd.DataFrame(np.arange(1,13).reshape(3,-1),
                index=['a','v','x'],
                columns=['q','w','f','d'])
print(df)
print(df.loc['x','f']) #행인덱스 라벨:'x', 열인덱스 라벨:'f'
print('#'*50)
print(df.loc['a':,'f']) #f열 기준 a행부터 쭉
print(df.loc['a',:]) #a행기준 쭉
print(df.loc[['a','x'],['w','f']]) #참조하고 싶은 항목이 여러개이면 대괄호로 묶어준다!!!
print(df.loc[df.q>5,:])

print('='*50)
print(df.loc['a',:])
print(type(df.loc['a',:]))
print(df)
print(type(df[:1]))
print(df['q'])
print(df[:]) #전체

print('='*50)
print(df[:1])
# print(df[])
#df[:1]: a행

def select_rows(df):
    return df.q>3
print(select_rows(df))
#df의 q열 값이 3보다 큰 행에 대한 f열 값 추출
print(df.loc[select_rows(df),['f']])
print(df[:1]<=3)
# print(df.loc[:,df[:1]]) ->인덱싱 조건으로 데이터프레임이 아닌 시리즈가 사용되어야 함
print(type(df.loc['a':]<=3)) #->DF
print(df.loc['a',:]<=3) #->type: 시리즈
print(df.loc[:,df.loc['a',:]<=3])
#        loc[행  , True인 q,w,f열에 대해서만     ]
print(''*50)
print(df.loc['a'])
df.loc["e"]=[13,14,15,16]
print(df)

df2=pd.DataFrame(np.arange(10,26).reshape(4,4),
                 #########################np.arange(1,10,3)
                 columns=np.arange(1,8,2))
print(df2)
print(df2.loc[1,7]) #1행7열이 아니라 실제 저 값을 가지는 인덱스의 값

########### 2.iloc인덱서: 순서를 나타내는 정수 인덱스 사용
print(df)
print(df.iloc[0,1])
print(df.iloc[:2,2])
print(df.iloc[0,-2:]) #넘재밌다 생각한 대로 출력될 때!!!
print(df.iloc[2:3,1:3])
print(df.iloc[ -1 ]) #마지막 행
df.iloc[-1]=df.iloc[-1]*2
print(df)

#정리-->둘은 동일
print(df.loc['a','q'])
print(df.iloc[0,0])
#스칼라가
print(df.at['a','q'])
print(df.iat[0,0])