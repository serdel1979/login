-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 13-03-2022 a las 23:48:03
-- Versión del servidor: 10.3.31-MariaDB
-- Versión de PHP: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `dbuser`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `solicitud_turnos`
--

CREATE TABLE `solicitud_turnos` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `id_vacuna` int(11) NOT NULL,
  `vacuna` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `fecha_solicitud` date DEFAULT NULL,
  `fecha_turno` date DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `solicitud_turnos`
--

INSERT INTO `solicitud_turnos` (`id`, `id_user`, `id_vacuna`, `vacuna`, `fecha_solicitud`, `fecha_turno`) VALUES
(1, 21, 3, 'Sarampion', '2022-03-13', NULL),
(2, 21, 4, 'Triple viral', '2022-03-13', NULL),
(3, 21, 8, 'Covid', '2022-03-13', NULL),
(4, 21, 8, 'Covid', '2022-03-13', NULL),
(5, 21, 7, 'Doble viral', '2022-03-13', NULL),
(6, 24, 8, 'Covid', '2022-03-13', NULL),
(7, 24, 3, 'Sarampion', '2022-03-13', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(150) NOT NULL,
  `nombre` varchar(150) DEFAULT NULL,
  `tipo` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `nombre`, `tipo`) VALUES
(1, 'admin', 'pbkdf2:sha256:260000$OTwHNAW4lq68Akwz$38d486f50471c5963a9efdacca752f4a3635eed1d70187847016bf59b9c52703', 'admin admin', 1),
(21, 'pipo', 'pbkdf2:sha256:260000$tKRcTtOFckc7tgq3$da90318704056a1a8be1ded4b2ec9d49b000866e81e5dce6251ce31f28d43e70', 'pipo', 2),
(24, 'pepe', 'pbkdf2:sha256:260000$C15aWWlug5Zpa79E$d190bf2d3192f45282f79ffa85180cffd2d072b40fe69cfe76ed335a77134a01', 'sapo pepe', 2),
(26, 'pancho', 'pbkdf2:sha256:260000$zS0Uzwye9n6hQDXO$4bc7f73814dd5360cfc42a505ff77608a567121509c787100efd3f8956622c3b', 'pancho croto', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vacunas`
--

CREATE TABLE `vacunas` (
  `id` int(11) NOT NULL,
  `vacuna` varchar(100) NOT NULL,
  `cantidad` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `vacunas`
--

INSERT INTO `vacunas` (`id`, `vacuna`, `cantidad`) VALUES
(3, 'Sarampion', 25),
(4, 'Triple viral', 10),
(7, 'Doble viral', 15),
(8, 'Covid', 5);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `solicitud_turnos`
--
ALTER TABLE `solicitud_turnos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `vacunas`
--
ALTER TABLE `vacunas`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `solicitud_turnos`
--
ALTER TABLE `solicitud_turnos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT de la tabla `vacunas`
--
ALTER TABLE `vacunas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
