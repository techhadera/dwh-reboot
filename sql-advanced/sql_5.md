# Практическое задание №5

1. Создать и вызвать функцию TheNumbers, производящую деление числа на 2

      * [Ссылка на файл](src/sql_5_1.sql)   
        ```
        create or replace function TheNumbers(num in number) return number
        is
        begin
          return num / 2;
        end;
        /
        select TheNumbers(11) from dual;
        ```

1. Создать произвольную таблицу и написать процедуру, удаляющую её

    * [Ссылка на файл](src/sql_5_2.sql)   
      ```
      create table tmp_pancakes_znu
        as (
          select * 
          from pies_znu
          where product_name = 'блин'
        );

      create or replace procedure drop_tmp_table_znu(table_name in varchar2)
      is
      begin
        execute immediate 'drop table ' || table_name;
      end;
      /
      begin
        drop_tmp_table_znu('tmp_pancakes_znu');
      end;
      ```

1. Создать функцию, которая будет инвертировать введённый текст длинной до 128 символов.

    * [Ссылка на файл](src/sql_5_3.sql)   
      ```
      create or replace function reverse_str(str in varchar2) return varchar2
      is
        reversed_str varchar2(128);
      begin
        reversed_str := revers(str);
        return reversed_str;
      end;
      /
      begin
        dbms_output.put_line(reverse_str('Reverse me'));
      end;
      ```