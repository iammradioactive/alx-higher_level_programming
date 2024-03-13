-- create table in the MySQL server with id and name
-- if table already exists script should not fail

CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
