show databases;
use aidb;
create table aitab
(
	id int auto_increment primary key, 
    name varchar(20), 
    kor tinyint, 
    eng tinyint, 
    mat tinyint
);
show tables;

insert into aitab(name, kor, eng, mat) values('이순신',85,87,90);
insert into aitab(name, kor, eng, mat) values('강감찬',75,80,95);
insert into aitab(name, kor, eng, mat) values('한석봉',99,98,99);
insert into aitab(name, kor, eng, mat) values('황진이',35,45,20);
insert into aitab(name, kor, eng, mat) values('안중근',90,85,90);
insert into aitab(name, kor, eng, mat) values('박문수',95,98,96);
insert into aitab(name, kor, eng, mat) values('임꺽정',15,35,45);
insert into aitab(name, kor, eng, mat) values('김정호',90,95,80);
insert into aitab(name, kor, eng, mat) values('정몽주',90,90,95);
insert into aitab(name, kor, eng, mat) values('양주종',50,45,60);

select * from aitab;
select name, (kor + eng + mat) as '총점' from aitab; 
-- alias로 (kor + eng + mat)의 값들을 총점으로 분류하고 각각의 이름과 (kor + eng + mat)의 값을 보여준다

select name, (kor + eng + mat) as '총점' from aitab order by (kor + eng + mat) desc;
-- 에러 발생 order by '총점'이 아닌 order by (kor + eng + mat)로 총점 값 그대로를 불러와 정렬

-- drop table aitab;
