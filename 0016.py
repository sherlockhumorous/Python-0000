#coding:utf-8
import os
import xlwt
import json

os.chdir(r"C:\Users\Alex.hasee-PC\Desktop\pythonprogram")
with open('0016.txt') as f:
    content=f.read()
d=json.loads(content)
workbook=xlwt.Workbook()
sheet1=workbook.add_sheet('sheet1')
for r,i in enumerate(d):
    for c,j in enumerate(i):
        sheet1.write(r,c,j)
workbook.save('numbers.xls')
