# key repair

Two modes for key repair: repair by Sorting (quick) or by Keycache (very slow)

"Repair by sorting" doesn't work for **UNIQUE** or **PRIMARY KEY**s

"Repair by sorting" uses the filesort routine, which in turn creates several temporary files (usually) in your tmpdir.

If your tmpdir does not have enough space for them, it will revert to "Repair by keycache". This is extremely bad as it's much slower AND creates less optimal indexes.

It chooses which method to use based on:
  * myisam_sort_buffer_size, 
  * myisam_max_sort_file_size, and
  * myisam_max_extra_sort_file_size [deprecated in v5]
These are SESSION variables, so they can be set on the connection right before the LOAD DATA INFILE.

The table can be repaired by sorting provided it meets the following requirements:

  * table at least has one key (index)
  * total size needed for individual key is less than **myisam_max_sort_file_size**
  * tmpdir has enough spare space

If it meets the above requirements, then it uses either regular sorting if myisam_repair_threads  = 1 (default) by building each key at a time or in parallel if myisam_repair_threads > 1 by using ‘n’ threads in parallel (n = total keys in the table). If you have a table with more than one key and table needs a frequent key rebuild, then setting myisam_repair_threads = 2 can speedup the repair/alter process.

If the table fails to satisfy the above two conditions, then it falls to expensive **keycache repair mode**.

**myisam_sort_buffer_size** can be up to 90% of the system RAM.

  SET SESSION myisam_sort_buffer_size = 500*1024*1024;
  
Note that **sort_buffer_size** is per secession so should be too large. The default is 2 MB or 256 kB. Someone said that 256 is better. 

# repair keys
```batch
@echo off

setlocal EnableDelayedExpansion
 
set db=mydb
set file=tbl_repair.txt

set i=0
echo %date% %time% repair tbl
echo %date% %time% db: %db%
for /f %%a in (%file%) do (
    set /a i=!i!+1
    echo !date! !time!   !i! table: %%a 
    "C:\MySQL\MySQLServer8.0\bin\mysqlcheck" --defaults-extra-file=sql_svr.cnf -r %db% %%a
)
 
echo %date% %time% all done!
```
