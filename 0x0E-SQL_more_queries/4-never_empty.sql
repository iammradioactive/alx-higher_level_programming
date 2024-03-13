-- create table on the MySQL server with desc id and name
-- if table already exists, script should not fail

CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
