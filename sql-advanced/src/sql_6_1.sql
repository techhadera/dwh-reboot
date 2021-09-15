with some_pies as (
  select p.*, row_number() over(order by price asc) rn
  from pies_znu p
)
select * from some_pies
where rn in (1,2,5);