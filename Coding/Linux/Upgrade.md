# Upgrade

## Upgrade failed
https://koen.vervloesem.eu/blog/fixing-a-failed-upgrade-to-ubuntu-2204-lts-in-recovery-mode/
```sh
sudo apt update
sudo apt upgrade
sudo do-release-upgrade
```

## issues after upgrade
Ctl + Alt + F3 to open terminal, then
```sh
sudo apt-get update && sudo apt-get upgrade -y
# if any errors follow instructions to fix it and run previous command again
sudo reboot now # reboot system
```
