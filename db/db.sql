-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: soiree
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item` (
  `iid` int NOT NULL AUTO_INCREMENT,
  `desc_p` varchar(85) DEFAULT NULL,
  `desc_g` varchar(256) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `calificacion` int DEFAULT NULL,
  `ubicacion` varchar(256) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `tipo` enum('Comida','Inmuebles','Floreria','Lugar') DEFAULT NULL,
  `nombre` varchar(10) DEFAULT NULL,
  `img` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`iid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item`
--

LOCK TABLES `item` WRITE;
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` VALUES (1,'Descripcion 1','Descripcion grande 1',19.99,5,'Ubicacion 1','2023-10-15','Comida','Nombre 1','img/evento1.jpg'),(2,'Descripcion 2','Descripcion grande 2',29.99,4,'Ubicacion 2','2023-10-16','Inmuebles','Nombre 2','img/evento1.jpg'),(3,'Descripcion 3','Descripcion grande 3',39.99,3,'Ubicacion 3','2023-10-17','Floreria','Nombre 3','img/evento1.jpg'),(4,'Descripcion 4','Descripcion grande 4',49.99,4,'Ubicacion 4','2023-10-18','Comida','Nombre 4','img/evento1.jpg'),(5,'Descripcion 5','Descripcion grande 5',59.99,5,'Ubicacion 5','2023-10-19','Inmuebles','Nombre 5','img/evento1.jpg'),(6,'Descripcion 6','Descripcion grande 6',69.99,3,'Ubicacion 6','2023-10-20','Floreria','Nombre 6','img/evento1.jpg'),(7,'Descripcion 7','Descripcion grande 7',79.99,4,'Ubicacion 7','2023-10-21','Comida','Nombre 7','img/evento1.jpg'),(8,'Descripcion 8','Descripcion grande 8',89.99,5,'Ubicacion 8','2023-10-22','Inmuebles','Nombre 8','img/evento1.jpg'),(9,'Descripcion 9','Descripcion grande 9',99.99,3,'Ubicacion 9','2023-10-23','Floreria','Nombre 9','img/evento1.jpg'),(10,'Descripcion 10','Descripcion grande 10',109.99,4,'Ubicacion 10','2023-10-24','Comida','Nombre 10','img/evento1.jpg');
/*!40000 ALTER TABLE `item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `uid` int NOT NULL AUTO_INCREMENT,
  `email` varchar(256) DEFAULT NULL,
  `password` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'juan','123'),(2,'joel','123');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-16 23:31:04
