#어느 회사의 전반기(1월 ~ 6월) 실적을 나타내는 데이터프레임과 후반기(7월 ~ 12월) 실적을
# 나타내는 데이터프레임을 만든 뒤 합친다. 실적 정보는 "매출", "비용", "이익" 으로 이루어진다.
# (이익 = 매출 - 비용).
#또한 1년간의 총 실적을 마지막 행으로 덧붙인다.

import pandas as pd
from pandas import DataFrame
import numpy as np

dfss=DataFrame(np.random.randint(3333,6666,size=(6,2)),
                  index=range(1,7),
                  columns=['매출','비용'])
# print(dfss)
dfss['이익']=dfss['매출']-dfss['비용']
dffw=DataFrame(np.random.randint(3333,6666,size=(6,2)),
                  index=range(7,13),
                  columns=['매출','비용'])
dffw['이익']=dffw['매출']-dffw['비용']
# print(dffw)
dfyr=pd.concat([dfss,dffw],join='outer')
# print(dfyr)
dfyr1=pd.concat([dfyr,DataFrame({'매출':dfyr['매출'].sum(),'비용':dfyr['비용'].sum(),
                           '이익':dfyr['이익'].sum()},index=['총실적'])])
print(dfyr1)
print(dfyr.mean())

