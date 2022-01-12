# WSL

## check if Intel Virtualization is enabled
```
Get-ComputerInfo -property "HyperV*"
```

## install docker
https://dev.to/bowmanjd/install-docker-on-windows-wsl-without-docker-desktop-34m9

## System has not been booted with systemd as init system (PID 1). Can't operate.
```
#do not use
sudo systemctl status docker
#instead
sudo service docker-server-name start
#get docker-server-name
service --status-all
```
