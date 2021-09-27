select count(*) total_count, gender
from znu_on_delete.state_names
group by gender;