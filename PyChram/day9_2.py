import numpy as np
import pandas as pd
from pandas import DataFrame as df
# df=DataFrame()
myDf=df({'num1':np.arange(5),
         'num2':np.random.randn(5)},
         index=['a1','a2','a3','a4','a5']
)
print(myDf)

newIndex=['a2','b3','r5','f3','s4']
            #reindex!index 재정의
            #reindex를 수행하면 기존 동일한 index에 해당하는 값은 동일 출력,
#            if not 새롭게 생성 및 NaN으로 채워짐 #인덱스 지정 시에도 사용 가능
#print(myDf=myDf.reindex(newIndex))
print(myDf)
            #reindex 지정해주기
print(myDf.reindex(newIndex, fill_value=0))
print(myDf.reindex(newIndex, fill_value='없음')) #영문으로 쓰는 게 바람직
            #시계열 데이터!
#날짜나 시간이 누락되어 임의 추가해서 재구성해서 시계열 데이터 생성할 수 있다.
print(pd.date_range('01/11/2019',periods=7,freq='D'))
dIndex=pd.date_range('01/11/2019',periods=3,freq='D')
df2=df({'d1':[1,2,3]}, index=dIndex)
print(df2)
print("="*50)
myDf3=pd.date_range("1/5/2019",periods=14)
print(myDf3)
print(df2.reindex(myDf3)) #reindex 해서 생긴 NaN 어떻게? method!
print("="*50)
print(df2.reindex(myDf3, method='ffill')) #method: 어떤 방향으로 결측값을 채울 것인가? 바로 이전 값을 취함
print(df2.reindex(myDf3, method='bfill')) #backward 거꾸로 채워지는 method: 'bfill'

#concat함수: 여러 개의 데이터를 합치는 작업 수행 ex날짜가 같은 것들만 묶기
#pd.concat()
"""
#objs:합치고자 하는 대상 데이터
#axis:좌우로 합칠 수도 있고 위아래(0)로 합칠 수도 있음 보통 0또는 1
join: 교집합(inner), 합집합(outer)
"""
df1=df({"a":["a1","a2","a3"],
"b":["b1","b2","b3"],
"c":["c1","c2","c3"],
"d":["d1","d2","d3"]})
print(df1)
df2=df({"a":["a11","a12","a13"],
"b":["b11","b12","b13"],
"c":["c11","c12","c13"],
"d":["d11","d12","d13"]}, index=[5,6,7])
print(df2)



print(pd.concat([df1,df2],axis=1))
print(pd.concat([df1,df2]))

df3=df({"e":["a6","a7","a8"],
"f":["b6","b7","b8"],
"g":["c6","c7","c8"],
"h":["d6","d7","d8"]})
#axis=1, df1,df3합쳐 df13으로
df13=pd.concat([df1,df3],axis=1)
print(df13)

            #join(연결, pd.concat()이용)<->normalization(정규화)
#연결:데이터프레임 2개를 합쳐서 1개의 데이터프레임 생성
#join속성을 이용해 다양한 방식으로 연결 가능
df4=df({"a":["a1","a2","a3"],
"b":["b1","b2","b3"],
"c":["c1","c2","c3"],
"e":["e1","e2","e3"]}, index=[0,1,3])
print(df4)
df14=pd.concat([df1,df4], join='outer') #default:outer 합집합으로 합쳐진다
print(df4)
df14_inner=pd.concat([df1,df4], join='inner')
print(df14_inner)

df1=df({"a":["a1","a2","a3"],
"b":["b1","b2","b3"],
"c":["c1","c2","c3"],
"d":["d1","d2","d3"]})
df4=df({"a":["a1","a2","a3"],
"b":["b1","b2","b3"],
"c":["c1","c2","c3"],
"e":["e1","e2","e3"]}, index=[0,1,3])
df14_axis1=pd.concat([df1,df4],axis=1)
print(df14_axis1)
df14_axis1_inner=pd.concat([df1,df4],axis=1,join='inner')
print(df14_axis1_inner) #->교집합

#join_axes -> 여기서 해당 df는 살려라
df14_axes=pd.concat([df1,df4],axis=1,join_axes=[df4.index])
print(df14_axes)

#->두 df는 a,b,c,d로 column동일
df5=df({"a":["a1","a2","a3"],
"b":["b1","b2","b3"],
"c":["c1","c2","c3"],
"d":["d1","d2","d3"]}, index=['row1','row2','row3'])

df6=df({"a":["a4","a5","a6"],
"b":["b4","b5","b6"],
"c":["c4","c5","c6"],
"d":["d4","d5","d6"]}, index=['row4','row5','row6'])
#합칠 때 인덱스 날리고싶을 때
df56=pd.concat([df5,df6], ignore_index=False) #False가 default
print(df56)
df56=pd.concat([df5,df6], ignore_index=True) #->두 df는 a,b,c,d로 column동일
print(df56)

import numpy as np
a=np.array([1,3,5]) #기본이 array /파이썬의 리스트를 넘파이의 array함수에
# 넣으면 n차원 배열(array)이 됩니다
a2=[1,3,5]
print(type(a))
print(type(a2))
print(a2)# ->그대로 나옴 컴마 존재

b=np.arange(7)
print(b) #[0 1 2~]->list아니라 array임
print(b<4) #->파이썬에서는 for문으로 출력해야하는데 np는 바로 나옴 시간복잡도 goooood
c=np.arange(3,7,0.1)
print(c)
