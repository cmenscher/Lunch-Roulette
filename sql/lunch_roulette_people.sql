# ************************************************************
# Sequel Pro SQL dump
# Version 3408
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Host: ec2-50-16-167-75.compute-1.amazonaws.com (MySQL 5.1.52)
# Database: lunch_roulette
# Generation Time: 2011-09-09 16:04:39 -0400
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table People
# ------------------------------------------------------------

LOCK TABLES `People` WRITE;
/*!40000 ALTER TABLE `People` DISABLE KEYS */;

INSERT INTO `People` (`id`, `name`, `email`, `avail_1`, `avail_2`, `avail_3`, `avail_4`, `last_updated`)
VALUES
	(1,'Adam Clarkson','adam@chartbeat.com',NULL,NULL,NULL,NULL,NULL),
	(2,'Alex Carusillo ','alex.carusillo@chartbeat.com',NULL,NULL,NULL,NULL,NULL),
	(3,'Alex Lines ','alex@chartbeat.com',NULL,NULL,NULL,NULL,NULL),
	(4,'Allan Beaufour ','allan@chartbeat.com',NULL,NULL,NULL,NULL,NULL),
	(5,'Amanda McCormick ','amanda@socialflow.com',NULL,NULL,NULL,NULL,NULL),
	(6,'Andrew Cohen','ac@bit.ly',NULL,NULL,NULL,NULL,NULL),
	(7,'Andrew Flockhart','af@bit.ly',NULL,NULL,NULL,NULL,NULL),
	(8,'Andy Weissman','andy@betaworks.com',NULL,NULL,NULL,NULL,NULL),
	(9,'Antonia Abraham','antonia@betaworks.com',NULL,NULL,NULL,NULL,NULL),
	(10,'Ben Rowland ','ben@chartbeat.com',NULL,NULL,NULL,NULL,NULL),
	(11,'Ben Stahl ','ben.stahl@chartbeat.com',NULL,NULL,NULL,NULL,NULL),
	(12,'Brian David Eoff','be@bit.ly',NULL,NULL,NULL,NULL,NULL),
	(13,'Brian Nobili','brian@socialflow.com',NULL,NULL,NULL,NULL,NULL),
	(14,'Cherie Meyer','cherie@socialflow.com',NULL,NULL,NULL,NULL,NULL),
	(15,'Chris Utz ','chris@chartbeat.com ',NULL,NULL,NULL,NULL,NULL),
	(16,'Chris White ','chris@madraces.com',NULL,NULL,NULL,NULL,NULL),
	(17,'Christopher Sira','chris@socialflow.com',NULL,NULL,NULL,NULL,NULL),
	(18,'Corey Menscher','corey@findings.com',NULL,NULL,NULL,NULL,NULL),
	(19,'Daniel McGrath','daniel@chartbeat.com',NULL,NULL,NULL,NULL,NULL),
	(20,'Dawn Williamson ','dawn@chartbeat.com',NULL,NULL,NULL,NULL,NULL),
	(21,'Drew Good ','drew@socialflow.com',NULL,NULL,NULL,NULL,NULL),
	(22,'Eliot Pierce','eliotpierce@gmail.com',NULL,NULL,NULL,NULL,NULL),
	(23,'Eran Dror','Eran@bit.ly',NULL,NULL,NULL,NULL,NULL),
	(24,'Erica Malko','erica@socialflow.com ',NULL,NULL,NULL,NULL,NULL),
	(25,'Eytan Daniyalzade ','eytan@chartbeat.com',NULL,NULL,NULL,NULL,NULL),
	(26,'Frank Speiser','frank@socialflow.com',NULL,NULL,NULL,NULL,NULL),
	(27,'Freyja Gallagher','freyja@socialflow.com',NULL,NULL,NULL,NULL,NULL),
	(28,'Gilad Lotan ','gilad@socialflow.com',NULL,NULL,NULL,NULL,NULL),
	(29,'Greg Tomlinson ','gt@bit.ly',NULL,NULL,NULL,NULL,NULL),
	(30,'Heewa Barfchin','heewa@chartbeat.com',NULL,NULL,NULL,NULL,NULL),
	(31,'Hilary Mason','h@bit.ly',NULL,NULL,NULL,NULL,NULL),
	(32,'Isaac Greenbaum','isaac@chartbeat.com',NULL,NULL,NULL,NULL,NULL),
	(33,'Jake Levine ','jake@news.me',NULL,NULL,NULL,NULL,NULL),
	(34,'James Summers ','james@socialflow.com',NULL,NULL,NULL,NULL,NULL),
	(35,'Jason Morrow','jason@betaworks.com',NULL,NULL,NULL,NULL,NULL),
	(36,'Jeff Lanza','jeff@socialflow.com',NULL,NULL,NULL,NULL,NULL),
	(37,'Jeff Tierney','jt@bit.ly',NULL,NULL,NULL,NULL,NULL),
	(38,'Jehiah Czebotar','jehiah@bit.ly',NULL,NULL,NULL,NULL,NULL),
	(39,'John Borthwick','john@betaworks.com',NULL,NULL,NULL,NULL,NULL),
	(40,'Jonathan Basker ','jonathan@betaworks.com',NULL,NULL,NULL,NULL,NULL),
	(41,'Justin Lintz','jl@bit.ly',NULL,NULL,NULL,NULL,NULL),
	(42,'Justin Van Slembrouck','justin@news.me',NULL,NULL,NULL,NULL,NULL),
	(43,'Kate Braner ','kate@chartbeat.com',NULL,NULL,NULL,NULL,NULL),
	(44,'Kevin Garcia ','kevin@chartbeat.com',NULL,NULL,NULL,NULL,NULL),
	(45,'Mario Menti','mario@bit.ly',NULL,NULL,NULL,NULL,NULL),
	(46,'Matt Bango','matt@chartbeat.com',NULL,NULL,NULL,NULL,NULL),
	(47,'Matt Flamman','matt@socialflow.com',NULL,NULL,NULL,NULL,NULL),
	(48,'Matt LeMay','m@bit.ly',NULL,NULL,NULL,NULL,NULL),
	(49,'Matt Reiferson','snakes@bit.ly',NULL,NULL,NULL,NULL,NULL),
	(50,'Matthew Moran','matt.moran@socialflow.com',NULL,NULL,NULL,NULL,NULL),
	(51,'Matthew Rothenberg','mroth@bit.ly',NULL,NULL,NULL,NULL,NULL),
	(52,'Meghan Wherrity ','meg@bit.ly',NULL,NULL,NULL,NULL,NULL),
	(53,'Michael Chin ','michael@socialflow.com',NULL,NULL,NULL,NULL,NULL),
	(54,'Michael Young ','my@news.me',NULL,NULL,NULL,NULL,NULL),
	(55,'Mike Auteri','atari@socialflow.com',NULL,NULL,NULL,NULL,NULL),
	(56,'Mike Perrone ','mike@socialflow.com',NULL,NULL,NULL,NULL,NULL),
	(57,'Mona Chaudhuri','mona@chartbeat.com',NULL,NULL,NULL,NULL,NULL),
	(58,'Neil Wehrle ','neil@betaworks.com',NULL,NULL,NULL,NULL,NULL),
	(59,'Nicole Frand','nicole@betaworks.com',NULL,NULL,NULL,NULL,NULL),
	(60,'Noah Hamann ','noah@socialflow.com',NULL,NULL,NULL,NULL,NULL),
	(61,'Pat Speiser ','pat@socialflow.com',NULL,NULL,NULL,NULL,NULL),
	(62,'Peter Hershberg','peter@socialflow.com',NULL,NULL,NULL,NULL,NULL),
	(63,'Peter Stern  ','peter@bit.ly',NULL,NULL,NULL,NULL,NULL),
	(64,'Raquel Bujans ','raquel@socialflow.com',NULL,NULL,NULL,NULL,NULL),
	(65,'Robert Haining','rob@news.me',NULL,NULL,NULL,NULL,NULL),
	(66,'Sam Kaufman','sam@socialflow.com',NULL,NULL,NULL,NULL,NULL),
	(67,'Scott Lederer','Scott@bit.ly',NULL,NULL,NULL,NULL,NULL),
	(68,'Simon Brief ','simon@bit.ly',NULL,NULL,NULL,NULL,NULL),
	(69,'Summer Bedard ','summer@betaworks.com',NULL,NULL,NULL,NULL,NULL),
	(70,'Tadas Vilkeliskis','tadas@chartbeat.com',NULL,NULL,NULL,NULL,NULL),
	(71,'Tim Devane','td@bit.ly',NULL,NULL,NULL,NULL,NULL),
	(72,'Todd Levy','todd@bit.ly',NULL,NULL,NULL,NULL,NULL),
	(73,'Tom Germeau','tom@chartbeat.com',NULL,NULL,NULL,NULL,NULL),
	(74,'Tony Haile','tony@chartbeat.com',NULL,NULL,NULL,NULL,NULL);

/*!40000 ALTER TABLE `People` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
