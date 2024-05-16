insert into user values(NULL, 'Ana', 'ana123');
insert into user values(NULL, 'Aca', 'aca123');
insert into user values(NULL, 'Maki', 'maki123');
select * from off.user;

create table user2 as select * from user; #pravi duplikat tj backup
select * from off.user2;

create table user3 as select * from user where 1 = 0; #pravi duplikat bez podataka

#napravljen triger user_AFTER_INSERT
insert into user values(NULL, 'Zoja', 'zoja123');
insert into user values(NULL, 'Mika', 'Mika123');
insert into user values(NULL, 'Pera', 'Pera123');
select * from off.user3;