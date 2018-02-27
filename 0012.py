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

for w in filterwords:
    scan=scan.replace(w,'*'*len(w))
print "Filter:%s" %scan
