-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- tv_shows table contains only 1 record where title = Dexter (id can be different)
-- Each record displays: tv_genres.name
-- Results must be sorted in ascending order by the genre name
SELECT tv_genres.name 
FROM tv_shows INNER JOIN tv_show_genres INNER JOIN tv_genres 
ON tv_shows.title = "Dexter" AND tv_show_genres.show_id = tv_shows.id 
AND tv_show_genres.genre_id = tv_genres.id 
GROUP BY tv_genres.name 
ORDER BY tv_genres.name ASC;
