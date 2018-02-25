from PIL import Image,ImageFont,ImageDraw,ImageFilter
import os
import random
import string

def rndcolor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
def fontcolor():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
def rndfont():
    s=string.ascii_letters+string.digits
    r=random.sample(s,4)
    return r
os.chdir(r"C:\Users\Alex.hasee-PC\Desktop\pythonprogram")
img=Image.new('RGB',(240,60),(255,255,255))
font=ImageFont.truetype(r"C:/windows/fonts/Arial.ttf",40)
draw=ImageDraw.Draw(img)
for x in range(240):
    for y in range(60):
        draw.point((x,y),fill=rndcolor())
print rndfont()
for i,f in enumerate(rndfont()):
    draw.text((60*i+10,10),f,font=font,fill=fontcolor())
img=img.filter(ImageFilter.BLUR)
img.show()
img.save('0010.jpg','jpeg')
