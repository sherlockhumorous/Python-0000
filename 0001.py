import random
import string

s=string.ascii_letters+string.digits
'''string=''
for i in r:
    string=string+i'''
for i in range(200):
    r=random.sample(s,16)
    for j in range(4,16,5):
        r.insert(j,'-')
    active = ''.join(r)
    print active
'''r=random.sample(s,16)
r=''.join(r)
print r
x=[r[i:i+4] for i in range(0,len(r),4)]
print '-'.join(x)'''
