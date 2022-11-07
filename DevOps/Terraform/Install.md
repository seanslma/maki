# Install

https://adamtheautomator.com/terraform-azure-vm/

## Windows
- download the exe and extract it into a folder
- add the folder path to the `path` env
- `terraform -version`

## Linux
https://www.terraform.io/downloads
```
curl -O <terraform_download_url>
unzip <zip_file_downloaded_in_previous_step>
mv terraform /usr/bin/
```

apt???
```
wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform
```
