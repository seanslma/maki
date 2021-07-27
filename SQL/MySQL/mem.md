# memory

## mysqld high RAM
This will show the memory usage
  select * from sys.memory_global_by_current_bytes;
  
key_catch used 2GB memory after table repair because key_buffer_size is 2GB. Reduce key_buffer_size to a lower value
  SET GLOBAL key_buffer_size = 1024 * 1024 * 1024;