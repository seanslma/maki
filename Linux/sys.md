# sys command
## update time
```
sudo ntpd ntp.ubuntu.com
sudo ntpdate ntp.ubuntu.com
```

## RAM
``` bash
free
free -m[-g]
cat /proc/meminfo
top #check memory and CPU usage per process, kill it by Ctrl + c
top -b -n 1 > top.txt 
htop #similar to top, more control with color, kill it by Ctrl + c
```

## disk space
``` bash
df -h
df -h /dev/sda
```

## w
show who is logged on and what they are doing
``` bash
w [options] user [...]
-h no header
-x
```

## services started up in runlevel 3
``` bash
ls /etc/rc3.d/S*
```
  
## folder permission
``` bash
chmod 700 yourDirectory/
ls -l #show
```
