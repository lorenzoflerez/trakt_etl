-- MySQL Script generated by MySQL Workbench
-- vie 04 dic 2020 05:12:46 -05
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Pelicula`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Pelicula` (
  `id_movie` INT NOT NULL,
  `title` VARCHAR(60) NULL,
  `year` VARCHAR(45) NULL,
  `overview` VARCHAR(255) NULL,
  `language` VARCHAR(45) NULL,
  `download_api` TIMESTAMP(16) NOT NULL,
  `upload_to_bd` TIMESTAMP(16) NOT NULL,
  PRIMARY KEY (`id_movie`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Estadistica`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Estadistica` (
  `title` VARCHAR(60) NULL,
  `released` TIMESTAMP(8) NULL,
  `country` VARCHAR(45) NULL,
  `runtime` INT(11) NULL,
  `rating` FLOAT NULL,
  `votes` INT(11) NULL,
  `comment_count` INT(11) NULL,
  `updated_at` TIMESTAMP(16) NULL,
  `download_api` TIMESTAMP(16) NOT NULL,
  `upload_to_bd` TIMESTAMP(16) NOT NULL,
  `Pelicula_id_movie` INT NOT NULL,
  INDEX `fk_Estadistica_Pelicula_idx` (`Pelicula_id_movie` ASC),
  PRIMARY KEY (`Pelicula_id_movie`),
  CONSTRAINT `fk_Estadistica_Pelicula`
    FOREIGN KEY (`Pelicula_id_movie`)
    REFERENCES `mydb`.`Pelicula` (`id_movie`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Persona`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Persona` (
  `id_persona` INT NOT NULL,
  `nombre` VARCHAR(60) NULL,
  `rol` VARCHAR(45) NULL,
  `download_api` TIMESTAMP(16) NOT NULL,
  `updated_to_bd` TIMESTAMP(16) NOT NULL,
  `Pelicula_id_movie` INT NOT NULL,
  PRIMARY KEY (`id_persona`),
  INDEX `fk_Persona_Pelicula1_idx` (`Pelicula_id_movie` ASC),
  CONSTRAINT `fk_Persona_Pelicula1`
    FOREIGN KEY (`Pelicula_id_movie`)
    REFERENCES `mydb`.`Pelicula` (`id_movie`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;