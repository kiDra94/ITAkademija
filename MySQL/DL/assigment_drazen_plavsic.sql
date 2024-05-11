-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: assigment_drazen_plavsic
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `korespondencija`
--

DROP TABLE IF EXISTS `korespondencija`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `korespondencija` (
  `korespondencija_id` int NOT NULL AUTO_INCREMENT,
  `poruka` mediumtext,
  `datum` datetime NOT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `posaljilac_korisnik_id` int NOT NULL,
  `primaoc_korisnik_id` int NOT NULL,
  PRIMARY KEY (`korespondencija_id`),
  KEY `fk_korespondencija_korisnik1_idx` (`posaljilac_korisnik_id`),
  KEY `fk_korespondencija_korisnik2_idx` (`primaoc_korisnik_id`),
  CONSTRAINT `fk_korespondencija_korisnik1` FOREIGN KEY (`posaljilac_korisnik_id`) REFERENCES `korisnik` (`korisnik_id`),
  CONSTRAINT `fk_korespondencija_korisnik2` FOREIGN KEY (`primaoc_korisnik_id`) REFERENCES `korisnik` (`korisnik_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `korespondencija`
--

LOCK TABLES `korespondencija` WRITE;
/*!40000 ALTER TABLE `korespondencija` DISABLE KEYS */;
INSERT INTO `korespondencija` VALUES (1,'cao','2024-04-02 07:56:00',1,1,2),(2,'cao!!','2024-04-02 07:56:15',1,2,1),(3,'mozes li mi poslati link','2024-04-02 07:59:15',1,1,2),(4,'naracvno stize za minut','2024-04-02 07:59:55',1,2,1),(5,'zasto me si ignorisu','2024-04-02 08:15:00',1,3,1),(6,'zasto me si ignorisu','2024-04-02 08:15:00',1,3,2),(7,'je li stize poruka','2024-04-02 08:15:35',0,2,3),(8,'je li stize poruka','2024-04-02 08:15:35',0,1,3);
/*!40000 ALTER TABLE `korespondencija` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `korisnik`
--

DROP TABLE IF EXISTS `korisnik`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `korisnik` (
  `korisnik_id` int NOT NULL AUTO_INCREMENT,
  `ime` varchar(45) NOT NULL,
  `prezime` varchar(45) NOT NULL,
  `datum_rodjenja` date NOT NULL,
  `email_adresa` varchar(45) DEFAULT NULL,
  `korisnicko_ime` varchar(45) NOT NULL,
  `biografija` tinytext,
  `fotografija` blob,
  PRIMARY KEY (`korisnik_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `korisnik`
--

LOCK TABLES `korisnik` WRITE;
/*!40000 ALTER TABLE `korisnik` DISABLE KEYS */;
INSERT INTO `korisnik` VALUES (1,'Drazen','Plavsic','1994-07-27','drazen@hotmail.com','dpla','nesto o meni',NULL),(2,'Jovan','Ivic','1992-04-02','jovan@hotmail.com','jivi','nesto o meni',NULL),(3,'Milica','Jovanovic','1993-05-11','milica@hotmail.com','mjov','nesto o meni',NULL);
/*!40000 ALTER TABLE `korisnik` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plate`
--

DROP TABLE IF EXISTS `plate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plate` (
  `plate_id` int NOT NULL AUTO_INCREMENT,
  `datum` date NOT NULL,
  `iznos` decimal(10,4) NOT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `korisnik_korisnik_id` int NOT NULL,
  PRIMARY KEY (`plate_id`),
  KEY `fk_plate_korisnik_idx` (`korisnik_korisnik_id`),
  CONSTRAINT `fk_plate_korisnik` FOREIGN KEY (`korisnik_korisnik_id`) REFERENCES `korisnik` (`korisnik_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plate`
--

LOCK TABLES `plate` WRITE;
/*!40000 ALTER TABLE `plate` DISABLE KEYS */;
INSERT INTO `plate` VALUES (1,'2023-04-02',1254.9900,1,1),(2,'2023-04-02',1459.5400,0,1),(3,'2023-04-02',1234.4400,0,2),(4,'2023-04-01',1456.6900,0,3);
/*!40000 ALTER TABLE `plate` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-05  6:39:19
