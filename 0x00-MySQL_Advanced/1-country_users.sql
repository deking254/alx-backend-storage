-- creates a user table and database if they dont exist
CREATE DATABASE IF NOT EXISTS holberton;
create table if not exists holberton.users(id int not null primary key auto_increment, 
email varchar(255) unique not null, name varchar(255), country enum('US', 'CO', 'IN') default 'US' not null);
