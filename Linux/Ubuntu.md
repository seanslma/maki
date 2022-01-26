# Ubuntu

## change mirror site in sources.list
```
sudo vi /etc/apt/sources.list
#replace http://archive.ubuntu.com/ubuntu with another mirror

#http://au.archive.ubuntu.com/ubuntu

:%s/search_string/replacement_string/g
:%s#search_string#replacement_string#g
```

## Enable hibernate
Disable swapfile and delete it
```
 sudo swapoff /swapfile  
 sudo rm /swapfile
```
https://ubuntuhandbook.org/index.php/2021/08/enable-hibernate-ubuntu-21-10/
