# Практическое задание №4


1. Написать цикл, выводящий последовательно квадраты чисел от 1 до 12

    * [Ссылка на файл](src/sql_4_1.sql)   
      ```
      begin
        for i in 1..12 loop
          dbms_output.put_line(i*i);
        end loop;
      end;
      ```

1. Написать цикл, увеличивающий цену пирожков на 20% до тех пор, пока средняя цена пирожков не будет равна или превышать среднюю цену на блины.

    * [Ссылка на файл](src/sql_4_2.sql)   
      ```
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
      ```

1. Дополнить цикл из задачи № 2 условием, по которому выполнение цикла прекратиться в случае, если максимальная цена на пирожок превысит максимальную цену на блин

    * [Ссылка на файл](src/sql_4_3.sql)   
      ```
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

      ```