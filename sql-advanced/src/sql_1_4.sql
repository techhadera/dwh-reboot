with abc as (
  select product_name, AVG(price) as average_price
  from pies_znu
  group by product_name
  having avg(price) > 70
)
select * from abc;