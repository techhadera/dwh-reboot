# Практическое задание № 1

1. В разделе declare объявить переменную mystr, положить в неё значение «Hello, World!». Затем вывести на экран, используя dbms_output.put_line();

    * [Ссылка на файл](https://github.com/techhadera/dwh-reboot/tree/master/sql-advanced/src/sql_1_1.sql)   
      ```
      declare
        mystr varchar2(30) := 'Hello, World!';
      begin
        dbms_output.put_line(mystr);
      end;
      ```

1. Повторить п.1, присвоив значение «Hello, World!» внутри блока begin..end с помощью конструкции :=

    * [Ссылка на файл](https://github.com/techhadera/dwh-reboot/tree/master/sql-advanced/src/sql_1_2.sql)   
      ```
      declare
        mystr varchar2(30);
      begin
        mystr := 'Hello, World!';
        dbms_output.put_line(mystr);
      end;
      ```


1. Повторить п.1, присвоив значение «Hello, World!» внутри блока begin..end с помощью конструкции select … into

    * [Ссылка на файл](https://github.com/techhadera/dwh-reboot/tree/master/sql-advanced/src/sql_1_3.sql)   
      ```
      declare
        mystr varchar2(30);
      begin
        select 'Hello, World!' into mystr from dual;
        dbms_output.put_line(mystr);
      end;
      ```

1. Используя with … as, создать табличное выражение, содержащее все записи, со средней ценой товара больше 70. С помощью select отобразить всё содержимое этого выражения. В видео есть небольшая оговорка про "проценты". Это, конечно, просто оговорка, имеется в виду абсолютное значение

    * [Ссылка на файл](https://github.com/techhadera/dwh-reboot/tree/master/sql-advanced/src/sql_1_4.sql)   
      ```
      with abc as (
        select 
          product_name,
          AVG(price) as average_price
        from pies_znu
        group by product_name
        having avg(price) > 70
      )
      select * from abc;
      ```