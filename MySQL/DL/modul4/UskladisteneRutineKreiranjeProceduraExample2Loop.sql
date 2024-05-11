CREATE DEFINER=`root`@`localhost` PROCEDURE `example2` ()
BEGIN

SET @x=10;
WHILE @x > 0 DO
	SET @x=@x-1;
    SELECT @x;
END WHILE;

END
