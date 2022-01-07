CREATE DATABASE IF NOT EXISTS `admin_db`;
USE `admin_db`;
CREATE TABLE IF NOT EXISTS 'admin_db'.'admin_teachers' ( Teacher_ID INT AUTO_INCREMENT , Name char(20) , Password char(20) );

DESC admin_teachers;