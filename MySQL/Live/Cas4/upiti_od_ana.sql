select * from fruitshop2.fruit;
select * from fruitshop2.vfruitinventory;

set sql_safe_updates = 0;

update fruitshop2.fruit set fruitshop2.fruit.FruitName = 'Visnja'
where fruitshop2.fruit.FruitName = 'Apple'; 

update fruitshop2.fruit set fruitshop2.fruit.FruitName = 'Apple'
where fruitshop2.fruit.FruitName = 'Visnja'; 