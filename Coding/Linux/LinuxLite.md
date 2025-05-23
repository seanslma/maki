# Linux Lite

## Install dual boot with winxp
create partitions for swap, boot and home

## Fix start with number lock
Edit: /etc/lightdm/lightdm.conf

Comment out: greeter-setup-script=/usr/bin/numlockx on

## Shutdown buttons missing
Open Lite Tweaks --> Login & Logout Options... select "Show all Options" and Apply.

Then logout and login again... Shutdown and Restart buttons should be enabled once again.

## Fix hibernation with swap partition
```sh
#1. copy swap UUID number
$ cat /etc/fstab #UUID=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX

#2. edit file /etc/default/grub
GRUB_CMDLINE_LINUX=""  -->
GRUB_CMDLINE_LINUX="resume=UUID=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"

3. update grub
$ sudo update-grub

4. install initramfs-tools
$ sudo apt-get update -y
$ sudo apt-get install -y initramfs-tools

5. update initramfs
$ sudo update-initramfs -u

6.- restart
```

## slow boot
https://www.reddit.com/r/Ubuntu/comments/clu0lj/short_guide_to_improve_slow_boot_on_ubuntu_1804/
```sh
systemd-analyze
systemd-analyze blame
systemd-analyze critical-chain
```

## delay service autostart
option 1: add an ExecStarPre command after the [service]
```sh
[Service]
ExecStartPre=/bin/sleep 5
EnvironmentFile=/etc/default/myservice
```

option 2: create a .timer systemd unit file to control the execution of the .service unit file.

Wait for 1 minute after boot-up before starting the foo.service.
```sh
[Timer]
OnBootSec=1min
```
It is important that the service is disabled, and the timer enabled
```sh
systemctl disable foo.service
systemctl enable foo.timer
```

## prevent docker autostart
```sh
#stop docker
sudo systemctl stop docker.service
sudo systemctl stop docker.socket
#disable docker
sudo systemctl disable docker.service
sudo systemctl disable docker.socket
#check status
systemctl status docker
#check boot status
systemctl list-unit-files | grep -i docker
systemctl list-unit-files | grep -i 'state\|docker'
```

## Colored terminal
  * Add this after the last 'fi' in .bashrc
```sh
# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
    # We have color support; assume it's compliant with Ecma-48
    # (ISO/IEC-6429). (Lack of such support is extremely rare, and such
    # a case would tend to support setf rather than setaf.)
    color_prompt=yes
    else
    color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt
```
  * In terminal input
```sh
source ~/.bashrc
```

## install vs code
```sh
sudo apt update
#install dependencies
sudo apt install software-properties-common apt-transport-https
#download repository and import Microsoft’s GPG key
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
#install vs code
sudo apt update
sudo apt install code
```

## Install PHP
```sh
sudo apt install php php-cli php-fpm php-json php-common php-mysql php-zip php-gd php-mbstring php-curl php-xml php-pear php-bcmath
php --version #check version
php -m #listing all loaded PHP modules
```

## install Python3 custom version
```sh
cd ~
mkdir tmp
cd tmp
wget https://www.python.org/ftp/python/3.9.7/Python-3.9.7.tgz
tar zxvf Python-3.9.7.tgz
cd Python-3.9.7
./configure --prefix=$HOME/opt/python-3.9.7
make
make install
export PATH=$HOME/opt/python-3.9.7/bin:$PATH#add to .bash_profile
. ~/.bash_profile #update to active loacal python env
```
