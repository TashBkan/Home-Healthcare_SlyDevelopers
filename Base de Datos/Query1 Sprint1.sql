CREATE DATABASE home_care;
USE home_care;
-- CREAR TABLA PACIENTES --
CREATE TABLE pacientes(
	Id INT NOT NULL PRIMARY KEY,
	nombres VARCHAR(50) NOT NULL,
	apellidos VARCHAR(50) NOT NULL,
	fechaNacimiento DATE NOT NULL,
	genero VARCHAR(50) NULL,
	direccion VARCHAR(50) NOT NULL,
	longitud VARCHAR(30) NULL,
	latitud VARCHAR(30) NULL,
	telefono VARCHAR(50) NOT NULL,
	ciudad VARCHAR(30) NOT NULL,
	Email VARCHAR(30) NOT NULL
);

-- CREAR TABLA MÉDICO --
CREATE TABLE medico(
	Id INT NOT NULL PRIMARY KEY,
	nombres VARCHAR(50) NOT NULL,
	apellidos VARCHAR(50) NOT NULL,
	genero VARCHAR(50) NULL,
	telefono VARCHAR(50) NOT NULL,
	registroMedico VARCHAR(50) NOT NULL,
	especialidad VARCHAR(50) NOT NULL,
	pacienteID INT,
	FOREIGN KEY (pacienteID) REFERENCES pacientes (ID)
);

-- CREAR TABLA ENFERMERO --
CREATE TABLE enfermero(
	Id INT NOT NULL PRIMARY KEY,
	nombres VARCHAR(50) NOT NULL,
	apellidos VARCHAR(50) NOT NULL,
	genero VARCHAR(50) NULL,
	telefono VARCHAR(50) NOT NULL,
	pacienteID INT,
	FOREIGN KEY (pacienteID) REFERENCES pacientes (ID)
);

-- CREAR TABLA AUXILIAR --
CREATE TABLE auxiliar(
	Id INT NOT NULL PRIMARY KEY,
	nombres VARCHAR(50) NOT NULL,
	apellidos VARCHAR(50) NOT NULL,
	genero VARCHAR(50) NULL,
	telefono VARCHAR(50) NOT NULL,
	pacienteID INT,
	FOREIGN KEY (pacienteID) REFERENCES pacientes (ID)
);

-- CREAR TABLA ACOMPAÑANTE --
CREATE TABLE acompañante(
	Id INT NOT NULL PRIMARY KEY,
	nombres VARCHAR(50) NOT NULL,
	apellidos VARCHAR(50) NOT NULL,
	genero VARCHAR(50) NULL,
	telefono VARCHAR(50) NOT NULL,
	parentezco VARCHAR(50) NOT NULL,
	Email VARCHAR(90) NOT NULL,
	pacienteID INT,
	FOREIGN KEY (pacienteID) REFERENCES pacientes (Id)
);

-- CREAR TABLA HISTORIA CLÍNICA --
CREATE TABLE historia_clinica(
	Id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	diagnostico VARCHAR(50) NOT NULL,
	signos VARCHAR(50) NOT NULL,
	oximetria VARCHAR(50) NULL,
	frecRespiratoria VARCHAR(50) NOT NULL,
	frecCardiaca VARCHAR(50) NOT NULL,
	temperatura VARCHAR(50) NOT NULL,
	presionArterial VARCHAR(50) NOT NULL,
	glicemias VARCHAR(50) NOT NULL,
	sugerenciasCuidado VARCHAR(50) NOT NULL,
	pacienteID INT,
	FOREIGN KEY (pacienteID) REFERENCES pacientes (ID)
);

-- CREAR TABLA PACIENTES --
INSERT INTO pacientes VALUES
(5489784, 'pedro', 'suarez', '1960-05-27', 'masculino', 'calle 30 50 20', '5°N', '20°E', '6930257', 'Bogota', 'pedro_sua@gmail.com'),
(5689745, 'juan', 'rodriguez', '1958-05-15', 'masculino', 'calle 25 50 10', '7°N', '9°E', '5698741', 'Bogota', 'juan_sua@gmail.com'),
(4589715, 'orieta', 'marquez', '1960-02-02', 'femenina', 'calle 22 09 15', '5°N', '3°E', '3201234562', 'Bogota', 'orietM@gmail.com');

INSERT INTO medico VALUES
(102564789, 'esteban', 'cortez', 'masculino', '3115230002', '4568793214', 'familiar', '5489784'),
(452365782, 'carlos', 'arevalo', 'masculino', '3114568700', '5211102142', 'medicina familiar', '5689745'),
(523654782, 'felipe', 'gonzalez', 'masculino', '3202220001', '5236547840', 'medicina_general', '4589715');

INSERT INTO enfermero VALUES
(102568974, 'julio', 'cortez', 'masculino', '3568789547', '5689745'),
(256547898, 'laura', 'zapata', 'femenina', '3502356800', '5489784'), 
(235642012, 'vanessa', 'jara', 'femenina', '3201110225', '4589715'); 

INSERT INTO auxiliar VALUES
(25636580, 'fernanda', 'aparicio', 'femenina', '3568789547', '5689745'),
(23564210, 'mauricio', 'perez', 'masculino', '3203330000', '5489784'),
(21022254, 'jairo', 'marin', 'masculino', '3151222320', '4589715');

INSERT INTO acompañante VALUES
(35235784, 'marcela', 'garcia', 'femenino', '3212564151', 'sobrina', 'marceG@gmail.com', '5489784'),
(45689421, 'carlos', 'rodriguez', 'masculino', '300221100', 'hijo', 'carlosC@gmail.com', '5689745'),
(20321451, 'laura', 'marquez', 'femenina', '3102321250', 'hermana', 'lauraM@gmail.com', '4589715');

INSERT INTO historia_clinica (diagnostico, signos, oximetria, frecRespiratoria, frecCardiaca, temperatura, presionArterial, glicemias, sugerenciasCuidado, pacienteID) VALUES ('tuberculosis', '70', '16', '12', '75', '36.5', '120/80', '7.8', 'continuar con administracion de medicamentos', '5489784'),
('hemiparesia', '75', '18', '13', '73', '37.5', '110/70', '8.8', 'se requiere fisioterapia', '5689745'),
('cirrosis', '69', '14', '15', '71', '39.5', '130/70', '9.8', 'valoracion medicina Interna', '4589715');

SELECT * FROM pacientes;
SELECT * FROM medico;

-- MODIFICACIONES Y BORRADO --
DELETE FROM pacientes WHERE nombres='pedro';

SELECT pacientes.nombres AS nombre_paciente, pacientes.apellidos AS apellidos_paciente, medico.nombres AS nombre_medico, medico.apellidos AS apellidos_medico, medico.especialidad AS especialidad_medica
FROM PACIENTES
INNER JOIN medico ON pacientes.Id= medico.pacienteID;