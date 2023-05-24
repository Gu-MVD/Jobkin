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
-- Table structure for table `decoding_competency`
--

DROP TABLE IF EXISTS `decoding_competency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `decoding_competency` (
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
  CONSTRAINT `Decoding_Competency_ibfk_1` FOREIGN KEY (`SPECIALTYCODE`) REFERENCES `specialty_code` (`SPECIALTYCODE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `decoding_competency`
--

LOCK TABLES `decoding_competency` WRITE;
/*!40000 ALTER TABLE `decoding_competency` DISABLE KEYS */;
/*!40000 ALTER TABLE `decoding_competency` ENABLE KEYS */;
UNLOCK TABLES;

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
/*!40000 ALTER TABLE `decoding_competency_full` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `driver_license`
--

DROP TABLE IF EXISTS `driver_license`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `driver_license` (
  `id` int NOT NULL AUTO_INCREMENT,
  `DRIVERLICENSE` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `driver_license`
--

LOCK TABLES `driver_license` WRITE;
/*!40000 ALTER TABLE `driver_license` DISABLE KEYS */;
/*!40000 ALTER TABLE `driver_license` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `foreign_language`
--

DROP TABLE IF EXISTS `foreign_language`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `foreign_language` (
  `id` int NOT NULL AUTO_INCREMENT,
  `FOREIGNLANGUAGE` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `foreign_language`
--

LOCK TABLES `foreign_language` WRITE;
/*!40000 ALTER TABLE `foreign_language` DISABLE KEYS */;
/*!40000 ALTER TABLE `foreign_language` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `form_of_study`
--

DROP TABLE IF EXISTS `form_of_study`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `form_of_study` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `FORMOFSTUDY` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `form_of_study`
--

LOCK TABLES `form_of_study` WRITE;
/*!40000 ALTER TABLE `form_of_study` DISABLE KEYS */;
/*!40000 ALTER TABLE `form_of_study` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `soft_skills`
--

DROP TABLE IF EXISTS `soft_skills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `soft_skills` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `SOFTSKILLS` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Soft_Skill_UNIQUE` (`SOFTSKILLS`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soft_skills`
--

LOCK TABLES `soft_skills` WRITE;
/*!40000 ALTER TABLE `soft_skills` DISABLE KEYS */;
/*!40000 ALTER TABLE `soft_skills` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=3668 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (3665,'Муратов С.С.','28.02.1998','24Вб',109,'79912767159','sergmur@mail.ru'),(3667,'Дубцова','21.04.2003','24Вб',109,'0913580983','sof@abc.com');
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
/*!40000 ALTER TABLE `student_education` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_job`
--

DROP TABLE IF EXISTS `student_job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_job` (
  `ID` int NOT NULL,
  `COMPANYNAME` varchar(255) DEFAULT NULL,
  `POSITION` varchar(255) DEFAULT NULL,
  `EXPERIENCE` varchar(255) DEFAULT NULL,
  `FUNCTION` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_job`
--

LOCK TABLES `student_job` WRITE;
/*!40000 ALTER TABLE `student_job` DISABLE KEYS */;
/*!40000 ALTER TABLE `student_job` ENABLE KEYS */;
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
/*!40000 ALTER TABLE `student_photo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_practice`
--

DROP TABLE IF EXISTS `student_practice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_practice` (
  `ID` int NOT NULL,
  `COMPANYNAME` varchar(255) DEFAULT NULL,
  `POSITION` varchar(255) DEFAULT NULL,
  `EXPERIENCE` varchar(255) DEFAULT NULL,
  `FUNCTION` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_practice`
--

LOCK TABLES `student_practice` WRITE;
/*!40000 ALTER TABLE `student_practice` DISABLE KEYS */;
/*!40000 ALTER TABLE `student_practice` ENABLE KEYS */;
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
/*!40000 ALTER TABLE `student_soft_skills` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `year_of_ending`
--

DROP TABLE IF EXISTS `year_of_ending`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `year_of_ending` (
  `id` int NOT NULL AUTO_INCREMENT,
  `YEAROFENDING` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `year_of_ending`
--

LOCK TABLES `year_of_ending` WRITE;
/*!40000 ALTER TABLE `year_of_ending` DISABLE KEYS */;
/*!40000 ALTER TABLE `year_of_ending` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-23 21:51:11
