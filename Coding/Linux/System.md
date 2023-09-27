# sys command

## update time
```sh
sudo ntpd ntp.ubuntu.com
sudo ntpdate ntp.ubuntu.com
```

## RAM
```sh
free
free -m[-g]
cat /proc/meminfo
top #check memory and CPU usage per process, kill it by Ctrl + c
top -b -n 1 > top.txt
htop #similar to top, more control with color, kill it by Ctrl + c
```

## disk space
```sh
df -h
df -h /dev/sda
```

## w
show who is logged on and what they are doing
```sh
w [options] user [...]
-h no header
-x
```

## services started up in runlevel 3
```sh
ls /etc/rc3.d/S*
```

## folder permission
```sh
chmod 700 yourDirectory/
ls -a  #show all
ls -1  #one line per file
ls -t  #sort latest changes to top
ls -rt #sort latest to bottom
```
