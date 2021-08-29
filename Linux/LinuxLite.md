# Linux Lite

## Install dual boot with winxp
create partitions for swap, boot and home

## Fix start with number lock
Edit: /etc/lightdm/lightdm.conf

Comment out: greeter-setup-script=/usr/bin/numlockx on

## Shutdown buttons missing
Open Lite Tweaks --> Login & Logout Options... select "Show all Options" and Apply. 

Then logout and login again... Shutdown and Restart buttons should be enabled once again.

## Dual boot OS selecttion time
  * open /etc/default/grub
  * change GRUB_TIMEOUT=10 [value in second] and save it
  * sudo update-grub and reboot

## Install PHP
sudo apt install php php-cli php-fpm php-json php-common php-mysql php-zip php-gd php-mbstring php-curl php-xml php-pear php-bcmath
php --version #check version
php -m #listing all loaded PHP modules

