#데이터프레임, 시리즈
import pandas as pd
from pandas import Series
from pandas import DataFrame
#axis=1 좌우합치기, default: 0
#pd.concat함수 이용해 df간 합치기, df와 시리즈간 합치기(드물다)
#중요한 건 결측값 처리
df1=pd.DataFrame({'a':['a1','a2','a3'],
'b':['b1','b2','b3'],
'c':['c1','c2','c3'],
'd':['d1','d2','d3']
              }, index=[0,1,2])
s1=pd.Series(['e1','e2','e3'],name='e')
print(df1)
print(s1)
print(pd.concat([df1,s1],axis=1))
print(pd.concat([df1,s1],axis=1, ignore_index=True))

s1=pd.Series(['e1','e2','e3'],name='e')
s2=pd.Series([1,2,3],name='f')
s3=pd.Series([10,20,30],name='g')
s12=pd.concat([s1,s2],axis=1)
print(s12)
print(type(s12))
s123=pd.concat([s3,s1,s2],axis=1, keys=['k1','k2','k3'])
print(s123)


df1=pd.DataFrame({'a':['a1','a2','a3'],
'b':['b1','b2','b3'],
'c':['c1','c2','c3'],
'd':['d1','d2','d3']
              }, index=[0,1,2])
s1=pd.Series(['e1','e2','e3','e4'],index=['a','b','c','d'])
print(df1)
print(s1)
print(df1.append(s1, ignore_index=True))

            #결측값: NaN
df1=DataFrame({'k':['k0','k1','k2','k3'],
's':['s0','s1','s2','s3'],
#'e':['k0','k1','k2','k3'],
'num':[1.6,2.3,4.5,6.54],       })
df2=DataFrame({'k':['k2','k3','k4','k5'],
'j':['j2','j3','j4','j5'],
'i':['i3','i3','i4','i5'],
#'num':[1.6,2.3,4.5,6.54],
})
newDf=pd.merge(df1,df2,how='outer',on='k')
print(newDf)
# print(newDf.isnull(),sum()) #열 단위
# print(pd.isnull(newDf).sum())#결측값에 대해->True
# print(newDf.isnull())
# print(pd.notnull(newDf))#결측값->False
# print(newDf.notnull().sum())
# print(newDf['num'].isnull().sum())

# print(newDf)
# print(newDf.ix[[0,1]])
# print(newDf.ix[[0,1],['k','s']])

# newDf.ix[[0,1],['k','s']]=None
# print(newDf.isnull(),sum(1)) #행 단위
newDf['count']=newDf.isnull().sum(1)
print(newDf)
# 'ncount'

import numpy as np
df2=DataFrame(np.arange(15).reshape(5,3), index=['a','b','c','d','e'],columns=['c1','c2','c3'])
print(df2.shape)
print(df2)

df2.ix[['b','d'],['c1']]=None
print(df2)
print(df2.sum())
print(df2['c1'].sum()) #R등과 다르게 NaN데이터 포함돼도 결과 나옴
print(df2['c2'].cumsum()) #누적합
print(df2.mean())
print(df2.mean(1))
print(df2['c3'].mean())
print(df2.std(1))

# df3=DataFrame(np.arange(15).reshape(5,3), index=['a','b','c','d','e'],columns=['c','f','e'])
# print(df3.sum()) #열의 합
# print(df3.sum(1)) #행의 합

print(df2)
df2['res']=df2['c1']*df2['c2'] #NaN이 한쪽에라도 있으면 0으로 만든다
print(df2)

import numpy as np
print(np.__version__)
arr=[1,2,3]
a=np.array(arr)
print(a) # array가 생성됨

arr=[(1,2,3),(4,5,6)]
a=np.array(arr, dtype=float)
print(a)
print(type(a))

#zeros 함수-모두 0(float)으로 초기화
a=np.zeros((3,4))
print(a)
#ones 함수-모두 1(float)로 초기화
a=np.ones((2,3,4), dtype=np.int16) #제일 안쪽에 있는[1 1 1 1]이 3개 모여있고 이 덩어리가 두 개
print(a)
#3X4를 모두 5로 초기화
a=np.full((3,4),5)
print(a)

a=np.eye(5)
print(a)

#like함수:지정한 배열과 모양이 같은 행렬을 만들 수 있음
a=np.array([[1,2,3],[4,5,6]]) #--->a는 (2,3)행렬
print(a)
a2=np.ones_like(1)
print(a2)
a=np.linspace(0,1,5) #0부터 1사이에 5개를 균등 간격으로
print(a)
import matplotlib.pyplot as plt
# plt.plot(a,'o')
# plt.show()
a=np.arange(0,10,2, np.float)
print(a)
# plt.plot(a,'o')
# plt.show()

            #numpy.random 모듈 - 난수 배열
    # 1. normal함수:정규분포확률밀도에서 표본 추출
mean=0
std=1
a=np.random.normal(mean,std, (2,3))
print(a)
data=np.random.normal(0,1,10000)

# plt.hist(data,bins=500) #bins:구간의 개수
# plt.show()
    # 2. rand함수: 균등한 비율로 0~1 사이 표본 추출
a=np.random.rand(3,2)
print(a)

np.random.randn(10000)
# plt.hist(data, bins=10)
# plt.show()
    #randint:정수 표본 추출(별로 많이 안쓰임)
a=np.random.randint(5,10,size=(2,4)) #5~9까지 정수 난수 생성
print(a)
    #random함수:0~1사이의 균등분포 난수 생성
print(np.random.random((2,4)))

#seed: 난수를 생성하기 위한 base
#random 모듈의 모든 함수는 실행시마다 랜덤값 발생
np.random.seed(778888) #변하지 않는 난수 생성시 사용
print(np.random.random((2,2)))
print(np.random.randint(0,10, (2,3)))

import pandas as pd
df3=pd.DataFrame(np.random.randn(5,3),
             columns=['c1','c2','c3'])
print(df3)
#np.nan: numpy 결측값 상수
df3.ix[4,'c3']=np.nan #->행과 열 지정으로 각 값 nan으로
df3.ix[3,'c2']=np.nan
df3.ix[1,['c1','c3']]=np.nan #->2개 이상은 대괄호로 묶어주기
print(df3)

#결측값을 모두 0으로 대체->df4라는 데이터프레임 이름으로 저장
df4=df3.fillna(0)
print(df4)
#결측값->"누락"
df5=df3.fillna("누락")
print(df5)

print(df3)
print('='*50)
df6=df3.fillna(method='ffill', limit=1) #limit: NaN이 연속될 때 대체할 NaN의 수
print(df6)
#결측값을 각 컬럼의 평균값으로 대체
print(df3.mean())
df7=df3.fillna(df3.mean())
print(df7)
#결측값을 'c2'열  평균값으로
#df8=df3.fillna(df3.mean('c2')) wrong
df8=df3.fillna(df3.mean()['c2'])
print(df8)

print(df3.mean()['c1':'c3'])
df9=df3.fillna(df3.mean()['c2':'c3'])
print(df9) #-->c1열은 그대로 NaN

#(조건,참,거짓)
df3['new']=np.where(pd.notnull(df3['c2'])==True, df3['c2'], df3['c1'])
#null이 아니면
print(df3)

