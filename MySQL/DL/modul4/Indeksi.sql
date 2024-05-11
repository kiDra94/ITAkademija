SHOW INDEX FROM customer;
SHOW INDEX FROM buy;
SELECT * FROM my_first_db.customer;
EXPLAIN SELECT last_name, first_name FROM customer
WHERE last_name = 'John' AND first_name LIKE 'J%';
EXPLAIN SELECT last_name, first_name FROM customer
WHERE last_name = 'John'; #radi i kad se izostavi firstname

SELECT * FROM sakila.film;
SELECT * FROM film WHERE MATCH (description) AGAINST ('epic drama');
#kad stavimo plus; obe se moraju pojaviti!!
SELECT * FROM film WHERE MATCH (description) AGAINST ('+epic +drama' IN BOOLEAN MODE);
#ne zelimo
SELECT * FROM film WHERE MATCH (description) AGAINST ('-epic +drama' IN BOOLEAN MODE);