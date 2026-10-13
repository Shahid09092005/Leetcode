select p.product_id, 
case
when round((sum(p.price*u.units)/sum(u.units)),2) is null then 0
else round((sum(p.price*u.units)/sum(u.units)),2)
end
as "average_price"
from Prices p
left join UnitsSold u
on p.product_id=u.product_id and (p.start_date<=u.purchase_date and u.purchase_date<=p.end_date)
group by p.product_id
