BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `Profesor` (
	`dni_id`	INTEGER,
	`nombre_profesor`	TEXT NOT NULL,
	`apellido_profesor`	TEXT NOT NULL,
	`curso_profesor`	INTEGER NOT NULL,
	`estado_profesor`	INTEGER NOT NULL,
	`email_profesor`	TEXT NOT NULL,
	PRIMARY KEY(`dni_id`)
);
CREATE TABLE IF NOT EXISTS `Materia` (
	`id_materia`	INTEGER,
	`nombre_materia`	TEXT NOT NULL,
	`curso_materia`	INTEGER NOT NULL,
	`descripcion`	TEXT,
	`horario`	INTEGER NOT NULL,
	PRIMARY KEY(`id_materia`)
);
CREATE TABLE IF NOT EXISTS `Estudiante` (
	`legajo_id`	INTEGER,
	`dni`	INTEGER NOT NULL,
	`nombre`	TEXT NOT NULL,
	`apellido`	TEXT NOT NULL,
	`edad`	INTEGER NOT NULL,
	`fecha_nacimiento`	INTEGER NOT NULL,
	`curso`	INTEGER NOT NULL,
	`estado`	INTEGER NOT NULL,
	`email`	TEXT NOT NULL,
	PRIMARY KEY(`legajo_id`)
);
CREATE TABLE IF NOT EXISTS `Calificacion` (
	`legajo_id`	INTEGER,
	`id_materia`	INTEGER NOT NULL,
	`nota`	INTEGER,
	`fecha`	INTEGER NOT NULL,
	PRIMARY KEY(`legajo_id`)
);
COMMIT;
