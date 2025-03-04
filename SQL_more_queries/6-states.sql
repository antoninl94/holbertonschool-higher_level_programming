-- This task is about creating a table in a given database
-- This script create a table in a given database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(256)
);
