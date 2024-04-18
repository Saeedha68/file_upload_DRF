-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: api2
-- ------------------------------------------------------
-- Server version	8.0.29

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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-04-15 18:56:49.114665'),(2,'auth','0001_initial','2024-04-15 18:56:49.550205'),(3,'admin','0001_initial','2024-04-15 18:56:49.657844'),(4,'admin','0002_logentry_remove_auto_add','2024-04-15 18:56:49.664883'),(5,'admin','0003_logentry_add_action_flag_choices','2024-04-15 18:56:49.670804'),(6,'contenttypes','0002_remove_content_type_name','2024-04-15 18:56:49.742559'),(7,'auth','0002_alter_permission_name_max_length','2024-04-15 18:56:49.788405'),(8,'auth','0003_alter_user_email_max_length','2024-04-15 18:56:49.812325'),(9,'auth','0004_alter_user_username_opts','2024-04-15 18:56:49.821297'),(10,'auth','0005_alter_user_last_login_null','2024-04-15 18:56:49.873122'),(11,'auth','0006_require_contenttypes_0002','2024-04-15 18:56:49.875115'),(12,'auth','0007_alter_validators_add_error_messages','2024-04-15 18:56:49.882095'),(13,'auth','0008_alter_user_username_max_length','2024-04-15 18:56:49.938905'),(14,'auth','0009_alter_user_last_name_max_length','2024-04-15 18:56:49.997706'),(15,'auth','0010_alter_group_name_max_length','2024-04-15 18:56:50.012655'),(16,'auth','0011_update_proxy_permissions','2024-04-15 18:56:50.020628'),(17,'auth','0012_alter_user_first_name_max_length','2024-04-15 18:56:50.079432'),(18,'authtoken','0001_initial','2024-04-15 18:56:50.150196'),(19,'authtoken','0002_auto_20160226_1747','2024-04-15 18:56:50.172121'),(20,'authtoken','0003_tokenproxy','2024-04-15 18:56:50.176109'),(21,'authtoken','0004_alter_tokenproxy_options','2024-04-15 18:56:50.180098'),(22,'fileupload','0001_initial','2024-04-15 18:56:50.208998'),(23,'sessions','0001_initial','2024-04-15 18:56:50.247867'),(24,'fileupload','0002_alter_document_text','2024-04-15 19:13:15.447418'),(25,'fileupload','0003_rename_text_document_path','2024-04-15 19:46:40.744296'),(26,'fileupload','0004_mymodel_rename_image_image_path','2024-04-16 22:36:57.478529');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-19  2:04:15
