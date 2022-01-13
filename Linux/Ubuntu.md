# Ubuntu

## change mirror dite in sources.list
```
sudo vi /etc/apt/sources.list
#replace http://archive.ubuntu.com/ubuntu with another mirror

:%s/search_string/replacement_string/g
:%s#search_string#replacement_string#g
```
