with ctc as (select person_id,person_name,turn, sum(weight) over(order by turn asc) as running_sum
from Queue )


select person_name
from ctc 
where ctc.running_sum<=1000
order by ctc.turn desc
limit 1