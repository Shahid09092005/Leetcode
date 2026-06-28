with ans2 as (select departmentId,name,Salary from (select DENSE_RANK() over(partition by departmentId order by salary desc) as rnk ,id,name,salary,departmentId
from Employee ) as ans1
where rnk<=3 )

select d.name as "Department", a.name  as "Employee",a.Salary
from ans2 a
left join Department d
on a.departmentId= d.id