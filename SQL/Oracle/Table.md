# Table

## find table with specific column
```sql
select owner as schema, table_name, column_name 
from all_tab_columns 
where lower(column_name) like '%juri%';
```

## find views with specific string
```sql
SELECT view_name, text
FROM all_views
where lower(view_name) like '%data%';
```
