-- creates a user table and database if they dont exist
CREATE DATABASE IF NOT EXISTS holberton;
CREATE TABLE IF NOT EXISTS holberton.users(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, email VARCHAR(255) UNIQUE NOT NULL, name VARCHAR(255));
