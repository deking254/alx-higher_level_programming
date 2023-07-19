-- lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT `title`, SUM(`rate`) AS `r` FROM `tv_shows` AS s INNER JOIN `tv_show_ratings` AS rat ON s.`id` = rat.`show_id` GROUP BY `title` ORDER BY `r` DESC;
