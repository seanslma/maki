# backup code

## mysql extra config
```cnf frto.cnf
[client]
host=xxx.xxx.xxx
port=3306
user=usr
password=pwd

[mysqld]
net_read_timeout = 7200
net_write_timeout = 7200

[mysql]
net_buffer_length=32704
max_allowed_packet = 512M
```

## backup databases
```sh dts.sh
#!/bin/bash

#./dts.sh r 2>&1 | tee backup_db_dtr.log

[ $# -eq 0 ] && ty="s" || ty="r"
create_list=$(( $#==0 ? 1 : 0 ))

fdb="db"$ty"_dump.txt"
dir="/media/data/test"
typ="BASE TABLE"
 
timestamp() {
    date +"%Y-%m-%d %H:%M:%S"
}

i=0 
echo $(timestamp) dump db$ty
while read db; do
    ((++i))  
    ftb=$dir/"tb"$ty"_"$db".txt"
    if [ $create_list -eq 1 ]; then
	qry='SELECT table_name FROM information_schema.tables WHERE table_schema='\'${db}\'' and table_type='\'${typ}\'' order by data_length asc;'
        mysql --defaults-extra-file=$dir/fr.cnf --skip-column-names -e "${qry}" >$ftb
    fi    
    echo $(timestamp) "  " db: $db
    j=0 
    while read tb; do
        ((++j))
        echo $(timestamp) "    "$j table: $tb 
        mysqldump --defaults-extra-file=$dir/fr.cnf $db $tb | mysql --defaults-extra-file=$dir/to.cnf $db
    done <$ftb 
done <$fdb

echo $(timestamp) all done!
```

## backup a table
```sh dtr.sh
#!/bin/bash

#./dtr.sh db 2>&1 | tee backup_xxx_db_dtr.log

dir="/media/data/test"
db=$1
 
timestamp() {
    date +"%Y-%m-%d %H:%M:%S"
}

echo $(timestamp) dump dbr
ftb=$dir/$db"_tbr.txt"    
echo $(timestamp) "  " db: $db
j=0 
while read tb; do
    ((++j))
    echo $(timestamp) "    "$j table: $tb 
    mysqldump --defaults-extra-file=$dir/fr.cnf $db $tb | mysql --defaults-extra-file=$dir/to.cnf $db
done <$ftb 

echo $(timestamp) all done!
```