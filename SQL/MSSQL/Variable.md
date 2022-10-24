# Variable

## set and use variable
```
declare @start_date as date = '2012-01-01';
 
select *
from my_table
where recorddate >= @date_start;
```

```
define start_date = TO_DATE('2012-01-01','yyyy-mm-dd');
 
select *
from my_table
where recorddate >= &date_start;
```

## pipeline variable: ignore filter if null
```
(@{pipeline().parameters.p} is null OR p = @{pipeline().parameters.p})
```
