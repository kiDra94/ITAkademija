DELIMITER //
create function checkNum(num int)
returns varchar(50)
begin
set @outputText = 'unknown';
if num = 0 then set @outputText = 'The number is zero'; end if;
if num < 5 and num != 0 then set @outputText = 'Lower than 5'; end if;
if num > 5 then set @outputText = 'Higher than 5'; end if;
if num = 5 then set @outputText = 'The number equals 5'; end if;
return @outputText;
end//
DELIMITER ;