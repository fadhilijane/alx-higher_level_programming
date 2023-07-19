-- creates the database hbtn_0d_usa
-- the table states (in the database hbtn_0d_usa)
-- id INT unique, auto generated, can’t be null and is a primary key
-- name VARCHAR(256) can’t be null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	NAME VARCHAR(256) NOT NULL,
	PRIMARY KEY(id));
