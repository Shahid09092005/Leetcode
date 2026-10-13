# Write your MySQL query statement below
-- daily active user count for a period of 30 days ending 2019-07-27 inclusively. A user was active on someday if they made at least one activity on that day.

select activity_date as 'day' ,count(distinct user_id) as 'active_users'
from Activity
where activity_date<='2019-07-27' and activity_date>'2019-06-27'
group by activity_date 