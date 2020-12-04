use mydb;

CREATE TABLE IF NOT EXISTS `mydb`.`Pelicula` (
  `id_movie` INT NOT NULL,
  `title` VARCHAR(60) NULL,
  `year` VARCHAR(45) NULL,
  `overview` VARCHAR(45) NULL,
  `language` VARCHAR(45) NULL,
  `download_api` TIMESTAMP(6) NULL,
  `upload_to_bd` TIMESTAMP(6) NULL,
  PRIMARY KEY (`id_movie`));
  
  CREATE TABLE IF NOT EXISTS `mydb`.`Estadistica` (
  `title` VARCHAR(60) NULL,
  `released` TIMESTAMP(6) NULL,
  `country` VARCHAR(45) NULL,
  `runtime` INT NULL,
  `rating` FLOAT NULL,
  `votes` INT NULL,
  `comment_count` INT NULL,
  `updated_at` TIMESTAMP(6) NULL,
  `download_api` TIMESTAMP(6) NOT NULL,
  `upload_to_bd` TIMESTAMP(6) NOT NULL,
  `Pelicula_id_movie` INT NOT NULL,
  INDEX `fk_Estadistica_Pelicula_idx` (`Pelicula_id_movie` ASC),
  PRIMARY KEY (`Pelicula_id_movie`),
  CONSTRAINT `fk_Estadistica_Pelicula`
    FOREIGN KEY (`Pelicula_id_movie`)
    REFERENCES `mydb`.`Pelicula` (`id_movie`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW TABLES
