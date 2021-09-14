declare
  avg_pancake_price number(5,2);
  avg_pie_price number(5,2);
  delta_price number(5,2);
begin
  select avg(price) into avg_pancake_price
  from pies_znu
  where product_name='блин'
  group by product_name;

  select avg(price) into avg_pie_price
  from pies_znu
  where product_name='пирожок'
  group by product_name;
  
  if avg_pancake_price < avg_pie_price then
    delta_price := abs(avg_pancake_price-avg_pie_price);
    dbms_output.put_line('В среднем, блины дешевле пирожков на '||delta_price||' руб');
  else
    dbms_output.put_line('Блины стоят не меньше пирожков');
  end if;
end;