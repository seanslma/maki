# perf

## show slow queries
```sql
select time_to_sec(query_time) as qry_time_sec, rows_sent, rows_examined, db, CONVERT(sql_text USING utf8) as qry_text
from mysql.slow_log 
order by query_time desc;
```

when use OPTIMIZE TABLE?

https://downloads.mysql.com/presentations/MySQL_Perfornance__Tuning_Overview_jp.pdf

http://porthos.ist.utl.pt/docs/mySQL/optimization.html#optimizing-myisam
https://www.liquidweb.com/kb/mysql-performance-myisam/

## MyISAM optimization

### key_buffer_size
usually **25%** of the total RAM
```sql
show status like 'key%';

show global variables like 'key%';

--calc required key_buffer_size
select count(INDEX_LENGTH) as Indexes,
floor(sum(INDEX_LENGTH)/1024/1024) as Total_Index_Length_MB,
floor(sum(INDEX_LENGTH)*(1+0.05)/1024/1024) as key_buffer_size_MB
FROM information_schema.TABLES WHERE ENGINE = 'MyISAM';

SET GLOBAL key_buffer_size = 1024 * 1024 * 1024 * 2;

--Calculate Key Cache Usage Rate
select VARIABLE_VALUE into @Key_blocks_unused 
FROM information_schema.global_status
WHERE VARIABLE_NAME = "Key_blocks_unused";
select @Key_blocks_unused as Key_blocks_unused,
    @@key_cache_block_size as key_cache_block_size,
    @@key_buffer_size as key_buffer_size\G
select truncate((1-((@Key_blocks_unused*@@key_cache_block_size)/@@key_buffer_size))*100, 2)
   as "(1-((Key_blocks_unused × key_cache_block_size) / key_buffer_size)) × 100;
```

## optimize MyISAM settings
DISABLE KEYS / ENABLE KEYS only works for MyISAM

**read_rnd_buffer_size** will affect query performance with sorted operations. As it is created per connection it is best to set it temporally

**key_buffer_size** [affects exporting performance] is for MyISAM. Default size 8 MB. You can increase the value to get better index handling for all reads and multiple writes; on a system whose primary function is to run MySQL using the MyISAM storage engine, **25%** of the machine's total memory is an acceptable value for this variable. Tune this to at least **30%** of your RAM or the re-indexing process will probably be too slow. However, if you make the value too large (for example, more than 50% of the machine's total memory), your system might start to page and become extremely slow. 

check the usage of the buff: SHOW STATUS LIKE 'Key%';

**Key Cache Usage Rate**: 1-(key_blocks_unused * key_cache_block_size / key_buffer_size)\\
This measures the percentage of the Key Cache that is filled, a helpful detail when determining if the key_buffer_size is large enough or if memory is being wasted.

**Key Cache Miss Rate**: key_reads / key_read_requests\\
This shows how often items that could be in the Key Cache are being read from a physical disk.

**Key Cache Flush Rate**: key_writes / key_write_requests\\
This value measures how frequently the Key Cache is written to disk. Frequent flushing can slow down MyISAM operations as writing data to a physical disk is much slower than writing to the Key Cache in memory. 

also consider to change '**bulk_insert_buffer_size**' [affects importing performance] to at least 32M:
  SET GLOBAL bulk_insert_buffer_size = 1024 * 1024 * 256;
  SET bulk_insert_buffer_size = 1024 * 1024 * 256;

  show global variables like 'bulk_insert%';
  show variables like 'bulk_insert%';
  
## MyISAM 2
For MyIsam i have some recommendations as

  key_buffer_size
Size of the Key Buffer, used to cache index blocks for MyISAM tables. Do not set it larger than 30% of your available memory, as some memory is also required by the OS to cache rows. Even if you're not using MyISAM tables, you should still set it to 8-64M as it will also be used for internal temporary disk tables.So You should set it from 2GB to 3GB.

  read_buffer_size
Size of the buffer used for doing full table scans of MyISAM tables. Allocated per thread, if a full scan is needed..You should set it to 8MB to 16MB .

  read_rnd_buffer_size
When reading rows in sorted order after a sort, the rows are read through this buffer to avoid disk seeks. You can improve ORDER BY performance a lot, if set this to a high value. Allocated per thread, when needed.

  bulk_insert_buffer_size
