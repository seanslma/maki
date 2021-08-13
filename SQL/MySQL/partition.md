# Partition

https://dev.mysql.com/doc/refman/8.0/en/partitioning.html

https://dev.mysql.com/doc/refman/8.0/en/partitioning-management-range-list.html

MySQL 8.0 does not currently support partitioning of tables using any storage engine other than **InnoDB** or **NDB**, such as MyISAM.

MySQL supports horizontal partitioning, which means that all rows matching the partitioning function will be assigned to different physical partitions.

## check if MySQL supports partition
```sql
SHOW PLUGINS;

#or like this
SELECT PLUGIN_NAME as Name, PLUGIN_VERSION as Version, PLUGIN_STATUS as Status
FROM INFORMATION_SCHEMA.PLUGINS
WHERE PLUGIN_TYPE='STORAGE ENGINE';
```

## create partition table
There are four partition types available: **RANGE**, **LIST**, **HASH** and **KEY**.

All columns used in the partition expression must be present in every unique key in the table, including the primary key. If the table does not have any unique keys (including primary keys), any column can be used in the partitioning expression that is compatible with the partitioning type.

```sql
#range: do not add the MAXVALUE partition when you want to add more partitions later
CREATE TABLE tbl (
    usr VARCHAR(20) NOT NULL,
    created DATETIME NOT NULL,
    PRIMARY KEY(usr, created)
)
PARTITION BY RANGE( YEAR(created) )(
    PARTITION l2014 VALUES LESS THAN (2014),
    PARTITION l2015 VALUES LESS THAN (2015),
    PARTITION lmaxy VALUES LESS THAN MAXVALUE
);

#list
PARTITION BY LIST(year(dt)) (
    PARTITION p0 VALUES IN (2010,2011),
    PARTITION p1 VALUES IN (2012,2013)
);
```

## redefine partition
```sql
ALTER TABLE tbl
PARTITION BY HASH(id) PARTITIONS 4;
```

## add partition
```sql
ALTER TABLE tbl ADD PARTITION (PARTITION p3 VALUES LESS THAN (2002));
```

## drop partition
**Note**: drop the partition will drop the data in the partition as well
```sql
ALTER TABLE tbl DROP PARTITION p0,p2;

#will remove all partitions
ALTER TABLE tbl remove PARTITIONING;
```

## reorgnize partitions
change the partitioning of a table without losing data
```sql
#split
ALTER TABLE tbl
REORGANIZE PARTITION l2014 INTO (
        PARTITION n0 VALUES LESS THAN (2013),
        PARTITION n1 VALUES LESS THAN (2014)
);

#merge
ALTER TABLE tbl 
REORGANIZE PARTITION n0,n1 INTO (
    PARTITION l2012 VALUES LESS THAN (2012),
    PARTITION l2014 VALUES LESS THAN (2014)
);
```
