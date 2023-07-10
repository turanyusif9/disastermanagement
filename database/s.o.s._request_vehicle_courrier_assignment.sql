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
-- Table structure for table `request_vehicle_courrier_assignment`
--

DROP TABLE IF EXISTS `request_vehicle_courrier_assignment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `request_vehicle_courrier_assignment` (
  `Request_RequestID` int NOT NULL,
  `Courier_CourierID` int NOT NULL,
  `Vehicle_VehicleID` int NOT NULL,
  `DeliveryTime` date DEFAULT NULL,
  PRIMARY KEY (`Request_RequestID`,`Courier_CourierID`,`Vehicle_VehicleID`),
  KEY `fk_Request_has_Courier_Courier1_idx` (`Courier_CourierID`),
  KEY `fk_Request_has_Courier_Request1_idx` (`Request_RequestID`),
  KEY `fk_Request_has_Courier_Vehicle1_idx` (`Vehicle_VehicleID`),
  CONSTRAINT `fk_Request_has_Courier_Courier1` FOREIGN KEY (`Courier_CourierID`) REFERENCES `courier` (`CourierID`),
  CONSTRAINT `fk_Request_has_Courier_Request1` FOREIGN KEY (`Request_RequestID`) REFERENCES `request` (`RequestID`),
  CONSTRAINT `fk_Request_has_Courier_Vehicle1` FOREIGN KEY (`Vehicle_VehicleID`) REFERENCES `vehicle` (`VehicleID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `request_vehicle_courrier_assignment`
--

LOCK TABLES `request_vehicle_courrier_assignment` WRITE;
/*!40000 ALTER TABLE `request_vehicle_courrier_assignment` DISABLE KEYS */;
INSERT INTO `request_vehicle_courrier_assignment` VALUES (1,2,12,'2020-10-24'),(2,1,3,'2020-11-23');
/*!40000 ALTER TABLE `request_vehicle_courrier_assignment` ENABLE KEYS */;
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
