select distinct l1.num as ConsecutiveNums
from Logs l1
inner join Logs l2
on l1.id=l2.id+1
inner join Logs l3
on l1.id=l3.id+2
where l1.num=l2.num and l3.num=l1.num;
