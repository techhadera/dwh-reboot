# Практическое задание №2

1. Вычислить 2 переменные: самый дешёвый продукт, производимый бабушкой и дедушкой. Сравнить эти переменные. Вывести строку "Самый дешёвый продукт делает %MAKER_TYPE%", либо сообщение о равенстве цен самых дешёвых продуктов.

    * [Ссылка на файл](https://github.com/techhadera/dwh-reboot/tree/master/sql-advanced/src/sql_2_1.sql)   
      ```
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
      ```

1. Если средняя цена на блины меньше, чем средняя на пирожки, вывести сообщение: «В среднем, блины дешевле пирожков на X руб», где X – абсолютное значение разницы между средней ценой пирожка и средней ценой блина. Если средняя цена на блины больше или равна средней цены на пирожки, вывести сообщение: «блины стоят не меньше пирожков».

    * [Ссылка на файл](https://github.com/techhadera/dwh-reboot/tree/master/sql-advanced/src/sql_2_2.sql)   
      ```
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
      ```