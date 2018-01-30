#coding:utf-8
import os
import re
from collections import defaultdict

os.chdir('C:\Users\Alex.hasee-PC\Desktop\pythonprogram')
txt=open("0004.txt")
count=0
data=txt.read()
#将所有字母小写
data=data.lower()
f=re.split(r";|,|\s|-|!|\.|:",data)
for i in f:
    count=count+1
print count
dict=defaultdict(int)
for words in f:
    dict[words]+=1
del dict['']
dict=sorted(dict.items(), key=lambda item:item[1], reverse=True)
for key,value in dict:
    print("%s:%d") %(key,value)
