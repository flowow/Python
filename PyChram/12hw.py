"""
bins = [1, 15, 25, 35, 60, 99]
labels = ["미성년자", "청년", "중년", "장년", "노년"]
타이타닉호 승객을 사망자와 생존자 그룹으로 나누고 각 그룹에 대해
'미성년자', '청년', '중년', '장년', '노년' 승객의 비율을 구한다.
각 그룹 별로 비율의 전체 합은 1이 되어야 한다.
1.특정 값을 가진 데이터만 뽑아 그룹만들기
2.나이에 따라 라벨링한다
3.특정값의 비율을 구한다
"""
import numpy as np
import pandas as pd
import seaborn as sns

titanic=sns.load_dataset("titanic")
print(titanic)
notsur=titanic[titanic['survived']==0]
sur=titanic[titanic['survived']==1]
print(notsur)
print(notsur['age'].value_counts())
n_age=list(notsur['age'])
s_age=list(sur['age'])

bins = [1, 15, 25, 35, 60, 99]
labels = ["미성년자", "청년", "중년", "장년", "노년"]
casualty=pd.cut(n_age, bins, labels=labels)
print(casualty.value_counts()/len(casualty))
survivor=pd.cut(s_age, bins, labels=labels)
print(survivor.value_counts()/len(survivor))

# sur=pd.DataFrame.drop(pd.DataFrame[titanic.survived==0].index)
# print(sur)
# print(np.sort(titanic['survived']))
# print(titanic['age'].value_counts())
# ages=[]
# bins = [1, 15, 25, 35, 60, 99]
# labels = ["미성년자", "청년", "중년", "장년", "노년"]
# cats=pd.cut(ages, bins, labels=labels)
# print(cats)

