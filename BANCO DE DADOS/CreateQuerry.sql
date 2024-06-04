CREATE DATABASE IF NOT EXISTS `global_solution`;

CREATE TABLE IF NOT EXISTS `global_solution`.`dados` (
	`GUID_coleta` VARCHAR(50) NOT NULL COLLATE 'latin1_swedish_ci',
	`GUID_nome` VARCHAR(50) NOT NULL COLLATE 'latin1_swedish_ci',
	`longitude` FLOAT NOT NULL DEFAULT '0',
	`latitude` FLOAT NOT NULL DEFAULT '0',
	`temperatura_ambiente` TINYINT(4) NOT NULL DEFAULT '0',
	`temperatura_agua` TINYINT(4) NOT NULL DEFAULT '0',
	`umidade` TINYINT(4) NOT NULL DEFAULT '0',
	`turbidez` INT(11) NOT NULL DEFAULT '0',
	`impurezas` BIGINT(20) NOT NULL DEFAULT '0',
	`data` VARCHAR(50) NOT NULL COLLATE 'latin1_swedish_ci',
	PRIMARY KEY (`GUID_coleta`) USING BTREE
)
COLLATE='latin1_swedish_ci'
ENGINE=InnoDB
;

CREATE TABLE IF NOT EXISTS `global_solution`.`dispositivos` (
	`GUID_nome` VARCHAR(50) NOT NULL COLLATE 'latin1_swedish_ci',
	`nome` VARCHAR(50) NOT NULL COLLATE 'latin1_swedish_ci',
	INDEX `GUID_nome` (`GUID_nome`) USING BTREE
)
COLLATE='latin1_swedish_ci'
ENGINE=InnoDB
;
