#Ukucaj na netu REGEXP npr plus2net.com i imas sva objasnjenja
SELECT	'plus2net.com' LIKE '%2n%';
SELECT 'nesto'; #isto kao print
SELECT	'plus2.net.com' LIKE '%2nf%';
SELECT	'plus2net.com' REGEXP '2n'; #ne moramo da navodimo %; REGEXP -> regular expression
SELECT	'plus2net.com' REGEXP '2nf';
SELECT * FROM SAKILA.ACTOR WHERE first_name REGEXP 'b*'; #vraca sve gdje ima i nema b
SELECT * FROM SAKILA.ACTOR WHERE first_name REGEXP 'b+'; #vraca sve gdje b imamo 1 ili vise puta
SELECT * FROM SAKILA.ACTOR WHERE first_name REGEXP 'ba+'; #vraca sve gdje ba imamo 1 ili vise puta
SELECT * FROM SAKILA.ACTOR WHERE first_name REGEXP '[wz]'; #vraca sva imena koja sadrze ili w ili z
SELECT * FROM SAKILA.ACTOR WHERE first_name REGEXP '[x-z]'; #vraca sva imena koja sadrze jedno od slova od x-z
SELECT * FROM SAKILA.ACTOR WHERE first_name REGEXP '^s'; # vraca sva koja pocinju sa s
SELECT * FROM SAKILA.ACTOR WHERE first_name REGEXP 'sa$'; #vraca sva koja se zavrsavaju sa sa
SELECT * FROM SAKILA.ACTOR WHERE first_name REGEXP '^sa$'; # svi koji pocinju i zavrsavaju sa sa, tj samo sa
SELECT * FROM SAKILA.ACTOR WHERE first_name REGEXP 'ss'; # gdje se s pojavlju 2 puta
SELECT * FROM SAKILA.ACTOR WHERE first_name REGEXP 's{2}'; # gdje se s pojavljuje 2 puta
SELECT * FROM SAKILA.ACTOR WHERE first_name REGEXP 's{2,3}'; # gdje se s pojavljuje 2-3 puta
SELECT * FROM SAKILA.ACTOR WHERE first_name REGEXP 's{1,3}'; # gdje se s pojavljuje 1-3 puta
SELECT * FROM SAKILA.ACTOR WHERE first_name REGEXP 's?'; # gdje se pojavljuje 0 ili 1 puta
SELECT * FROM SAKILA.ACTOR WHERE first_name REGEXP 'joh(n)+'; #kupi sve joh i nijedno ili jedno n poslije
SELECT * FROM SAKILA.ACTOR WHERE first_name REGEXP 'joh(n){2,}'; #kupi sve joh i n 2 ili vise puta poslije
SELECT * FROM SAKILA.ACTOR WHERE first_name REGEXP '^[AB]'; #svi koji pocinju sa a ili b
SELECT * FROM SAKILA.ACTOR WHERE first_name REGEXP '^BO'; #svi koji pocinju sa bo
#() na sta djeluje; [] jedno ili drugo ili trece
SELECT * FROM SAKILA.ACTOR WHERE first_name REGEXP '^...$'; # svi koji imaju samo 3 karaktera
#'...' su karakteri tj . je zamjena za kareter
#zamjena za cifre su \d ; \w su i cifre i slova
SELECT * FROM SAKILA.ACTOR WHERE first_name REGEXP '^.{4}$'; # svi kojimaju tacno 4 karatera
SELECT * FROM SAKILA.ACTOR WHERE first_name REGEXP '^.{2,4}$'; # svi kojimaju tacno 2-4 karatera
SELECT * FROM SAKILA.ACTOR WHERE first_name REGEXP '^[abgtrjkm]'; #svi koji pocinju sa ovim slovima
SELECT * FROM SAKILA.ACTOR WHERE first_name NOT REGEXP '^[abgtrjkm]'; #svi koji ne pocinju sa ovim slovima
#BINARY ako hocemo da bude osjetljiv na velika i mala slova
SELECT * FROM SAKILA.ACTOR WHERE first_name REGEXP BINARY '^[AB]'; #iz nekog razloga ne radi, nece da gubi vrijeme
SELECT * FROM SAKILA.ACTOR WHERE first_name REGEXP BINARY '^[Ab]';








