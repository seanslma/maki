# Partition

https://dev.mysql.com/doc/refman/8.0/en/partitioning.html

MySQL 8.0 does not currently support partitioning of tables using any storage engine other than **InnoDB** or **NDB**, such as MyISAM.

https://www.vertabelo.com/blog/everything-you-need-to-know-about-mysql-partitions/

MySQL supports horizontal partitioning, which means that all rows matching the partitioning function will be assigned to different physical partitions.

## check if MySQL supports partion
```sql
SHOW PLUGINS;

#or like this
SELECT PLUGIN_NAME as Name, PLUGIN_VERSION as Version, PLUGIN_STATUS as Status
FROM INFORMATION_SCHEMA.PLUGINS
WHERE PLUGIN_TYPE='STORAGE ENGINE';
```

## create partion table
There are four partition types available: **RANGE**, **LIST**, **HASH** and **KEY**.

All columns used in the partition expression must be present in every unique key in the table, including the primary key. If the table does not have any unique keys (including primary keys), any column can be used in the partitioning expression that is compatible with the partitioning type.

```sql
CREATE TABLE tbl (
    usr VARCHAR(20) NOT NULL,
    created DATETIME NOT NULL,
    PRIMARY KEY(usr, created)
)
PARTITION BY RANGE( YEAR(created) )(
    PARTITION le2014 VALUES LESS THAN (2014),
    PARTITION le2015 VALUES LESS THAN (2015),
    PARTITION lemaxy VALUES LESS THAN MAXVALUE
);
```
