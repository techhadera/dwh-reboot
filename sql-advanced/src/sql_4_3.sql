declare
  avg_pie_price number(5,2);
  avg_pancake_price number(5,2);
  max_pie_price number(5,2);
  max_pancake_price number(5,2);
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

  -- Инициализация максимальной стоимости пирожка
  select max(price) into max_pie_price
  from pies_znu
  where product_name = 'пирожок';

  -- Инициализация максимальной стоимости блина
  select max(price) into max_pancake_price
  from pies_znu
  where product_name = 'блин';
  
  while avg_pie_price < avg_pancake_price loop

    -- Завершить цикл, если максимальная цена
    -- на пирожок превысит максимальную цену на блин
    if max_pie_price > max_pancake_price then
      exit;
    end if;

    -- Обновление стоимости всех пирожков
    update pies_znu
    set price = price * 1.2
    where product_name = 'пирожок';
    
    -- Обновление средней стоимости пирожка
    select avg(price) into avg_pie_price
    from pies_znu
    where product_name = 'пирожок'
    group by product_name;

    -- Обновление максимальной стоимости пирожка
    select max(price) into max_pie_price
    from pies_znu
    where product_name = 'пирожок';
  end loop;
  commit;
end;
