# pgcli

## start pgcli
```sh
pgcli \d db_name
```

## connect to db
```sh
\c db_name
```

## list all schemas
```sh
\dn
```

## list all tables
```sh
\dt schema.*
```

## show details of table cols
```sh
\d schema.table_name
```

## expanded mode
Show all columns from a query result without truncation. 
In this mode, each column value will be displayed on a new line, making it easier to view long values.
```sh
\x
\x off
```
