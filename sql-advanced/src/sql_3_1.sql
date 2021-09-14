select
  product_name,
  filling,
  price,
  case
    when price > 200 then 'Too expensive, I can''t'' afford it'
    when price <= 200 and filling='малина' then 'Affordable price, I can buy it'
  end as decision
from (
  select *
  from pies_znu
  where product_name='блин' and filling='малина'
)