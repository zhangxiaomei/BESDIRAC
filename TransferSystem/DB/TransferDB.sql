-- usage:
--   $ mysql --user=root -p
--   > create database TransferDB;
--   > ...
--   $ mysql -u Dirac -pXXX --database=TransferDB < TransferDB.sql

ALTER DATABASE CHARACTER SET "utf8";

-- for foreign key
drop table if exists TransferFileList;
drop table if exists TransferRequest;

create table TransferRequest (
  id int not null auto_increment primary key,
  username varchar(255) not null,
  index(username),
  dataset varchar(255) not null,
  srcSE varchar(255) not null,
  dstSE varchar(255) not null,
  submit_time datetime not null,
  status enum('new', 'transfer', 'finish') not null,
  index(status)
) ENGINE=InnoDB;

drop table if exists TransferFileList;

create table TransferFileList (
  id int not null auto_increment primary key,
  LFN varchar(255) not null,
  trans_req_id int not null,
  start_time datetime,
  finish_time datetime,
  status enum('new', 'transfer', 'finish') not null,
  index(status),
  foreign key (trans_req_id) references TransferRequest (id)
) ENGINE=InnoDB;
