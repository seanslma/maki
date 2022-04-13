# Ubuntu

## Change mirror site in sources.list
```
sudo vi /etc/apt/sources.list
#replace http://archive.ubuntu.com/ubuntu with another mirror

#http://au.archive.ubuntu.com/ubuntu

:%s/search_string/replacement_string/g
:%s#search_string#replacement_string#g
```

## Enable hibernate
```
systemctl hibernate
Failed to hibernate system via logind: Sleep verb not supported
```
Perhaps the error should be: Failed to hibernate system via logind: Please use BIOS to `disable secure boot`.

Disable swapfile and delete it
```
 sudo swapoff /swapfile  
 sudo rm /swapfile
```
https://ubuntuhandbook.org/index.php/2021/08/enable-hibernate-ubuntu-21-10/

## Auto hibernate after timeout
https://unix.stackexchange.com/questions/645535/shutdown-system-by-timeout-during-suspend

https://ubuntuhandbook.org/index.php/2021/06/automatic-shutdown-hibernate-on-idle-ubuntu/

Does not work
```
dbus-send --system --print-reply --dest=org.freedesktop.login1 /org/freedesktop/login1 org.freedesktop.login1.Manager.Hibernate boolean:true
```

## Dual boot wrong time
https://itsfoss.com/wrong-time-dual-boot/

A hardware clock which is also called RTC (real time clock) or CMOS/BIOS clock. By default, Linux assumes that the time stored in the hardware clock is in UTC, while Windows thinks that the time stored on the hardware clock is local time.

### Solution 1 
Setup for Linux system to use the local time for the hardware clock (RTC)
```
timedatectl set-local-rtc 1 #0 for UTC time standard,  1 for localtime time standard
```

### Solution 2
Setup for Windows system to use the UTC for the hardware clock (RTC). 

For 64-bit Windows, open regedit then browse to HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation. 
Create a new QWORD entry called RealTimeIsUniversal, then set its value to 1. Reboot the system. The clock should now be in UTC time.
```
Reg add HKLM\SYSTEM\CurrentControlSet\Control\TimeZoneInformation /v RealTimeIsUniversal /t REG_QWORD /d 1
```
