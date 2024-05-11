#TRIGERI SE AKTIVIRA KAD SE KORISTI INSERT UPDATE ILI DELETE, prije ili poslije; befor i after trigeri
CREATE TRIGGER test_trigger BEFORE INSERT ON customer FOR EACH ROW SET
new.first_name = concat(new.first_name, '_test');
INSERT INTO customer (first_name, last_name, date) VALUES ('John', 'Davidson', '1988-05-05');
SELECT * FROM my_first_db.customer;
DROP TRIGGER test_trigger;

DELIMITER //
CREATE TRIGGER test_trigger BEFORE INSERT ON customer FOR EACH ROW 
BEGIN
IF length(new.first_name) < 5 THEN 
SET new.first_name = concat(new.first_name, "_test");
END IF;
END //
DELIMITER ;
INSERT INTO customer (first_name, last_name, date) VALUES ('John', 'Davidson', '1988-05-05');
INSERT INTO customer (first_name, last_name, date) VALUES ('Johnny', 'Davidson', '1988-05-05');
SELECT * FROM my_first_db.customer;
UPDATE customer SET first_name='new' WHERE idcustomer= 1;
SELECT * FROM my_first_db.customer; #postavili smo za triger md5 -> koristi se za kriptovanje lozinki
INSERT INTO customer (first_name, last_name, date) VALUES ('John', 'Davidson', '1988-05-05');
#Kursori
DELIMITER //
CREATE PROCEDURE film_cursor()
BEGIN

DECLARE sum float DEFAULT 0;
DECLARE counter int DEFAULT 0;
DECLARE a float;
DECLARE e int DEFAULT 0;
DECLARE c CURSOR FOR SELECT length FROM film;

DECLARE CONTINUE HANDLER FOR NOT FOUND SET e = 1;

OPEN c;
REPEAT 
	FETCH c INTO a;
		IF NOT ISNULL(a) THEN
			SET sum = sum + a;
		END IF;
        
        SET counter = counter + 1;
UNTIL e END REPEAT;
CLOSE c;
SELECT sum/counter;
END //
DELIMITER ;























