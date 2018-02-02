from PIL import Image
import os

os.getcwd()
os.chdir(r'C:\Users\Alex.hasee-PC\Desktop\pythonprogram\0005')
def resize(filename):
    img=Image.open(filename)
    out=img.resize((640,1130),Image.ANTIALIAS)
    f=filename.strip(".jpg")
    newname=f+"r.jpg"
    out.save(newname)
list=os.listdir(r'C:\Users\Alex.hasee-PC\Desktop\pythonprogram\0005')
f_list=[]
def getextension():
    for i in list:
        if os.path.splitext(i)[1]=='.jpg':
            f_list.append(i)
getextension()
for i in  f_list:
    resize(i)
