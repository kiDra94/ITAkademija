#zadatak da izvucemo podatke o focu koje se prodaje na komad
SELECT * FROM fruitshop2.fruit
where UnitID = 1;

SELECT * FROM fruitshop2.units
where UnitName = 'Piece';

SELECT UnitId FROM fruitshop2.units
where UnitName = 'Piece'; #vraca unitID tj 1

SELECT * FROM fruitshop2.fruit
where UnitID = (SELECT UnitId FROM fruitshop2.units
where UnitName = 'Piece');

select * from fruitshop2.units, fruitshop2.fruit
where fruitshop2.units.UnitId = fruitshop2.fruit.UnitId
and fruitshop2.units.UnitName = 'Piece';

select fruitshop2.fruit.FruitName from fruitshop2.units, fruitshop2.fruit
where fruitshop2.units.UnitId = fruitshop2.fruit.UnitId
and fruitshop2.units.UnitName = 'Piece';

select * from fruitshop2.units inner join fruitshop2.fruit
on fruitshop2.units.UnitId = fruitshop2.fruit.UnitId
and fruitshop2.units.UnitName = 'Piece'; #inner join spaje samo odgovarajuce koje trazimo iz obe tabele

select * from fruitshop2.units left join fruitshop2.fruit
on fruitshop2.units.UnitId = fruitshop2.fruit.UnitId
and fruitshop2.units.UnitName = 'Piece'; #uzima u obzir cijelu lijevu tabelu tj ispise sve iz lijeve i ono sto se mecuje sa desnom

SELECT * FROM Fruit
WHERE Inventory <= 10;

SELECT * FROM Fruit
WHERE UnitId = 1 OR UnitId = 2;

SELECT * FROM Fruit
WHERE DateEntered
BETWEEN '2015-01-25' AND '2015-02-25';

SELECT * FROM Fruit
WHERE NOT (FruitName = 'Apple');

set sql_safe_updates = 0;

UPDATE Fruit
SET UnitId = 2
WHERE FruitName = 'Apple';

select * from Fruit;

UPDATE Fruit
SET UnitId = 1
WHERE FruitName = 'Apple';

set sql_safe_updates = 1;

UPDATE Fruit
SET FruitName = 'Red Grapes', Inventory = '11'
WHERE FruitId = 5;

DELETE FROM Fruit; #brise sve ako nema were, i normalno ne radi dok je safemode upaljen

#kad su velike tabele i zelim sve da ih obrisemo koristimo truncate (mnogo brze od delete)

truncate table fruitshop2.fruit;