MyISAM uses special tree-like cache to make bulk inserts (that is, INSERT ... SELECT, INSERT ... VALUES (...), (...), ..., and LOAD DATA INFILE) faster. This variable limits the size of the cache tree in bytes per thread. Setting it to 0 will disable this optimisation. Do not set it larger than "key_buffer_size" for optimal performance. This buffer is allocated when a bulk insert is detected.Set it to 512 MB to 1GB.

  myisam_sort_buffer_size
This buffer is allocated when MySQL needs to rebuild the index in REPAIR, OPTIMIZE, ALTER table statements as well as in LOAD DATA INFILE into an empty table. It is allocated per thread so be careful with large settings.So You should set it to 2M

  myisam_max_sort_file_size
The maximum size of the temporary file MySQL is allowed to use while recreating the index (during REPAIR, ALTER TABLE or LOAD DATA INFILE. If the file-size would be bigger than this, the index will be created through the key cache (which is slower).Set it to as you need.

  myisam_repair_threads 
If a table has more than one index, MyISAM can use more than one thread to repair them by sorting in parallel. This makes sense if you have multiple CPUs and plenty of memory.Set it to 1.

  myisam_recover
Automatically check and repair not properly closed MyISAM tables.
## optimize InnoDB settings
For Innodb we need to diable unique_checks and foreign_key_checks using
```
set unique_checks=0; set foreign_key_checks=0; disable auto_commit.
inserts......
set unique_checks=1; set foreign_key_checks=1; enable auto_commit.
```
Which improves bulk inserts performance.

Your process is slow due to heavy disk I/O activity for SQL operations. You need to optimize innodb for intensive operations. Modify your mysql configuration file to have these lines:
  innodb_buffer_pool_size = 4G
  innodb_log_buffer_size = 256M
  innodb_log_file_size = 1G
  innodb_write_io_threads = 16

**innodb_buffer_pool_size**: the memory area where InnoDB caches table and index data. When table data is cached in the InnoDB buffer pool, it can be accessed repeatedly by queries without requiring any disk I/O. Data changes are cached rather than immediately written to disk.

A larger buffer pool requires less disk I/O to access the same table data more than once. On a dedicated database server, you might set the buffer pool size to 80% of the machine's physical memory else use 50 to 75 percent of system memory. The default buffer pool size is 128MB.

To determine the optimal size, do:
```sql
SELECT (PagesData*PageSize)/POWER(1024,3) DataGB 
FROM
(SELECT variable_value PagesData
 FROM performance_schema.global_status
 WHERE variable_name='Innodb_buffer_pool_pages_data') A,
(SELECT variable_value PageSize
 FROM performance_schema.global_status
 WHERE variable_name='Innodb_page_size') B;
```

                        Duration / Fetch
  353 row(s) returned 34.422 sec / 125.797 sec (8MB innodb buffer_pool_size)
  353 row(s) returned  0.500 sec /   1.297 sec (1GB innodb buffer_pool_size)

**innodb_log_buffer_size**: The size in bytes of the buffer that InnoDB uses to write to the log files on disk.

A large log buffer enables large transactions to run without the need to write the log to disk before the transactions commit. Thus, if you have transactions that update, insert, or delete many rows, making the log buffer larger saves disk I/O.

**innodb_log_file_size**: The size in bytes of each log file in a log group. A large size ensures that the server can smooth out peaks and troughs in workload activity, which often means that there is enough redo log space to handle more than an hour of write activity. The larger the value, the less checkpoint flush activity is required in the buffer pool, saving disk I/O.

**Innodb_write_io_threads**: The number of I/O threads for write operations in InnoDB. The default value is 4. InnoDB uses background threads to service various types of I/O requests. You can configure the number of background threads that service read and write I/O on data pages using the innodb_read_io_threads and innodb_write_io_threads configuration parameters.

These parameters signify the number of background threads used for read and write requests, respectively. Each background thread can handle up to 256 pending I/O requests.

If you are importing to innodb the single most effective thing you can do is to put **innodb_flush_log_at_trx_commit** = **2** in your my.cnf, temporarily while the import is running. you can put it back to **1** if you need ACID. Your hint with innodb_flush_log_at_trx_commit = 2 saved my day. Importing a 600 MB dump (as a single big transaction) would have needed 6 hours, but with this temporary setting, it was done in 30 minutes! someone suggested a performance gain of 100x faster

https://dev.mysql.com/doc/refman/5.7/en/optimizing-innodb-bulk-data-loading.html

https://www.oreilly.com/library/view/high-performance-mysql/9780596101718/ch04.html

replace In subquery with inner join will be much faster

creating temporal table is faster than directly using inner join statement

## InnoDB optimization example
https://dba.stackexchange.com/questions/227742/extreme-performance-loss-due-to-moving-from-mysql-5-7-23-to-mysql-8-0-status-c
Big update
Spent half a day reading into internas, taking your suggestions in consideration and what I was told on IRC.
I did the opposite of the professional: I made 10 changes at once, I can't afford so many restarts in a gradual change process:
1) Giving the system lots of parallel write opportunity without choking it
  innodb_read_io_threads = 16  
  innodb_write_io_threads = 16  
  innodb_thread_concurrency=64  # cpus*2 
 
