drop database if exists PaperRockTijera;

create database PaperRockTijera;

use PaperRockTijera;

create table player(
    id int auto_increment primary key,
    nombre varchar(50) not null,
    wins int not null DEFAULT 0,
    draw int not null DEFAULT 0,
    defeat int not null DEFAULT 0,
    piedra int not null DEFAULT 0,
    papel int not null DEFAULT 0,
    tijera int not null DEFAULT 0
);


create table partida(
    id int auto_increment primary key,
    Ganador varchar(50) not null,
    Perdedor varchar(50) not null,
    Empate varchar(50) not null
);

