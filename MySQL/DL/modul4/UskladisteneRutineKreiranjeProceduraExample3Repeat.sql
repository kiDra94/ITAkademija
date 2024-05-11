CREATE DEFINER=`root`@`localhost` PROCEDURE `example3`()
BEGIN

REPEAT
	SET @x = @x - 1;
    SELECT @x;
    UNTIL @x = 0
END REPEAT;

END