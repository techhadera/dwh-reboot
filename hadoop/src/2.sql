select nn.name, nn.year_, sn.count_
from znu_on_delete.national_names nn
join znu_on_delete.state_names sn
on (sn.name = nn.name and sn.year_ = nn.year_)
order by nn.year_ desc
limit 10;