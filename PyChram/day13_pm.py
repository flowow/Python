#rnn-Istm:시계열 자료->예측
#시계열:DateTimeIndex 자료형
import pandas as pd
import numpy as np
datestr=["2019, 1, 17","2019, 1, 20","2019, 1, 23","2019, 1, 26"]
#날짜 데이터를 어떻게 행으로 만들 수 있을까?to_datetime()
idx=pd.to_datetime(datestr) #날짜/시간 문자열 데이터->datetime 자료형 변환
print(idx)
s=pd.Series(np.random.randn(4), index=idx)
print(s)
#2.날짜 추가 방법?
print(pd.date_range("2019-1-1","2019-1-17"))
#3.periods는 출력하고 싶은 데이터 크기, W는 일요일,B는 평일, H:시간, T:분, s:초
print(pd.date_range("2019-1-1", periods=30, freq='W'))

#shift:인덱스는 고정, 데이터는 이동
ts=pd.Series(np.random.randn(4), index=pd.date_range("2019-1-17",periods=4,freq="M"))
print(ts)
#4.데이터를 한 칸씩 아래로 이동하고 싶다
print(ts.shift(1))
#반대로 위로 이동
print(ts.shift(-1))

import matplotlib as mpl
import matplotlib.pylab as plt
# x=np.linspace(-np.pi,np.pi, 256) #시작점과 끝점 사이에 256개
# print(x)
# c=np.cos(x)
# plt.plot(x,c)
# plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
# plt.yticks([-1,0,1])
# print(c)
# plt.show()

# t=np.arange(0.,5.,0.2)
# plt.title("여러개 선 그리기")
# #(x,y,스타일, x1,y1,스타일
# plt.plot(t,t,'r--',t,0.5 * t**2, 'bs:' ,t,0.2*t**3,'g^-')
# plt.show()

# x=np.linspace(-np.pi,np.pi, 256)
# c,s=np.cos(x),np.sin(x)
# plt.plot(x,c, ls="--",label="cosine")
# plt.plot(x,s, ls=":",label="sine")
# plt.legend(loc=2)
# plt.title("Plot")
# plt.xlabel("time")
# plt.ylabel("amplitude")
# plt.show()
#Figure 1개에는 적어도 1개 이상의 Axes가 존재
#Axes(그려진 그래프라고 생각) 1개에는 두 개 이상의 Axis(가로축, 세로축)이 존재

#플롯을 작성하면 자동으로 figure가 생성됨
f1=plt.figure(figsize=(10,2)) #그림을 출력할 종이를 생성 figure는 눈에 보이지 않는 틀
plt.title("My figure")
plt.plot(np.random.randn(100))
plt.show()

print(plt.gcf())# 현재 사용되고 있는 figure객체 출력
print(id(f1))

#figure 1개에 여러 개의 플롯을 출력:subplot함수
x1=np.linspace(0.0, 5.0)
x2=np.linspace(0.0, 2.0)
y1=np.cos(2*np.pi*x1)*np.exp(-x1)
y2=np.cos(2*np.pi*x2)
print(len(x1))
print(x1)

ax1=plt.subplot(2,1,1) #2행 1열 위
plt.plot(x1,y1,'yo-')
plt.title('2 subplot')
plt.ylabel('y axis')
ax1=plt.subplot(2,1,2)
plt.plot(x2,y2,'r.-')
plt.title('x axis')
plt.ylabel('y axis')
plt.show()

