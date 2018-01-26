#coding:utf-8
#Image:对象的实例代表一张图片，可以进行一些大小变换和仿射变换操作
#ImageFont:用来加载准备阶段中下载的字体库文件
#ImageDraw: 基于image对象，创建一个可以在Image实例上画线条、贴文字的对象。
from PIL import Image,ImageDraw,ImageFont
#这里使用图片的绝对路径
img=Image.open(r'C:\Users\Alex.hasee-PC\Desktop\pythonprogram\1.jpg')

draw=ImageDraw.Draw(img)

#设置字体及大小
font = ImageFont.truetype('C:/windows/fonts/STHUPO.ttf', size=40)
#设置字体颜色
fontcolor = "#38b0de"
#输出宽和高(像素),可以确定右上方位置
'''w,h=img.size
print w,h'''
#draw.text((530,0),'99', font=font, fill=fontcolor)
draw.text((400,0),unicode('big熊猫','utf-8'), font=font, fill=fontcolor)
img.save(r'C:\Users\Alex.hasee-PC\Desktop\pythonprogram\1-copy.jpg','jpeg')
img.show()
