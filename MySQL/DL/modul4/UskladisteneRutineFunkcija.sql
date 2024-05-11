DELIMITER //
CREATE FUNCTION my_function()
RETURNS VARCHAR(20)
DETERMINISTIC
BEGIN
RETURN 'HELLO FROM UDF';
END//
DELIMITER ;

SELECT my_function();
SELECT movie_over_2_hours(6); #vraca 1 to je treu (film sa id 6)

CALL example;
CALL example2;
CALL example3; # mrtva petlja nikad ne ispunjava uslov!