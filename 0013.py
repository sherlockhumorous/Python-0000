#coding:utf-8
import requests
from bs4 import BeautifulSoup
import os

os.chdir(r'C:\Users\Alex.hasee-PC\Desktop\pythonprogram\0013')
url='http://tieba.baidu.com/p/2166231880'
data=requests.get(url).text
soup=BeautifulSoup(data,'html.parser')

'''for count,i in enumerate(soup.select('img.BDE_Image')):
    img=requests.get(i['src'])
    with open('%04d.jpg'%count,'wb') as f:
        f.write(img.content)'''
flag=1
for i in soup.select('img.BDE_Image'):
    img=requests.get(i['src'])
    with open ("%04d.jpg"%flag,'wb') as f:
        f.write(img.content)
    flag+=1
