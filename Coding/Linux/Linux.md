# Linux
Ctrl + Alt + T: open terminal

WinSCP to access file on a linux machine, but connection is not stable

show all users
```sh
cut -d: -f1 /etc/passwd
```

## create a folder
```sh
mkdir /tmp/new_folder
```

## delete things in folder
```sh
rm -rf /tmp/*
```
## run sh in linux from win
http://the.earth.li/~sgtatham/putty/0.58/htmldoc/Chapter7.html
https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
```sh
plink -ssh hostname
/ls list by disabling color.
REM otherwise win console will not be able to
REM interpret the color and show strange characters
./dts.sh 2>&1 | tee backup.log
```

login with root if sudo is required
```sh
plink.exe -ssh -pw xvcvvx  -t root@xxx-xxx.xx.xx
```

## terminal to console and file
```sh
make 2>&1 | tee file.txt
```

## list scheduled cron jobs
```sh
#root
less /etc/crontab
crontab -l

#current user
crontab -l
#specific user
crontab -l -u juser

#root user
/etc/crontab
#all other users
/var/spool/cron/crontabs

#enabled system timers
systemctl list-timers
```

## list dirs in current folder
```sh
ls -d */
```

## where is /tmp mounted
```sh
$ df -h /tmp
Filesystem     1K-blocks     Used Available Use% Mounted on
/dev/root      480589544 42607368 413546516  10% /

$ cat /proc/cmdline | grep root
BOOT_IMAGE=/boot/vmlinuz-3.19.0-32-generic root=UUID=0cde5cf9-b15d-4369-b3b1-4405204fd9ff ro

$ sudo blkid
/dev/sda1: UUID="0cde5cf9-b15d-4369-b3b1-4405204fd9ff" TYPE="ext4"
/dev/sda5: UUID="37bc6a9c-a27f-43dc-a485-5fb1830e1e42" TYPE="swap"
/dev/sdb1: UUID="177c3cec-5612-44a7-9716-4dcba27c69f9" TYPE="ext4"
```

## check disks
```sh
#set password
sudo passwd

#check disk info
df -h
df -h |grep ^/dev #does not work for multiline cases
sudo fdisk -l
sudo sfdisk -l -uM
sudo parted -l
```

## check mysql
```sh
service --status-all
service mysqld status

top grep mysql
systemctrl status mysqld.service
mysqladmin -u root -p status
mysqladmin -u root -p version

```

## chkconfig for services
https://www.thegeekdiary.com/how-to-enable-or-disable-service-on-boot-with-chkconfig/

```sh
chkconfig --list
chkconfig --list mysqld
chkconfig --level 345 mysqld on
chkconfig --add [servicename]
chkconfig [servicename] reset
chkconfig [servicename] off
```
## bash
```sh
#!/bin/bash

#set executable permission
chmod +x my.sh

#show permission
ls -l my.sh
```

## backup databases
```sh
#!/bin/bash

fdb=dump_dbs.txt
dir="/media/data/test"

create_list=$(( $#==0 ? 1 : 0 ))

timestamp() {
    date +"%Y-%m-%d %H:%M:%S"
}

i=0
echo $(timestamp) dump dbs
while read db; do
    ((++i))
    ftb=$dir/$db"_tbs.txt"
    if [ $create_list -eq 1 ]; then
        qry='SELECT table_name FROM information_schema.tables WHERE table_schema='\'${db}\'' order by table_name;'
        mysql --defaults-extra-file=$dir/svr_fr.cnf --skip-column-names -e "${qry}" >$ftb
    fi
    echo $(timestamp) "  " db: $db
    j=0
    while read tb; do
        ((++j))
        echo $(timestamp) "    "$j table: $tb
        mysqldump --defaults-extra-file=$dir/svr_fr.cnf $db $tb | mysql --defaults-extra-file=$dir/svr_to.cnf $db
    done <$ftb
done <$fdb

echo $(timestamp) all done!
```

## backup hdd
DISCALIMER: this will erase the destination/new hdd.
  - Get a Linux live disk. Linux Mint works great and is not a huge download.
  - Boot off the linux live disk.
  - Make sure you are connected to the internet. Open the web browser to make sure.
  - Open a command line. On most linux systems this can be done by pressing Ctrl+Alt+T. If that doesn't work, search through the menu for a program called Terminal or something like that.
  - Type "sudo bash". If prompted for a password, just press enter(assuming you are using linux mint. If you are using another distro, you will have to find out what the pasword for that is.)
  - Type "apt-get update"
  - Type "apt-get -y install pv"
  - Type "apt-get -y install gparted"
  - Type "gparted"
  - This will open a disk utility program. Using the drop-down on the top-right of the program, figure out which hard drive is your old hdd and which is your new hdd. You can figure it out by looking which hdd has a windows partition. The new hdd should be blank. Write down which hdd is which. DO NOT GET THEM MIXED UP! Or you will erase your entire hdd. It should be something like /dev/sda and /dev/sdb but make sure.
  - Type "dd if=<oldhdd> | pv | dd of=<newhdd>" replacing <oldhdd> with the device id of your old hdd and <newhdd> with your new hdd. For example, if your old hdd was /dev/sda and your new hdd was /dev/sdb, then you would type "dd if=/dev/sda | pv | dd of=/dev/sdb".
  - Your drive is now being cloned. It will tell you the speed of the clone and how much it has transferred so far. It will take a LOONG time. Your new HDD will be EXACTLY the same as your old hdd. All your files will be there, and you will be able to boot off it just like always.
This is the most reliable method I know, although it is slow and cumbersome. Alternatively, you could try WinDD which is a windows tool to do the same thing, but I have never used it before and cannot guarantee that it will work. I personally would just use the linux method.

## check hardware
```sh
lspci
cat /proc/cpuinfo - Displays CPU info
cat /proc/meminfo - Displays memory info
hdparm -I /dev/sda - Disk
sosreport - most info in CentOS
```
