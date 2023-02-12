-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema Contaminacion_Madrid
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Contaminacion_Madrid
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Contaminacion_Madrid` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `Contaminacion_Madrid` ;

-- -----------------------------------------------------
-- Table `Contaminacion_Madrid`.`Estaciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Contaminacion_Madrid`.`Estaciones` (
  `estaciones_id` INT NOT NULL,
  `estacion` VARCHAR(100) NULL,
  PRIMARY KEY (`estaciones_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Contaminacion_Madrid`.`Magnitudes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Contaminacion_Madrid`.`Magnitudes` (
  `magnitudes_id` INT NOT NULL,
  `magnitud` VARCHAR(100) NULL,
  PRIMARY KEY (`magnitudes_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Contaminacion_Madrid`.`unidades_medida`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Contaminacion_Madrid`.`unidades_medida` (
  `unidades_id` INT NOT NULL,
  `unidad` VARCHAR(45) NULL,
  PRIMARY KEY (`unidades_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Contaminacion_Madrid`.`Datos_anteriores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Contaminacion_Madrid`.`Datos_anteriores` (
  `estacion_id` INT NOT NULL,
  `magnitud_id` INT NOT NULL,
  `unidad_id` INT NOT NULL,
  `ano` INT NOT NULL,
  `mes` INT NOT NULL,
  `dia` INT NOT NULL,
  `1` INT NULL,
  `2` INT NULL,
  `3` INT NULL,
  `4` INT NULL,
  `5` INT NULL,
  `6` INT NULL,
  `7` INT NULL,
  `8` INT NULL,
  `9` INT NULL,
  `10` INT NULL,
  `11` INT NULL,
  `12` INT NULL,
  `13` INT NULL,
  `14` INT NULL,
  `15` INT NULL,
  `16` INT NULL,
  `17` INT NULL,
  `18` INT NULL,
  `19` INT NULL,
  `20` INT NULL,
  `21` INT NULL,
  `22` INT NULL,
  `23` INT NULL,
  `24` INT NULL,
  INDEX `fk_Datos_anteriores_Estaciones_idx` (`estacion_id` ASC) VISIBLE,
  INDEX `fk_Datos_anteriores_Magnitudes1_idx` (`magnitud_id` ASC) VISIBLE,
  INDEX `fk_Datos_anteriores_unidades_medida1_idx` (`unidad_id` ASC) VISIBLE,
  CONSTRAINT `fk_Datos_anteriores_Estaciones`
    FOREIGN KEY (`estacion_id`)
    REFERENCES `Contaminacion_Madrid`.`Estaciones` (`estaciones_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Datos_anteriores_Magnitudes1`
    FOREIGN KEY (`magnitud_id`)
    REFERENCES `Contaminacion_Madrid`.`Magnitudes` (`magnitudes_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Datos_anteriores_unidades_medida1`
    FOREIGN KEY (`unidad_id`)
    REFERENCES `Contaminacion_Madrid`.`unidades_medida` (`unidades_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Contaminacion_Madrid`.`Datos_nuevos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Contaminacion_Madrid`.`Datos_nuevos` (
  `estacion_id` INT NOT NULL,
  `magnitud_id` INT NOT NULL,
  `unidad_id` INT NOT NULL,
  `ano` INT NOT NULL,
  `mes` INT NOT NULL,
  `dia` INT NOT NULL,
  `hora` INT NOT NULL,
  `valor` INT NULL,
  INDEX `fk_Datos_nuevos_Estaciones1_idx` (`estacion_id` ASC) VISIBLE,
  INDEX `fk_Datos_nuevos_Magnitudes1_idx` (`magnitud_id` ASC) VISIBLE,
  INDEX `fk_Datos_nuevos_unidades_medida1_idx` (`unidad_id` ASC) VISIBLE,
  CONSTRAINT `fk_Datos_nuevos_Estaciones1`
    FOREIGN KEY (`estacion_id`)
    REFERENCES `Contaminacion_Madrid`.`Estaciones` (`estaciones_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Datos_nuevos_Magnitudes1`
    FOREIGN KEY (`magnitud_id`)
    REFERENCES `Contaminacion_Madrid`.`Magnitudes` (`magnitudes_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Datos_nuevos_unidades_medida1`
    FOREIGN KEY (`unidad_id`)
    REFERENCES `Contaminacion_Madrid`.`unidades_medida` (`unidades_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
