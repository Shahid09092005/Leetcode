with ctc as ((select requester_id as "people"  from RequestAccepted )
union all
(select accepter_id as "people"  from RequestAccepted ) )

select people as "id",count(*) as num
from ctc 
group by people
order by num desc
limit 1;

