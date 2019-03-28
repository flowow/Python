
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# page = urlopen("https://www.g2crowd.com/products/sap-erp/reviews")
# doc=page.read
# soup=BeautifulSoup(doc, "html.parser")

req = Request('https://www.g2crowd.com/products/sap-erp/reviews',
              headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup=BeautifulSoup(webpage, "html.parser")
cons=soup.select("formatted-text")
print(cons)

#pjax-container > div.row.full > div.column.xlarge-8.xxlarge-9 > div.nested-ajax-loading >
# div:nth-child(2) > div > div > div.col-2 > div:nth-child(2) > div > div > div:nth-child(4) > p

#pjax-container > div.row.full > div.column.xlarge-8.xxlarge-9 > div.nested-ajax-loading >
# div:nth-child(4) > div > div > div.col-2 > div:nth-child(2) > div > div:nth-child(3) > div:nth-child(4) > p
#pjax-container > div.row.full > div.column.xlarge-8.xxlarge-9 > div.nested-ajax-loading >
# div:nth-child(4) > div > div > div.col-2 > div:nth-child(2) > div > div:nth-child(3) > div:nth-child(4) > p

#pjax-container > div.row.full > div.column.xlarge-8.xxlarge-9 > div.nested-ajax-loading >
# div:nth-child(6) > div > div > div.col-2 > div:nth-child(2) > div > div > div:nth-child(4) > p

#pjax-container > div.row.full > div.column.xlarge-8.xxlarge-9 > div.nested-ajax-loading >
# div:nth-child(7) > div > div > div.col-2 > div:nth-child(2) > div > div > div:nth-child(4) > p

#pjax-container > div.row.full > div.column.xlarge-8.xxlarge-9 > div.nested-ajax-loading >
# div:nth-child(8) > div > div > div.col-2 > div:nth-child(2) > div > div > div:nth-child(4) > p