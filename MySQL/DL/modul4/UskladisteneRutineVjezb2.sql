DELIMITER //
create PROCEDURE insertuser(newname varchar(50))
BEGIN
   declare usersCount int;
   select count(id) from users where name=newname into usersCount;
   if usersCount<1 then
   insert into users (name,status) values (newname,1);
   end if;
END;

DELIMITER ;