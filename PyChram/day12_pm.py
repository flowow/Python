import pandas as pd
import numpy as np
s=pd.Series(range(10,20))
print(s)
s[3]=np.nan #결측값
print(s)
print(s.count()) #NaN을 제외한 데이터 개수셀 때
print('-'*50)
np.random.seed(2)
df=pd.DataFrame(np.random.randint(5,size=(4,4)), dtype=float) #0~4범위
e=pd.DataFrame(np.random.randint(6,size=(2,5)),dtype=float)
df.iloc[2,3]=np.nan #np.nan np.nan
print(df)
print(df.count()) #->열에 대해서 데이터 개수!!!!!!!!!!!
print(e)

import seaborn as sns
titanic=sns.load_dataset("titanic")
print(titanic)
print(titanic[0:100])
s2=pd.Series(np.random.randint(6, size=100))
print(s2.tail()) #끝부분 5개 출력
print(s2.value_counts()) #value_counts()는 DF에서 사용불가,Series만 해당 값이 몇 번 나오는지? value_counts(hat)
#DF에서는 Series단위로 적용
#다음은 적용 예시
# 2    22
# 1    18
# 0    17
# 3    16
# 5    14
# 4    13
df=pd.DataFrame(np.random.randint(5,size=(4,4)), dtype=float)
print(df)
print(df[0].value_counts()) #->열 한개가 추출되면 Series임 즉 value_counts() 가능!
print(df.count())

#sort_index: 인덱스를 기준으로 정렬
#sort_values: 값을 기준으로 정렬
print(s2.value_counts().sort_values())
print(s2.value_counts().sort_values(ascending=False)) #내림차순
print(s.sort_values()) #NaN이 있는 경우 맨뒤로 정렬됨
print(df)
print(df.sort_values(by=1)) #1열 기준으로 행이 오름차순으로 정렬됨 ex수욜 기준으로 각 과자 섭취 횟수 오름차순 정렬
print(df.sort_values(by=[1,3])) #1열을 기준으로 하되 값이 같으면 3열이 먼저 나올 수 있도록 한다

