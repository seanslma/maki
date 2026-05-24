# USB Stick

## tools
- On Linux, use Etcher
- On Windows, use Rufus to create a bootable usb stick

## linux
linux lite dropped x86 support, so the latest version can be installed is v3.8
- Swap Partition:  size = 4G 1-2 times RAM, format = linux-swap
- Root Partition:  size = 40GB, format = Ext4, mount point = "/"
- Home Partition:  size = 76G rest of disk, format = Ext4, mount point = "/home"
