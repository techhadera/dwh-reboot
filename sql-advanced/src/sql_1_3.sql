declare
  mystr varchar2(30);
begin
  select 'Hello, World!' into mystr from dual;
  dbms_output.put_line(mystr);
end;