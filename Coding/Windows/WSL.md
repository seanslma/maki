# WSL

## check if Intel Virtualization is enabled
```
Get-ComputerInfo -property "HyperV*"
```
To check if virtualization is enabled in the BIOS (Basic Input/Output System) of your computer, you'll need to follow these general steps. Keep in mind that the exact steps might vary slightly depending on your computer's manufacturer and model. Here's a basic guide:

1. **Access the BIOS/UEFI:**
   - Reboot your computer.
   - During the boot process, press the key to access the BIOS or UEFI. Common keys include F2, F10, F12, ESC, or DEL. The correct key is usually displayed on the screen during the boot process.

2. **Navigate to the Virtualization Setting:**
   - Once in the BIOS/UEFI, use the arrow keys to navigate through the menus.
   - Look for a section related to "Advanced," "CPU Configuration," "Advanced CPU Configuration," or something similar.

3. **Find Virtualization Technology:**
   - Within the advanced settings, look for an option called "Virtualization Technology," "Intel VT," "Intel Virtualization Technology," "AMD-V," or something similar. The exact wording might differ based on your CPU manufacturer (Intel or AMD).

4. **Enable Virtualization:**
   - If you find the virtualization option, make sure it is set to "Enabled." Use the arrow keys to navigate to the option, and change the setting if necessary.

5. **Save and Exit:**
   - After enabling virtualization, navigate to the option to save your changes and exit the BIOS/UEFI. This is typically done by selecting "Save & Exit" or a similar option. Confirm that you want to save the changes.

6. **Reboot:**
   - Allow the computer to reboot for the changes to take effect.

7. **Verify Virtualization:**
   - Once your computer has restarted, you can verify if virtualization is enabled by using a system information tool or checking within the operating system.

Keep in mind that not all computers support virtualization, and the option might not be available in the BIOS/UEFI on some systems. If you're unable to find the virtualization option or are unsure, consult your computer's documentation or the manufacturer's website for specific instructions.

## enable windows features
- Virtual Machine Platform
- Windows Subsystem for Linux

## install
```
wsl -l -o #show available Linux distributions
wsl --install -d <Distribution Name> #install distribution
wsl -l -v #show installed Linux distributions
```

## config to limit memory
https://learn.microsoft.com/en-us/windows/wsl/wsl-config#configuration-setting-for-wslconfig
- `vi editor "$(wslpath "C:\Users\<usr>\.wslconfig")"`
add to `.wslconfig` file (unix newline): 
```
[wsl2]
memory=4GB
```
- `wsl --shutdown` #restart
- `free -h --giga` #check total memory

## release disk space back
https://github.com/microsoft/WSL/issues/4699

WSL2 will not automatically release used disk space - have to do it manually

### compact option in diskpart
```
wsl --shutdown
diskpart
# open window Diskpart
select vdisk file="C:\Users\<user>\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu20.04onWindows_79rhkp1fndgsc\LocalState\ext4.vhdx"
attach vdisk readonly
compact vdisk
detach vdisk
exit
```

### optimize-vhd
only available in Windows 10 Pro with Hyper-v feature installed
```
cd C:\Users\<usr>\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu20.04onWindows_79rhkp1fndgsc\LocalState
wsl --shutdown
optimize-vhd -Path .\ext4.vhdx -Mode full
```

## install docker
https://dev.to/bowmanjd/install-docker-on-windows-wsl-without-docker-desktop-34m9

## System has not been booted with systemd as init system (PID 1). Can't operate.
```
#do not use
sudo systemctl status docker
#instead
sudo service docker status
sudo service docker start
#get docker-server-name
service --status-all
```

## Auto start cron in wsl
https://www.howtogeek.com/746532/how-to-launch-cron-automatically-in-wsl-on-windows-10-and-11/
### Change wsl settings in wsl2 terminal
Disable password requirement for starting cron service
- run: `sudo visudo`
- add: `%sudo<tab not space>ALL=NOPASSWD: usr/sbin/service cron start`
- add an empty at the end

### Create a scheduled task in windows
- taskschd.msc
- Actions > Create Basic Task
- Triggers: When the computer starts
- Action: Start a program: `C:\Windows\System32\wsl.exe`, args: `sudo /usr/sbin/service cron start`
- Finish: Run whether the user logged on or not

## Clock is out of sync with Windows
temporal solution (need to run it after each restart)
```sh
sudo hwclock -s # not work
sudo ntpdate pool.ntp.org
```
