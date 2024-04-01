# Disk

## show disk usage
```sh
df -h
du -sh ./*  #total
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

## mount help
```sh
man mount.cifs
```

## unmount cifs
```sh
umount -a -t cifs -l    # umount all cifs
umount /mnt/cifs_share  # umount a specific cifs
```

## mount cifs network drive
- https://linuxize.com/post/how-to-mount-cifs-windows-share-on-linux/
- https://unix.stackexchange.com/questions/68079/mount-cifs-network-drive-write-permissions-and-chown

On Linux and UNIX operating systems, a Windows share can be mounted on a particular mount point 
in the local directory tree using the cifs option of the mount command.

The Common Internet File System (CIFS) is a network file-sharing protocol. CIFS is a form of SMB.
```sh
sudo mkdir /mnt/dat
sudo mount -t cifs -o username=${USER},password=${PASSWORD},uid=$(id -u),gid=$(id -g) //server-address/folder /mnt/dat
sudo mount -t cifs -o credentials=/etc/smb.credentials //server-address/folder /mnt/dat
sudo mount -t cifs //my-drive/dev /mnt/dev -o uid=1000,gid=1000,vers=3.0,defaults,credentials=/home/user/smb.credentials --verbose
```

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
findmnt --target /etc/fstab # show mounted path
sudo cat /etc/fstab         # check the file content
mountpoint /mnt/myfolder    # will also tell if not mounted
```

## mounted path is `ro` or `rw`
```sh
cat /proc/mounts
//xyz1wes01/dat /mnt/dat cifs rw,relatime,vers=1.0,cache=strict,username=usr,domain=,uid=1000,forceuid,gid=1000,forcegid,
addr=90.800.70.60,file_mode=0755,dir_mode=0755,soft,nounix,mapposix,rsize=61440,wsize=65536,echo_interval=60,actimeo=1 0 0
```

## cifs logs
https://community.microfocus.com/img/oes/w/tips/14583/cifs-writing-in-2-differents-log-file
- /var/log/messages
- /var/log/cifs/cifs.log
- /etc/rsyslog.d/cifs-log.conf

## cifs troubleshooting
https://wiki.samba.org/index.php/LinuxCIFS_troubleshooting
- debug data: `/proc/fs/cifs/DebugData`
- debug message: `dmesg`

enalbe/disable debug
```sh
echo 7 | sudo tee /proc/fs/cifs/cifsFYI #enable debug
dmesg                                   #check log
echo 0 | sudo tee /proc/fs/cifs/cifsFYI #disable debug
```

- check cifs client package: `dpkg -l | grep cifs-utils`
- check cifs kernel module: `lsmod | grep cifs`
- list all services: `systemctl list-units` 

## check mounted drive
To verify that the remote Windows share is successfully mounted, use either the `mount` or `df -h` command.

Can also check the network using `ping <cifs_server_ip_or_hostname>`

## cifs issue
### cifs mount suddenly no longer works
https://ubuntuforums.org/showthread.php?t=2490382

`nodfs`: disable dfs on the client side - for latest new Linux kernels on the client machine
```sh
sudo mount -t cifs //192.168.1.16/user /media/cloudbox -o username=user,password=xxx,vers=1.0,nodfs
```

### CIFS VFS: Server has not responded
https://forums.linuxmint.com/viewtopic.php?t=190961

Solution: 
- Auto Mounting Samba Shares Using AutoFS: http://forums.linuxmint.com/viewtopic.php?f=42&t=144997
- AutoFS is an "automounter" which means it doesn't mount at boot or login it only mounts when the mount point is accessed.
- It also unmounts by itself when the share is not being used.

## access cifs via smbclient
https://unix.stackexchange.com/questions/706325/smbclient-works-but-mount-cifs-doesnt-nt-status-more-processing-required
```sh
smbclient '\\172.25.162.14\nda20' -N -m NT1 --option="client min protocol"=NT1
mount -t cifs -vvvv //172.25.162.14/nda20 /mnt/aa -o username=root,vers=1.0,guest
```

## smb error class and code
https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-cifs/8f11e0f3-d545-46cc-97e6-f00569e3e1bc
