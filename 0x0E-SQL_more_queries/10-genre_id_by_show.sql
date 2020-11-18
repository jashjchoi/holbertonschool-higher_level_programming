-- lists all shows contained in hbtn_0d_tvshows
-- have at least one genre linked
-- Each record displays: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in asc order by tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show_genres INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
