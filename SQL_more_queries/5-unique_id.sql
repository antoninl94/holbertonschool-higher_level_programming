-- This task is about creating a table in a given database
-- This script create a table in a given database
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT UNIQUE 1,
    name VARCHAR(256)
);
