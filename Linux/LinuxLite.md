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
```bash
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

## Dual boot OS selecttion time
  * open /etc/default/grub
  * change GRUB_TIMEOUT=10 [value in second] and save it
  * sudo update-grub and reboot

## Colored terminal
  1 Add this after the last 'fi' in .bashrc
```bash
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
  1 In terminal input
```bash
source ~/.bashrc
```

## Install PHP
sudo apt install php php-cli php-fpm php-json php-common php-mysql php-zip php-gd php-mbstring php-curl php-xml php-pear php-bcmath
php --version #check version
php -m #listing all loaded PHP modules

