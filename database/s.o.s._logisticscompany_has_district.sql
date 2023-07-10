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
-- Table structure for table `logisticscompany_has_district`
--

DROP TABLE IF EXISTS `logisticscompany_has_district`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `logisticscompany_has_district` (
  `LogisticsCompany_CompanyID` int NOT NULL,
  `District_DistrictID` int NOT NULL,
  `CostOfOutsource` decimal(2,0) DEFAULT NULL,
  PRIMARY KEY (`LogisticsCompany_CompanyID`,`District_DistrictID`),
  KEY `fk_LogisticsCompany_has_District_District1_idx` (`District_DistrictID`),
  KEY `fk_LogisticsCompany_has_District_LogisticsCompany1_idx` (`LogisticsCompany_CompanyID`),
  CONSTRAINT `fk_LogisticsCompany_has_District_District1` FOREIGN KEY (`District_DistrictID`) REFERENCES `district` (`DistrictID`),
  CONSTRAINT `fk_LogisticsCompany_has_District_LogisticsCompany1` FOREIGN KEY (`LogisticsCompany_CompanyID`) REFERENCES `logisticscompany` (`CompanyID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logisticscompany_has_district`
--

LOCK TABLES `logisticscompany_has_district` WRITE;
/*!40000 ALTER TABLE `logisticscompany_has_district` DISABLE KEYS */;
INSERT INTO `logisticscompany_has_district` VALUES (1,2,16),(2,1,14);
/*!40000 ALTER TABLE `logisticscompany_has_district` ENABLE KEYS */;
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
