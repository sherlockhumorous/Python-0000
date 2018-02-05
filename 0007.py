#coding:utf-8

import os
import re
from collections import defaultdict

os.chdir(r'C:\Users\Alex.hasee-PC\Desktop\pythonprogram\0007')
def getfile(path):
    list=os.listdir(path)
    filelist=[]
    for i in list:
        if os.path.splitext(i)[1]=='.py':
            filelist.append(i)
    return filelist
def count(filename):
    totalline,blankline,comment=0,0,0
    py=open(filename)
    lines=py.readlines()
    for line in lines:
        totalline+=1
        fline=line.strip()
        if not fline:
            blankline+=1
        elif fline.startswith('#'):
            comment+=1
        elif fline.startswith("'''") or fline.startswith('"""'):
            comment+=1
            i=lines.index(line)
            for k in range(i+1,len(lines)):
                 comment+=1
                 if '"""' in lines[k] or "'''" in lines[k]:
                    break
    codeline=totalline-blankline-comment
    print ("name:%s : codeline:%d,blankline:%d,comment:%d") %(filename,codeline,blankline,comment)
    return codeline,blankline,comment

code,blank,comments=0,0,0
f=getfile(r'C:\Users\Alex.hasee-PC\Desktop\pythonprogram\0007')
for i in f:
    c=count(i)
    code+=c[0]
    blank+=c[1]
    comments+=c[2]
print "codeline:",code
print "blankline:",blank
print "comments:",comments
