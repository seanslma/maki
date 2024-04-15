# Disk

## show disk uage
```sh
df -h
```

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

## mount cifs network drive
- https://linuxize.com/post/how-to-mount-cifs-windows-share-on-linux/
- https://unix.stackexchange.com/questions/68079/mount-cifs-network-drive-write-permissions-and-chown

On Linux and UNIX operating systems, a Windows share can be mounted on a particular mount point 
in the local directory tree using the cifs option of the mount command.

The Common Internet File System (CIFS) is a network file-sharing protocol. CIFS is a form of SMB.
```sh
sudo mkdir /mnt/dat
sudo mount -t cifs -o credentials=/etc/smb.credentials //server-address/folder /mnt/dat
sudo mount -t cifs -o username=${USER},password=${PASSWORD},uid=$(id -u),gid=$(id -g)
//server-address/folder /mnt/dat
```
To verify that the remote Windows share is successfully mounted, use either the `mount` or `df -h` command.

To ensure the mount persists on system reboots, this command must be added to 
the `fstab` or equivalent to mount the DOCS DATA and VIEWER DATA on system startup.
```
# <file system>          <dir>    <type> <options>                                                   <dump>  <pass>
//server-address/folder  /mnt/dat  cifs  file_mode=0755,dir_mode=0755,credentials=/etc/win-credentials 0       0

# dat mount directory
//xyz1wes01/dat  /mnt/dat  cifs  uid=1000,gid=1000,vers=1.0,defaults,credentials=/home/user/smb.credentials 0 0
```
Run the following command to mount/umount the share:
```sh
sudo mount /mnt/dat
sudo umount /mnt/dat
```

## where a path is mounted from
```sh
sudo cat /etc/fstab      # check the file content
mountpoint /mnt/myfolder # will also tell if not mounted
```

## mounted path is `ro` or `rw`
```sh
cat /proc/mounts
//xyz1wes01/dat /mnt/dat cifs rw,relatime,vers=1.0,cache=strict,username=usr,domain=,uid=1000,forceuid,gid=1000,forcegid,
addr=90.800.70.60,file_mode=0755,dir_mode=0755,soft,nounix,mapposix,rsize=61440,wsize=65536,echo_interval=60,actimeo=1 0 0
```
