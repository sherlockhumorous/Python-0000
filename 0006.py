#coding:utf-8
import os
import re
from collections import defaultdict

os.chdir(r'C:\Users\Alex.hasee-PC\Desktop\pythonprogram\0006')
list_=[]
flist_=[]
ignore_words=['i','a','an','is','it','are','of','by','the','and','for','in','to']
list_=os.listdir(r'C:\Users\Alex.hasee-PC\Desktop\pythonprogram\0006')
def istext():
    for i in list_:
        if os.path.splitext(i)[1]=='.txt':
            flist_.append(i)
def count(filename):
    txt=open(filename)
    data=txt.read()
    data=data.lower()
    split=re.split(r";|,|\s|-|!|\.|:",data)
    dict=defaultdict(int)
    for words in split:
        if words in ignore_words:
            continue
        else:
            dict[words]+=1
    del dict['']
    dict=sorted(dict.items(), key=lambda item:item[1], reverse=True)
    print dict[0]
istext()
for i in flist_:
    count(i)
