create or replace function TheNumbers(num in number) return number
is
begin
  return num / 2;
end;
/
select TheNumbers(11) from dual;