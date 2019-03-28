#차원 축소 연산
import numpy as np
a=np.array([1,2,3]) #1차원, 벡터
print(np.sum(a)) #0차원, 스칼라
print(a.sum())
print(a.min())
print(a.max())
print(a.argmax()) # [1,2,3]
print(a.argmin()) # [1,2,3]

a=np.array([1,2,3,1])
print(a.mean()) #평균
print(np.median(a)) #중위수(중앙값) => 1 1 2 3 => 1.5
print(np.all([True, True]))
print(np.all([True, True, False])) #모두 참 -> 참
print(np.any([True, True, False]))#어느 하나 참 -> 참

x=np.zeros((10,10), dtype=np.int)
print(x)
print(np.any(x != 0))#0이 아닌 값이 적어도 1개 이상 존재->참
print(np.all(x==x))

x=np.array([1,2,3,2])
y=np.array([2,2,3,2])
z=np.array([6,5,5,5])
print(x<=y)
print((x<=y).all())
print((x<=y) & (y<=z))
print(((x<=y) & (y<=z)).all())
#연산 대상이 2차원 이상 => 어느 차원으로 연산? axis로 지정
#axis=0 => 열(디폴트), 1=>행
x=np.array([[1,1],[2,2]])
print(x)
print(x.sum(axis=0)) #열 합계
print(x.sum(axis=1)) #행 합계

#정렬시에도 axis를 지정해서 수행
x=np.array([[3,1,2,7],
           [1,9,4,5],
           [2,1,7,5]])
print(np.sort(x, axis=0)) #열 단위로 오름차순 정렬
print(x)
print(np.sort(x, axis=1)) #행 단위로 오름차순 정렬
print(np.sort(x, axis=-1)) #가장 안쪽 차원을 기준으로 정렬

x=np.array([3,1,2,7]) # => 1 2 3 7 => index:1 2 0 3
a=np.argsort(x)
print(a) #[1 2 0 3]
print(x[a])
print('='*50)
#기술 통계:간단한 통계를 계산한 함수들의 묶음
# 개수, 평균, 분산, 사분위수, 최대/최소, 표준편차, 중앙값
# #

x=np.array([12,5,-3,9,2,4,1,-2,9,0])
print(len(x))
print(np.mean(x))
#분산:각 데이터와 평균사이의 거리의 제곱의 평균
print(np.var(x))
#분산값이 작다 -> 데이터가 모여있다
#표준편차 : 분산의 양의 제곱근
print(np.std(x))

#사분위:데이터를 오름차순 정렬시, 1/4, 2/4(중앙값),
#3/4, 4/4 위치 데이터
#백분위

print(np.percentile(x,0)) #최소값
print(np.percentile(x,25)) #1사분위
print(np.percentile(x,50)) #2사분위
print(np.percentile(x,75)) #3사분위
print(np.percentile(x,100)) #최대값


x=np.arange(10)
print(x)
np.random.shuffle(x) ##########################################
print(x)

#데이터 샘플링:choice함수, 데이터를 무작위로 추출
data=np.arange(1,46)#50 <= data <= 99
print(np.random.choice(data,6, replace=False)) #data에 저장된 수 중 하나를 추출
#data에서 10개 추출, replace=True:한 번 선택한 데이터가 다시 선택
#a:배열 or 숫자(=arange(5))
print(np.random.choice(10,5))

#unique(중복값 제거) or bincount
print(np.unique([5,5,1,1,3,3,1,3,3]))
print(np.unique([5,5,1,1,3,3,1,3,3],return_counts=True))
#(array([1, 3, 5]), array([3, 4, 2], dtype=int64))
#   unique한 값들, 각 데이터 개수
uni, cnt=np.unique([5,5,1,1,3,3,1,3,3],return_counts=True)
#주사위 눈의 개수에 대해 unique를 적용 -> 1,3,5는  count됨.
#2,4,6는 count되지 않음
print(uni)
print(cnt)
print(np.bincount([1,2,2,3,1,1,5], minlength=7))
#minlength=6 => 0~5까지의 범위 => [0 3 2 1 0 1]

#matplotlib:데이터를 차트, 플롯 등으로 시각화 패키지
# matplotlib.org/gallery.html

import numpy as np
import matplotlib.pyplot as plt


# Compute areas and colors
N = 150
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
print(theta)
area = 200 * r**2
colors = theta

ax = plt.subplot(111, projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

# plt.show()
































































