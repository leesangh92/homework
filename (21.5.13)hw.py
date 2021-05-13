import sqlite3 as sql

connect = sql.connect('c:\\dd\\mydb')
c = connect.cursor()
'''
c.execute('create table Man(name, age)') 
# 테이블이 만들어진 후에 코드를 다시 실행하면 에러 발생
# sqlite3.OperationalError: table Man already exists
'''
c.execute('insert into Man values("김연아", 32)')
c.execute('insert into Man values("손흥민", 30)')
c.execute('insert into Man values("이강인", 21)')

c.execute('select * from movie order by audience desc')
'''
Data = connect.fetchall() 
# AttributeError 'sqlite3.Connection' object has no attribute 'fetchall'
'''
Data = c.fetchall() # 꺼내오기
print(Data)

print('*' * 10)

for i in Data:
    print(i[0], i[1], i[2], i[3])
'''
for i in all:
    print()
'''

connect.commit()
c.close()
connect.close()