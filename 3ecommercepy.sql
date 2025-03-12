-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 19, 2024 at 04:55 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `3ecommercepy`
--

-- --------------------------------------------------------

--
-- Table structure for table `booktb`
--

CREATE TABLE `booktb` (
  `id` bigint(10) NOT NULL auto_increment,
  `UserName` varchar(250) NOT NULL,
  `Bookid` varchar(250) NOT NULL,
  `Qty` varchar(250) NOT NULL,
  `Amount` varchar(250) NOT NULL,
  `CardName` varchar(250) NOT NULL,
  `CardNo` varchar(250) NOT NULL,
  `CvNo` varchar(250) NOT NULL,
  `Date` date NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `booktb`
--

INSERT INTO `booktb` (`id`, `UserName`, `Bookid`, `Qty`, `Amount`, `CardName`, `CardNo`, `CvNo`, `Date`) VALUES
(1, 'san', 'BOOKID1', '5.00', '300.00', 'mastercard', '1252363475698679', '123', '2024-02-26');

-- --------------------------------------------------------

--
-- Table structure for table `carttb`
--

CREATE TABLE `carttb` (
  `id` bigint(10) NOT NULL auto_increment,
  `UserName` varchar(250) NOT NULL,
  `ProductName` varchar(250) NOT NULL,
  `ProductType` varchar(250) NOT NULL,
  `Price` varchar(250) NOT NULL,
  `Qty` decimal(18,2) NOT NULL,
  `Tprice` decimal(28,2) NOT NULL,
  `Image` varchar(500) NOT NULL,
  `Date` date NOT NULL,
  `Status` varchar(250) NOT NULL,
  `Bookid` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `carttb`
--

INSERT INTO `carttb` (`id`, `UserName`, `ProductName`, `ProductType`, `Price`, `Qty`, `Tprice`, `Image`, `Date`, `Status`, `Bookid`) VALUES
(1, 'san', 'Granite', 'Biscuit', '60', '2.00', '120.00', '6829.png', '2024-02-26', '1', 'BOOKID1'),
(2, 'san', 'Granite', 'Biscuit', '60', '3.00', '180.00', '6829.png', '2024-02-26', '1', 'BOOKID1');

-- --------------------------------------------------------

--
-- Table structure for table `manuftb`
--

CREATE TABLE `manuftb` (
  `id` bigint(10) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `manuftb`
--

INSERT INTO `manuftb` (`id`, `Name`, `Email`, `Mobile`, `Address`, `UserName`, `Password`) VALUES
(1, 'sangeeth Kumar', 'sangeeth5535@gmail.com', '9486365535', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san', 'san');

-- --------------------------------------------------------

--
-- Table structure for table `protb`
--

CREATE TABLE `protb` (
  `id` bigint(10) NOT NULL auto_increment,
  `ProductId` varchar(250) NOT NULL,
  `ProductName` varchar(250) NOT NULL,
  `ProductType` varchar(250) NOT NULL,
  `Price` varchar(250) NOT NULL,
  `Qty` varchar(250) NOT NULL,
  `Date` date NOT NULL,
  `Info` varchar(1000) NOT NULL,
  `Image` varchar(500) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `protb`
--

INSERT INTO `protb` (`id`, `ProductId`, `ProductName`, `ProductType`, `Price`, `Qty`, `Date`, `Info`, `Image`) VALUES
(1, '1234', 'Granite', 'Biscuit', '60', '500', '2024-02-26', 'asdsa', '6829.png');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `Name` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`Name`, `Email`, `Mobile`, `Address`, `UserName`, `Password`) VALUES
('sangeeth Kumar', 'sangeeth5535@gmail.com', '9486365535', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san', 'san');

-- --------------------------------------------------------

--
-- Table structure for table `sbooktb`
--

CREATE TABLE `sbooktb` (
  `id` int(10) NOT NULL auto_increment,
  `UserName` varchar(250) NOT NULL,
  `ServicerName` varchar(250) NOT NULL,
  `Amount` varchar(250) NOT NULL,
  `Date` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `sbooktb`
--

INSERT INTO `sbooktb` (`id`, `UserName`, `ServicerName`, `Amount`, `Date`) VALUES
(1, 'san', 'gas', '900', '2024-03-20');

-- --------------------------------------------------------

--
-- Table structure for table `servicetb`
--

CREATE TABLE `servicetb` (
  `id` bigint(10) NOT NULL auto_increment,
  `ServiceName` varchar(250) NOT NULL,
  `ServiceType` varchar(250) NOT NULL,
  `Amount` varchar(250) NOT NULL,
  `Info` varchar(500) NOT NULL,
  `Sname` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `servicetb`
--

INSERT INTO `servicetb` (`id`, `ServiceName`, `ServiceType`, `Amount`, `Info`, `Sname`) VALUES
(1, 'gas', 'Repair', '900', 'futr', 'san');
