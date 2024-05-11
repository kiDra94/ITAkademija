set autocommit=0; /*iskljucuje automatski potvrdu; u ovom slucaju bi 
ana vidila podatke u tabeli iako je ona obrisana!!!; tj u memoriji je obrisana informacija
dok je na harddisku jos uvijek tu*/
set sql_safe_updates=0;
delete from fruitshop2.fruit;
select * from fruitshop2.fruit; #upamtio u memoriji delete; ikao nisu obrisani vidi gore!
rollback; /*vraca podatke iz memorije nazad; nesto kao undo; radi samo kad je
autocommit iskljucen tj 0*/
select * from fruitshop2.fruit;

delete from fruitshop2.fruit;
commit; #brise sa harddiska; tako da i ana ne vidi nista
/*transakcija je radnja koja je cijela zavrsena; od promjene do izvrsenja;
ona se potvrdjuje sa commit-om*/

INSERT INTO Fruit
VALUES
(1,'Apple',10,1,'2015-02-15 10:30:00','2015-02-15 10:30:00'),
(2,'Orange',5,2,'2015-02-15 10:30:00','2015-02-15 10:30:00'),
(3,'Banana',20,6,'2015-02-15 10:30:00','2015-02-15 10:30:00'),
(4,'Watermelon',10,1,'2015-02-15 10:30:00','2015-02-15 10:30:00'),
(5,'Grapes',15,6,'2015-02-15 10:30:00','2015-02-15 10:30:00'),
(6,'Strawberry',12,7,'2015-02-15 10:30:00','2015-02-15 10:30:00');
commit;