declare
  min_price_granny number(5);
  min_price_granddad number(5);
begin
  select min(price) into min_price_granny from pies_znu
  where maker_type='бабушка';
  
  select min(price) into min_price_granddad from pies_znu
  where maker_type='дедушка';
  
  if min_price_granny > min_price_granddad then
    dbms_output.put_line('Самый дешёвый продукт делает дедушка');
  elsif min_price_granny < min_price_granddad then
    dbms_output.put_line('Самый дешёвый продукт делает бабушка');
  else
    dbms_output.put_line('Минимальная цена самого дешевого продукта одинакова');
  end if;
end;
