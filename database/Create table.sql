CREATE DATABASE `test` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci */

CREATE TABLE `customers` (
   `customer_id` int(11) NOT NULL AUTO_INCREMENT,
   `first_name` varchar(100) NOT NULL,
   `last_name` varchar(100) NOT NULL,
   `email` varchar(100) NOT NULL,
   `phone` varchar(15) NOT NULL,
   PRIMARY KEY (`customer_id`)
 ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT;
 
 CREATE TABLE `employees` (
   `employee_id` int(11) NOT NULL AUTO_INCREMENT,
   `first_name` varchar(100) NOT NULL,
   `last_name` varchar(100) NOT NULL,
   `email` varchar(50) NOT NULL,
   `phone` varchar(20) NOT NULL,
   `salary` decimal(10,2) NOT NULL,
   PRIMARY KEY (`employee_id`)
 ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAUL;
 
 CREATE TABLE `products` (
   `product_id` int(11) NOT NULL AUTO_INCREMENT,
   `product_name` varchar(100) NOT NULL,
   `price` decimal(10,2) NOT NULL,
   `stock_quantity` int(11) NOT NULL,
   PRIMARY KEY (`product_id`)
 ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT;
 
 CREATE TABLE `orders` (
   `order_id` int(11) NOT NULL AUTO_INCREMENT,
   `customer_id` int(11) NOT NULL,
   `order_date` varchar(20) NOT NULL,
   PRIMARY KEY (`order_id`)
 ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT;
 
 CREATE TABLE `orderitems` (
   `order_item_id` int(11) NOT NULL AUTO_INCREMENT,
   `order_id` int(11) NOT NULL,
   `product_id` int(11) NOT NULL,
   `quantity` int(11) NOT NULL,
   `subtotal` decimal(10,2) NOT NULL,
   PRIMARY KEY (`order_item_id`)
 ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAUL;