import numpy as np
import matplotlib as mpl
import matplotlib.pylab as plt
y=[2,3,1]
x=np.arange(len(y))
print(x)
xlabel=['x label']
error=np.random.rand(len(y))
plt.title("Bar Chart")
plt.barh(x,y, alpha=0.5,xerr=error) #alpha는 투명도, xerr:에러의 허용범위
plt.show()

#스템 플롯(폭이 없는 막대차트)
x=np.linspace(0.1, 2*np.pi, 10)
plt.title("Stem Plot")
plt.stem(x, np.cos(x), '-.')
plt.show()

#파이차트
label=['자바','씨','씨++','파이썬']
sizes=[15,30,45,10]
colors=['yellowgreen','gold','lightskyblue','lightcoral']
plt.title('Pie Chart')
plt.pie(sizes, labels=label, colors=colors, startangle=90) #shadow=True로 그림자 넣어줄 수도 있음
plt.axis('equal') #
plt.show()

#히스토그램(도수분포표 막대그래프로 나타낸 것)
x=np.random.randn(1000)
plt.title("histogram")
plt.hist(x,bins=10)
plt.show()

#scatter 플롯(산점도): 2차원 데이터의 상관관계를 나타낼 때 사용
x=np.random.normal(0,1,100)
y=np.random.normal(0,1,100)
plt.title("Scatter Plot")
plt.scatter(x,y)
plt.show()
