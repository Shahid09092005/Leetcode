with daily as (
    select visited_on,sum(amount) as "amount"
    from Customer
    group by visited_on
),
ans as (select visited_on , round(sum(amount) over (ORDER BY visited_on
    RANGE BETWEEN INTERVAL 6 DAY PRECEDING
          AND CURRENT ROW) ,2) as "amount",
    round(avg(amount) over (ORDER BY visited_on
    RANGE BETWEEN INTERVAL 6 DAY PRECEDING
          AND CURRENT ROW),2) as "average_amount"
from daily 
order by visited_on asc)

select * from ans
where visited_on >= date_add((select min(visited_on) from Customer),INTERVAL 6 DAY)