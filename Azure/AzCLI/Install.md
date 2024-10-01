# Install

## specific version
https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt

check available versions:
```sh
apt-cache policy azure-cli
```

Install
```sh
AZ_VER=2.51.0              # Azure CLI version
AZ_DIST=$(lsb_release -cs) # currently installed distribution
# Install a specific version
sudo apt-get install azure-cli=${AZ_VER}-1~${AZ_DIST}
```
