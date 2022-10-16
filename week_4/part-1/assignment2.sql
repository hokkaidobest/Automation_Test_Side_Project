CREATE TABLE `StudentScore`(
 `id` VARCHAR(20),
 `name` VARCHAR(20) NOT NULL DEFAULT '',
 `birth` VARCHAR(20) NOT NULL DEFAULT '',
 `sex` VARCHAR(10) NOT NULL DEFAULT '',
 `course` VARCHAR(10) NOT NULL DEFAULT '',
 `score` INT NOT NULL DEFAULT 0
);

insert into StudentScore values('01' , '周雷' , '1990-01-01' , '男', 'Chinese', 80);
insert into StudentScore values('01' , '周雷' , '1990-01-01' , '男', 'English', 90);
insert into StudentScore values('01' , '周雷' , '1990-01-01' , '男', 'Maths', 60);
insert into StudentScore values('02' , '錢電' , '1990-12-21' , '男', 'Chinese', 75);
insert into StudentScore values('02' , '錢電' , '1990-12-21' , '男', 'English', 75);
insert into StudentScore values('02' , '錢電' , '1990-12-21' , '男', 'Maths', 75);
insert into StudentScore values('03' , '孫風' , '1990-05-20' , '男', 'Chinese', 50);
insert into StudentScore values('03' , '孫風' , '1990-05-20' , '男', 'English', 40);
insert into StudentScore values('03' , '孫風' , '1990-05-20' , '男', 'Maths', 60);
insert into StudentScore values('04' , '周雲' , '1990-08-06' , '男', 'Chinese', 53);
insert into StudentScore values('04' , '周雲' , '1990-08-06' , '男', 'English', 13);
insert into StudentScore values('04' , '周雲' , '1990-08-06' , '男', 'Maths', 70);
insert into StudentScore values('05' , '周梅' , '1991-12-01' , '女', 'Chinese', 100);
insert into StudentScore values('05' , '周梅' , '1991-12-01' , '女', 'English', 90);
insert into StudentScore values('05' , '周梅' , '1991-12-01' , '女', 'Maths', 95);
insert into StudentScore values('06' , '吳蘭' , '1992-03-01' , '女', 'Chinese', 60);
insert into StudentScore values('06' , '吳蘭' , '1992-03-01' , '女', 'English', 60);
insert into StudentScore values('06' , '吳蘭' , '1992-03-01' , '女', 'Maths', 30);
insert into StudentScore values('07' , '鄭竹' , '1989-07-01' , '女', 'Chinese', 70);
insert into StudentScore values('07' , '鄭竹' , '1989-07-01' , '女', 'English', 85);
insert into StudentScore values('07' , '鄭竹' , '1989-07-01' , '女', 'Maths', 20);
insert into StudentScore values('08' , '王菊' , '1990-01-20' , '女', 'Chinese', 15);
insert into StudentScore values('08' , '王菊' , '1990-01-20' , '女', 'English', 35);
insert into StudentScore values('08' , '王菊' , '1990-01-20' , '女', 'Maths', 25);