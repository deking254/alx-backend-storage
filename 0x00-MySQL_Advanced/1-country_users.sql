-- creates a user table and database if they dont exist
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
	email VARCHAR(255) UNIQUE NOT NULL, name VARCHAR(255), country ENUM('US', 'CO', 'IN') DEFAULT 'US' NOT NULL);
