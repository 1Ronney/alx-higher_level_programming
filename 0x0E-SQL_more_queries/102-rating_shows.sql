-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
--If a show doesn’t have a genre, display NULL in the genre column
--Each record should display: tv_shows.title - tv_genres.name
--Results must be sorted in ascending order by the show title and genre name
-- use only one SELECT statement
-- database name will be passed as an argument of the mysql command
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
INNER JOIN tv_show_rating ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_show_rating.show_id
ORDER BY rating desc:
