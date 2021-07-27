# group

```sql
--simulation time statistics
select t.sim_name, t.sim_id, avg(t.simtime_minutes), min(t.simtime_minutes), max(t.simtime_minutes) 
from (
    select sim_name, sim_id, sim_start, sim_end, (time_to_sec(sim_start) - time_to_sec(sim_end))/60 as simtime_minutes
    from db.sim
    having simtime_minutes > 1
    order by sim_name, simtime_minutes
) as t
group by t.sim_name;
```