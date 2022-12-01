-- creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa

-- switch database
USE hbtn_0d_usa

-- Create table in database
CREATE TABLE IF NOT EXISTS cities(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL FOREIGN KEY REFERENCES states(id),
	name VARCHAR(256)
);
