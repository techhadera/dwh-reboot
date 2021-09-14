select
  pi.product_name,
  pi.filling,
  pi.maker_id,
  pi.maker_type,
  pa.price,
  pi.available,
  pi.prod_date
from pies_est pi
join pies_est pa on
  pi.filling = pa.filling and pi.product_name='пирожок' and pa.product_name='блин';
