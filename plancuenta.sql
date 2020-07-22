-- --------------------------------------------------------
-- Host:                         localhost
-- Versión del servidor:         10.4.6-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             10.2.0.5599
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para plancuenta
CREATE DATABASE IF NOT EXISTS `plancuenta` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `plancuenta`;

-- Volcando estructura para tabla plancuenta.grupo
CREATE TABLE IF NOT EXISTS `grupo` (
  `idgrupo` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) DEFAULT '0',
  PRIMARY KEY (`idgrupo`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla plancuenta.grupo: ~5 rows (aproximadamente)
/*!40000 ALTER TABLE `grupo` DISABLE KEYS */;
INSERT INTO `grupo` (`idgrupo`, `descripcion`) VALUES
	(1, 'Activos'),
	(2, 'Pasivo'),
	(3, 'Patrimonio'),
	(5, 'Ingresos');
/*!40000 ALTER TABLE `grupo` ENABLE KEYS */;

-- Volcando estructura para tabla plancuenta.plancuenta
CREATE TABLE IF NOT EXISTS `plancuenta` (
  `idplan` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(50) DEFAULT '0',
  `idgrupo` int(11) NOT NULL,
  `descripcion` varchar(50) DEFAULT '',
  `naturaleza` varchar(50) DEFAULT NULL,
  `estado` bit(1) DEFAULT NULL,
  PRIMARY KEY (`idplan`),
  KEY `FK__grupo` (`idgrupo`),
  CONSTRAINT `FK__grupo` FOREIGN KEY (`idgrupo`) REFERENCES `grupo` (`idgrupo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla plancuenta.plancuenta: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `plancuenta` DISABLE KEYS */;
INSERT INTO `plancuenta` (`idplan`, `codigo`, `idgrupo`, `descripcion`, `naturaleza`, `estado`) VALUES
	(1, '01', 1, 'Caja', 'D', b'1'),
	(3, '01', 2, 'cuentasxpagar', 'A', b'1');
/*!40000 ALTER TABLE `plancuenta` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
