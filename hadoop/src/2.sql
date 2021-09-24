select nn.name, nn.year_, sn.count_
from znu_names.national_names nn
join znu_names.state_names sn
  on (sn.name = nn.name and sn.year_ = nn.year_)
order by nn.year_ desc
limit 10;