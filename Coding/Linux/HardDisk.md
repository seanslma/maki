# Hard disk

## check hard disk health
install `sudo apt install smartmontools`
```sh
lsblk #list all hard drives, or use sudo fdisk -l
lsblk -o NAME,MODEL,SIZE,TYPE #list type as well
df /home/user/Documents #find the disk the folder belongs to
sudo smartctl -a /dev/sda #check disk health
```

## file-system became read-only
A common reason for a file-system to be read-only is because it has errors, and needs `fsck` (file system check).
```sh
mount | grep sda1

sudo fsck -Af -M
sudo fsck.ext4 -f /dev/sda1 #if the file system is ext4
sudo reboot
```

## /var/lib/docker: Device or resource busy
When run `rm -rf /var/lib/docker` or `umount /dev/xxx` got the error.
Possible reason: still in the mounted device.

## where a path is mounted from
```sh
sudo cat /etc/fstab      # check the file content
mountpoint /mnt/myfolder # will also tell if not mounted
```
## mounted path is `ro` or `rw`
```sh
cat /proc/mounts
```
