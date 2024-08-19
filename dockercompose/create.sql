-- 12. Using phpmyadmin sql editor create database, table in that database and insert rows,
-- using following commands:
create database mydb;
use mydb: create table mytable ( id int AUTO_INCREMENT primary key, data text, datamodified timestamp default now());
insert into mytable (data)values ("testdata0");
  insert into mytable (data)values ("testdata03");
    insert into mytable (data)values ("testdata03");
