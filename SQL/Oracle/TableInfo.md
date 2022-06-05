# Table info

## describe table
```sql
describe schema_name.table_name;
```

## Tables accessible to the current user
```sql
select 
    col.column_id, 
    col.owner as schema_name,
    col.table_name, 
    col.column_name, 
    col.data_type, 
    col.data_length, 
    col.data_precision, 
    col.data_scale, 
    col.nullable
from sys.all_tab_columns col
inner join sys.all_tables t 
    on col.owner = t.owner and col.table_name = t.table_name
-- excluding some Oracle maintained schemas
where 
    col.owner not in ('ANONYMOUS','CTXSYS','DBSNMP','EXFSYS', 'LBACSYS', 
   'MDSYS', 'MGMT_VIEW','OLAPSYS','OWBSYS','ORDPLUGINS', 'ORDSYS','OUTLN', 
   'SI_INFORMTN_SCHEMA','SYS','SYSMAN','SYSTEM','TSMSYS','WK_TEST','WKSYS', 
   'WKPROXY','WMSYS','XDB','APEX_040000', 'APEX_PUBLIC_USER','DIP', 
   'FLOWS_30000','FLOWS_FILES','MDDATA', 'ORACLE_OCM', 'XS$NULL',
   'SPATIAL_CSW_ADMIN_USR', 'SPATIAL_WFS_ADMIN_USR', 'PUBLIC')  
order by col.owner, col.table_name, col.column_id;
```
