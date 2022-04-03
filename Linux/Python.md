# Python

## miniforge install
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
