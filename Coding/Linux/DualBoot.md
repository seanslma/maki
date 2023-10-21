# Dual boot

## Repair grub efi overwritten by windows update
https://askubuntu.com/questions/88384/how-can-i-repair-grub-how-to-get-ubuntu-back-after-installing-windows

When starting up the computer, it goes straight to Windows, without giving me the option of booting Ubuntu.

Reason: Windows assumes it is the only operating system (OS) on the machine. During update it replaces GRUB with its own boot loader.

Solution: Replace the Windows boot loader with GRUB.
- Boot from the live USB, in "Try Ubuntu" mode
- Determine the partition number of your main partition `sudo fdisk -l`
- Mount your partition `sudo mount /dev/nvme0n1p7 /mnt`
- Bind mount some other stuff `for i in /sys /proc /run /dev; do sudo mount --rbind "$i" "/mnt$i"; done`
- `sudo chroot /mnt`
- update grub `update-grub`
- reinstall grub `grub-install /dev/nvme0n1`
- reboot `exit` and `sudo reboot`

## Stuck at GRUB command line - GNU GRUB version 2.06-3~deb11u2
https://medium.com/codebrace/rescuing-a-non-booting-grub-on-linux-9409dd623743

This means the grub could not find the root system so we need to repair it.

### find disk and partition info
https://ubuntuforums.org/showthread.php?t=2455336
```sh
sudo fdisk -lu
```
My disk is `/dev/nvme0n1` and the partition for linux is `/dev/nvme0n1p7`

### find the partition with `/boot/grub`
- Type `ls` to list all partitions that GRUB sees
- Use `ls (hd0,gpt7)/` command to find the partition with `/boot/grub`
- Ensure this is the linux partition: `grub> cat (hd0,gpt7)/etc/issue` will return `Ubuntu 20.04 LTS \n \l`

### temporally boot from grub into the linux system (only works once)
In the second line `root=/dev/sdX` sets the location of the root filesystem. Mine is `/dev/nvme0n1`.
The third line sets the initrd file, which must be the same version number as the kernel.
```sh
grub> set root=(hd0,gpt7)
grub> linux /boot/vmlinuz-3.13.0-29-generic root=/dev/sda1
grub> initrd /boot/initrd.img-3.13.0-29-generic
grub> boot
```

### making permanent repairs
Open a terminal in the linux
```sh
sudo update-grub
sudo grub-install /dev/nvme0n1p7
```
Install the grub to the boot sector of your hard drive and not to a partition.
