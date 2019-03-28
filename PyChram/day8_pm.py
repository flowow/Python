#데이터 전처리 and 분석, 시각화(numpy, pandas, matplotlib# )
import csv #comma seperated values
def read_cars():
    f=open("data/cars.csv","r")
    rows=[]
    for row in f:
        #print(row, end="")
        #print(row.strip()) #제거하겠다
        #print(row.strip().split(",")) #split->문자열을 컴마로 분리한 걸 리스트 안으로!
        rows.append(row.strip().split(","))
    f.close()
    return rows
row=read_cars()
print(row)

def read_tree():
    f=open('data/trees.csv','r')
    rows=[] #대괄호 하나이기 때문에 feature가 3개인 1차원
    for row in csv.reader(f): #컴마로 구분된 상태로 데이터를 읽을 수 있음
        print(row)
        rows.append(row)
    f.close()
    return rows

def write_tree(rows):
    f=open('data/mytree.txt','w', newline='') #오픈 안에 경로 넣어준다 newline='':뉴라인 없이 붙여서 출력
    #csv.writer(f).writerows(rows)
    writer=csv.writer(f,delimiter=":") #delimiter는 구분자! 구분자로 넣고싶은 특수문자 지정해 줄 수 있다
    for row in rows:
        writer.writerow(row)
    f.close()

rows=read_tree()
#print(rows) #--->[[:2차원
write_tree(rows)