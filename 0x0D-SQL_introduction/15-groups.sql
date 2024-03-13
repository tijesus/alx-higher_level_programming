-- List numbers of record in a script
SELECT score, COUNT(*) as `number` FROM second_table 
GROUP BY score ORDER BY `number` DESC;