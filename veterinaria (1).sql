-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 21-08-2026 a las 15:59:13
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `veterinaria`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `animal`
--

CREATE TABLE `animal` (
  `id_animal` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `especie` varchar(100) NOT NULL,
  `raza` varchar(50) NOT NULL,
  `fecha_nacimiento` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `id_dueño` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `animal`
--

INSERT INTO `animal` (`id_animal`, `nombre`, `especie`, `raza`, `fecha_nacimiento`, `id_dueño`) VALUES
(1, 'yupi', 'perro', 'labrador retriver', '2026-08-07 12:56:42', 1),
(2, 'leonoro', 'perro', 'pastor aleman', '2026-08-07 12:56:42', 1),
(3, 'supra', 'perro', 'bulldog ingles', '2026-08-07 12:56:42', 2),
(4, 'lamao', 'perro', 'boxer', '2026-08-07 12:56:42', 2),
(5, 'serpia', 'perro', 'gran danes', '2026-08-07 12:56:42', 3),
(6, 'sepro', 'perro', 'siberian husky', '2026-08-07 12:56:42', 4),
(7, 'liu kan ', 'perro', 'pug', '2026-08-07 12:56:42', 4),
(8, 'lupros', 'loro', 'periquito', '2026-08-07 12:56:42', 5),
(9, 'nert', 'loro', 'loro gris africano', '2026-08-07 12:56:42', 5),
(10, 'canela', 'gato', 'siames', '2026-08-07 12:56:42', 6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `consulta`
--

CREATE TABLE `consulta` (
  `id_consulta` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `hora` time NOT NULL,
  `motivo` varchar(100) NOT NULL,
  `id_animal` int(11) NOT NULL,
  `id_veterinario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `consulta`
--

INSERT INTO `consulta` (`id_consulta`, `fecha`, `hora`, `motivo`, `id_animal`, `id_veterinario`) VALUES
(1, '2026-08-01', '04:00:00', 'vomito', 1, 1),
(2, '2026-08-04', '06:00:00', 'problemas físicos', 10, 1),
(3, '2026-09-10', '08:00:00', 'problemas para dormir', 2, 2),
(4, '2026-09-03', '05:00:00', 'problemas de conducta ', 7, 3),
(5, '2026-09-14', '06:00:00', 'no come bien', 5, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dueño`
--

CREATE TABLE `dueño` (
  `id_dueño` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `rut` varchar(30) NOT NULL,
  `telefono` varchar(50) NOT NULL,
  `direccion` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `dueño`
--

INSERT INTO `dueño` (`id_dueño`, `nombre`, `rut`, `telefono`, `direccion`) VALUES
(1, 'jose', '8274197648', '+9172948987', 'cancha rayada'),
(2, 'manolo', '2371287823', '+918732r977', 'av olivarera'),
(3, 'pedro', '871263214', '+889126834', 'los artesanos'),
(4, 'felipe', '801278237', '+82739118094', 'cancha rayada'),
(5, 'miguel', '9173975552', '+91278386434', 'la paz'),
(6, 'ana', '8173723855', '+1781287843', 'av. capitán avalos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tratamiento`
--

CREATE TABLE `tratamiento` (
  `id_tratamiento` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `dosis` decimal(10,2) NOT NULL,
  `duracion` varchar(100) NOT NULL,
  `id_consulta` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tratamiento`
--

INSERT INTO `tratamiento` (`id_tratamiento`, `nombre`, `dosis`, `duracion`, `id_consulta`) VALUES
(1, 'vacunación', 2.00, 'unos 3 meses', 1),
(2, 'nutrición', 50.00, 'dale porciones del 50% de su plato durante 2 samanas', 5),
(3, 'conductismo', 40.00, 'entre 2 o 3 samanas', 4),
(4, 'desparasitarío', 3.00, 'durara entre 4 a 5 meses ', 1),
(5, 'hidroterapia ', 40.00, 'entre unos 2 semanas', 2),
(6, 'hidroterapia ', 50.00, 'vamos a trabajar entre 2 a 3 semanas ', 2),
(7, 'conductismo', 30.00, 'trabajaremos 1 o 2 semanas  ', 4),
(8, 'conductismo', 40.00, 'esta muy agresivo lo tendremos entre 2 a 3 semanas  ', 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `veterinario`
--

CREATE TABLE `veterinario` (
  `id_veterinario` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `especialidad` varchar(100) NOT NULL,
  `horario` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `veterinario`
--

INSERT INTO `veterinario` (`id_veterinario`, `nombre`, `especialidad`, `horario`) VALUES
(1, 'gustavo', 'dermatologia', '06:00:00'),
(2, 'sara ', 'anestesiologia', '06:00:00'),
(3, 'loren', 'etologia clinica', '08:00:00');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `animal`
--
ALTER TABLE `animal`
  ADD PRIMARY KEY (`id_animal`),
  ADD KEY `fk_animal_dueño` (`id_dueño`);

--
-- Indices de la tabla `consulta`
--
ALTER TABLE `consulta`
  ADD PRIMARY KEY (`id_consulta`),
  ADD KEY `fk_consulta_animal` (`id_animal`),
  ADD KEY `fk_consulta_veterinario` (`id_veterinario`);

--
-- Indices de la tabla `dueño`
--
ALTER TABLE `dueño`
  ADD PRIMARY KEY (`id_dueño`);

--
-- Indices de la tabla `tratamiento`
--
ALTER TABLE `tratamiento`
  ADD PRIMARY KEY (`id_tratamiento`),
  ADD KEY `fk_tratamiento_consulta` (`id_consulta`);

--
-- Indices de la tabla `veterinario`
--
ALTER TABLE `veterinario`
  ADD PRIMARY KEY (`id_veterinario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `animal`
--
ALTER TABLE `animal`
  MODIFY `id_animal` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `consulta`
--
ALTER TABLE `consulta`
  MODIFY `id_consulta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `dueño`
--
ALTER TABLE `dueño`
  MODIFY `id_dueño` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `tratamiento`
--
ALTER TABLE `tratamiento`
  MODIFY `id_tratamiento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `veterinario`
--
ALTER TABLE `veterinario`
  MODIFY `id_veterinario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `animal`
--
ALTER TABLE `animal`
  ADD CONSTRAINT `fk_animal_dueño` FOREIGN KEY (`id_dueño`) REFERENCES `dueño` (`id_dueño`) ON DELETE CASCADE;

--
-- Filtros para la tabla `consulta`
--
ALTER TABLE `consulta`
  ADD CONSTRAINT `fk_consulta_animal` FOREIGN KEY (`id_animal`) REFERENCES `animal` (`id_animal`) ON DELETE CASCADE,
  ADD CONSTRAINT `fk_consulta_veterinario` FOREIGN KEY (`id_veterinario`) REFERENCES `veterinario` (`id_veterinario`) ON DELETE CASCADE;

--
-- Filtros para la tabla `tratamiento`
--
ALTER TABLE `tratamiento`
  ADD CONSTRAINT `fk_tratamiento_consulta` FOREIGN KEY (`id_consulta`) REFERENCES `consulta` (`id_consulta`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
