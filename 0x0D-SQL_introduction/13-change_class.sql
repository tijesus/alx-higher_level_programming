-- Remove all low scores
DELETE FROM `second_table`
WHERE `score` <= 5;
