#coding:utf-8
import os

os.chdir(r'C:\Users\Alex.hasee-PC\Desktop\pythonprogram')

def getfilter():
    file=open('filtered_words.txt')
    words=[]
    for w in file.readlines():
        words.append(w.strip('\n'))
    return words
    
scan=raw_input('>>>')
filterwords=getfilter()
flag=0

for i in filterwords:
    if i in scan:
        flag=1
        break
    else:
        flag=0
if flag==1:
    print "Freedom"
elif flag==0:
    print "Human Rights"

