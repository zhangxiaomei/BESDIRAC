-- usage:
--   $ mysql --user=root -p
--   > create database TransferDB;
--   > ...
--   $ mysql -u Dirac -pXXX --database=TransferDB < TransferDB.sql

ALTER DATABASE CHARACTER SET "utf8";

drop table if exists TransferRequest;

create table TransferRequest (
  id int not null auto_increment primary key,
  username varchar(255) not null,
  index(username),
  submit_time datetime
);

