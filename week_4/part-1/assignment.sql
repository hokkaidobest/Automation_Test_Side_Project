CREATE DATABASE `assignment`;

USE `assignment`;

CREATE TABLE `user` (
    `id` int AUTO_INCREMENT,
    `email` varchar(255) NOT NULL,
    `password` varchar(255) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE (`email`)
);