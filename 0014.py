#coding:utf-8
import xlwt
import os
import json

os.chdir(r'C:\Users\Alex.hasee-PC\Desktop\pythonprogram')
with open('0014.txt') as f:
    content=f.read()
content=content.decode('utf-8-sig')
d=json.loads(content)
d=sorted(d.items(), key=lambda item:item[0], reverse=False)
workbook=xlwt.Workbook(encoding='utf-8')
sheet1=workbook.add_sheet('sheet1')
r=0
c=1
for key,value in d:
    sheet1.write(r,0,key)
    for v in value:
        sheet1.write(r,c,v)
        c+=1
    r+=1
    c=1
workbook.save('student.xls')
