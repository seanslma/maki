# Hard disk

## check hard disk health
install `sudo apt install smartmontools`
```
lsblk #list all hard drives, or use sudo fdisk -l
lsblk -o NAME,MODEL,SIZE,TYPE #list type as well
df /home/user/Documents #find the disk the folder belongs to
sudo smartctl -a /dev/sda #check disk health
```

## file-system became read-only
A common reason for a file-system to be read-only is because it has errors, and needs `fsck` (file system check).
```
mount | grep sda1

sudo fsck -Af -M
sudo fsck.ext4 -f /dev/sda1 #if the file system is ext4
sudo reboot
```
