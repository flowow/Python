#벡터화 연산:넘파이에서는 반복 연산을 하나의 명령어 처리
import numpy as np
# #1. 반복연산
# data=[1,2,3,4,5]
# data2=[]
# for d in data:
#     data2.append(d*2)
# print(data2)
# import numpy as np
# # print(data*2) #리스트가 2번 반복
# # #2.벡터화 연산 => 선형 대수에 적용
# # x=np.array(data)
# # print(x*2)
# #
# # x=np.array([1,2,3])
# # y=np.array([4,5,6])
# # #x 요소에 2배 + y 요소를 합한 결과를 출력
# # print(x*2+y)
# #
# # print(x==2)
# # print(y>5)
# # print((x==2) & (y>4))
# #
# # #2*3 array(2차원 배열)
# # z=np.array([[1,2,3], [4,5,6]])
# # print(len(z))#행 길이
# # print(len(z[0]))#열 길이
# #
# # #2*3*4 array(3차원 배열)
# # d=np.array([[[1,2,3,4],
# #              [5,6,7,8],
# #              [9,10,11,12]],
# #              [[1,2,3,4],
# #              [5,6,7,8],
# #              [9,10,11,12]]])
# # print(len(d)) #행
# # print(len(d[0])) #열
# # print(len(d[0][0]))#깊이
# #
# # print(d.ndim) #3차원 배열
# # print(d.shape) #(2,3,4) (행,열,깊이)
# #
# # z=np.array([[1,2,3], [4,5,6]])
# # print(z.ndim) #2차원 배열
# # print(z.shape) #(2,3) (행,열)
# #
# # #numpy 1차원 배열 인덱싱(파이썬 리스트 인덱싱과 같음)
# # x=np.array([1,2,3,4,5])
# # print(x[3])
# # print(x[-3])
# #
# # #numpy 다차원 배열 인덱싱(컴마로 접근)
# # z=np.array([[1,2,3], [4,5,6]])
# # print(z[0][1]) #2 참조
# # print(z[0,1])
# # print(z[-1][-2])
# # print(z[-1,-2])#마지막 행의 마지막 열에서 2번째 값
# #
# #
# # z=np.array([[1,2,3], [4,5,6]])
# # print(z[0])
# # print(z[0,:]) #  [행,열]
# # print(z[:,1]) #두 번째 열 접근
# #   #두번째 행의 두번째 열부터 끝까지 추출 =>5 6
# # print(z[1,1:])
# #
# # #Numpy는 팬시 인덱싱을 제공
# #
# # x=np.array([1,2,3,4,5,6])
# # print(x%2)
# # print(x%2==0)
# # print(x[x%2==0]) #팬시 인덱싱
# # ind=np.array([0,0,0,2,2,2,4,4,4])
# # print(x[ind])#팬시 인덱싱
# #
# # y=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# # print(y[:,[True, False, False, True]])
# # print(y[[2,0,1], : ])
# #
# # #array에서는 데이터타입이 동일해야 함
# # a=np.array([1,2.1,3])
# # print(a)
# # print(a.dtype)
# #
# # b=np.array([1,2,3],dtype='f')
# # print(b.dtype)
# #
# # #무한대:np.inf(infinity),
# # #정의할 수 없는 숫자:np.nan(not a number)
# #
# # print(np.array([1,0,-3,0]) / np.array([0,3,0,0]))
# # #inf:0으로 나누려고 한 경우
# # #np.nan:0을 0으로 나누려고 한 경우
#
# #print(np.log(0))
#
# x=np.arange(12)
# y=x.reshape(3,-1)#-1은 계산한 결과가 들어감 #y=x.reshape(3,4)
# print(y)
#
# #다차원 배열 -> 1차원 배열
# print(y.flatten())
# print(y.ravel())
#
# #길이가 4인 1차원 배열
# a=np.arange(4)
# b=a.reshape(1,4)
# c=a.reshape(4,1) #a, b, c가 모두 다른 구조의 배열
# print(a)
# print(b)
# print(c)
#
# #newaxis : 배열 차원 1증가
# print(a)
# a=a[:,np.newaxis]
# print(a)
#
# #배열 연결(stack)
# a=np.ones((2,3))
# print(a)
# b=np.zeros((3,3))
# print(b)
# #print(np.hstack([a,b]))
# print(np.vstack([a,b]))
#
# print("="*50)
# #dstack:depth(깊이) 방향으로 합치는 작업
# #shape (3,4)배열이 2개 -> dstack -> (3,4,2)
# a=np.ones((3,4))
# print(a)
# print("="*50)
# b=np.zeros((3,4))
# print(b)
# print("="*50)
# c=np.dstack([a,b])
# print(c)
#
# #dstack 마지막 차원으로 배열이 연결
# #stack함수는 작성자가 지정한 축(axis)으로 배열이 연결됨
#
# #shape이 (3,4)인 2개 배열 ->axis=0(기본값), stack-> (2,3,4)
#
# c=np.stack([a,b])
# print(c)
# print(c.shape) #(2,3,4)
#
#
# c=np.stack([a,b], axis=1)
# print(c)
# print(c.shape) #(3,2,4)


#인덱서:()가 없는 메서드로서, [] 기호를 사용하는 메서드
x=np.array([1,2,3])
y=np.array([4,5,6])
z=np.r_[x,y] # [1,2,3,4,5,6] hstack과 동일한 특수한 함수
print(z)

#c_:좌우 연결, 차원을 증가시킴
z=np.c_[x,y]
print(z)

#tile:배열을 반복해서 연결
x=np.array([[1,2,3], [4,5,6]])
print(x)
print(np.tile(x,3))
print(np.tile(x,(2,3)))


x=np.array([1,2,3])
y=np.array([1,2,3])
print(x==y)
print(x<y)
print(np.all(x==y)) #두 배열 전체가 모두 같은지 비교

x=np.arange(5)
print(np.exp(x))
print(10**x)
print(np.log(x+1))
#broadcasting:크기가 작은 배열을 자동으로 확장해서
#크기가 큰 배열에 맞추는 동작
#넘파이는 브로드캐스팅을 지원함.
#브로드캐스팅을 하는 이유?행렬 연산
#벡터(행렬)끼리 덧셈 등 연산하려면 두 벡터(행렬)는
# 크기가 같아야 함

x=np.arange(3)    #[0 1 2]
y=np.ones_like(x) #[1 1 1]
print(x+y)
print(x+1)


















































































































