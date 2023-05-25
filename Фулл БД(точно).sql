-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: hackaton
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `decoding_competency_full`
--

DROP TABLE IF EXISTS `decoding_competency_full`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `decoding_competency_full` (
  `SPECIALTYCODE` int NOT NULL,
  `COMPETENCE1` text NOT NULL,
  `COMPETENCE2` text NOT NULL,
  `COMPETENCE3` text NOT NULL,
  `COMPETENCE4` text NOT NULL,
  `COMPETENCE5` text NOT NULL,
  `COMPETENCE6` text,
  `COMPETENCE7` text,
  `COMPETENCE8` text,
  `COMPETENCE9` text,
  `COMPETENCE10` text,
  `COMPETENCE11` text,
  `COMPETENCE12` text,
  `COMPETENCE13` text,
  `COMPETENCE14` text,
  `COMPETENCE15` text,
  KEY `SPECIALTYCODE` (`SPECIALTYCODE`),
  CONSTRAINT `Decoding_Competency_Full_ibfk_1` FOREIGN KEY (`SPECIALTYCODE`) REFERENCES `specialty_code` (`SPECIALTYCODE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `decoding_competency_full`
--

LOCK TABLES `decoding_competency_full` WRITE;
/*!40000 ALTER TABLE `decoding_competency_full` DISABLE KEYS */;
INSERT INTO `decoding_competency_full` VALUES (109,'Основы SQL','ООП','Математическое моделирование','Технология разработки и защиты баз данных','Основы философии',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `decoding_competency_full` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `specialty_code`
--

DROP TABLE IF EXISTS `specialty_code`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `specialty_code` (
  `SPECIALTYCODE` int NOT NULL AUTO_INCREMENT,
  `SPECIALTYNAME` varchar(255) NOT NULL,
  PRIMARY KEY (`SPECIALTYCODE`)
) ENGINE=InnoDB AUTO_INCREMENT=110 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `specialty_code`
--

LOCK TABLES `specialty_code` WRITE;
/*!40000 ALTER TABLE `specialty_code` DISABLE KEYS */;
INSERT INTO `specialty_code` VALUES (109,'Программист');
/*!40000 ALTER TABLE `specialty_code` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `STUDENTNAME` varchar(255) NOT NULL,
  `DATEOFBIRTH` varchar(50) NOT NULL,
  `GROUPNUMBER` varchar(14) NOT NULL,
  `SPECIALTYCODE` int NOT NULL,
  `TELEPHONENUMBER` varchar(16) NOT NULL,
  `EMAILADDRESS` varchar(32) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Student_ibfk_1` (`SPECIALTYCODE`),
  CONSTRAINT `Student_ibfk_1` FOREIGN KEY (`SPECIALTYCODE`) REFERENCES `specialty_code` (`SPECIALTYCODE`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3669 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1,'Муратов С.С.','28.02.1998','24Вб',109,'80912840','serg@mail.ru'),(3666,'Дубцова С.А.','21.04.2003','24Вб',109,'36293875','sofa@abc.com'),(3668,'Иванов И.А.','13.12.2001','24Вб',109,'892435982','oisn@asdf.ru');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_additional_info`
--

DROP TABLE IF EXISTS `student_additional_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_additional_info` (
  `ADDITIONALINFO` longtext NOT NULL,
  `FOREIGNLANGUAGE` varchar(255) NOT NULL,
  `DRIVERLICENSE` varchar(255) NOT NULL,
  `ADDITIONALCOMPETENCIES` varchar(255) NOT NULL,
  `SOCIALNETWORK` varchar(255) NOT NULL,
  `ID` int DEFAULT NULL,
  KEY `Student_Additional_Info_ibfk_1` (`ID`),
  CONSTRAINT `Student_Additional_Info_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `student` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_additional_info`
--

LOCK TABLES `student_additional_info` WRITE;
/*!40000 ALTER TABLE `student_additional_info` DISABLE KEYS */;
INSERT INTO `student_additional_info` VALUES ('Дополнительная информация','Английский','Да','Дополнительные компетиции','вконтакте.ру',1);
/*!40000 ALTER TABLE `student_additional_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_competencies`
--

DROP TABLE IF EXISTS `student_competencies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_competencies` (
  `ID` int NOT NULL,
  `COMPETENCE1` mediumtext,
  `COMPETENCE2` mediumtext,
  `COMPETENCE3` mediumtext,
  `COMPETENCE4` mediumtext,
  `COMPETENCE5` mediumtext,
  `COMPETENCE6` mediumtext,
  `COMPETENCE7` mediumtext,
  `COMPETENCE8` mediumtext,
  `COMPETENCE9` mediumtext,
  `COMPETENCE10` mediumtext,
  `COMPETENCE11` mediumtext,
  `COMPETENCE12` mediumtext,
  `COMPETENCE13` mediumtext,
  `COMPETENCE14` mediumtext,
  `COMPETENCE15` mediumtext,
  KEY `Student_Competencies_ibfk_2` (`ID`),
  CONSTRAINT `Student_Competencies_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `student` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Student_Competencies_ibfk_2` FOREIGN KEY (`ID`) REFERENCES `student` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_competencies`
--

LOCK TABLES `student_competencies` WRITE;
/*!40000 ALTER TABLE `student_competencies` DISABLE KEYS */;
INSERT INTO `student_competencies` VALUES (1,'Какая-то компетиция',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `student_competencies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_education`
--

DROP TABLE IF EXISTS `student_education`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_education` (
  `ID` int NOT NULL,
  `ESTABLISHMENT` varchar(255) DEFAULT NULL,
  `FACULTY` varchar(255) DEFAULT NULL,
  `FORMOFSTUDY` varchar(255) DEFAULT NULL,
  `YEAROFENDING` varchar(255) DEFAULT NULL,
  `CITY` varchar(255) DEFAULT NULL,
  KEY `Student_Education_ibfk_2` (`ID`),
  CONSTRAINT `Student_Education_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `student` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Student_Education_ibfk_2` FOREIGN KEY (`ID`) REFERENCES `student` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_education`
--

LOCK TABLES `student_education` WRITE;
/*!40000 ALTER TABLE `student_education` DISABLE KEYS */;
INSERT INTO `student_education` VALUES (1,'Колледж на связи №54','Инофрмационные системы и программирование','Очная','2024','Москва');
/*!40000 ALTER TABLE `student_education` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_photo`
--

DROP TABLE IF EXISTS `student_photo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_photo` (
  `ID` int NOT NULL,
  `PHOTO` mediumblob NOT NULL,
  KEY `Student_Photo_ibfk_1` (`ID`),
  CONSTRAINT `Student_Photo_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `student` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_photo`
--

LOCK TABLES `student_photo` WRITE;
/*!40000 ALTER TABLE `student_photo` DISABLE KEYS */;
INSERT INTO `student_photo` VALUES (1,_binary 'Фотография');
/*!40000 ALTER TABLE `student_photo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_soft_skills`
--

DROP TABLE IF EXISTS `student_soft_skills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_soft_skills` (
  `ID` int NOT NULL,
  `FIRSTSOFTSKILL` varchar(255) DEFAULT NULL,
  `SECONDSOFTSKILL` varchar(255) DEFAULT NULL,
  `THIRDSOFTSKILL` varchar(255) DEFAULT NULL,
  `FOURTHOFTSKILL` varchar(255) DEFAULT NULL,
  `FIVETHSOFTSKILL` varchar(255) DEFAULT NULL,
  KEY `Student_Soft_Skills_ibfk_2` (`ID`),
  CONSTRAINT `Student_Soft_Skills_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `student` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Student_Soft_Skills_ibfk_2` FOREIGN KEY (`ID`) REFERENCES `student` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_soft_skills`
--

LOCK TABLES `student_soft_skills` WRITE;
/*!40000 ALTER TABLE `student_soft_skills` DISABLE KEYS */;
INSERT INTO `student_soft_skills` VALUES (1,'Самостоятельность','Общительность','Навыки презентации','Командная работа','Проактивность');
/*!40000 ALTER TABLE `student_soft_skills` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-25 12:16:00
