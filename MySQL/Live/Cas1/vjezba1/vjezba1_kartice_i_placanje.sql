#use model_proba1; koristi shemu
select * from model_proba1.korisnik; #ovo je bolje tj ispravno
#treca varijanta je dupli klik na ime sheme; tako da query koristi tu shemu!
select * from korisnik; # * otvara sve
select idkorisnik,ime from korisnik; # moze i ovako da se imena unose
insert into model_proba1.korisnik values(null, "Mika") #dodaje anu u korisnik; idkorinsik se sam puno zato sto autoincrement sam popunjava
#moze se sad umjesto ANA napisati Mika; i mika ce biti dodan; ana ce biti zadrzana!