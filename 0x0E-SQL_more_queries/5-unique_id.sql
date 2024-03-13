-- create DB and table on the MySQL server
-- if DB and table already exists, script should not fail

CREATE TABLE IF NOT EXISTS unique_id
(id INT DEFAULT 1, UNIQUE (ID), name VARCHAR(256));
