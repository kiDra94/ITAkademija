CREATE TABLE `poruke` (
  `idporuke` int(11) NOT NULL AUTO_INCREMENT,
  `tekst` varchar(45) DEFAULT NULL,
  `idroditelj` int(11) DEFAULT NULL,
  PRIMARY KEY (`idporuke`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

INSERT INTO `poruke` VALUES (1,'Kako si?',0),(2,'Dobro sam, a ti?',1),(3,'Evo nije loše.',2),(4,'A kako si ti?',0),(5,'Evo, i ja sam dobro.',1);
UNLOCK TABLES;

SELECT * FROM poruke;

UPDATE poruke SET idroditelj = 4 WHERE idporuke = 5; 

SELECT a.tekst,b.tekst FROM poruke AS a,poruke AS b
WHERE a.idporuke=b.idroditelj;

#popunjavanje organizacije
INSERT INTO organizacija SELECT * FROM poruke; #presipamo sve iz tabele poruke tj kopiramo sve
SELECT * FROM organizacija; 
CREATE TABLE poruke_backup AS SELECT * FROM poruke; #najjeftiniji nacin za pravljenje backup-a
SELECT * FROM poruke_backup; 
TRUNCATE TABLE organizacija; #ili delete from organizacija; (safemode mora biti uncheked)
INSERT INTO `organizacija` VALUES 
(null,'Direktor',0), #null -> zato sto je autoincrement
(null,'Menadzer1',1),
(null,'Menadzer2',1),
(null,'Menadzer3',2),
(null,'Radnik',4);
UNLOCK TABLES;
SELECT * FROM organizacija; 
SELECT a.pozicija,b.pozicija FROM organizacija AS a,organizacija AS b
WHERE a.idorganizacija=b.id_nadredjenog;
SELECT a.pozicija AS nadredjeni, b.pozicija AS podredjeni FROM organizacija AS a INNER JOIN organizacija AS b
ON a.idorganizacija=b.id_nadredjenog; #radi istcustomerso kao zapis iznad!

SELECT * FROM customers; 
TRUNCATE TABLE customers;
SELECT * FROM customers WHERE address = 'Valley 345'; 




