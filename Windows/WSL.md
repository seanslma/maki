# WSL

## check if Intel Virtualization is enabled
```
Get-ComputerInfo -property "HyperV*"
```

## install
```
wsl -l -o #show available Linux distributions
wsl --install -d <Distribution Name> #install distribution
wsl -l -v #show installed Linux distributions
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
### Change wsl settings
Disable password requirement for starting cron service
- run: `sudo visudo`
- add: `%sudo ALL=NOPASSWD: usr/sbin/service start cron`
### Create a scheduled task
- taskschd.msc
- Actions > Create Basic Task
- Triggers: When the computer starts
- Action: Start a program: `C:\Windows\System32\wsl.exe`, args: `sudo /usr/sbin/service start cron`
- Finish: Run whether the user logged on or not
