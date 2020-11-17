-- creates the database hbtn_0d_usa and the table 
-- cities (in the database hbtn_0d_usa) on MySQL server
-- id INT unique, auto generated, cant be null and is a primary key
-- state_id INT, cant be null and must be a FOREIGN KEY that references to id of the states table
-- name VARCHAR(256) cant be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, state_id INT NOT NULL, FOREIGN KEY(state_id) REFERENCES states(id), name VARCHAR(256) NOT NULL);
