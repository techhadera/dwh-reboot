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