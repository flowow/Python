###################자료형
print(5==5)
print(5!=5) #다르다?
print(5>3)
print(5<3)
#거짓: 0, None, [](빈 리스트), ()(빈 튜플), {}(딕셔너리 아님 셋),""
#list는 순서가 유지됨
#참: 1, [1,2,3], "test"
x=0
if x: #x가 참이면
    print("참")
else:
    print("거짓")

su=[10,20,30]
while su: #su가 참일동안
    print(su.pop())
print(bool("test"))
print(bool([]))
#과제1
l=['How','are','you']
print(" ".join(l))
#과제2
a=[90,30,80,20,10]
a.sort()
print(a)
a.reverse()
print(a)

#과제3
dic={'subject':'python', 'dept':'cse', 'sn':'201901'}
print(dic)

#과제4
tu=(50,70,90)
lis = list(tu)
print(lis)
lis.insert(0,30)
print(tuple(lis))

w= ['List','인덱싱','append','extend','sort','reverse','remove','pop','count','딕셔너리','Tuple','자료형']
print("#".join(w))