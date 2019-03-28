#데이터프레임을 파일로 저장

import pandas as pd
import numpy as np
from pandas import DataFrame as df #pd에서 data가져오겠다
# 혹은 이 줄이 없다면 DataFrame 사용시 pd.DataFrame으로 명시해주면 된다 but 불편해서 걍 import,
# DataFrame도 pd처럼 as df등으로 닉네임 줄 수 잇다

#용이한 데이터분석을 위해
            #!!!딕셔너리(파이썬의 자료구조) -> 데이터 프레임(판다스 자려구조) 생성!!
            #python->pandas
            #딕셔너리의 key들이 dataframe에서 column으로, 값들이 행벡터와 열벡터로
data={
#    'id':['a1','b1'] or {'addr':'incheon'}등의 리스트,딕셔너리 형태도 가능
     'id':['id1','id2','id3'],
    'x':['x1','x2','x3'],
    'y':[10,20,30] }
print(data) #for문에서는 들여쓰기 중요하지만 딕셔너리같은 자료구조는 상관없음 보기 안 좋을뿐
#Code>auto_indent line하면 자동 줄정리
#python으로 시각화할 수 있지만 코딩이 너무 어려움 그래서 시각화 패키지를 이용하고
#(통계분석을 위한)pandas패키지를 이용하는 것임돠

"""
최고의 교재는 기본사이트!
https://matplotlib.org/:
http://www.numpy.org/:빠른 행렬연산, 수치해석(처리)
http://pandas.pydata.org/pandas-docs/stable/:데이터분석 도구 집합소
"""

# df=DataFrame(data)
# print(df)
#
# df=DataFrame(data, index=['20191','20192','20193'])#index의 크기는 데이터와 맞아야 한다
# print(df)
# df2=df.reindex(['20191','20192','20193','20194'])#--->NaN:결측치(값 누락), 딥러닝에서는 오류를 의미
# print(df2)
# #csv파일 만들기, NaN처리 na_rep, sep는 구분자, header(첫번째 줄)=True가 기본값
# df2.to_csv("df2.csv", na_rep="NaN", sep=",",header=False)

#데이터프레임 작성 -> 속성 확인

# myDf1=df()#데이터프레임을 생성하고 myDf1에 저장, 생성자메서드 호출. 객체를 만들어 왼쪽에 대입하라
# print(myDf1)
# print(type(myDf1)) # df는 만들어졌지만 아직 empty

# myDf1=df(data=np.arange(2,10).reshape(2,4)) #range와 비슷. arange(6)은 0~5까지 df 생성,
# 여기서 속성은 data하나, 속성과 속성은 컴마로 연결
#index와 colums 속성 추가!
myDf1=df(data=np.arange(2,10).reshape(2,4),
         index=['c1','c2'],
         columns=['s1','s2','s3','s4'])
#객체.메서드가 하나의 객체로 인식되고 뒤에 다른 메서드가 올 수 있다
# 1열-자동 인덱스,2열-생성된 데이터
print(myDf1)


            #전치행렬(transpose matrix): 행렬의 행/열을 뒤바꾼 행렬 .T
print(myDf1.T)
#axis(축), axes(모든 축)
print(myDf1.axes) #행과 열의 이름 출력
print(myDf1.dtypes) #데이터 형태 출력
print(myDf1.shape) #!자주 사용! 데이터프레임 모양(2,4)
print(myDf1.size) #데이터 개수
print(myDf1) #데이터프레임 모습으로 출력
print(myDf1.values) #데이터를 numpy형태(행렬)로 출력

            #따로 dict지정 필요 없이 바로 딕셔너리 df에서 넣어줘서 df만들 수도 있다.
            #DataFrame(x)
myDf2=df({
    'category':['a','b','a','b','c'],
    'num1':np.arange(5,10),
    'num2':np.random.randn(5) #randn(normal distibution)표준정규분포따르는 난수함수
}, index=['행0', '행1', '행2', '행3', '행4']) #->index앞 {}는 data를 의미!
print(myDf2) #->category열벡터, num1벡터,

            #데이터를 특정 행 또는 열(feature) 단위로 추출할 수 있어야 함-slicing이 중요한 이유
print(myDf2.index)
print(myDf2.ix[2]) #세번째 행 뽑고싶다?index[]는 0부터 시작하니까 ix[2]!특정 행 추출!
print(myDf2.ix[2:]) #ix[2]부터 마지막 행까지
print(myDf2.ix['행2']) #row이름을 직접 입력해도 ㅇㅋ
            ##df.head()상위부터 추출 <-> df.tail(): 하위부터
print(myDf2.head(3))
print(myDf2.tail(2))
            ##열벡터 추출: '컬럼의 이름'
print(myDf2.columns) #--->Index(['category', 'num1', 'num2'], dtype='object')
print(myDf2['num1']) #num1 열벡터 추출(대괄호 한 쌍)
print(myDf2[['category','num2']]) #2개 이상은 행렬형태이기에 다시 []로 묶어주긔
            #(+)만약 시험을 못 본 학생의 시험점수를 어떻게 처리할 것인가?


#데이터전처리, 데이터차원축소

