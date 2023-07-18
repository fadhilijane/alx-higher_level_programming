-- lists the number of records with the same score in the table
-- sorted by the number of records (descending)

SELECT score, COUNT(score) AS number FROM second_table GROUP BY number DESC;
