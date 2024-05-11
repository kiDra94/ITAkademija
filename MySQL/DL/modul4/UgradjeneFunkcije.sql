#vrijeme
SELECT now();
SELECT curdate();
SELECT curtime();
SELECT date_format(now(), '%d. %M %Y.'); #veliko M je Mart, malo m je 03
SELECT date_format(now(), '%d. %M %Y. %h:%i:%s %p'); #%p je am tj PM
SELECT date_add(NOW(), INTERVAL 10 DAY);
SELECT date_sub(NOW(), INTERVAL 10 DAY);
#strin
SELECT concat('Hello from', 'mysql'); #spaja 2 stringa
SELECT replace('my text', 'my', 'Link');# mijenja
SELECT insert('my text', 4, 4, 'new'); #  Prvi parametar txt, drugi gdje pocinje insert, treci koliko karaktera se gazi, cetvrti sta se umece
SELECT insert('my text', 4, 0, 'new'); #u ovom sluicaju ne gazi samo insert!
SELECT left('LinkGroup', 4); #odsjeca sa lijeve stranee, drugi parametar govori poslije kojeg karaktera odsjeca
SELECT right('LinkGroup', 5); #odsjeca sa desne stranee, drugi parametar govori poslije kojeg karaktera odsjeca
SELECT mid('LinkGroup', 5, 1); #prvi je txt, drugi je pocetak odsjecanja, treci duzina
SELECT substring('my string', 4); # prvi txt, pocetni index novog stringa
SELECT trim('   string           '); #odsjeca sva prazna mjesta
SELECT ltrim('   string           '); #odsjeca sva prazna mjesta s lijeve strane
SELECT rtrim('   string           '); #odsjeca sva prazna mjesta s desne strane
SELECT length('my string'); #vraca duzinu
#rad sa numerickim vrijednostima
SELECT abs(-434); #vraca absolutnu vrijednost
SELECT ceil(5.7); #zaokruzuje uvijek na veci broj
SELECT floor(5.7); #zaokruzuje na manji
SELECT pi();
SELECT pow(2, 3); #ovo znaci 2 na trecu
SELECT round(23.23); #zaokruzuje
SELECT rand(); #random 0-1
SELECT truncate(23.3446545, 2); #izbacuje decimale, drugi par je koliko ih ostavlja
#sumarne funkcije
SELECT count(customer_id) FROM customer; #broji broj zapisa jedne tabele
SELECT SUM(length), MAX(length), MIN(length), AVG(length) FROM film;
SELECT count(title), rating FROM film GROUP BY rating;
SELECT count(title), rating FROM film GROUP BY rating HAVING count(title)>200; #samo oni koji imaju vise od 200 filmova
#kontrolne funkcije
SELECT IF(1=2, 'TRUE', 'FALSE'); #prvi sta, drugi ako je true, treci ako je false
SELECT title, if(length > 120, 'over 2 houres', 'less then 2 hours') AS Length FROM film;
SELECT title,
CASE rating
WHEN 'G' THEN 'Suitible for all ages'
WHEN 'PG' THEN 'Not sutible for all ages'
WHEN 'PG-13' THEN 'Not suitble for all ages'
WHEN 'R' THEN 'Not sutible for all ages'
WHEN 'NC-17' THEN 'Notsutible for all ages'
END
AS Raiting FROM film;
SELECT ifnull(5, 'Value is null'); #prvi vrijednost, drugi se emituje ukoliko je prvi null!




