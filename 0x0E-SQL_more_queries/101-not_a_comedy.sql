-- Lists all shows without the comedy genre in the database hbtn_0d_tvshows.
SELECT DISTINCT `title` FROM `tv_shows` AS d LEFT JOIN `tv_show_genres` AS s ON s.`show_id` = d.`id` LEFT JOIN `tv_genres` AS g
ON g.`id` = s.`genre_id` WHERE d.`title` NOT IN (SELECT `title` FROM `tv_shows` AS t INNER JOIN `tv_show_genres` AS s ON s.`show_id` = t.`id` INNER JOIN `tv_genres` AS g
ON g.`id` = s.`genre_id` WHERE g.`name` = "Comedy") ORDER BY `title`;
