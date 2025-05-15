# Ubuntu

## install libssl1.1 latest in ubuntu 22.04 
- https://github.com/microsoft/azure-pipelines-agent/blob/master/src/Misc/layoutbin/installdependencies.sh
- https://stackoverflow.com/questions/72133316/libssl-so-1-1-cannot-open-shared-object-file-no-such-file-or-directory

use wget
```sh
package=$(wget -qO- http://security.ubuntu.com/ubuntu/pool/main/o/openssl/ | grep -oP '(libssl1.1_1.1.1f.*?_amd64.deb)' | head -1)
wget "http://security.ubuntu.com/ubuntu/pool/main/o/openssl/${package}" && dpkg -i $package 
```

use curl
```sh
package=$(curl -sL http://security.ubuntu.com/ubuntu/pool/main/o/openssl/ | grep -oP '(libssl1.1_1.1.1f.*?_amd64.deb)' | head -1)
curl -LO "http://security.ubuntu.com/ubuntu/pool/main/o/openssl/${package}" && dpkg -i $package
```

## Change mirror site in sources.list
```sh
sudo vi /etc/apt/sources.list
#replace http://archive.ubuntu.com/ubuntu with another mirror

#http://au.archive.ubuntu.com/ubuntu

:%s/search_string/replacement_string/g
:%s#search_string#replacement_string#g
```

## gnome top bar to left
https://askubuntu.com/questions/1162884/can-i-move-the-gnome-top-bar-and-status-icons-to-the-side


## Enable hibernate
```sh
systemctl hibernate
Failed to hibernate system via logind: Sleep verb not supported
```
Perhaps the error should be: Failed to hibernate system via logind: Please use BIOS to `disable secure boot`.

Disable swapfile and delete it
```sh
sudo swapoff /swapfile
sudo rm /swapfile
```
https://ubuntuhandbook.org/index.php/2021/08/enable-hibernate-ubuntu-21-10/

## Auto hibernate after timeout
https://unix.stackexchange.com/questions/645535/shutdown-system-by-timeout-during-suspend

https://ubuntuhandbook.org/index.php/2021/06/automatic-shutdown-hibernate-on-idle-ubuntu/

Shortcut key does not work but works in terminal with pwd
```sh
dbus-send --system --print-reply --dest=org.freedesktop.login1 /org/freedesktop/login1 org.freedesktop.login1.Manager.Hibernate boolean:true
dbus-send --system --print-reply --type=method_call --dest=org.freedesktop.login1 /org/freedesktop/login1 org.freedesktop.login1.Manager.Hibernate boolean:true
```

Set the timeout value:
- https://wiki.archlinux.org/title/Power_management#Suspend_and_hibernate
- https://man.archlinux.org/man/sleep.conf.d.5
```sh
/etc/systemd/sleep.conf
```

## Dual boot wrong time
https://itsfoss.com/wrong-time-dual-boot/

A hardware clock which is also called RTC (real time clock) or CMOS/BIOS clock. By default, Linux assumes that the time stored in the hardware clock is in UTC, while Windows thinks that the time stored on the hardware clock is local time.

### Solution 1
Setup for Linux system to use the local time for the hardware clock (RTC)
```sh
timedatectl set-local-rtc 1 #0 for UTC time standard,  1 for localtime time standard
```

### Solution 2
Setup for Windows system to use the UTC for the hardware clock (RTC).

For 64-bit Windows, open regedit then browse to HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation.
Create a new QWORD entry called RealTimeIsUniversal, then set its value to 1.
Reboot the system. The clock should now be in UTC time.
```sh
Reg add HKLM\SYSTEM\CurrentControlSet\Control\TimeZoneInformation /v RealTimeIsUniversal /t REG_QWORD /d 1
```

## Wifi setting is missing
- power off
- disconnect power cable
- hold the power button for 30 seconds
- wifi should be back - but just a temporal solution (usually reboot works)

Other solution for ubuntu 24.04: https://gist.github.com/UbuntuEvangelist/e36f6a1a9ef7cb0a0b24e592eb925b68
