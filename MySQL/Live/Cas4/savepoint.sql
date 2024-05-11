set autocommit=0; 
select * from fruitshop2.fruit;
delete from fruitshop2.fruit where FruitId=5;
commit;
delete from fruitshop2.fruit where FruitId=2;
savepoint orders_import1;
delete from fruitshop2.fruit where FruitId=4;
rollback to orders_import1; #vraca sve podatke do ovog savepointa (fali 2 i 5)
rollback; #vraca sve podatke do posljednjeg commita (fali samo 5)
commit;
truncate table fruitshop2.fruit; #za ovu komandu ne treba commit!!!