select count(*) total_count, gender
from znu_names.state_names
group by gender;