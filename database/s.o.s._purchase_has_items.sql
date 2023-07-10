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
-- Table structure for table `purchase_has_items`
--

DROP TABLE IF EXISTS `purchase_has_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchase_has_items` (
  `Purchase_PurchaseTransactionID` int NOT NULL,
  `Items_ItemID` int NOT NULL,
  `Amount` int DEFAULT NULL,
  `UnitItemCost` decimal(2,0) DEFAULT NULL,
  PRIMARY KEY (`Purchase_PurchaseTransactionID`,`Items_ItemID`),
  KEY `fk_Purchase_has_Items_Items1_idx` (`Items_ItemID`),
  KEY `fk_Purchase_has_Items_Purchase1_idx` (`Purchase_PurchaseTransactionID`),
  CONSTRAINT `fk_Purchase_has_Items_Items1` FOREIGN KEY (`Items_ItemID`) REFERENCES `items` (`ItemID`),
  CONSTRAINT `fk_Purchase_has_Items_Purchase1` FOREIGN KEY (`Purchase_PurchaseTransactionID`) REFERENCES `purchase` (`PurchaseTransactionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchase_has_items`
--

LOCK TABLES `purchase_has_items` WRITE;
/*!40000 ALTER TABLE `purchase_has_items` DISABLE KEYS */;
/*!40000 ALTER TABLE `purchase_has_items` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-27 23:40:49
