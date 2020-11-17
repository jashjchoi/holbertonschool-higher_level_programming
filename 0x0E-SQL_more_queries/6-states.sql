-- creates the database hbtn_0d_usa and the table states 
-- (in the database hbtn_0d_usa) on MySQL server
-- states id INT unique, auto generated, 
-- states id cant be null and is a primary key
-- states name VARCHAR(256) cant be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL);
