import pandas as pd
import numpy as np
s=pd.Series(range(10,20))
s[3]=np.nan
print(s)
print(s.count()) #Nan을 제외한 데이터 개수

print("="*50)
np.random.seed(2)
df=pd.DataFrame(np.random.randint(5, size=(4,4)), dtype=float)
df.iloc[2,3]=np.nan
print(df)
print(df.count())

import seaborn as sns
titanic=sns.load_dataset("titanic")
print(titanic)
print(titanic[:])

s2=pd.Series(np.random.randint(6, size=100))
print(s2.tail())
print(s2.value_counts())#value_counts함수는 시리즈에서만 사용
df=pd.DataFrame(np.random.randint(5, size=(4,4)), dtype=float)
print(df)
print(df[0].value_counts())
#데이터프레임에서는 각각의 열(시리즈) 단위로 value_counts를 적용
print("각 데이터 개수",df.count())

# sort_index:인덱스를 기준으로 정렬
# sort_values:값을 기준으로 정렬
print(s2.value_counts())
print(s2.value_counts().sort_index())
print(s2.value_counts().sort_values())
s=pd.Series(range(10,20))
s[3]=np.nan
print(s.sort_values(ascending=False))#Nan이 있는 경우에는 맨 뒤로 정렬됨
print(df)
print(df.sort_values(by=1))#1번 열 인덱스 값 기준 오름차순정렬
print(df.sort_values(by=[1,3]))




















