# Get latest records

## latest in each group
daily revenue values for each state
```sql
SELECT region, country, year(value_timestamp) as [year], month(value_timestamp) as [month], sum(revenue) as revenue from (
    SELECT [state],[country],[region],DATEADD(HOUR,10,value_timestamp) as value_timestamp,[revenue]
		,row_number() over(partition by state, update_date order by update_date desc) as rn
    FROM [dev].[annual_revenue]
    WHERE value_type = 'forecast'
) t
WHERE t.rn = 1
GROUP BY country, region, year(value_timestamp), month(value_timestamp)
ORDER BY region, country, year(value_timestamp), month(value_timestamp)
;
```
