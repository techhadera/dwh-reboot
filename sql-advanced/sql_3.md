# Практическое задание №3

1. Используя CASE вывести своё мнение о цене на блинчики с малиной

    * [Ссылка на файл](src/sql_3_1.sql)   
    ```
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
    ```

1. Вывести данные о пирожках, подменив цену на пирожки с определённой начинкой, соответствующей ценой на блины с той же начинкой. Это задание можно сделать проще, чем кажется на первый взгляд.

    * [Ссылка на файл](src/sql_3_2.sql)   
    ```
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
    ```

1. Увеличить цену пирожков на 33%, уменьшить цену блинов на 33%. Можно выполнить только одну команду update

    * [Ссылка на файл](src/sql_3_3.sql)   
    ```
    update pies_znu set price=
      case
        when product_name='пирожок' then price*1.33
        when product_name='блин' then price*0.77
      end;
    ```