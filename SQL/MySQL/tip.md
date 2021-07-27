# tip

## max of columns
```sql
SELECT GREATEST(v1, v2 ...) FROM t
```

## use variables to select "consecutive" rows with same values
```sql
SET @id = NULL, @val = NULL, @same = 0, @cnt = 0;

SELECT @prev_id := @id AS prev_id,
@prev_val := @val AS prev_val,
@id := id AS id,
@val := val AS val,
@same := if(@prev_id = @id && @prev_val = @val, 1, 0) AS same
@cnt := if(@same = 0, 0, @cnt + 1) AS cnt
FROM test 
ORDER by id, reg_id;
```

## lag function to update with previous row value
```sql
-- update prev_v using lag(expr, offset, default)
-- tbl(id, dt, v, prev_v) primary key (id,dt)
with a as(
    select id, dt, v, 
    LAG(v, 1, 0) OVER (
        PARTITION BY id
        ORDER BY id, dt asc
    ) as pv
    from tbl
)
update tbl t
inner join a on a.pk = t.pk  
set t.pv = a.pv;
```
