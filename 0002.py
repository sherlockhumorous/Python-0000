import pymssql
import random
import string

s=string.ascii_letters+string.digits
def randomcode():
    list_id=[]
    for i in range(200):
        r=random.sample(s,16)
        for j in range(4,16,5):
            r.insert(j,'-')
        active = ''.join(r)
        list_id.insert(i,active)
    return list_id
con=pymssql.connect(host='localhost',user='sa',password='123',database="testdb")
cur=con.cursor()
cur.execute("IF EXISTS(SELECT * FROM sysobjects WHERE name='activation_code') DROP TABLE activation_code")
sql1="""create table activation_code(
       id int,
       code varchar(20))"""
cur.execute(sql1)
rd=randomcode()
for i in range(200):
    sql2="insert into activation_code(id,code) values('%d','%s')" %(i,rd[i])
    cur.execute(sql2)
cur.close()
con.commit()
con.close()
