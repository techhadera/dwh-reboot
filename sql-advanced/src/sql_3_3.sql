update pies_znu set price=
  case
    when product_name='пирожок' then price*1.33
    when product_name='блин' then price*0.77
  end;