# wget

`wget <OPTION> <URL>`

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

## dos
```dos
@echo off

set wget="wget.exe"
set despath="C:/Files"
set website="https://www.example.com/data/"

%wget% -P %despath% -A .zip -N -nd -r -l1  %website%
%wget% -P %despath% -A .ZIP -N -nd -r -l1  %website%

@pause
```

<text>
-P destination path
-A extension
-N Turn on time-stamping
-r Turn on recursive retrieving
-l1 One level depth
-nd Do not create a hierarchy of directories when retrieving recursively

Note: extension is case sensitive. Extension .ZIP should also be considered
</text>
