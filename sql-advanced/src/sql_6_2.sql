with actual_data as (
  select pc.*, row_number() over(partition by product order by efd desc) rn
  from product_conf pc
)
select * from actual_data
where rn = 1;