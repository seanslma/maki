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

## disable shutdown confirmation
```sh
gsettings set org.gnome.SessionManager logout-prompt false
```

## change font size
```sh
gsettings set org.gnome.desktop.interface text-scaling-factor 1.05
```

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

## 24.04 hibernation issues
After hibernation, the laptop will immediately wake up to the login screen.

Solution:
- after hibernation failed, quickly check log:
```sh
journalctl --since "3 minutes ago" | grep -i "hiber"
journalctl -p err -b | grep -i "power|hiber|swap"
journalctl -p crit -b | grep -i "power|hiber|swap"
```
- found the message `Wakeup event detected during hibernation, rolling back`
- based on the message search online and found: https://bugs.launchpad.net/ubuntu/+source/systemd/+bug/2057687
- there are many worked solutions. #18 solved my issue as well.
- #18: add the line `blacklist intel_hid` to `/etc/modprobe.d/blacklist.conf` and then run
```sh
sudo update-grub
sudo update-initramfs -c -k all
```
- for similar discussion see also: https://bugzilla.kernel.org/show_bug.cgi?id=218634
