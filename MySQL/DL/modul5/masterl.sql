CREATE USER 'replication_user'@'localhost' IDENTIFIED BY '12345678';
GRANT REPLICATION SLAVE ON *.* TO 'replication_user'@'localhost';
SHOW MASTER STATUS;
CREATE DATABASE replicationdb;
create table replicationdb.simples (id int not null primary key);
insert into  replicationdb.simples value (999), (1), (13), (125);