2) Speeding up the background sync:
  innodb_lru_scan_depth=100
  
3) Disabling highest reliability settings that have a hard performance impact
  performance_schema=OFF
  skip-log-bin 
  sync_binlog=0 
  innodb_flush_log_at_trx_commit=0  # not crash safe, 0 is crash safe 
 
4) More multithreading in backend memory
  innodb_buffer_pool_instances=12  
  
5) Increasing logfiles significantly, increasing logfile buffer moderatly
  innodb_log_file_size = 3G # 
  innodb_log_buffer_size = 64M
  
What happened: About 10 times increase in read performance,1.5x times write performance, I am not where I want to be but it's 15 times faster than before!
IOPS usage doubled from ~5-6k to 9k-12k, so I am at 60% IO usage
CPU usage increased from 7% to 50%

**Update**\\
I think the problem can be considered half solved, I've made another update after the previous successful one and the performance is acceptable now.

The last changes involved write/read threads. I've put them to 32 each.
write buffer increased to 128M (for my heavy workload higher might be better)
logfiles increased to 8GB
buffer_pool_instances increased to 64 (max) for better memory fragmentation
page_cleaners increased to 64 (max) to have one for each buffer instance.

write performance increased by another ~20%, read performance increased by another ~30%.

It's been a 24 hour ride to get mysql perform acceptable, definitely not a simple upgrade.
## Limitations of the MySQL Query Optimizer

### Correlated subqueries
bad:
```sql
SELECT * FROM sakila.film
WHERE film_id IN
(
   SELECT film_id FROM sakila.film_actor WHERE actor_id = 1
);
```

optimized to:
```sql
SELECT * FROM sakila.film
WHERE EXISTS 
(
   SELECT * FROM sakila.film_actor WHERE actor_id = 1
   AND film_actor.film_id = film.film_id
);
```

good:
```sql
SELECT film.* FROM sakila.film
INNER JOIN sakila.film_actor USING(film_id)
WHERE actor_id = 1;
```

Another good optimization is to manually generate the IN() list by executing the subquery as a separate query with GROUP_CONCAT(). Sometimes this can be faster than a JOIN.

### slow limit query

https://stackoverflow.com/questions/17747871/why-is-mysql-slow-when-using-limit-in-my-query

Same problem happened in my project, I did some test, and found out that LIMIT is slow because of row lookups

See: MySQL ORDER BY / LIMIT performance: late row lookups

So, the solution is:
  * when using LIMIT, select not all columns, but only the PK columns
  * Select all columns you need, and then join with the result set of PK cols

SQL should likes:
```sql
SELECT  * FROM
    orders t1   <=== this is what you want
JOIN (  SELECT ID FROM orders     <== fetch the PK column only, this should be fast        
        WHERE [your query condition]        <== filter record by condition
        ORDER BY [your order by condition]  <== control the record order
        LIMIT 2000, 50                      <== filter record by paging condition
) as t2
ON t1.ID = t2.ID
ORDER BY [your order by condition]          <== control the record order
```
in my DB, the old SQL which select all columns using "LIMIT 21560, 20", costs about 4.484s. the new sql costs only 0.063s. The new one is about 71 times faster
