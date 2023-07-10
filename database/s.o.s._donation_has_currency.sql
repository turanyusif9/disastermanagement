-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: s.o.s.
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `donation_has_currency`
--

DROP TABLE IF EXISTS `donation_has_currency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `donation_has_currency` (
  `Donation_DonationID` int NOT NULL,
  `Currency_CurrencyType` varchar(45) NOT NULL,
  `Amount` int DEFAULT NULL,
  PRIMARY KEY (`Donation_DonationID`),
  KEY `fk_Donation_has_Currency_Currency1_idx` (`Currency_CurrencyType`),
  KEY `fk_Donation_has_Currency_Donation1_idx` (`Donation_DonationID`),
  CONSTRAINT `fk_Donation_has_Currency_Currency1` FOREIGN KEY (`Currency_CurrencyType`) REFERENCES `currency` (`CurrencyType`),
  CONSTRAINT `fk_Donation_has_Currency_Donation1` FOREIGN KEY (`Donation_DonationID`) REFERENCES `donation` (`DonationID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `donation_has_currency`
--

LOCK TABLES `donation_has_currency` WRITE;
/*!40000 ALTER TABLE `donation_has_currency` DISABLE KEYS */;
INSERT INTO `donation_has_currency` VALUES (1,'azn',13),(3,'try',1500);
/*!40000 ALTER TABLE `donation_has_currency` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-27 23:40:48
