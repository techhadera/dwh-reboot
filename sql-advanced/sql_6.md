# Практическое задание №6

1. Вывести 1,2 и 5 строки из PIES в порядке увеличения цены продукта

    * [Ссылка на файл](https://github.com/techhadera/dwh-reboot/tree/master/sql-advanced/src/sql_6_1.sql)   
      ```
      with some_pies as (
        select p.*, row_number() over(order by price asc) rn
        from pies_znu p
      )
      select * from some_pies
      where rn in (1,2,5);
      ```

1. Написать запрос, выводящий актуальную (с самым большим EFD) конфигурацию по каждому продукту из таблицы PRODUCT_CONF

    * [Ссылка на файл](https://github.com/techhadera/dwh-reboot/tree/master/sql-advanced/src/sql_6_2.sql)   
      ```
      with actual_data as (
        select pc.*, row_number() over(partition by product order by efd desc) rn
        from product_conf pc
      )
      select * from actual_data
      where rn = 1;
      ```