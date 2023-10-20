-- phpMyAdmin SQL Dump
-- version 4.5.4.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 20-Out-2023 às 00:03
-- Versão do servidor: 5.7.11
-- PHP Version: 5.6.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bd_atividade`
--
CREATE DATABASE IF NOT EXISTS `bd_atividade` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `bd_atividade`;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tb_dados_viagens`
--

CREATE TABLE `tb_dados_viagens` (
  `nome_cliente` varchar(50) NOT NULL,
  `data_viagem` date NOT NULL,
  `local_origem` varchar(50) NOT NULL,
  `local_destino` varchar(50) NOT NULL,
  `forma_pagamento` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `tb_dados_viagens`
--

INSERT INTO `tb_dados_viagens` (`nome_cliente`, `data_viagem`, `local_origem`, `local_destino`, `forma_pagamento`) VALUES
('gg', '2023-10-20', 'ARGENTINA', 'CANADÁ', 'BOLETO'),
('gg', '2023-10-20', 'BRASIL', 'ESTADOS UNIDOS', 'CARTÃO DE CRÉDITO'),
('bill', '2023-10-20', 'BRASIL', 'ESTADOS UNIDOS', 'PIX');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_dados_viagens`
--
ALTER TABLE `tb_dados_viagens`
  ADD PRIMARY KEY (`forma_pagamento`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
