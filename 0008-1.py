#coding:utf-8
import requests
from bs4 import BeautifulSoup
import re

url='http://www.biquge.com.tw/4_4029/2349287.html'
req=requests.get(url)
req.encoding='gbk'
data=req.text
soup=BeautifulSoup(data,'html.parser')
content=soup.select('div#content')
for i in content:
    i=i.get_text().encode('gbk','ignore')
    print i
for link in soup.find_all(href=re.compile("http://")):
    print link.encode('gbk')
