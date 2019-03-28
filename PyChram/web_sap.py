import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.pylab as plt
base_url="https://www.featuredcustomers.com/vendor/sap/testimonials?p={}"
# req = urllib.request.Request(base_url,
#                              headers={'User-Agent': 'Mozilla/5.0'})
# response = urllib.request.urlopen(req).read()
# text = response.decode('utf-8')
# print(text)

d=pd.DataFrame()
c=[]
for i in range(1,3):
    url=base_url.format(i)
    req = urllib.request.Request(url,
                                 headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req).read()
    text = response.decode('utf-8')
    soup = BeautifulSoup(text, 'html.parser')
    industries = soup.select('div.half_width>span')
    b = []
    for industry in industries:
        field = industry.get_text()
        a = field.split(sep="Employees")
        b += a #한페이지의 전체 크롤링 리스트
    print(len(b))
    c=c+b
print(len(c))
all=pd.DataFrame(c)
    #     c=pd.DataFrame(b)
    # e=pd.concat([c,e])
    # print(e)
    # print(d)
# s=[]
# for scale in c:
#     if "-"or"+" in scale:
#         s+=scale
# print(s)
s=all[0].value_counts()
ds=pd.DataFrame(s)
print(ds[:3])
print(ds.index)
print(ds)
label_size=['','10,000+ ', '1001-5000 ', '11-50 ', '5001-10,000 ',
       '51-200 ', '501-1000 ', '1-10 ','201-500 ']
for i in ds.index :
    if i in label_size:
        industry=ds.drop(i)
        # size=ds.append(i)
print(industry)

# size=ds.pop(['10,000+ ', '1001-5000 ', '5001-10,000 ','11-50 ', '201-500 ', '51-200 ','501-1000 ','1-10 '])

# print(size)
# print(size)
# scale={k: ds[k] for k in set(wanted_keys) & set(ds.keys())}
# print(scale)
#
# for i in set(wanted_keys):
#     del(ds[i])
# del(ds[''])
# industry=ds
# print(type(industry.items()))
# df1=pd.DataFrame()
# for key, value in industry.items():
#     df1.index
#
# 원하는 것! 데이터 시각화하기

# df_industry=pd.DataFrame
# df_industry['industry']=industry.keys()
# df_industry['counts']=industry.values()
# print(df_industry)






# %matplotlib inline
# import matplotlib.pyplot as plt


# soup=BeautifulSoup(text,'html.parser')
# print(soup)
# industries=soup.select('div.half_width>span')
# print('https://www.featuredcustomers.com/vendor/sap/testimonials')

# b=[]
# for industry in industries:
#     field=industry.get_text()
#     a=field.split(sep="Employees")
#     # print(a)
#     b+=a
# # print(b)
# c=pd.DataFrame(b)
# print(c)
# d=c[0].value_counts()
# print(d)
# print(type(a))
# b=pd.Series(a)




"""
https://www.featuredcustomers.com/vendor/sap/testimonials
https://www.featuredcustomers.com/vendor/sap/testimonials?p=2
https://www.featuredcustomers.com/vendor/sap/testimonials?p=12

body > div.tab_links_bg.clearboth > div:nth-child(2) >
div > div > div > div.tab_link_right > div.tab_link_right_inner >
div.testimonials_bg.clearboth.premium_border > div:nth-child(2) >
div.testi_box_left.premium_border_right > div:nth-child(3) > span

body > div.tab_links_bg.clearboth > div:nth-child(2) >
div > div > div > div.tab_link_right > div.tab_link_right_inner >
div.testimonials_bg.clearboth.premium_border > div:nth-child(3) >
div.testi_box_left.premium_border_right > div:nth-child(3) > span

body > div.tab_links_bg.clearboth > div:nth-child(2) >
div > div > div > div.tab_link_right > div.tab_link_right_inner >
div.testimonials_bg.clearboth.premium_border > div:nth-child(4) >
div.testi_box_left.premium_border_right > div:nth-child(3) > span

body > div.tab_links_bg.clearboth > div:nth-child(2) > 
div > div > div > div.tab_link_right > div.tab_link_right_inner > 
div.testimonials_bg.clearboth.premium_border > div:nth-child(19) > 
div.testi_box_left.premium_border_right > div.half_width > span
"""
