import numpy as np
import pandas as pd
np.random.seed(1)
df=pd.DataFrame(np.random.randint(10, size=(4,8)))
print(df)
print(df.sum(axis=1))
df["RowSum"]=df.sum(axis=1)
print(df)
print(df.sum(axis=0))
print(df.sum())#디폴트 axis=0(열 합계)
#각각의 열 합계를 구한 다음 'ColTotal'이름으로 새로운 줄을 추가
#(loc인덱서 사용)
df.loc["ColTotal",:]=df.sum()
print(df)

#apply함수: 행 또는 열 단위로 처리
df2=pd.DataFrame({
    'A':[1,3,5,2,4],
    'B':[2,3,7,1,3],
    'C':[2,4,5,2,4] })
print(df2)
#각 열에 대한 최대값 - 최소값
print(df2.apply(lambda  x:x.max() - x.min(), axis=1))
#데이터프레임에 람다 함수를 적용해라
#데이터프레임의 각각의 열이 x에 전달->각 열 최대값-각 열 최소값
#axis=1은 행, axis=0은 default로서 열 단위로 수행
print("="*50)
print(df2)
# df2=df2.apply(pd.value_counts)
# print(df2)
#value_counts:각 열에대해 어떤 값이 얼마나 사용되었는지를 세는함수
print(df2.apply(pd.value_counts))

#NaN값 fillna 메서드를 이용해 원하는 값으로 변경
print(df2.apply(pd.value_counts).fillna(0).astype(int))
#float 타입이 int 타입으로 변환

#실수 데이터의 크기를 기준으로 카테고리 값을 변환
ages=[0,2,10,21,23,37,31,61,20,41,32,100]
bins=[1,15,25,35,60,99] #구간
labels=["미성년자", "청년", "중년", "장년", "노년"]
#cut함수 : 실수값을 카테고리로 변환
cats=pd.cut(ages, bins, labels=labels)
print(cats)
print(cats.categories)
print(cats.codes)

data=np.random.randn(1000)
print(data)
cats=pd.qcut(data, 4, labels=["Q1","Q2","Q3","Q4"])
print(cats)
print(pd.value_counts(cats))

print(type(list('ABCDE')))
print(np.round(np.random.rand(3,5), 2)) #2는 소수 몇째자리까지 나타낼지
print(np.vstack([list('ABCDE'),
                 np.round(np.random.rand(3,5), 2)]).T)

df1=pd.DataFrame(np.vstack([list('ABCDE'),
                 np.round(np.random.rand(3,5), 2)]).T,
                 columns=["C1","C2","C3","C4"])
print(df1)
#인덱스 지정! set_index()
df2=df1.set_index("C1")
print(df2)
df3=df2.set_index("C2")
print(df3)

#다중인덱스:행, 열이 여러 계층으로 구성

df3=pd.DataFrame(
    np.round(np.random.randn(5,4),2),
    columns=[["A","A","B","B"],
             ["C1","C2","C1","C2"]]
)
print(df3)
df3.columns.names=["Cidx1", "Cidx2"]
print(df3)
df4=pd.DataFrame(
    np.round(np.random.randn(6,4),2),
    columns=[["A","A","B","B"],
             ["C1","C2","C1","C2"]],
    # index=[["M","M","M","F","F","F"],
    # ["R1","R2","R3","R1","R2","R3"]]
    index=[["M","M","M","F","F","F"],
     ["R"+str(i+1) for i in range(3)]*2]
)
print(df4)
df4.columns.names=["Cindex1","Cindex2"]
df4.index.names=["Rindex1","Rindex2"]
print(df4)
#데이터프레임 stack():열 인덱스->행 인덱스 변환,
# unstack():행 인덱스->열 인덱스 변환
print("="*50)
print(df4.stack("Cindex1"))
print("="*50)
print(df4)
print("="*50)
print(df4.unstack("Rindex2"))

df3.columns.names=["Cidx1","Cidx2"]
print(df3)
#다중 인덱스 경우에는 ()로 인덱싱을 해야 함
print(df3[("B","C1")]) #열 전체 추출
print(df3.loc[0,("B","C1")])
df3.loc[0,("B","C1")]=10
print(df3)

#merge  데이터병합
#두 개 데이터프레임-> 공통 열 or 인덱스 기준(key)으로 합치기
df1=pd.DataFrame({
    '고객번호':[1001,1002,1003,1004,1005,1006,1007],
    '이름':['둘리', '도우너','또치','길동','희동',
          '마이콜','영희']
},columns=['고객번호', '이름'])
print(df1)
df2=pd.DataFrame({
    '고객번호':[1001,1001,1005,1006,1008,1001],
    '금액':[100, 200, 150, 50, 100, 300]
}, columns=['고객번호', '금액'])
#공통으로 존재하는 열인 고객번호를 기준으로 병합
#inner join:교집합, outer join:합집합
#inner join이 디폴트
print(pd.merge(df1,df2))
print("-"*50)
print(pd.merge(df1,df2, how='outer')) #합집합
###############################키가 중복될때 어떤 것을 기준으로 삼을 것인가
print(pd.merge(df1,df2, how='left'))#df1의 키값을 모두 보여줌
print("-"*50)
print(pd.merge(df1,df2, how='right'))#df2의 키값을 모두 보여줌

###테이블 키 값이 같은 데이터가 여러개 있는 경우에 대한 조합
df1=pd.DataFrame({
    '품종':['setosa','setosa','virginica','virginica'],
    '꽃잎길이':[1.4,1.3,1.5,1.3]
},columns=['품종', '꽃잎길이'])
df2=pd.DataFrame({
    '품종':['setosa','virginica','virginica', 'versicolor'],
    '꽃잎너비':[0.4,0.3,0.5,0.3]
},columns=['품종', '꽃잎너비'])
print(pd.merge(df1,df2))
# #이름이 같은 열이 키가 된다.
# #이름은 같지만 키가 안됐으면 좋겠다? on인수로 키의 기준열을 지정



df5=pd.DataFrame({
    '이름':['영희','철수','철수'],
    '성적':[1,2,3]
})
df6=pd.DataFrame({
    '성명':['영희','영희','철수'],
    '성적':[4,5,6]
})
print(pd.merge(df5,df6, left_on='이름',right_on='성명'))
# print(pd.merge(df5,df6, left_on='성명',right_on='성명'))