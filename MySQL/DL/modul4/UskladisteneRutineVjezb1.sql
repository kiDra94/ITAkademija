DELIMITER //
create PROCEDURE insertuser(newname varchar(50))
BEGIN
   insert into users (name,status) values (newname,1);
END//
DELIMITER ;