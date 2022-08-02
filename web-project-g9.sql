-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 31, 2022 at 09:41 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `web-project-g9`
--
--
-- Table structure for table `contact_us`
--

CREATE TABLE `contact_us` (
  `CONTACT_ID` int(11) NOT NULL,
  `NAME` varchar(50) NOT NULL,
  `EMAIL` varchar(50) NOT NULL,
  `TIME_UPLOADED` datetime NOT NULL,
  `TEXT` varchar(255) DEFAULT NULL,
  `IMAGE_SRC` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `dogs`
--

CREATE TABLE `dogs` (
  `USER_ID` int(11) NOT NULL,
  `DOG_ID` int(11) NOT NULL,
  `DOG_NAME` varchar(25) NOT NULL,
  `DOG_TYPE` varchar(50) NOT NULL,
  `DOG_GENDER` varchar(10) NOT NULL,
  `DOG_SIZE` varchar(10) NOT NULL,
  `DATE_BIRTH` varchar(10) NOT NULL,
  `DOG_NATURE` varchar(10) NOT NULL,
  `IMAGE_SRC` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------


--
-- Table structure for table `matches`
--

CREATE TABLE `matches` (
  `MATCH_ID` int(11) NOT NULL,
  `DOG_1` int(11) NOT NULL,
  `DOG_2` int(11) NOT NULL,
  `DATE_MATCH` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `USER_ID` int(11) NOT NULL,
  `PRODUCT_ID` int(11) NOT NULL,
  `NAME` varchar(50) NOT NULL,
  `CATEGORY_ID` int(11) NOT NULL,
  `TIME_UPLOADED` datetime NOT NULL,
  `FREE` char(5) NOT NULL,
  `PRICE` int(11) NOT NULL DEFAULT 1,
  `DESCRIPTION` varchar(255) DEFAULT NULL,
  `IMAGE_SRC` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `USER_ID` int(11) NOT NULL,
  `USER_NAME` varchar(25) NOT NULL,
  `GENDER` varchar(25) NOT NULL,
  `EMAIL` varchar(50) NOT NULL,
  `PASSWORD` varchar(10) NOT NULL,
  `DATE_BIRTH` varchar(10) NOT NULL,
  `PHONE_NUMBER` varchar(10) NOT NULL,
  `U_IMAGE_SRC` varchar(255) DEFAULT NULL,
  `CITY` varchar(255) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--

-- Indexes for table `contact_us`
--
ALTER TABLE `contact_us`
  ADD PRIMARY KEY (`CONTACT_ID`),
  ADD UNIQUE KEY `users_ID_uindex` (`CONTACT_ID`);

--
-- Indexes for table `dogs`
--
ALTER TABLE `dogs`
  ADD PRIMARY KEY (`DOG_ID`),
  ADD UNIQUE KEY `users_ID_uindex` (`DOG_ID`),
  ADD KEY `USER_ID_FK` (`USER_ID`);


-- Indexes for table `matches`
--
ALTER TABLE `matches`
  ADD PRIMARY KEY (`MATCH_ID`),
  ADD UNIQUE KEY `MATCH_ID_uindex` (`MATCH_ID`),
  ADD KEY `DOG_1_FK` (`DOG_1`),
  ADD KEY `DOG_2_FK` (`DOG_2`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`PRODUCT_ID`),
  ADD UNIQUE KEY `PRODUCT_ID_uindex` (`PRODUCT_ID`),
  ADD KEY `PRODUCT_USER_ID_FK` (`USER_ID`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`USER_ID`),
  ADD UNIQUE KEY `users_ID_uindex` (`USER_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
--
-- AUTO_INCREMENT for table `contact_us`
--
ALTER TABLE `contact_us`
  MODIFY `CONTACT_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `dogs`
--
ALTER TABLE `dogs`
  MODIFY `DOG_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `matches`
--
ALTER TABLE `matches`
  MODIFY `MATCH_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `PRODUCT_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `USER_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `dogs`
--
ALTER TABLE `dogs`
  ADD CONSTRAINT `USER_ID_FK` FOREIGN KEY (`USER_ID`) REFERENCES `users` (`USER_ID`);

--
-- Constraints for table `matches`
--
ALTER TABLE `matches`
  ADD CONSTRAINT `DOG_1_FK` FOREIGN KEY (`DOG_1`) REFERENCES `dogs` (`DOG_ID`),
  ADD CONSTRAINT `DOG_2_FK` FOREIGN KEY (`DOG_2`) REFERENCES `dogs` (`DOG_ID`);

--
-- Constraints for table `products`
--
ALTER TABLE `products`
  ADD CONSTRAINT `PRODUCT_USER_ID_FK` FOREIGN KEY (`USER_ID`) REFERENCES `users` (`USER_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
