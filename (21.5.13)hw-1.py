
import pymysql as pymovie

Connect = pymovie.connect(host='127.0.0.1', user='root', password='pw', db='mydb')
c = Connect.cursor()

c.execute('select * from movie')

List = c.fetchall()
print(List)

print(List[0][0], List[0][1], List[0][2])
print(List[1][0], List[1][1], List[1][2])
print(List[2][0], List[2][1], List[2][2])

c.execute('insert into movie value("명량", "최민식", 1761)')
c.execute('update movie set actor = "김혜수" where audience = 1302')
c.execute('delete from movie where title = "광해"')

c.execute('select * from movie')

Connect.commit()
c.close()
Connect.close()




import pymysql as pyman

Connect = pyman.connect(host='127.0.0.1', user='root', password='password', db='mydb')
c1 = Connect.cursor()

c1.execute('create table Man(name char(10), age int)')
c1.execute('insert into Man value("김연아", 32)')
c1.execute('insert into Man value("손흥민", 30)')
c1.execute('insert into Man value("이강인", 21)')

c1.execute('select * from Man')

Connect.commit()
c1.close()
Connect.close()