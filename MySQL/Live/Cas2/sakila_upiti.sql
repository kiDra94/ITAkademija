SELECT * FROM sakila.actor;
SELECT * FROM sakila.actor WHERE actor_id<=50; #radi zato sto znamo tj vidimo da id ide od 1
SELECT * FROM sakila.actor LIMIT 50;
SELECT * FROM sakila.actor WHERE first_name = "PENELOPE";
SELECT first_name, last_name FROM sakila.actor WHERE first_name = "PENELOPE";
SELECT first_name, last_name FROM sakila.actor WHERE first_name LIKE "PEN%"; # % mijenja karaktere; ide LIKE umjesto = !!!
SELECT first_name, last_name FROM sakila.actor WHERE first_name LIKE "%PEN%";

SELECT count(*) FROM sakila.actor;
SELECT count(actor_id) FROM sakila.actor;
SELECT DISTINCT first_name FROM sakila.actor; #distinct sklanja duplikate
SELECT count(DISTINCT first_name) AS broj FROM sakila.actor;
SELECT "Neki ispis" AS ispis;

SELECT * FROM sakila.actor ORDER BY  first_name; # samo po imenu
SELECT * FROM sakila.actor ORDER BY  first_name, last_name; #ime i prezime
SELECT * FROM sakila.actor ORDER BY  first_name DESC, last_name DESC; #DESC je opadajuci

SELECT title FROM sakila.film WHERE length>120;
SELECT count(title) FROM sakila.film WHERE length>120;
SELECT count(*) FROM (SELECT title FROM sakila.film WHERE length>120) AS broj;

SELECT first_name,count(first_name) FROM sakila.actor GROUP BY first_name;
SELECT first_name,count(first_name) FROM sakila.actor GROUP BY first_name HAVING count(first_name) =1; #having zamjenjuje where kad se koristi group by
SELECT first_name,count(first_name) FROM sakila.actor GROUP BY first_name HAVING count(first_name) >1;

SELECT * FROM sakila.film WHERE rental_rate > 3 AND length BETWEEN 120 AND 180;
SELECT count(*) FROM sakila.film WHERE rental_rate > 3 AND length BETWEEN 120 AND 180;

