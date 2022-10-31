# Variable

## declare
https://stackoverflow.com/questions/8039907/simple-oracle-variable-sql-assignment

The `DECLARE` keyword is used to define variables scoped in a PL/SQL block (whose body is delimited by BEGIN and END;).
```
DECLARE 
    startDate DATE := to_date('03/11/2011', 'dd/mm/yyyy');
    reccount INTEGER;
BEGIN
    SELECT count(*) INTO reccount 
        FROM my_table tab 
        WHERE tab.somedate < startDate;
    dbms_output.put_line(reccount);
END;
```

## define
`DEFINE` statement for simple `string` substitution variables.
```
DEFINE start_date = "to_date('03/11/2011', 'dd/mm/yyyy')"
SELECT COUNT(*) from my_table tab where tab.some_date < &start_date;
```

## define and use variable
```sql
define col = 'date';
define day = to_date('2022-07-01', 'YYYY-MM-DD');
SELECT '&&col' from my_table where date > &&day;
```

```sql
define val = 12;
SELECT * from my_table where value > &&val;
```
