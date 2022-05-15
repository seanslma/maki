# wget

## download to current working folder
```
wget http://mirror.ctan.org/<package_path+package_name.zip>
```

## download to a target folder
```
wget -O $HOME/Download http://mirror.ctan.org/<package_path+package_name.zip>
```

## unpack the archive
```
mkdir -p /path/to/directory
unzip filename.zip -d /path/to/directory
tar -xvf filename.tar --C /path/to/directory
tar -xvf filename.tar --directory /path/to/directory
```