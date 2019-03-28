            #pandas file 읽기
#파이썬에서는 csv내의 write메서드 이용하거나 read이용해서 파일 읽어왔다
#txt,csv파일 읽어서 dataframe(데이터테이블)으로 저장하자
            #data읽어들이는 기본 형식
import pandas as pd
csv_test=pd.read_csv('data/text_csv.csv') #csv_test는 data frame이 됨!!
print(type(csv_test))
print(csv_test.shape) #--->(6,3) 6줄 3칸

txt_test=pd.read_csv('data/test_txt.txt', sep='|')
print(txt_test)
#txt_test=pd.read_csv('data/test_txt.txt', sep='|',index_col=0) #id가 컬럼으로 사용됨
txt_test=pd.read_csv('data/test_txt.txt', sep='|',index_col=1) #1번째인 X가 사용됨 index는 for 데이터 식별
print(txt_test)
txt_test2=pd.read_csv('data/test_txt.txt', sep='|',index_col='X') #특정 컬럼으로 바로 명시도 가능
print(txt_test2)

