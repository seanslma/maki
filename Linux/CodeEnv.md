# Code Env

## install vs code
```
#Update the packages index and install the dependencies 
sudo apt update
sudo apt install software-properties-common apt-transport-https wget

#Import MS GPG key andenable vs code repository
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"

#install vs code
sudo apt install code

#update
sudo apt update
sudo apt upgrade
```

## install python miniforge
```
sudo apt update
sudo apt upgrade

#get Miniforge and make it the main Python interpreter
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh -O ~/miniforge.sh
bash ~/miniforge.sh -b -p ~/miniforge
rm ~/miniforge.sh

echo "PATH=$PATH:$HOME/miniforge/bin" >> .bashrc
source .bashrc
```

## install powershell
```
sudo apt update
sudo apt install -y wget apt-transport-https software-properties-common                               #install pre-requisite packages
wget -q "https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/packages-microsoft-prod.deb" #download Microsoft repository GPG keys
sudo dpkg -i packages-microsoft-prod.deb                                                              #register Microsoft repository GPG keys
sudo apt update                           #update package list after adding packages.microsoft.com
sudo apt-get install -y powershell        #install PowerShell
pwsh                                      #start PowerShell
```
