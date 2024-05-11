create database geekprofile;

create table if not exists accounts( id int(11) not null auto_increment, username varchar(50) not null, password varchar(255) not null, email varchar(100) not null, organisation varchar(100) not null, address varchar(100) not null, city varchar(100) not null, state varchar(100) not null, country varchar(100) not null, postalcode varchar(100) not null, primary key (id) ) engine=InnoDB auto_increment=1 default char set=utf8;

SELECT * FROM accounts; 