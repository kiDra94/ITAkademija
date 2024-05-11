select * from sakila.actor;
select * from sakila.actor where first_name='Scarlett';
select * from sakila.actor where last_name like 'Joh%';
select distinct last_name from sakila.actor; #disticnt= razliciti!!!
select count(distinct last_name) from sakila.actor;
select count(*) from sakila.actor;
select count(*) from 
(select last_name from sakila.actor group by last_name) as prezimena;
select last_name,count(last_name) as broj from sakila.actor group by last_name 
order by broj desc; 
select last_name,count(last_name) as broj from sakila.actor group by last_name 
order by broj desc limit 5; 
select last_name,count(last_name) as broj from sakila.actor group by last_name 
having count(last_name) > 1; #having je where kad se koristi group by
#povezivanje tabela film i actor
select count(*) from sakila.actor; #200
select count(*) from sakila.film_actor; #5462
select count(*) from sakila.film; #1000
select count(*) from sakila.actor, sakila.film_actor; #1 092 400 pogresno ne provjerava kljuceve !!! 
select count(*) from sakila.actor, sakila.film_actor, sakila.film; #1 092 400 000
select count(*) from sakila.actor, sakila.film_actor 
where sakila.actor.actor_id = sakila.film_actor.actor_id; #5462 provjera kljuceve!; ovo su samo glumci
select count(*) from sakila.actor, sakila.film_actor, sakila.film 
where sakila.actor.actor_id = sakila.film_actor.actor_id 
and sakila.film.film_id = sakila.film_actor.film_id;#5462 provjera kljuceve!
select * from sakila.actor, sakila.film_actor, sakila.film 
where sakila.actor.actor_id = sakila.film_actor.actor_id 
and sakila.film.film_id = sakila.film_actor.film_id; #spaja sve tabele jednu do druge; treba skratiti
select first_name, last_name, title, length  from sakila.actor, sakila.film_actor, sakila.film 
where sakila.actor.actor_id = sakila.film_actor.actor_id 
and sakila.film.film_id = sakila.film_actor.film_id; #skracen upit; u sustini unesi sam sta ti treba!
#sakila.actor.actor_id = sakila.film_actor.actor_id and sakila.film.film_id = sakila.film_actor.film_id -> kljucni dio koda
# najduzi film, svi filmovi duzi od 2h i koliko ih ima sve filmove gdje glumi 'PENELOPE'
select first_name, last_name, title, length  from sakila.actor, sakila.film_actor, sakila.film 
where sakila.actor.actor_id = sakila.film_actor.actor_id 
and sakila.film.film_id = sakila.film_actor.film_id order by length desc limit 1; #najduzi
select first_name, last_name, title, length  from sakila.actor, sakila.film_actor, sakila.film 
where sakila.actor.actor_id = sakila.film_actor.actor_id 
and sakila.film.film_id = sakila.film_actor.film_id and length > 120 order by length; #duzi od 2h
select count(*) from (select first_name, last_name, title, length  from sakila.actor, sakila.film_actor, sakila.film 
where sakila.actor.actor_id = sakila.film_actor.actor_id 
and sakila.film.film_id = sakila.film_actor.film_id and length > 120 order by length) as broj; #2497 duzih od 2 sata
select first_name, last_name, title, length  from sakila.actor, sakila.film_actor, sakila.film 
where sakila.actor.actor_id = sakila.film_actor.actor_id 
and sakila.film.film_id = sakila.film_actor.film_id and first_name='PENELOPE';
#koki glumac glumi u koliko filmova?
select a.first_name, a.last_name, count(*) as broj_uloga from sakila.actor as a, sakila.film_actor as fa 
where a.actor_id = fa.actor_id group by fa.actor_id order by broj_uloga desc;
# da li je film Academy Dinosauer dostupan u store 1
select * from sakila.inventory;
select f.title, s.store_id from sakila.store as s, sakila.inventory as i, sakila.film as f
where f.film_id = i.film_id and s.store_id = i.store_id and f.title='Academy Dinosaur';
select f.title,s.store_id  from sakila.film as f join sakila.inventory as i using(film_id) join sakila.store as s using(store_id)
where f.title = 'Academy Dinosaur' and s.store_id = 1;


