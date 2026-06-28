with res1 as (select product_id,order_date,sum(unit) as totalquant
from Orders 
where date_format(order_date,'%Y-%m')='2020-02'
group by product_id
having totalquant>=100 )

select p.product_name,r.totalquant as "unit"
from res1 r
join Products p
on r.product_id=p.product_id