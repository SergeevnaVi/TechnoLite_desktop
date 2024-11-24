-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: shop
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `cart_items`
--

DROP TABLE IF EXISTS `cart_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart_items` (
  `id_cart_item` int NOT NULL AUTO_INCREMENT,
  `id_user` int NOT NULL,
  `id_product` int NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`id_cart_item`),
  KEY `id_user` (`id_user`),
  KEY `id_product` (`id_product`),
  CONSTRAINT `cart_items_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`) ON DELETE CASCADE,
  CONSTRAINT `cart_items_ibfk_2` FOREIGN KEY (`id_product`) REFERENCES `products` (`id_product`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart_items`
--

LOCK TABLES `cart_items` WRITE;
/*!40000 ALTER TABLE `cart_items` DISABLE KEYS */;
INSERT INTO `cart_items` VALUES (30,24,57,1),(31,24,7,3);
/*!40000 ALTER TABLE `cart_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `id_category` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id_category`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (2,'Компьютеры, ноутбуки и планшеты'),(3,'Смартфоны и гаджеты'),(1,'Телевизоры и Цифровое ТВ'),(5,'Техника для дома'),(4,'Техника для кухни');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `delivery_methods`
--

DROP TABLE IF EXISTS `delivery_methods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delivery_methods` (
  `id_method` int NOT NULL AUTO_INCREMENT,
  `method_name` varchar(255) NOT NULL,
  `cost` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id_method`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delivery_methods`
--

LOCK TABLES `delivery_methods` WRITE;
/*!40000 ALTER TABLE `delivery_methods` DISABLE KEYS */;
INSERT INTO `delivery_methods` VALUES (1,'Courier',500.00),(2,'Pickup Point',0.00),(3,'Express Delivery',1550.00);
/*!40000 ALTER TABLE `delivery_methods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manufacturers`
--

DROP TABLE IF EXISTS `manufacturers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manufacturers` (
  `id_manufacturer` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id_manufacturer`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manufacturers`
--

LOCK TABLES `manufacturers` WRITE;
/*!40000 ALTER TABLE `manufacturers` DISABLE KEYS */;
INSERT INTO `manufacturers` VALUES (5,'Apple'),(9,'Gorenje'),(3,'Haier'),(6,'Honor'),(2,'LG'),(8,'Philips'),(1,'Samsung'),(7,'Tefal'),(10,'Weissgauff'),(4,'Xiaomi');
/*!40000 ALTER TABLE `manufacturers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_details`
--

DROP TABLE IF EXISTS `order_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_details` (
  `id_order_detail` int NOT NULL AUTO_INCREMENT,
  `id_order` int NOT NULL,
  `id_product` int NOT NULL,
  `quantity` int NOT NULL,
  `price` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id_order_detail`),
  KEY `id_order` (`id_order`),
  KEY `id_product` (`id_product`),
  CONSTRAINT `order_details_ibfk_1` FOREIGN KEY (`id_order`) REFERENCES `orders` (`id_order`) ON DELETE CASCADE,
  CONSTRAINT `order_details_ibfk_2` FOREIGN KEY (`id_product`) REFERENCES `products` (`id_product`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_details`
--

LOCK TABLES `order_details` WRITE;
/*!40000 ALTER TABLE `order_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `order_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_status_history`
--

DROP TABLE IF EXISTS `order_status_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_status_history` (
  `id_history` int NOT NULL AUTO_INCREMENT,
  `id_order` int NOT NULL,
  `id_order_status` int NOT NULL,
  `changed_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_history`),
  KEY `id_order` (`id_order`),
  KEY `id_order_status` (`id_order_status`),
  CONSTRAINT `order_status_history_ibfk_1` FOREIGN KEY (`id_order`) REFERENCES `orders` (`id_order`) ON DELETE CASCADE,
  CONSTRAINT `order_status_history_ibfk_2` FOREIGN KEY (`id_order_status`) REFERENCES `order_statuses` (`id_order_status`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_status_history`
--

LOCK TABLES `order_status_history` WRITE;
/*!40000 ALTER TABLE `order_status_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `order_status_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_statuses`
--

DROP TABLE IF EXISTS `order_statuses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_statuses` (
  `id_order_status` int NOT NULL AUTO_INCREMENT,
  `status_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id_order_status`),
  UNIQUE KEY `status_name` (`status_name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_statuses`
--

LOCK TABLES `order_statuses` WRITE;
/*!40000 ALTER TABLE `order_statuses` DISABLE KEYS */;
INSERT INTO `order_statuses` VALUES (5,'cancelled'),(4,'delivered'),(1,'pending'),(2,'processing'),(3,'shipped');
/*!40000 ALTER TABLE `order_statuses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id_order` int NOT NULL AUTO_INCREMENT,
  `id_user` int NOT NULL,
  `id_order_status` int NOT NULL,
  `id_payment_status` int NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `shipping_address` text,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_order`),
  KEY `id_user` (`id_user`),
  KEY `id_order_status` (`id_order_status`),
  KEY `id_payment_status` (`id_payment_status`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`) ON DELETE CASCADE,
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`id_order_status`) REFERENCES `order_statuses` (`id_order_status`) ON DELETE CASCADE,
  CONSTRAINT `orders_ibfk_3` FOREIGN KEY (`id_payment_status`) REFERENCES `payment_statuses` (`id_payment_status`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,1,2,2,12000.00,'ул. Тверская, д. 12, Москва, Россия','2024-11-17 15:53:01'),(2,2,1,1,42050.50,'ул. Ленина, д. 45, Санкт-Петербург, Россия','2024-11-17 15:53:01'),(3,3,4,1,12356.00,'пр. Мира, д. 78, Новосибирск, Россия','2024-11-17 15:53:01'),(4,4,5,3,41000.50,'ул. Пушкина, д. 21, Казань, Россия','2024-11-17 15:53:01'),(5,5,3,2,78023.00,'ул. Севастопольская, д. 9, Екатеринбург, Россия','2024-11-17 15:53:01');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment_statuses`
--

DROP TABLE IF EXISTS `payment_statuses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment_statuses` (
  `id_payment_status` int NOT NULL AUTO_INCREMENT,
  `payment_status_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id_payment_status`),
  UNIQUE KEY `payment_status_name` (`payment_status_name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment_statuses`
--

LOCK TABLES `payment_statuses` WRITE;
/*!40000 ALTER TABLE `payment_statuses` DISABLE KEYS */;
INSERT INTO `payment_statuses` VALUES (2,'completed'),(3,'failed'),(1,'pending');
/*!40000 ALTER TABLE `payment_statuses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `id_payment` int NOT NULL AUTO_INCREMENT,
  `id_order` int NOT NULL,
  `payment_method` varchar(50) NOT NULL,
  `id_payment_status` int NOT NULL,
  PRIMARY KEY (`id_payment`),
  KEY `id_order` (`id_order`),
  KEY `id_payment_status` (`id_payment_status`),
  CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`id_order`) REFERENCES `orders` (`id_order`) ON DELETE CASCADE,
  CONSTRAINT `payments_ibfk_2` FOREIGN KEY (`id_payment_status`) REFERENCES `payment_statuses` (`id_payment_status`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
INSERT INTO `payments` VALUES (1,1,'Карта',2),(2,2,'СБП',1);
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_characteristics`
--

DROP TABLE IF EXISTS `product_characteristics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_characteristics` (
  `id_characteristic` int NOT NULL AUTO_INCREMENT,
  `id_product` int NOT NULL,
  `characteristic_name` varchar(255) NOT NULL,
  `characteristic_value` varchar(255) NOT NULL,
  PRIMARY KEY (`id_characteristic`),
  KEY `id_product` (`id_product`),
  CONSTRAINT `product_characteristics_ibfk_1` FOREIGN KEY (`id_product`) REFERENCES `products` (`id_product`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=181 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_characteristics`
--

LOCK TABLES `product_characteristics` WRITE;
/*!40000 ALTER TABLE `product_characteristics` DISABLE KEYS */;
INSERT INTO `product_characteristics` VALUES (1,1,'Диагональ','50\"'),(2,1,'Разрешение экрана','3840x2160 Пикс (4K Ultra HD)'),(3,1,'Страна','Египет'),(4,2,'Диагональ','55\"'),(5,2,'Разрешение экрана','3840x2160 Пикс (4K Ultra HD)'),(6,2,'Страна','Польша'),(7,3,'Диагональ','55\"'),(8,3,'Разрешение экрана','3840x2160 Пикс (4K Ultra HD)'),(9,3,'Страна','Китай'),(10,4,'Диагональ','32\"'),(11,4,'Разрешение экрана','1366x768 Пикс (720 HD)'),(12,4,'Страна','Китай'),(13,5,'Тип наушников','Вкладыши'),(14,5,'Цвет','Light Blue'),(15,5,'Частотный диапазон','20 - 20000 Гц'),(16,6,'Тип наушников','Вставные'),(17,6,'Цвет','Wireless Graphite'),(18,6,'Емкость аккумулятора','515 мА*ч'),(19,7,'Тип наушников','Накладные'),(20,7,'Цвет','Pink'),(21,7,'Частотный диапазон','8-20000 Гц'),(22,8,'Тип наушников','Вкладыши'),(23,8,'Цвет','Graphite Black'),(24,8,'Частотный диапазон','16-40000 Гц'),(25,9,'Память','512GB'),(26,9,'Цвет','Titanium Gray'),(27,9,'Диагональ экрана','6.67\"'),(28,10,'Память','256GB'),(29,10,'Цвет','Black'),(30,10,'Диагональ экрана','6.67\"'),(31,11,'Память','256GB'),(32,11,'Цвет','Midnight'),(33,11,'Диагональ экрана','6.1\"'),(34,12,'Память','256GB'),(35,12,'Цвет','Emerald Green'),(36,12,'Диагональ экрана','6.7\"'),(37,13,'Память','256GB'),(38,13,'Цвет','Space Gray'),(39,13,'Диагональ экрана','12.1\"'),(40,14,'Память','128GB'),(41,14,'Цвет','Mist Blue'),(42,14,'Диагональ экрана','11\"'),(43,15,'Память','256GB'),(44,15,'Цвет','Gray'),(45,15,'Диагональ экрана','14.6\"'),(46,16,'Память','128GB'),(47,16,'Цвет','Blue'),(48,16,'Диагональ экрана','13\"'),(49,17,'Емкость аккумулятора','460 мА*ч'),(50,17,'Цвет','Silver'),(51,17,'Диагональ экрана','1.75\"'),(52,18,'Емкость аккумулятора','470 мА*ч'),(53,18,'Цвет','Midnight Black'),(54,18,'Диагональ экрана','2\"'),(55,19,'Емкость аккумулятора','451 мА*ч'),(56,19,'Цвет','Gold'),(57,19,'Диагональ экрана','1.75\"'),(58,20,'Емкость аккумулятора','300 мА*ч'),(59,20,'Цвет','Silver'),(60,20,'Диагональ экрана','1.75\"'),(61,21,'Тип','Двухкамерный'),(62,21,'Цвет','White'),(63,21,'Полезный объем','400 л'),(64,22,'Тип','Side-by-Side'),(65,22,'Цвет','Dark Silver'),(66,22,'Полезный объем','504 л'),(67,23,'Тип','Двухкамерны'),(68,23,'Цвет','White'),(69,23,'Полезный объем','419 л'),(70,24,'Тип','Side-by-Side'),(71,24,'Цвет','Gray'),(72,24,'Полезный объем','595 л'),(73,25,'Память','32GB'),(74,25,'Цвет','Black'),(75,25,'Тип кабеля','Lightning/USB'),(76,26,'Память','128GB'),(77,26,'Цвет','Black'),(78,26,'Тип вилки','Европейская (Тип F)'),(79,27,'Память','8GB'),(80,27,'Цвет','Black'),(81,27,'Тип кабеля','HDMI'),(82,28,'Память','8GB'),(83,28,'Цвет','Black'),(84,28,'Тип кабеля','USB'),(85,29,'Память','512GB'),(86,29,'Цвет','Gray'),(87,29,'Диагональ экрана','15.6\"'),(88,30,'Память','256GB'),(89,30,'Цвет','Silver'),(90,30,'Диагональ экрана','13.6\"'),(91,31,'Память','512GB'),(92,31,'Цвет','Silver'),(93,31,'Диагональ экрана','13\"'),(94,32,'Память','512GB'),(95,32,'Цвет','Dark Grey'),(96,32,'Диагональ экрана','15.6\"'),(97,33,'Тип используемого кофе','молотый'),(98,33,'Объем резервуара для воды','1.25 л'),(99,33,'Цвет','Grey-Black'),(100,34,'Тип используемого кофе','в зернах/ молотый'),(101,34,'Объем резервуара для воды','1.8 л'),(102,34,'Цвет','Black'),(103,35,'Тип используемого кофе','Зерновой, Молотый'),(104,35,'Объем резервуара для воды','1.8 л'),(105,35,'Цвет','Silver, Black'),(106,36,'Тип используемого кофе','Молотый'),(107,36,'Объем резервуара для воды','1.25 л'),(108,36,'Цвет','Black'),(109,37,'Экран','34\"/3440x1440 Пикс'),(110,37,'Частота обновления','180 Гц'),(111,37,'Тип матрицы','VA'),(112,38,'Экран','24\"/1920x1080 Пикс'),(113,38,'Частота обновления','165 Гц'),(114,38,'Тип матрицы','VA'),(115,39,'Экран','34\"/3440x1440 Пикс'),(116,39,'Частота обновления','160 Гц'),(117,39,'Тип матрицы','VA'),(118,40,'Экран','27\"/2560x1440 Пикс'),(119,40,'Частота обновления','165 Гц'),(120,40,'Тип матрицы','VA'),(121,41,'Время нагрева','1 мин'),(122,41,'Потребляемая мощность','3100 Вт'),(123,41,'Резервуар для воды','400 мл'),(124,42,'Время нагрева','1 мин'),(125,42,'Потребляемая мощность','2000 Вт'),(126,42,'Резервуар для воды','280 мл'),(127,43,'Время нагрева','2 мин'),(128,43,'Потребляемая мощность','2800 Вт'),(129,43,'Резервуар для воды','270 мл'),(130,44,'Время нагрева','0.58 мин'),(131,44,'Потребляемая мощность','2600 Вт'),(132,44,'Резервуар для воды','300 мл'),(133,45,'Объем контейнера для пыли','1.3 л'),(134,45,'Максимальная мощность всасывания','380 Вт'),(135,45,'Количество насадок','3 шт'),(136,46,'Объем контейнера для пыли','1.3 л'),(137,46,'Максимальная мощность всасывания','400 Вт'),(138,46,'Количество насадок','1 шт'),(139,47,'Объем контейнера для пыли','1.2 л'),(140,47,'Максимальная мощность всасывания','420 Вт'),(141,47,'Количество насадок','3 шт'),(142,48,'Объем контейнера для пыли','2.5 л'),(143,48,'Максимальная мощность всасывания','900 Вт'),(144,48,'Количество насадок','2 шт'),(145,49,'Объем чаши','5 л'),(146,49,'Количество автоматических программ','16'),(147,49,'Максимальная потребляемая мощность','750 Вт'),(148,50,'Объем чаши','3 л'),(149,50,'Количество автоматических программ','8'),(150,50,'Максимальная потребляемая мощность','1300 Вт'),(151,51,'Объем чаши','3 л'),(152,51,'Количество автоматических программ','8'),(153,51,'Максимальная потребляемая мощность','710 Вт'),(154,52,'Объем чаши','5 л'),(155,52,'Количество автоматических программ','60'),(156,52,'Максимальная потребляемая мощность','980 Вт'),(157,53,'Максимальная загрузка белья','7 кг'),(158,53,'Максимальная скорость отжима','1200 об/мин'),(159,53,'Тип дисплея','LED'),(160,54,'Максимальная загрузка белья','6 кг'),(161,54,'Максимальная скорость отжима','1200 об/мин'),(162,55,'Тип дисплея','цифровой (символьный)'),(163,55,'Максимальная загрузка белья','6 кг'),(164,55,'Максимальная скорость отжима','1000 об/мин'),(165,55,'Тип дисплея','электронное'),(166,56,'Максимальная загрузка белья','10 кг'),(167,56,'Максимальная скорость отжима','1200 об/мин'),(168,56,'Тип дисплея','цифровой (символьный)'),(169,57,'Количество конфорок','4'),(170,57,'Объем духовки','71 л'),(171,57,'Количество режимов работы','11'),(172,58,'Количество конфорок','4'),(173,58,'Объем духовки','71 л'),(174,58,'Количество режимов работы','11'),(175,59,'Количество конфорок','3'),(176,59,'Объем духовки','50 л'),(177,59,'Количество режимов работы','3'),(178,60,'Количество конфорок','4'),(179,60,'Объем духовки','50 л'),(180,60,'Количество режимов работы','5');
/*!40000 ALTER TABLE `product_characteristics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_images`
--

DROP TABLE IF EXISTS `product_images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_images` (
  `id_image` int NOT NULL AUTO_INCREMENT,
  `id_product` int NOT NULL,
  `image_url` varchar(255) NOT NULL,
  PRIMARY KEY (`id_image`),
  KEY `id_product` (`id_product`),
  CONSTRAINT `product_images_ibfk_1` FOREIGN KEY (`id_product`) REFERENCES `products` (`id_product`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_images`
--

LOCK TABLES `product_images` WRITE;
/*!40000 ALTER TABLE `product_images` DISABLE KEYS */;
INSERT INTO `product_images` VALUES (1,1,'images/Samsung_TV.jpeg'),(2,2,'images/LG_TV.jpeg'),(3,3,'images/Haier_TV.jpeg'),(4,4,'images/Xiomi_TV.jpeg'),(5,5,'images/Honor_headph.jpeg'),(6,6,'images/Samsung_headph.jpeg'),(7,7,'images/Apple_headph.jpeg'),(8,8,'images/Xiomi_headph.jpeg'),(9,9,'images/Xiomi_phone.jpeg'),(10,10,'images/Samsung_phone.jpeg'),(11,11,'images/Apple_phone.jpeg'),(12,12,'images/Honor_phone.jpeg'),(13,13,'images/Honor_pad.jpeg'),(14,14,'images/Xiomi_pad.jpeg'),(15,15,'images/Samsung_pad.jpeg'),(16,16,'images/Apple_pad.jpeg'),(17,17,'images/Apple_watch.jpeg'),(18,18,'images/Xiomi_watch.jpeg'),(19,19,'images/Honor_watch.jpeg'),(20,20,'images/Samsung_watch.jpeg'),(21,21,'images/Haier_fridge.jpeg'),(22,22,'images/Haier2_fridge.jpeg'),(23,23,'images/LG_fridge.jpeg'),(24,24,'images/LG2_fridge.jpeg'),(25,25,'images/Apple_box.jpeg'),(26,26,'images/Apple2_box.jpeg'),(27,27,'images/Xiomi_box.jpeg'),(28,28,'images/Xiomi2_box.jpeg'),(29,29,'images/Haier_laptop.jpeg'),(30,30,'images/Apple_laptop.jpeg'),(31,31,'images/Xiomi_laptop.jpeg'),(32,32,'images/Samsung_laptop.jpeg'),(33,33,'images/Tefal_coffeemaker.jpeg'),(34,34,'images/Philips_coffeemaker.jpeg'),(35,35,'images/Philips2_coffeemaker.jpeg'),(36,36,'images/Tefal2_coffeemaker.jpeg'),(37,37,'images/Xiomi_screen.jpeg'),(38,38,'images/Samsung_screen.jpeg'),(39,39,'images/LG_screen.jpeg'),(40,40,'images/Philips_screen.jpeg'),(41,41,'images/Haier_iron.jpeg'),(42,42,'images/Xiomi_iron.jpeg'),(43,43,'images/Tefal_iron.jpeg'),(44,44,'images/Philips_iron.jpeg'),(45,45,'images/LG_vacuum.jpeg'),(46,46,'images/Tefal_vacuum.jpeg'),(47,47,'images/LG2_vacuum.jpeg'),(48,48,'images/Tefal2_vacuum.jpeg'),(49,49,'images/Tefal_multicooker.jpeg'),(50,50,'images/Xiomi_multicooker.jpeg'),(51,51,'images/Xiomi2_multicooker.jpeg'),(52,52,'images/Philips_multicooker.jpeg'),(53,53,'images/LG_washer.jpeg'),(54,54,'images/Haier_washer.jpeg'),(55,55,'images/Samsung_washer.jpeg'),(56,56,'images/Xiomi_washer.jpeg'),(57,57,'images/Weissgauff_electric_stove.jpeg'),(58,58,'images/Gorenje_electric_stove.jpeg'),(59,59,'images/Gorenje2_electric_stove.jpeg'),(60,60,'images/Weissgauff2_electric_stove.jpeg');
/*!40000 ALTER TABLE `product_images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_models`
--

DROP TABLE IF EXISTS `product_models`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_models` (
  `id_model` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `id_manufacturer` int NOT NULL,
  PRIMARY KEY (`id_model`),
  KEY `id_manufacturer` (`id_manufacturer`),
  CONSTRAINT `product_models_ibfk_1` FOREIGN KEY (`id_manufacturer`) REFERENCES `manufacturers` (`id_manufacturer`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_models`
--

LOCK TABLES `product_models` WRITE;
/*!40000 ALTER TABLE `product_models` DISABLE KEYS */;
INSERT INTO `product_models` VALUES (1,'UE50DU7100UXRU',1),(2,'55QNED816RA',2),(3,'55 Smart TV AX Pro',3),(4,'TV A 32 2025',4),(5,'Choice Earbuds X5E',6),(6,'SM- R510',1),(7,'MGYM3',5),(8,'BHR8118GL',4),(9,'14T',4),(10,'Galaxy S23',1),(11,'iPhone 13',5),(12,'90',6),(13,'Pad 9',6),(14,'Pad 6',4),(15,'Galaxy Tab S10 Ultra',1),(16,'Ipad Air 13',5),(17,'Watch SE 2022',5),(18,'Redmi Watch 5',4),(19,'Watch 4',6),(20,'Galaxy Watch7',1),(21,'C4F640CWU1',3),(22,'HRF-541DM7RU',3),(23,'GC-B509SQCL',2),(24,'InstaView GC-Q22FTAKL',2),(25,'MHY93',5),(26,'MN893',5),(27,'MDZ-28-AA',4),(28,'MDZ-27-AA',4),(29,'AX1550SD',3),(30,'MLXY3',5),(31,'JYU4251CN',4),(32,'NP750QGK-LG1IN',1),(33,'CM883D10',7),(34,'EP1200/00',8),(35,'EP4349/70',8),(36,'CM272N',7),(37,'G34WQi',4),(38,'S24AG320NI',1),(39,'34WP65C-B',2),(40,'27M1C5500VL',8),(41,'HI-600',3),(42,'YD-012V',4),(43,'FV5780E1',7),(44,'DST3041/80',8),(45,'VC-5420NNTS',2),(46,'TW1931RH',7),(47,'VK89309H',2),(48,'TW4B36EA',7),(49,'RK321A32',7),(50,'CR-HGX1',4),(51,'bhr7919eu',4),(52,'HD4713/40',8),(53,'F2J6HSFW',2),(54,'HW60-BP12919BS',3),(55,'WW60AG4S00CELD',1),(56,'XQG100MJ108',4),(57,'WES E1V07 W',10),(58,'GEC6C60XA',9),(59,'GECS6B70CLI',9),(60,'WES E2V05 B',10);
/*!40000 ALTER TABLE `product_models` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `id_product` int NOT NULL AUTO_INCREMENT,
  `id_model` int NOT NULL,
  `id_subcategory` int NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `description` text,
  `stock_quantity` int NOT NULL DEFAULT '0',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_product`),
  KEY `id_model` (`id_model`),
  KEY `id_subcategory` (`id_subcategory`),
  CONSTRAINT `products_ibfk_1` FOREIGN KEY (`id_model`) REFERENCES `product_models` (`id_model`) ON DELETE CASCADE,
  CONSTRAINT `products_ibfk_2` FOREIGN KEY (`id_subcategory`) REFERENCES `subcategories` (`id_subcategory`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,1,1,48499.00,'Ultra HD (4K) LED телевизор 50\" Samsung UE50DU7100UXRU со встроенным процессором Crystal Processor 4K оборудован операционной системой Tizen с интуитивно понятным интерфейсом.',20,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(2,2,1,84999.00,'Ultra HD (4K) QNED-телевизор 55\" LG 55QNED816RA разработан с применением технологии QNED, которая обеспечивает не только высокий уровень яркости, но и естественное отображение всех оттенков.',96,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(3,3,1,69999.50,'Ultra HD (4K) HQLED телевизор 55\" Haier 55 Smart TV AX Pro имеет тонкую рамку, что увеличивает угол обзора. Широкоформатный экран воспроизводит качественное изображение с разрешением 3840х2160 пикселей.',50,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(4,4,1,23990.00,'Телевизор Xiaomi TV A 32 2025 сочетает в себе качество, функциональность и стильный дизайн.',42,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(5,5,7,2588.00,'Наушники True Wireless Honor Choice TRN-ME00 Light Blue — компактные и стильные беспроводные вкладыши с защитой корпуса от воды и пыли согласно стандарту IP54.',56,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(6,6,7,11999.00,'Беспроводные наушники с микрофоном Samsung Galaxy Buds 2 Pro True Wireless Graphite позволяют наслаждаться музыкой в высоком качестве. Предусмотрена система активного шумоподавления, функция обнаружения голоса рядом.',105,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(7,7,7,48000.00,'AirPods Max — это совершенно новый взгляд на полноразмерные наушники. Все элементы AirPods Max, от амбушюров до оголовья, спроектированы таким образом, чтобы наушники оптимально прилегали к голове любой формы.',92,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(8,8,7,9999.00,'Беспроводные наушники Xiaomi Buds 5-Graphite Black (BHR8118GL) имеют радиус действия 10 м. Для комфортного прослушивания треков без отвлечения на посторонние звуки предусмотрена система активного шумоподавления.',77,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(9,9,6,59998.99,'Смартфон Xiaomi 14T 12/512GB Titanium Gray имеет восьмиядерный процессор MediaTek Dimensity 8300 Ultra. Благодаря этому устройство не зависает даже при высокой нагрузке.',100,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(10,10,6,85000.50,'Смартфон Samsung Galaxy S23 256GB Green (SM-S911/DS) оптимален для работы с ресурсоемкими приложениями, так как характеризуется высокой вычислительной мощностью.',108,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(11,11,6,75000.00,'Смартфон Apple iPhone 13 256GB Midnight оснащен усовершенствованной системой из двух камер с несколькими фотографическими стилями и супербыстрым чипом A15 Bionic.',55,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(12,12,6,30100.00,'Смартфон Honor 90 12/512GB Emerald Green с тремя основными камерами 200+12+2+af Мпикс позволит создать четкие, яркие и детализированные снимки благодаря зуму 10х и поддержке HDR.',131,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(13,13,5,27999.00,'Планшет Honor Pad 9 8/256GB Wi-Fi Space Gray (5301AHNJ) оснащен дисплеем IPS, который обеспечивает реалистичное отображение цветов и оттенков.',20,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(14,14,5,31000.00,'Планшет Xiaomi Pad 6 Mist Blue (47846) способен проработать в автономном режиме на протяжении 12 часов за счет встроенного аккумулятора емкостью 8840 мА*ч.',38,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(15,15,5,142999.00,'Планшет Samsung Galaxy Tab S10 Ultra 5G 256GB Gray (SM-X926B) оснащен восьмиядерным процессором. Благодаря этому устройство не зависает при запуске нескольких ресурсоемких программ.',15,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(16,16,5,89999.50,'Планшет Apple IPad Air 13 Wi-Fi 128GB Blue MV283 с экраном диагональю 13\" позволяет просматривать контент в разрешении 2732x2048 пикс.',45,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(17,17,8,28999.00,'Смарт-часы Apple Watch SE 44 мм SilverAlum./White Sport M/L (MNTJ3) оснащены сенсорным дисплеем Retina LTPO OLED яркостью 1000 кд/м².',55,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(18,18,8,3500.00,'Смарт-часы Xiaomi Redmi Watch 5 Active Midnight Black (BHR8784GL) дают возможность осуществлять мониторинг основных показателей. Устройство может контролировать уровень стресса, ЧСС, состояние сна, пройденное расстояние и сожженные калории.',23,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(19,19,8,13499.50,'Смарт-часы Honor Watch 4 Gold (TMA-B19) поддерживают платформы Android и iOS, что позволяет подключать их к любой модели телефона. Водоустойчивый корпус позволяет не снимать прибор во время купания.',104,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(20,20,8,25000.00,'Смарт-часы Samsung Galaxy Watch7 44mm LTE с корпусом серебристого цвета оснащены картой eSIM и способны осуществлять телефонные звонки без подключения к смартфону.',23,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(21,21,9,80000.00,'Холодильник Haier C4F640CWU1 двухкамерного типа имеет объем 400 л. Модель оснащена светодиодной подсветкой в основной камере. За счет технологии No Frost устройство не требует разморозки.',556,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(22,22,9,107000.00,'Холодильник Haier HRF-541DM7RU — это устройство Side-by-Side с множеством функций, которые помогут в повседневной жизни. Есть режим «Отпуск», благодаря которому не придется беспокоиться о продуктах во время долгого отсутствия.',43,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(23,23,9,78690.00,'Холодильник LG GC-B509SQCL двухкамерного типа с двумя дверьми обладает общим объемом 419 л, включая холодильную камеру на 292 л и морозильную на 127 л. Модель отличается низким уровнем шума - всего 36 дБ.',74,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(24,24,9,72400.99,'Холодильник LG InstaView GC-Q22FTAKL оснащен инверторным компрессором, который обеспечивает оптимальное энергопотребление и низкий уровень шума. Благодаря технологии DoorCooling+ происходит равномерный обдув основной камеры воздухом.',75,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(25,25,2,12500.00,'Телевизионная приставка Apple TV HD 32GB (MHY93) оснащена процессором A8, характеризующимся высокой производительностью и энергоэффективностью.',8,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(26,26,2,25000.50,'ТВ-приставка Apple TV 4K 128GB WiFi + Ethernet 3rd Gen (MN893) оптимальна для просмотра видео в формате 4К. В корпусе предусмотрен интерфейс HDMI для подключения монитора или телевизора.',18,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(27,27,2,9000.00,'Smart-TV-приставка Xiaomi TV Box S 2nd Gen 4K (MDZ-28-AA) обладает высокой производительностью, что обусловлено наличием мощного многоядерного процессора. С помощью устройства можно расширить функционал устаревшего телевизора.',24,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(28,28,2,3560.99,'Smart-TV-приставка Xiaomi Mi 4K TV Stick M24E (PFJ4122EU) функционирует на базе операционной системы Android TV с поддержкой функции Smart TV. Благодаря этому можно загружать мультимедийные приложения, пользоваться потоковыми сервисами и онлайн-кинотеатрами.',52,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(29,29,4,38999.99,'Ноутбук Haier AX1550SD оснащен процессором, который характеризуется высокой производительностью и обеспечивает быструю загрузку системы и приложений.',5,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(30,30,4,10999.99,'Ноутбук Apple MacBook Air 13 MLXY3, предлагает широкие возможности для решения бизнес-задач, офисной работы, игр со сложной графикой. Высокую производительность устройства обеспечивает чип М2.',16,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(31,31,4,75896.00,'Ноутбук Xiaomi Redmi Book 13 JYU4251CN c AMD Ryzen 5 4500U 2.3 ГГц процессором и опертивной памятью 16 ГБ. Отлично подходит для офиса и работы.',1,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(32,32,4,137999.50,'Ноутбук Samsung NP750QGK-LG1IN Dark Grey — высокопроизводительное устройство, способное работать с ресурсоемким ПО и поддерживающее современные игры. Поставляется с предустановленной ОС Windows 11 Home.',10,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(33,33,12,9839.00,'Кофеварка капельного типа Tefal Majestuo CM883D10 представлена в корпусе серебристого цвета. Мощность прибора составляет 1050 Вт. Объем кофеварки — 1,25 л, что позволяет готовить до 10-15 чашек кофе за раз.',45,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(34,34,12,38000.50,'Кофемашина Philips EP1221 Series 1200 приготовит разнообразные напитки с добавлением молока благодаря ручной системе приготовления капучино. Поддон для капель и контейнер для кофейной гущи можно мыть в посудомоечной машине.',103,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(35,35,12,98999.99,'Эспрессо, капучино, латте макиато, ристретто и многое другое – кофемашина Philips EP4341/50 умеет делать восемь напитков на любой вкус. Удобная сенсорная панель, оснащённая большим TFT-дисплеем с рисунками-подсказками, поможет быстро разобраться в управлении.',7,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(36,36,12,13058.50,'Кофемашина с фильтром Tefal CM272N Principio Select Откройте для себя удовольствие от завтрака с кофемашиной с фильтром Principio Select от Tefal. Эта современная кофемашина матового черного цвета вмещает до 15 чашек.',2,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(37,37,3,34000.00,'Игровой монитор Xiaomi G34WQi в корпусе черного цвета оснащен 34-дюймовым дисплеем разрешением 3440x1440 пикселей и частотой обновления 180 Гц. Даже во время быстрой игры картинки меняются плавно, отклик составляет всего 1 мс.',55,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(38,38,3,15999.99,'Игровой монитор Samsung Odyssey G3 (S24AG320NI) поставляется в комплекте с подставкой для устойчивого настольного размещения. Высоту экрана можно регулировать. Встроен вход HDMI для подключения к системному блоку.',20,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(39,39,3,35839.50,'LG UltraWide 34WP65C-B — монитор для геймеров с изогнутым экраном, тонким корпусом, возможностью регулировки положения и широким набором настроек для погружения в мир гейминга и мультимедиа. Сертифицированные технологии защиты зрения снижают нагрузку на глаза даже при длительной работе за экраном.',37,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(40,40,3,25000.00,'Игровой монитор Philips 27M1C5500VL с диагональю 27\" и разрешением 2560x1440 пикс обеспечивает высокую детализацию и четкость картинки. На экран нанесено антибликовое покрытие.',99,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(41,41,15,7000.00,'Утюг Haier HI-600 имеет электронную систему управления. Благодаря системе самоочистки утюг Haier HI-600 не требует специального ухода и характеризуется длительным сроком эксплуатации.',21,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(42,42,15,2999.99,'Утюг Xiaomi Lofans Electric Steam Iron Violet (YD-012V) оснащен рабочей станцией. Модель снимается с базы после нагрева и устанавливается обратно во время перерыва. Благодаря отсутствию провода можно гладить одежду под любым углом',9,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(43,43,15,7999.99,'Утюг Tefal Easygliss Eco FV5780E1 с корпусом белого и коричневого цветов нагревается до рабочего состояния за 2 минуты за счет мощности 2800 Вт. Прибор с подошвой Durilium AirGlide подходит для сухого глажения и отпаривания текстильных изделий в вертикальном положении.',85,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(44,44,15,3200.00,'Утюг Philips DST3041/80 мощностью 2600 Вт обеспечивает высокую производительность и нагрев подошвы до необходимой температуры за 0,58 мин. Подошва изготовлена из высококачественной керамики, которая обеспечивает плавное скольжение.',41,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(45,45,14,10490.99,'Пылесос с контейнером для пыли LG VC-5420NNTS получил пластиковый корпус серебристого цвета с автоматическим сматыванием 5,3-метрового сетевого шнура. Во время работы уровень шума достигает 82 дБ.',12,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(46,46,14,6000.00,'Пылесос с контейнером для пыли Tefal TW1931RH оснащен циклонической системой, гарантирующей до 99,98% всасывания мелких частиц на мощности до 1200 Вт. Пылесборник из высокопрочного пластика легко снимается. Широкая эргономическая ручка обеспечивает удобство переноски.',50,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(47,47,14,17980.50,'Пылесос с контейнером для пыли LG VK89309H Silver использует технологию прессования пыли. За счет этого и системы «Мультициклон» мощность всасывания остается стабильно высокой на протяжении всего процесса уборки и составляет 420 Вт.',77,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(48,48,14,12000.00,'Пылесос Tefal Compact Power XXL (TW4B36EA) с уровнем шума 75 дБ оснащен механическим выключателем, который расположен на корпусе. Модель предназначена для сухой уборки комнаты.',5,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(49,49,11,13000.00,'Мультиварка Tefal Essential Cook RK321A32 — удобное в эксплуатации устройство, предназначенное для приготовления вкусных и полезных блюд. Объем чаши составляет 5 л, чего достаточно для нескольких пользователей.',67,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(50,50,11,10999.99,'Мультиварка Xiaomi Qcooker Cooking Pot CR-HGX1 оснащена чашей объемом 3 л. Емкость имеет антипригарное покрытие, которое исключает прилипание продуктов. Таймер используется для установки определенного интервала времени работы устройства.',29,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(51,51,11,5000.00,'Современная мультиварка MiJia имеет множество программ для приготовления риса и других блюд. Технология электромагнитного воздействия делает нагрев равномерным и быстрым. Управлять электроприбором можно удаленно.',42,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(52,52,11,11820.00,'Простота приготовления вкусных блюд 24/7. Нажмите кнопку и наслаждайтесь неизменно вкусными блюдами. Придайте разнообразие и вкус любому блюду в течение дня, используя 60 удобных в использовании заданных программ.',23,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(53,53,13,42280.00,'Откройте для себя идеальное сочетание элегантности, инноваций и заботы о вашей одежде с Стиральной машиной LG F2J6HSFW. Специально разработанная технология Steam предоставляет три уникальных цикла стирки – «Одежда малыша», «Гипоаллергенный» и «Хлопок + Пар», обеспечивая бережное отношение к чувствительной коже и сохранение качества тканей.',99,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(54,54,13,34999.99,'Стиральная машина Haier HW60-BP12919BS обладает оптимальным объёмом загрузки 6 кг, который одинаково хорошо подходит для ежедневной и интенсивной, объёмной стирки.',45,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(55,55,13,32855.50,'Стиральная машина Samsung WW60AG4S00CELD - это современное и функциональное устройство, которое станет незаменимым помощником в вашем доме. Стиральная машина оснащена инверторным двигателем, который обеспечивает тихую и эффективную работу.',12,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(56,56,13,78000.00,'Стиральная машинка оснащена двигателем с прямым приводом, обеспечивающим точность вращения барабана и низкий уровень шума при стирке и отжиме. Функция быстрой стирки позволяет получить чистую одежду всего за 36 минут, что позволяет значительно сэкономить количество электричества и воды, не ухудшая качество стирки.',1,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(57,57,10,28000.00,'Электрическая отдельностоящая плита Weissgauff оснащенная духовкой с впечатляющим объемом 50 литров, а также стеклокерамической панелью с 4 Hi-Light конфорками - это сочетание великолепной функциональности и практичности.',51,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(58,58,10,63999.99,'Электрическая плита Gorenje GEC6C60XA оснащена многофункциональной духовкой вместительностью 71 л. Процесс приготовления пищи значительно упрощается наличием 11 режимов работы, в том числе большого гриля, вентиляционного и классического нагрева, размораживания.',5,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(59,59,10,68790.50,'Электрическая плита Gorenje GECS6B70CLI оснащена четырьмя конфорками, имеет расширяющиеся зоны нагрева. Благодаря этому можно с комфортом готовить завтраки, обеды и ужины для всей семьи. Духовой шкаф поддерживает 11 режимов работы.',28,'2024-11-16 23:42:11','2024-11-16 23:42:11'),(60,60,10,31000.00,'Электрическая плита Weissgauff WES E2V05 B имеет три конфорки стола типа Hi-Light. Зоны нагрева разного размера и мощности оптимальны для приготовления еды в больших кастрюлях и маленьких сотейниках. Духовой шкаф поддерживает три режима тепловой обработки пищи.',16,'2024-11-16 23:42:11','2024-11-16 23:42:11');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shipping`
--

DROP TABLE IF EXISTS `shipping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shipping` (
  `id_shipping` int NOT NULL AUTO_INCREMENT,
  `id_order` int NOT NULL,
  `shipping_status` varchar(255) DEFAULT 'pending',
  `shipping_address` text NOT NULL,
  `id_method` int NOT NULL,
  PRIMARY KEY (`id_shipping`),
  KEY `id_order` (`id_order`),
  KEY `fk_shipping_method` (`id_method`),
  CONSTRAINT `fk_shipping_method` FOREIGN KEY (`id_method`) REFERENCES `delivery_methods` (`id_method`) ON DELETE CASCADE,
  CONSTRAINT `shipping_ibfk_1` FOREIGN KEY (`id_order`) REFERENCES `orders` (`id_order`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shipping`
--

LOCK TABLES `shipping` WRITE;
/*!40000 ALTER TABLE `shipping` DISABLE KEYS */;
INSERT INTO `shipping` VALUES (1,1,'pending','ул. Тверская, д. 12, Москва, Россия',1),(2,2,'shipped','ул. Ленина, д. 45, Санкт-Петербург, Россия',2),(3,3,'delivered','пр. Мира, д. 78, Новосибирск, Россия',3),(4,4,'pending','ул. Пушкина, д. 21, Казань, Россия',1),(5,5,'pending','ул. Севастопольская, д. 9, Екатеринбург, Россия',2);
/*!40000 ALTER TABLE `shipping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subcategories`
--

DROP TABLE IF EXISTS `subcategories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subcategories` (
  `id_subcategory` int NOT NULL AUTO_INCREMENT,
  `id_category` int NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id_subcategory`),
  KEY `id_category` (`id_category`),
  CONSTRAINT `subcategories_ibfk_1` FOREIGN KEY (`id_category`) REFERENCES `categories` (`id_category`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subcategories`
--

LOCK TABLES `subcategories` WRITE;
/*!40000 ALTER TABLE `subcategories` DISABLE KEYS */;
INSERT INTO `subcategories` VALUES (1,1,'Телевизоры'),(2,1,'Приставки'),(3,2,'Компьютеры'),(4,2,'Ноутбуки'),(5,2,'Планшеты'),(6,3,'Смартфоны'),(7,3,'Наушники'),(8,3,'Часы'),(9,4,'Холодильники'),(10,4,'Плиты электрические'),(11,4,'Мультиварки'),(12,4,'Кофемашины'),(13,5,'Стиральные машины'),(14,5,'Пылесосы'),(15,5,'Утюги');
/*!40000 ALTER TABLE `subcategories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id_user` int NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `role` varchar(50) DEFAULT 'customer',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_user`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'user123@gmail.com','Userpassword','Username','89558235689','customer','2024-11-17 15:37:32','2024-11-17 23:43:18'),(2,'Polina123@mail.ru','Polinapsw','Polina','89345678934','customer','2024-11-17 15:37:32','2024-11-17 23:43:31'),(3,'Igor000@mail.ru','Igorpassword','Igor','89223456547','customer','2024-11-17 15:37:32','2024-11-17 23:43:40'),(4,'Violetta1@gmail.com','Violettapsw','Violetta','89567876543','customer','2024-11-17 15:37:32','2024-11-17 23:43:51'),(5,'test6789@gmail.com','Testpassword','Testuser','89334566664','customer','2024-11-17 15:43:29','2024-11-17 23:43:59'),(6,'vi@gmail.com','$2b$12$dehsfHNGCKa6RorPy3ete.Qx0pnMyVcJU/Dip/n7ConKaFdwuk1JS','Violetta','89228237565','customer','2024-11-18 15:27:33','2024-11-18 15:27:33'),(8,'vi@dmail.com','$2b$12$F20Eq6c/1JPZdPo50is4vupTJ2oWCm0OQRe3jLw76qNNmaN8OB1HS','Violetta','89562563256','customer','2024-11-18 15:31:24','2024-11-18 15:31:24'),(10,'vio@gmail.com','$2b$12$g.P.VRnh6C4WxgCQhKfreuY9ZGM4DaXx.2Pqcfti4scJc7skWSzgi','VILETA','89562378451','customer','2024-11-18 15:39:33','2024-11-18 15:39:33'),(11,'sufhfh@gmail.com','$2b$12$ZxRaGPCrL8tHRE0kbc9WNO0M6wCTptbQspaz1isWWKHsfQLFLCc.m','Daria','89562385212','customer','2024-11-18 15:44:23','2024-11-18 15:44:23'),(19,'vi2@gmail.com','$2b$12$exn5OgDO.BiZN9H.RdBru.Txumb7R3ecgnqcdIfpmXOFdzcdG2l72','vi','89562378452','customer','2024-11-18 18:23:24','2024-11-18 18:23:24'),(21,'pavel@gmail.com','$2b$12$L1mBxAWGi4Q/Wa0XOiNcwu8J.9uLTa4CeAbqSUqP1/h54vNcuccPa','Pavel','89562378450','customer','2024-11-24 15:45:44','2024-11-24 15:45:44'),(22,'mi@gmail.com','$2b$12$dXOx4tkkHC6Z9fet.qhoU.QfWwAsfsM7OWKraUA.5HXTyzIOdsWxu','михаил','89562321548','customer','2024-11-24 15:58:07','2024-11-24 15:58:07'),(24,'mia@gmail.com','$2b$12$IvMQ5rcYqTzPLnpZ8ICkvuDJ1iUi1VPe02Sh7SxXGigROfwtFq3aS','Mihail','12345678900','customer','2024-11-24 15:59:24','2024-11-24 15:59:24'),(25,'viol@mail.ru','$2b$12$j8bEJA7Ucb/fG5qoq/INu.LvHgU.pUyiWbzWQm4v4E2KdmDEGWLvW','VVioletta','74185296300','customer','2024-11-24 17:58:20','2024-11-24 17:58:20');
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

-- Dump completed on 2024-11-24 22:08:25
