-- CREACION DE LA BASE DE DATOS
CREATE DATABASE bd_prueba;

-- CREACION Y ASIGNACION DE PERMISOS A USUARIOS EXISTENTES Y NUEVOS
grant all privileges on database "bd_prueba" to postgres;
ALTER USER postgres WITH PASSWORD 'postgres';
create user usr_consulta with password '1234';
grant all on database "bd_prueba" to usr_consulta;

-- CREACION DEL UN ESQUEMA
CREATE SCHEMA sist_distri
    AUTHORIZATION usr_prueba;

-- CREAR TABLAS 
CREATE TABLE sist_distri.ciudades ( -- Tabla ciudades
    ciud_id serial NOT NULL, 
    ciud_nombre VARCHAR(50) NOT NULL,
    PRIMARY KEY (ciud_id)
) ;

CREATE TABLE sist_distri.personas ( -- Tabla personas
    dir_tel serial NOT NULL, 
    dir_tipo_tel VARCHAR(50) NOT NULL,
    dir_nombre VARCHAR(50) NOT NULL,
    dir_direccion VARCHAR(50) NOT NULL,
    dir_ciud_id int NOT NULL,
    FOREIGN KEY (dir_ciud_id) REFERENCES sist_distri.ciudades(ciud_id),
    PRIMARY KEY (dir_tel)
) ;

-- INSERT Datos de pruebas
INSERT INTO sist_distri.ciudades (ciud_nombre) values ('Bogotá'), ('Barranquilla'), ('Manizales'), ('Medellín'), ('Pereira');
INSERT INTO sist_distri.ciudades (ciud_nombre) VALUES ('Arauca'), ('San José del Guaviare'), ('Bello'), ('Arauca'), ('Girardot');

INSERT INTO sist_distri.personas (dir_tipo_tel,dir_nombre,dir_direccion,dir_ciud_id) VALUES ('Cel','Armando Felipe', 'Calle 87 # 1-59 Apto 91', 1);
INSERT INTO sist_distri.personas (dir_tipo_tel,dir_nombre,dir_direccion,dir_ciud_id) VALUES ('Fijo','Juan Fuentes', 'Circular 7 # 40-65', 2);
INSERT INTO sist_distri.personas (dir_tipo_tel,dir_nombre,dir_direccion,dir_ciud_id) VALUES ('Fijo','Ricardo Ignacio Melendez', 'Carrera 33 # 22-50', 3);
INSERT INTO sist_distri.personas (dir_tipo_tel,dir_nombre,dir_direccion,dir_ciud_id) VALUES ('Cel','Ingrid Vasquez', 'Calle 59 # 28-12', 4);
INSERT INTO sist_distri.personas (dir_tipo_tel,dir_nombre,dir_direccion,dir_ciud_id) VALUES ('Cel','Mateo Bustamante', 'Avenida 89A # 48-62', 4);


-- CREAR VISTA
CREATE VIEW sist_distri.vw_cruce AS
SELECT p.dir_tel as "Telefono", ,
p.dir_nombre as "Nombre",
p.dir_direccion as "Dirección",
c.ciud_nombre as "Ciudad"
from sist_distri.personas p 
left join sist_distri.ciudades c on p.dir_ciud_id = c.ciud_id
order by p.dir_nombre ;

ALTER TABLE sist_distri.vw_cruce
    OWNER TO postgres;

