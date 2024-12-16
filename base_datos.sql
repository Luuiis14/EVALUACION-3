

CREATE DATABASE GestionEmpleados;
USE GestionEmpleados;


CREATE TABLE Usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50) NOT NULL,
    contrasena_hash VARCHAR(255) NOT NULL,
    tipo_usuario ENUM('Admin', 'Empleado') NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Empleado (
    id_empleado INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    nombre_completo VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(15),
    puesto VARCHAR(50),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);


CREATE TABLE IndicadorEconomico (
    id_indicador INT AUTO_INCREMENT PRIMARY KEY,
    nombre_indicador VARCHAR(50) NOT NULL,
    fecha_consulta DATE NOT NULL,
    valor DECIMAL(10, 2) NOT NULL,
    fuente VARCHAR(100) NOT NULL
);


CREATE TABLE RegistroIndicador (
    id_registro INT AUTO_INCREMENT PRIMARY KEY,
    id_indicador INT NOT NULL,
    id_usuario INT NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_indicador) REFERENCES IndicadorEconomico(id_indicador),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);
