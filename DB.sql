-- --------------------------------------------------------
-- Host:                         localhost
-- Versión del servidor:         10.5.8-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para asistencia_l4g
CREATE DATABASE IF NOT EXISTS `asistencia_l4g` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `asistencia_l4g`;

-- Volcando estructura para tabla asistencia_l4g.attendances
CREATE TABLE IF NOT EXISTS `attendances` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `sesion_id` int(10) unsigned NOT NULL,
  `student_id` int(10) unsigned NOT NULL,
  `present` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK__sesions` (`sesion_id`),
  KEY `FK__students` (`student_id`),
  CONSTRAINT `FK__sesions` FOREIGN KEY (`sesion_id`) REFERENCES `sesions` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `FK__students` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla asistencia_l4g.attendances: ~13 rows (aproximadamente)
/*!40000 ALTER TABLE `attendances` DISABLE KEYS */;
INSERT INTO `attendances` (`id`, `sesion_id`, `student_id`, `present`) VALUES
	(6, 1, 5, 'no'),
	(7, 1, 3, 'no'),
	(8, 2, 4, 'si');
/*!40000 ALTER TABLE `attendances` ENABLE KEYS */;

-- Volcando estructura para tabla asistencia_l4g.sesions
CREATE TABLE IF NOT EXISTS `sesions` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `subject_id` int(10) unsigned NOT NULL,
  `date` varchar(50) NOT NULL,
  `time_start` varchar(50) NOT NULL,
  `time_end` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `FK_attendances_subjects` (`subject_id`),
  CONSTRAINT `FK_attendances_subjects` FOREIGN KEY (`subject_id`) REFERENCES `subjects` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla asistencia_l4g.sesions: ~9 rows (aproximadamente)
/*!40000 ALTER TABLE `sesions` DISABLE KEYS */;
INSERT INTO `sesions` (`id`, `subject_id`, `date`, `time_start`, `time_end`) VALUES
	(1, 1, '2021-04-28', '17:14:43', '17:14:48'),
	(2, 1, '2021-04-22', '17:36:00', '17:40:00'),
	(3, 2, '2021-04-15', '17:40:00', '18:40:00'),
	(4, 2, '2021-04-23', '07:30:00', '08:30:00');
/*!40000 ALTER TABLE `sesions` ENABLE KEYS */;

-- Volcando estructura para tabla asistencia_l4g.students
CREATE TABLE IF NOT EXISTS `students` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `identity` varchar(50) NOT NULL,
  `names` varchar(250) NOT NULL,
  `surname` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `phone` varchar(250) NOT NULL,
  `semester` varchar(250) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`),
  UNIQUE KEY `identity` (`identity`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla asistencia_l4g.students: ~5 rows (aproximadamente)
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` (`id`, `identity`, `names`, `surname`, `email`, `phone`, `semester`) VALUES
	(1, '8773465599', 'Rogelio', 'Rival', 'Rival@gmail.com', '3167884894', 'noveno'),
	(2, '1228946733', 'Alejandro', 'Cordoba', 'prueba@gmail.com', '32434312', 'cuarto'),
	(3, '1991793322', 'Alejandra', 'Saldado soto', 'Aleja@gamail.com', '23556678333', 'primero'),
	(4, '188374666', 'Rogelio', 'Rincon', 'rincon@gmail.com', '315763388', 'segundo'),
	(5, '34353323', 'Alexander', 'Penagos', 'alexander@gmail.com', '315883920', 'tercero');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;

-- Volcando estructura para tabla asistencia_l4g.subjects
CREATE TABLE IF NOT EXISTS `subjects` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `names` varchar(250) NOT NULL,
  `semester` varchar(250) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla asistencia_l4g.subjects: ~8 rows (aproximadamente)
/*!40000 ALTER TABLE `subjects` DISABLE KEYS */;
INSERT INTO `subjects` (`id`, `names`, `semester`) VALUES
	(1, 'calculo', 'tercero'),
	(2, 'redes', 'cuarto'),
	(5, 'algebra', 'segundo'),
	(6, 'politica', 'septimo');
/*!40000 ALTER TABLE `subjects` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
