DELIMITER //
create function setStatus(username varchar(50),statusname varchar(50))
returns int
begin
set @statusId = 0;
select id from statuses where name = statusname into @statusId;
if @statusId != 0 then
update users set status = @statusId where name = username;
end if;
return @statusId;
DELIMITER ;