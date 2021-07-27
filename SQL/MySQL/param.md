# param

## tmpdir
make sure it is on a disk with enough space. Otherwise it will affect the performance of many queries.

## max_execution_time
default value is 0, means no timeout. This applies to the select queries.

## range_optimizer_max_mem_size
default value 8 MB. a value of 0 means no limits. to control the memory available to the range optimizer.

## code example
```sql
rows_affected = 0
do {
   rows_affected = do_query(
      "DELETE FROM messages WHERE created < DATE_SUB(NOW(),INTERVAL 3 MONTH)
      LIMIT 10000")
} while rows_affected > 0
```