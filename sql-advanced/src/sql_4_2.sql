declare
  avg_pie_price number(5,2);
  avg_pancake_price number(5,2);
begin
  -- Инициализация средней стоимости пирожков
  select avg(price) into avg_pie_price
  from pies_znu
  where product_name = 'пирожок'
  group by product_name;
  
  -- Инициализация средней стоимости блинов
  select avg(price) into avg_pancake_price
  from pies_znu
  where product_name = 'блин'
  group by product_name;
  
  while avg_pie_price < avg_pancake_price loop
    -- Обновление стоимости всех пирожков
    update pies_znu
    set price = price * 1.2
    where product_name = 'пирожок';
    
    -- Обновление средней стоимости пирожков
    select avg(price) into avg_pie_price
    from pies_znu
    where product_name = 'пирожок'
    group by product_name;
  end loop;
  commit;
end;
