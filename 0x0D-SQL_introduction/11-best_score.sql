-- lists all records with a score >= 10 
-- in the table second_table of the database hbtn_0c_0 in MySQL server
-- ordered by top score first
SELECT score, name FROM second_table HAVING score >= 10 ORDER BY score DESC;
