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