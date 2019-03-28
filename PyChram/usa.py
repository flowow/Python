path="example.txt"
data=open(path).readline() #한 줄만 읽어들임
print(data)
import json
#key,value 쌍으로 구성된 json형식의 데이터를 읽기 위해 json을 가져옴
#json 모듈에 있는 loads함수를 이용해 데이터를 읽음
path="example.txt"
records=[ json.loads(line) for line in open(path,encoding='utf-8') ]
#line에 있는 데이터를 읽어서 records 리스트를 생성하라
# print(records)
print(len(records[0]))



print(type(subset_loc))#Series
print(type(subset_tail))#데이터프레임

df.iloc([[-2,5,100]])
df.iloc([[1702,5,100]])
subset=df.loc[: ,['year','pop']] #loc는 colomn 인덱스,
subset=df.iloc[: ,[2,4]] #iloc는 열의 순서
print(subset) #전체 출력
print(subset.head()) #위 5개만

print(type(list(range(5)))) #range의 타입은 list가 아니라 range여서
small_range=list(range(5))
subset=df.iloc[ : ,small_range]
print(subset.head())

small_range=list(range(0,6,2))
subset=df.iloc[ : ,small_range]
print(subset.head())