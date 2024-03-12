-- list number oof records with the same score
-- in the table of the DB

SELECT score, COUNT('score') as number FROM second_table
GROUP BY score ORDER BY score DESC;
