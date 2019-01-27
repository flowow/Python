import numpy as np
import pandas as pd
df=pd.read_excel('score.xlsx')
# print(df)

#과제1. 총점과 평균 열 추가하기
# df[('총점','평균')]
df['총점']=df.loc[:,'kor':].sum(axis=1)
df['평균']=df.loc[:,'kor':'sci'].mean(axis=1)
# ####?한번에 선언하는 방법?
# print(df)

# # df=pd.DataFrame({df.mean(df.loc[:,'kor':]))
#과제2. 평균을 기준으로 내림차순 정렬 출력(1등부터)
df2=df.sort_values(by='평균', ascending=False)
print(df2)

#과제3. 내림차순 정렬된 데이터의 name필드 사용해 막대그래프 출력
import matplotlib as mpl
import matplotlib.pylab as plt
y=df2['평균']
x=df2['name']
ylabel=['평균']
xlabel=['name']
plt.title("name_mean")
plt.bar(x,y)
plt.show()

#과제4. 1반과 2반에 대한 총점과 평균을 구한 다음 어느 반이 더 잘했는지 출력
# df.loc['각반총점']=pd.DataFrame(df.loc['class'==1])
# df['1반총점'].apply(lambda x: df.loc['총점'].sum() if df.loc['class'==1] else 1)
sum1=df['총점'][:6].sum()
sum2=df['총점'][6:12].sum()

s1=df['class']
s2=s1.value_counts()

print('1반 총점은:' , sum1)
print('2반 총점은:' , sum2)
print('1반 평균은:', sum1/s2[1])
print('2반 평균은:', sum2/s2[2])
if sum1/s2[1]>sum2/s2[2]:
    print("1반이 성적이 더 우수")
else : print("2반이 성적이 더 우수")



# # df['평균']=df.loc[:,'kor':'sci'].mean(axis=1)
# # df.drop_duplicated(['1반총점'])
# print(df)
# # df.loc[:,'5'].sum('총점')
#
#
# #5. 전체 데이터를 막대그래프로 출력
# # -범례: kor,eng, mat, sci
# # -각 학생별 과목에 대한 세로 막대 그래프
# # df1=df(index=[])
# # y1=df['kor']
# # y2=df['eng']
# # y3=df['math']
# # y4=df['sci']
# # x=df['name']
# # ylabel=['score']
# # xlabel=['name']
# # plt.bar(x,y1)
# # plt.bar(x,y2,stacked=False)
# # plt.bar(x,y3,stacked=False)
# # plt.bar(x,y4,stacked=False)
# # plt.show()
#
# # ####Sol
df2=df.drop(['class','총점','평균'],1)
print(df2)
df2.plot('name',kind='bar')
plt.show()
#
# #6.과목별 상관도 출력
# #ex) mat & sci
# #ex) kor & eng
# # colors=['yellowgreen','gold','lightskyblue','lightcoral']
#
# #########sol
x=df['kor']
y1=df['sci']
y2=df['eng']
y3=df['math']
plt.scatter(x,y1, c='r')
plt.scatter(x,y2, c='purple') #국어와 영어
plt.scatter(x,y3, c='b')
plt.scatter(y1,y2, c='yellow')
plt.scatter(y1,y3, c='green') #수학과 과학
plt.scatter(y2,y3, c='coral')
plt.show()


