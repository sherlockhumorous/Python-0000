#coding:utf-8
import xlwt
import os
import json

os.chdir(r"C:\Users\Alex.hasee-PC\Desktop\pythonprogram")
with open('0015.txt') as f:
    content=f.read()
content=content.decode('utf-8-sig')
d=json.loads(content)
d=sorted(d.items(), key=lambda item:item[0], reverse=False)
workbook=xlwt.Workbook(encoding='utf-8')
sheet1=workbook.add_sheet('sheet1')
i=0
for key,value in d:
    sheet1.write(i,0,key)
    sheet1.write(i,1,value)
    i+=1
workbook.save('city.xls')
