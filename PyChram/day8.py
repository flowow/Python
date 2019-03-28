#0~9까지 출력
for i in range(10):
    print(i, end=" ")
print()
for i in range(0,10):
    print(i, end=" ")
print()
for i in range(0,10,1):
    print(i, end=" ")
print()

#0~9까지 정수 거꾸로 출력
for i in range(9,-1,-1):
    print(i,end=" ")
print()
for i in reversed(range(10)):
    print(i,end=" ")
print()
print()

#리스트에서
a=[1,3,5]
print(a[0],a[1],a[2])
print(a)
a.append(10)
a[0]=a[2]
print(a) #[5,3,5,10]
for i in range(len(a)-1, -1,-1):
    print(i, a[i])   #3 10
                     #2 5 ...
for i in reversed(a):
    print(i)        #10
print()
print()

a=3
b=5
a,b=b,a
print(a,b)
# list:[], tuple:(), set, dictionary:[]
t=(1,3,5)
print(t)
print(t[0],t[1],t[2])
#t[0]=9 튜플은 바꿀 수 없음
#t.append(9)
print()
print(t)
t1=(3,5)
print(t1, t1[0], t1[1]) #-->한 줄에 출력됨
t2=3,5  #pack
print(t2, type(t2))
t3,t4=t2 #unpack
print(t3, t4) #-->3 5 unpack
print()
def order(a,b):
    if a<b:
        return a,b
    return b,a
print(order(4,9))
print(order(9,4))
r=order(4,9)
print(type(r), r[0], r[1])
min,max=order(4,9)
print(min, max)
_,max=order(4,9)
#텐서플로우에서 _ 기호의 의미:값을 사용하지 않음
print('결과:',max, _)
###################?
# def dummy():
#     pass
# print(dummy())

#중복 제거--->set()
ns=[1,3,5,1,3,5,1,3,5] #중단점
a=[4,3,5,5,6,6,6,7]
print(set(a))
unique=[]
print(set(ns))
for i in ns: #i:1
    if not i in unique: #unique리스트에 i값이 존재하지 않는다면
        unique.append(i) #1 3 5
print(unique)
print(list(set(ns)))

print()


a=dict(name="kim", age=20)#딕셔너리 생성
print(a)
#kim출력
# print(a[0]) #KeyError:0
# print(a[name])#name 정의 안됨->오류
print(a['name'])
print(a)
###딕셔너리 추가!!a딕셔너리에 'addr'키와 '경복궁' 값을 추가하세요
a['addr']='경복궁'
print(a)
#'경복궁'값을 '창경궁'으로 변경하세요
a['addr']='창경궁'
print(a)
#a 딕셔너리의 키들을 출력하세요
print(a.keys())
print(a.values())
print(a.items())
print(a.keys())
#같은 표현
for i in a.keys():
    print(i, a[i])
for k,v in a.items():
    print(k, v)
for k in a:
    print(k, a[k])
for k in a.keys():
    print(k, a[k])

for v in a.values():
    print(v)
for item in a.items():
    print(item, item[0], item[1])
for k in reversed(list(a.keys())):
    print(k,a[k])

print()
###########딕셔너리 중복 세기
# (1) i in dic.keys
s=['a','b','c','a','b','c']
dic={}
for i in s:
    if i not in dic.keys():
        dic[i]=0
    dic[i]+=1
print(dic)
#print(dic.keys())

#(2)setdefault
print()
s=['a','b','c','a','b','c']
dic2={}
for k in s:
    dic2.setdefault(k,0)
    dic2[k]+=1
print(dic2)

# (3) collections.defaultdict(int)
print()
import collections
s=['a','b','c','a','b','c']
dic3=collections.defaultdict(int)
print(dic3)#--->defaultdict(<class 'int'>, {})
for k in s:
    dic3[k]+=1
    print(dic3)
print(dict(dic3))

# (4) collections.Counter(s)
print()
s=['a','b','c','a','b','c']
c=collections.Counter(s)
print(c)
print(dict(c))

#####################slicing
print()
a=[1,3,5,7,9,0,2,4,6,8]
print(a[len(a)-1],a[len(a)-2])
print(a[-1], a[-2])
print(a[3:6])
#a리스트의 앞쪽 절반을 출력하세요[1,3,5,7,9]
print(a[0:len(a)//2])
#a리스트의 뒤쪽 절반을 출력하세요
print(a[len(a)//2:])
print(a[len(a)//2:len(a)])
#print(a[시작위치:끝위치])
print(a[3:4])
print(a[3:3])

print()
print(a)
print(a[len(a)-1:0])#진행방향 --> a[시작위치:끝위치] <=>시작<끝
print(a[len(a)-1:0:-1])
print(a[::-1])

print()
#[1, 3, 5, 7, 9, 0, 2, 4, 6,8]
#a리스트를 거꾸로 짝수 번째만 출력(8,4,0,7,3)
#a리스트를 거꾸로 홀수 번째만 출력(6,2,9,5,1)
print(a[::-1])#a[시작위치:끝위치:증감]
print(a[::-2])#a[시작위치:끝위치:증감]
print(a[-2::-2])#a[시작위치:끝위치:증감]