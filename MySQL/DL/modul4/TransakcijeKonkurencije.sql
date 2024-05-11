SET @@autocommit=0; #ne komituje podatke odma
INSERT INTO country (country) VALUES ('Serbia');
INSERT INTO country (country) VALUES ('Bosnia');
INSERT INTO country (country) VALUES ('Croatia');
ROLLBACK; #opoziva transakcije
COMMIT; #tranaskcija se izvrsava
SELECT * FROM sakila.country;

START TRANSACTION; #eksplicitno kreirane, nije bitno da li autocommit ukljucen ili ne; zavrsava se sa commit ili rollback
INSERT INTO country (country) VALUES ('Serbia');
SAVEPOINT created_first_country; #Kontrolna tacka!
INSERT INTO country (country) VALUES ('Bosnia');
SAVEPOINT created_second_country;
INSERT INTO country (country) VALUES ('Croatia');
SAVEPOINT created_third_country;

ROLLBACK TO SAVEPOINT created_first_country;

#vracanje tabele na staro; rucno brisanje pa onda
ALTER TABLE `sakila`.`country` 
AUTO_INCREMENT = 110 ;

#KONKURENCIJA
LOCK TABLES customer READ; #Moze i WRITE


#vracanje autocommit
SET @@autocommit=1;




















