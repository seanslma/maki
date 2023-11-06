# apache

## install
```bat
cd C:\Apache\Apache2.2\bin
httpd.exe -k install -n "Apache server"
```

## uninstall
```bat
cd C:\Apache\Apache2.2\bin
httpd.exe -k uninstall -n "Apache server"
```

## restart
```bat
cd C:\Apache\Apache2.2\bin
httpd.exe -k restart
```

## change port
```bat
Listen 8080
```

## apache does not run .php, in httpd.conf
````bat
AddType application/x-httpd-php .php
LoadModule php7_module "C:\php\php7apache2_4.dll"
````
