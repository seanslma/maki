# How to install and setup WSL on Windows 

Windows Subsystem for Linux (WSL) is one of the best options if you need both Windows and Linux at the same time but do not want to setup a dualboot. 
WSL allows you install a Linux distribution like Ubuntu, Debian, OpenSUSE, etc and you can use Linux applications and tools directly on windows.

## Prerequisites
Before install WSL you must ensure your Windows machine has been setup appropriately. 

Generally you must be running Windows 10 version 2004 and higher or Windows 11 to use the installation commands below. 
Otherwide you need to install the WSL manually.

Another important thing is that the `Virtualization` on your machine must be enabled. 
If not sure, you can open the task manager and click the `Performance` tab to check. 
If it shows your machine is running as `virtual machine` rahter than `virtualization`, 
you must enable the `virtualization`.

Also, your Windows features like `Virtual Machine Platform` and `Windows Subsystem for Linux` must be enabled.

If your are not sure how to enable the required feature, you can use a search engine or ChatGPT and Bard to help you.

## WSL installation via commands
Once the prerequisites are met, WSL can be installed easily using the following commands:
```sh
wsl -l -o                            # Show available Linux distributions
wsl --install -d <Distribution Name> # Install a distribution such as `wsl --install -d Ubuntu-22.04`
wsl -l -v                            # Show installed Linux distributions
```

## Configuration to limit WSL memory usage
If you do not limit the amount of memory your WSL can use, it might use most of the memory available on your machine. 
This might slow down your Windows aplications. 
 
To limit the memory that can be used by WSL, you can setup it in your WSL config file by appending (must be the Unix newline terminator): 
```
[wsl2]
memory=4GB
```
Note that the WSL config file is usually can be found at `C:\Users\<your-user-name>\.wslconfig`.

After the configuration setting update, run the bellow commands:
```sh
# Run it in Windows terminal
wsl --shutdown # Restart WSL
# Run it in WSL terminal
free -h --giga # Check total memory
```

## Commands to release disk space back
After using WSL for a while you might find that your hard disk is full and WSL uses most capacity.
This is because WSL2 will not automatically release used disk space so we have to do it manually.

There are two options to release the disk space used by WSL.

### compact option in diskpart
This option uses the `compact` command in `diskpart` to relaese the disk space. Please remmeber to change the filepath accordingly.
```
# Run them in Windows terminal
wsl --shutdown
diskpart # Will open window Diskpart

# Run them in the opened Diskpart window
select vdisk file="C:\Users\<your-user-name>\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu20.04onWindows_79rhkp1fndgsc\LocalState\ext4.vhdx"
attach vdisk readonly
compact vdisk
detach vdisk
exit
```

### optimize-vhd
The command `optimize-vhd` is only available in Windows 10 Pro with Hyper-v feature installed.
```
cd C:\Users\<your-user-name>\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu20.04onWindows_79rhkp1fndgsc\LocalState
wsl --shutdown
optimize-vhd -Path .\ext4.vhdx -Mode full
```

After the installation of WSL, you can install other applications such as Docker, Azure CLI etc. 
You can also setup crontab to run scheduled tasks. 
Files can be copied between Windows and WSL as well.
For example, copy a file from `C:/test/data.csv` to your current folder you can run `cp /mnt/c/test/data.csv ./data.csv`.
