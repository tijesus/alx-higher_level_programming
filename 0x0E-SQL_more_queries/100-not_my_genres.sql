-- List all genre that is not for DEXTER
SELECT `tv_genres`.`name` FROM `tv_genres`
WHERE `tv_genres`.`id` IN (
    SELECT `tv_shows`.`id` FROM `tv_shows`
    WHERE `title` = 'DEXTER'
)
ORDER BY `tv_genres`.`name` ASC;
