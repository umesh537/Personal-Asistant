-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 13, 2021 at 04:34 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `logindb`
--

-- --------------------------------------------------------

--
-- Table structure for table `commands`
--

CREATE TABLE `commands` (
  `id` int(11) NOT NULL,
  `command` varchar(500) DEFAULT NULL,
  `ans` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `commands`
--

INSERT INTO `commands` (`id`, `command`, `ans`) VALUES
(11, 'open chrome', 'C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe'),
(12, 'open python', 'C:\\\\Program Files\\\\python.exe'),
(13, 'open youtube', 'https://www.youtube.com/'),
(14, 'open google', 'google.com'),
(15, 'open Dev c', 'C:\\\\Program Files (x86)\\\\Dev-Cpp\\\\dev.exe'),
(16, 'open Java T Point', 'https://www.javatpoint.com/'),
(17, 'open netbeans', 'C:\\\\Program Files\\\\NetBeans 8.1\\\\bin\\\\netbeans.exe'),
(18, 'open vs code', 'C:\\\\Users\\\\ADMIN\\\\AppData\\\\Local\\\\Programs\\\\Microsoft VS Code\\\\Code.exe'),
(20, 'open apple website', 'https://www.apple.com/');

-- --------------------------------------------------------

--
-- Table structure for table `usertable`
--

CREATE TABLE `usertable` (
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `usertable`
--

INSERT INTO `usertable` (`username`, `password`, `phone`, `email`) VALUES
('karan', '123', '665522448', 'karan@gmail.com'),
('sakshi', '123456', '8546553784', 'sakshi@gmail.com'),
('admin', '12345', '9861237845', 'admin@gmail.com'),
('tester', 'testy', '4567846786', 'test@gmail.com'),
('priya', 'priyaa', '9853677546', 'priya456@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `commands`
--
ALTER TABLE `commands`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `commands`
--
ALTER TABLE `commands`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
