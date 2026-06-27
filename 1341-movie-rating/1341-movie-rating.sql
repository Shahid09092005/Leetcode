# name of the user who has rated the greatest number of movies
with moviecnt as (select user_id,count(*) as cnt
from MovieRating
group by user_id ) ,

ratingavg  as (select movie_id,avg(rating) as avgrate
from MovieRating
where date_format(created_at,'%Y-%m')="2020-02"
group by movie_id )

(select u.name as "results"
from Moviecnt m
join Users u 
on m.user_id = u.user_id
order by m.cnt desc,u.name asc
limit 1)

union all

#movie name with the highest average rating in February 2020  2020-02  

(select m.title as "results"
from ratingavg r
join Movies m
on r.movie_id = m.movie_id
order by r.avgrate desc,m.title asc
limit 1
)