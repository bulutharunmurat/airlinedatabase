-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1:3306
-- Üretim Zamanı: 07 Oca 2021, 20:31:06
-- Sunucu sürümü: 5.7.31
-- PHP Sürümü: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `airlinedatabase`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `airline`
--

DROP TABLE IF EXISTS `airline`;
CREATE TABLE IF NOT EXISTS `airline` (
  `Airline_Company_Name` varchar(30) NOT NULL,
  `Airline_Company_Total_Passenger` int(11) DEFAULT NULL,
  `Airline_Company_Country` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Airline_Company_Name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Tablo döküm verisi `airline`
--

INSERT INTO `airline` (`Airline_Company_Name`, `Airline_Company_Total_Passenger`, `Airline_Company_Country`) VALUES
('Ryanair', 72020123, 'Ireland'),
('Air Canada', 23056266, 'Canada'),
('THY', 29955568, 'Turkey'),
('Lufthansa', 72020123, 'Germany'),
('American Airlines', 86530123, 'USA'),
('Emirates', 31007756, 'United Arab Emirates');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `airplane`
--

DROP TABLE IF EXISTS `airplane`;
CREATE TABLE IF NOT EXISTS `airplane` (
  `Airplane_Model` varchar(40) NOT NULL,
  `Airplane_Manufacturer` varchar(50) DEFAULT NULL,
  `Active_Number_of_Airplane_Model` int(11) DEFAULT NULL,
  PRIMARY KEY (`Airplane_Model`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Tablo döküm verisi `airplane`
--

INSERT INTO `airplane` (`Airplane_Model`, `Airplane_Manufacturer`, `Active_Number_of_Airplane_Model`) VALUES
('Airbus A320', 'Airbus', 7215),
('Boeing 737-800', 'Boeing', 9602),
('Airbus A319', 'Airbus', 1847),
('Cessna 172', 'Textron Aviation', 4098),
('Airbus A320neo', 'Airbus', 3227),
('Embraer ERJ-175LR', 'Embraer', 1738);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `arrival_airport`
--

DROP TABLE IF EXISTS `arrival_airport`;
CREATE TABLE IF NOT EXISTS `arrival_airport` (
  `Arrival_Airport` varchar(10) NOT NULL,
  `Arrival_Airport_Country` varchar(50) DEFAULT NULL,
  `Arrival_Airport_Total_Passengers` int(11) DEFAULT NULL,
  `Arrival_Airport_Elevation_feet` float DEFAULT NULL,
  PRIMARY KEY (`Arrival_Airport`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Tablo döküm verisi `arrival_airport`
--

INSERT INTO `arrival_airport` (`Arrival_Airport`, `Arrival_Airport_Country`, `Arrival_Airport_Total_Passengers`, `Arrival_Airport_Elevation_feet`) VALUES
('AMS', 'Netherlands', 71706999, -11),
('CDG', 'France', 76150007, 392),
('FRA', 'Germany', 70560987, 364),
('LGW', 'United Kingdom', 46574786, 202),
('SYD', 'Australia', 44443927, 21),
('LAS', 'United States', 51537638, 2184);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `bag`
--

DROP TABLE IF EXISTS `bag`;
CREATE TABLE IF NOT EXISTS `bag` (
  `Bag_ID` int(11) NOT NULL,
  `Bag_Weight` float DEFAULT NULL,
  PRIMARY KEY (`Bag_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Tablo döküm verisi `bag`
--

INSERT INTO `bag` (`Bag_ID`, `Bag_Weight`) VALUES
(1, 42),
(2, 22),
(3, 32.8),
(5, 53.5),
(6, 39.7),
(7, 22),
(8, 50.99),
(9, 78.9),
(10, 33.7),
(11, 67),
(12, 24.55),
(13, 39.6),
(14, 51.2),
(15, 48.7),
(16, 39.6),
(17, 78.7),
(18, 22.4),
(19, 87.4),
(20, 26.5);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `captain`
--

DROP TABLE IF EXISTS `captain`;
CREATE TABLE IF NOT EXISTS `captain` (
  `Captain_Certification_Number` int(11) NOT NULL,
  `Captain_Name` varchar(40) DEFAULT NULL,
  `Captain_Surname` varchar(40) DEFAULT NULL,
  `Captain_Age` smallint(6) DEFAULT NULL,
  `Captain_Flight_Hour_Experience` float DEFAULT NULL,
  PRIMARY KEY (`Captain_Certification_Number`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Tablo döküm verisi `captain`
--

INSERT INTO `captain` (`Captain_Certification_Number`, `Captain_Name`, `Captain_Surname`, `Captain_Age`, `Captain_Flight_Hour_Experience`) VALUES
(102500, 'Jaylen', 'Adams', 42, 1533),
(253689, 'Alex', 'Lioen', 30, 786),
(887966, 'Mariana', 'Dellinton', 39, 4100),
(563389, 'Carles', 'Rexach', 38, 9622),
(889669, 'Javier', 'Saviola', 33, 2233),
(100563, 'Vince', 'Hayes', 50, 6522);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `departure_airport`
--

DROP TABLE IF EXISTS `departure_airport`;
CREATE TABLE IF NOT EXISTS `departure_airport` (
  `Departure_Airport` varchar(10) NOT NULL,
  `Departure_Airport_Country` varchar(50) DEFAULT NULL,
  `Departure_Airport_Total_Passengers` int(11) DEFAULT NULL,
  `Departure_Airport_Elevation_feet` float DEFAULT NULL,
  PRIMARY KEY (`Departure_Airport`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Tablo döküm verisi `departure_airport`
--

INSERT INTO `departure_airport` (`Departure_Airport`, `Departure_Airport_Country`, `Departure_Airport_Total_Passengers`, `Departure_Airport_Elevation_feet`) VALUES
('IST', 'Turkey', 52578008, 325),
('ATL', 'United States', 110531300, 1026),
('DEN', 'United States', 69015703, 5431),
('BCN', 'Spain', 52686314, 12),
('YYZ', 'Canada', 50499431, 569),
('MUC', 'Germany', 47959887, 1487);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `flight`
--

DROP TABLE IF EXISTS `flight`;
CREATE TABLE IF NOT EXISTS `flight` (
  `Flight_Number` varchar(10) NOT NULL,
  `Captain_Certification_Number` int(11) DEFAULT NULL,
  `Airline_Company_Name` varchar(30) DEFAULT NULL,
  `Airplane_Model` varchar(50) DEFAULT NULL,
  `Departure_Airport` varchar(50) DEFAULT NULL,
  `Arrival_Airport` varchar(50) DEFAULT NULL,
  `Departure_Date_Time` datetime DEFAULT NULL,
  `Arrival_Date_Time` datetime DEFAULT NULL,
  PRIMARY KEY (`Flight_Number`),
  KEY `Captain_Certification_Number` (`Captain_Certification_Number`),
  KEY `Airline_Company_Name` (`Airline_Company_Name`),
  KEY `Airplane_Model` (`Airplane_Model`),
  KEY `Departure_Airport` (`Departure_Airport`),
  KEY `Arrival_Airport` (`Arrival_Airport`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Tablo döküm verisi `flight`
--

INSERT INTO `flight` (`Flight_Number`, `Captain_Certification_Number`, `Airline_Company_Name`, `Airplane_Model`, `Departure_Airport`, `Arrival_Airport`, `Departure_Date_Time`, `Arrival_Date_Time`) VALUES
('RA2684', 102500, 'Ryanair', 'Airbus A320', 'IST', 'AMS', '2020-11-05 12:00:00', '2020-11-05 14:30:00'),
('CA1002', 253689, 'Air Canada', 'Boeing 737-800', 'ATL', 'CDG', '2020-04-22 08:00:00', '2020-04-22 22:30:00'),
('THY4526', 887966, 'THY', 'Airbus A319', 'DEN', 'FRA', '2020-11-05 00:00:00', '2020-08-05 08:30:00'),
('LF5202', 563389, 'Lufthansa', 'Cessna 172', 'BCN', 'LGW', '2020-11-18 15:30:00', '2020-11-18 17:30:00'),
('AA9602', 889669, 'American Airlines', 'Airbus A320neo', 'YYZ', 'SYD', '2020-09-08 15:30:00', '2020-09-09 00:30:00'),
('ER7752', 100565, 'Emirates', 'Embraer ERJ-175LR', 'MUC', 'LAS', '2020-12-02 12:30:00', '2020-12-02 23:30:00');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `passenger`
--

DROP TABLE IF EXISTS `passenger`;
CREATE TABLE IF NOT EXISTS `passenger` (
  `Passenger_Passport_Number` int(11) NOT NULL,
  `Passenger_Name` varchar(40) DEFAULT NULL,
  `Passenger_Surname` varchar(40) DEFAULT NULL,
  `Passenger_Age` smallint(5) UNSIGNED DEFAULT NULL,
  `Passenger_Gender` varchar(10) DEFAULT NULL,
  `Passenger_Nationality` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Passenger_Passport_Number`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Tablo döküm verisi `passenger`
--

INSERT INTO `passenger` (`Passenger_Passport_Number`, `Passenger_Name`, `Passenger_Surname`, `Passenger_Age`, `Passenger_Gender`, `Passenger_Nationality`) VALUES
(112023, 'Luis', 'Enrique', 25, 'M', 'Spain'),
(552231, 'Jack', 'London', 40, 'M', 'Spain'),
(334233, 'Paul', 'Dennis', 29, 'M', 'Spain'),
(523498, 'Steven', 'Nash', 28, 'M', 'German'),
(716554, 'Mariana', 'Balet', 41, 'F', 'French'),
(413213, 'Sebastian', 'Nulker', 19, 'F', 'German'),
(344531, 'Mark', 'Zunner', 41, 'M', 'German'),
(433318, 'Joshua', 'Kimmich', 28, 'M', 'German'),
(221319, 'Eric', 'Abidal', 42, 'M', 'Switzerland'),
(278633, 'Julio', 'Alberto', 55, 'F', 'Spain'),
(721328, 'Michael', 'Reiziger', 42, 'M', 'Netherlands'),
(588138, 'Gary', 'Lineker', 28, 'M', 'England'),
(213219, 'Gianluca', 'Zambrotta', 22, 'M', 'Italy'),
(213513, 'Ivan', 'Rakitic', 32, 'M', 'Croatia'),
(987946, 'Rafael', 'Marquez', 30, 'M', 'Mexico'),
(321569, 'Frank', 'Barrett', 18, 'M', 'Scotland'),
(213218, 'Johnny', 'Carey', 25, 'M', 'Ireland'),
(823126, 'Stan', 'Pearson', 88, 'M', 'England'),
(500025, 'Manfred', 'Bender', 26, 'F', 'German'),
(528558, 'Dieter', 'Brenninger', 40, 'F', 'German');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `payment`
--

DROP TABLE IF EXISTS `payment`;
CREATE TABLE IF NOT EXISTS `payment` (
  `Payment_ID` int(11) NOT NULL,
  `Payment_Type` varchar(20) DEFAULT NULL,
  `Payment_Date` datetime DEFAULT NULL,
  `Payment_Amount` float DEFAULT NULL,
  PRIMARY KEY (`Payment_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Tablo döküm verisi `payment`
--

INSERT INTO `payment` (`Payment_ID`, `Payment_Type`, `Payment_Date`, `Payment_Amount`) VALUES
(568478, 'PayPal', '2020-04-14 16:31:05', 230),
(245435, 'Credit Card', '2020-05-23 07:41:06', 20.5),
(789238, 'Credit Card', '2020-03-12 06:55:04', 44.8),
(231283, 'Bank Transfer', '2020-05-05 22:55:34', 135),
(978569, 'Credit Card', '2020-06-11 12:12:00', 220),
(145325, 'Cash', '2020-08-29 17:42:12', 500.15),
(100102, 'Credit Card', '2020-03-26 14:13:13', 120),
(122122, 'Cash', '2020-02-11 09:12:12', 68.22),
(235213, 'Mobile Payment', '2020-02-12 23:32:33', 58.5),
(525113, 'Credit Card', '2020-02-25 08:02:44', 78.86),
(245313, 'PayPal', '2020-02-14 16:42:00', 120.2),
(144115, 'Credit Card', '2020-07-05 12:42:44', 50),
(234213, 'Credit Card', '2020-08-12 14:22:39', 84.5),
(235613, 'Mobile Payment', '2020-10-05 00:30:44', 98.45),
(123122, 'Cash', '2020-02-22 10:40:12', 346),
(125402, 'Credit Card', '2020-01-28 17:30:54', 326.23),
(134525, 'Cash', '2020-04-04 14:20:00', 120.2),
(978539, 'Credit Card', '2020-05-15 19:45:40', 86),
(231243, 'Bank Transfer', '2020-06-12 18:30:40', 125),
(713414, 'Credit Card', '2020-03-11 20:22:00', 778.52);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `ticket`
--

DROP TABLE IF EXISTS `ticket`;
CREATE TABLE IF NOT EXISTS `ticket` (
  `Ticket_ID` int(11) NOT NULL,
  `Payment_ID` int(11) DEFAULT NULL,
  `Flight_Class` varchar(20) DEFAULT NULL,
  `Passenger_Seat` varchar(10) DEFAULT NULL,
  `Bag_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`Ticket_ID`),
  KEY `Payment_ID` (`Payment_ID`),
  KEY `Bag_ID` (`Bag_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Tablo döküm verisi `ticket`
--

INSERT INTO `ticket` (`Ticket_ID`, `Payment_ID`, `Flight_Class`, `Passenger_Seat`, `Bag_ID`) VALUES
(212331, 144115, 'First Class', 'B12', 1),
(421422, 245313, 'First Class', 'C21', 2),
(124114, 525113, 'Economy Class', 'A11', 3),
(122538, 235213, 'Economy Class', 'D1', 4),
(135983, 122122, 'Economy Class', 'F3', 5),
(968325, 100102, 'First Class', 'A24', 6),
(906345, 145325, 'Business Class', 'E4', 7),
(102358, 978569, 'Economy Class', 'A1', 8),
(100235, 231283, 'First Class', 'D24', 9),
(869543, 789238, 'Economy Class', 'B18', 10),
(996300, 245435, 'First Class', 'D3', 11),
(963245, 568478, 'Business Class', 'E18', 12),
(420036, 234213, 'Economy Class', 'A21', 13),
(364205, 235613, 'Economy Class', 'D22', 14),
(310025, 123122, 'Business Class', 'B4', 15),
(355369, 125402, 'Economy Class', 'A15', 16),
(875589, 134525, 'Economy Class', 'A7', 17),
(100236, 978539, 'Economy Class', 'D12', 18),
(200157, 231243, 'Economy Class', 'D8', 19),
(986534, 713414, 'Economy Class', 'F9', 20);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `ticket_flight`
--

DROP TABLE IF EXISTS `ticket_flight`;
CREATE TABLE IF NOT EXISTS `ticket_flight` (
  `Passenger_Passport_Number` int(11) NOT NULL,
  `Flight_Number` varchar(10) NOT NULL,
  `Ticket_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`Passenger_Passport_Number`,`Flight_Number`),
  KEY `Ticket_ID` (`Ticket_ID`),
  KEY `Flight_Number` (`Flight_Number`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Tablo döküm verisi `ticket_flight`
--

INSERT INTO `ticket_flight` (`Passenger_Passport_Number`, `Flight_Number`, `Ticket_ID`) VALUES
(112023, 'RA2684', 212331),
(552231, 'RA2684', 421422),
(334233, 'RA2684', 124114),
(523498, 'CA1002', 122538),
(716554, 'CA1002', 135983),
(413213, 'THY4526', 968325),
(344531, 'THY4526', 906345),
(433318, 'THY4526', 102358),
(221319, 'LF5202', 100235),
(278633, 'LF5202', 869543),
(721328, 'LF5202', 996300),
(588138, 'LF5202', 963245),
(213219, 'AA9602', 420036),
(213513, 'AA9602', 364205),
(987946, 'AA9602', 310025),
(321569, 'AA9602', 355369),
(213218, 'ER7752', 875589),
(823126, 'ER7752', 100236),
(500025, 'ER7752', 200157),
(528558, 'ER7752', 986534);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
