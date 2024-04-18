/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - image_retrieval
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`image_retrieval` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `image_retrieval`;

/*Table structure for table `assigned_cases` */

DROP TABLE IF EXISTS `assigned_cases`;

CREATE TABLE `assigned_cases` (
  `assign_id` int(11) NOT NULL AUTO_INCREMENT,
  `case_id` int(11) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`assign_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `assigned_cases` */

insert  into `assigned_cases`(`assign_id`,`case_id`,`staff_id`,`date`,`status`) values 
(1,1,1,'2024-03-19','pending'),
(2,1,1,'2024-03-19','pending');

/*Table structure for table `case_status` */

DROP TABLE IF EXISTS `case_status`;

CREATE TABLE `case_status` (
  `case_status_id` int(11) NOT NULL AUTO_INCREMENT,
  `assigned_id` int(11) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`case_status_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `case_status` */

insert  into `case_status`(`case_status_id`,`assigned_id`,`description`,`date`) values 
(1,1,'ok','2024-03-19');

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`complaint_id`,`sender_id`,`title`,`description`,`reply`,`date`) values 
(1,1,'sdfghj','sdfghjk cf','ok','2024-03-4'),
(2,4,'aa','aaaa','pending','2024-03-19'),
(3,6,'ok','ok','done','2024-03-19');

/*Table structure for table `division` */

DROP TABLE IF EXISTS `division`;

CREATE TABLE `division` (
  `division_id` int(11) NOT NULL AUTO_INCREMENT,
  `division_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`division_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `division` */

insert  into `division`(`division_id`,`division_name`) values 
(1,'as'),
(2,'aaaa');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(2,'qqq','aaa','station'),
(3,'ttt','ttt','station'),
(4,'ooo','ooo','station'),
(5,'ann','123','station'),
(6,'amal','123','staff'),
(7,'aaa','123','staff');

/*Table structure for table `registered_cases` */

DROP TABLE IF EXISTS `registered_cases`;

CREATE TABLE `registered_cases` (
  `case_id` int(11) NOT NULL AUTO_INCREMENT,
  `station_id` int(11) DEFAULT NULL,
  `case_name` varchar(100) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`case_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `registered_cases` */

insert  into `registered_cases`(`case_id`,`station_id`,`case_name`,`details`,`date`,`status`) values 
(1,1,'uu','uu','2024-03-19','pending');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `station_id` int(11) DEFAULT NULL,
  `staff_name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `designation` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`login_id`,`station_id`,`staff_name`,`place`,`phone`,`email`,`designation`) values 
(1,6,1,'amal james','peramangalam','09876543201','amaljames@gmail.com','dfghj');

/*Table structure for table `station` */

DROP TABLE IF EXISTS `station`;

CREATE TABLE `station` (
  `station_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `division_id` int(11) DEFAULT NULL,
  `station_name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`station_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `station` */

insert  into `station`(`station_id`,`login_id`,`division_id`,`station_name`,`place`,`phone`,`email`) values 
(1,4,1,'akhd','gfg','nbbjhb','nbhb');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
