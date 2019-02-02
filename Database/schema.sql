-- create database ece651;
-- use ece651;

DROP TABLE IF EXISTS `Login_Credentials`;
CREATE TABLE `Login_Credentials` (
  `Email or phone #` varchar(50),
  `Password` varchar(50),
  PRIMARY KEY (`Email or phone #`, `Password`)
);

DROP TABLE IF EXISTS `Health measurements/stats`;
CREATE TABLE `Health measurements/stats` (
  `Patient ID` int,
  `Blood pressure` int,
  `Heart rate` int,
  `weight` int,
  KEY `FK` (`Patient ID`)
);

DROP TABLE IF EXISTS `Doctor`;
CREATE TABLE `Doctor` (
  `Doctor ID` int,
  `first Name` varchar(50),
  `Last Name` varchar(50),
  `Email` varchar(50),
  `phone #` varchar(10),
  `street` varchar(50),
  `city` varchar(50),
  `state` varchar(2),
  `postal code` varchar(6),
  `Country` varchar(50),
  PRIMARY KEY (`Doctor ID`)
);

DROP TABLE IF EXISTS `Patient`;
CREATE TABLE `Patient` (
  `Patient ID` int,
  `Doctor ID` int,
  `First Name` varchar(50),
  `Last Name` varchar(50),
  `DOB` varchar(50),
  `Sex` varchar(1),
  `height` varchar(10),
  `email` varchar(50),
  `phone #` varchar(10),
  `street` varchar(50),
  `city` varchar(50),
  `state` varchar(2),
  `postal code` varchar(6),
  `country` varchar(50),
  PRIMARY KEY (`Patient ID`),
  KEY `Fk` (`Doctor ID`)
);

DROP TABLE IF EXISTS `Emergency  Contact`;
CREATE TABLE `Emergency  Contact` (
  `Patient ID` int,
  `contact name` varchar(50),
  `relationship` varchar(50),
  `phone` varchar(10),
  KEY `FK` (`Patient ID`)
);

DROP TABLE IF EXISTS `Patient_RecordLog`;
CREATE TABLE `Patient_RecordLog` (
  `Record ID` int,
  `Patient ID` int,
  `Blood pressure` int,
  `weight` int,
  `Date` varchar(50),
  PRIMARY KEY (`Record ID`),
  KEY `FK` (`Patient ID`)
);

DROP TABLE IF EXISTS `Doctor_login`;
CREATE TABLE `Doctor_login` (
  `Login_ID` int,
  `Email or phone #` varchar(10),
  `Date` varchar(50),
  `Time` varchar(50),
  `status` int,
  PRIMARY KEY (`Login_ID`),
  KEY `FK` (`Email or phone #`)
);

DROP TABLE IF EXISTS `Patient_login`;
CREATE TABLE `Patient_login` (
  `LoginID` int,
  `Email or phone #` int,
  `Date` varchar(50),
  `Time` varchar(50),
  `status` int,
  PRIMARY KEY (`LoginID`),
  KEY `FK` (`Email or phone #`)
);


