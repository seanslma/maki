# sys command

# RAM
``` bash
free
free -m[-g]
cat /proc/meminfo
top #check memory and CPU usage per process
htop #similar to top, more control with color
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
