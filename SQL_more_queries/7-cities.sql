-- This task is about creating a table in a given database
-- This script create a table in a given database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
