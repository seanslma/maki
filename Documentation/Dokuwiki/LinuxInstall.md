# Install Docuwiki on Linux

## install php 7.0 and extensions
```sh
sudo apt install -y php7.0 php7.0-cli php7.0-fpm php7.0-gd php7.0-xml php7.0-zip
```

## install apache2
```sh
sudo apt update
sudo apt install apache2

sudo apt install libapache2-mod-php7.0
sudo a2enmod php7.0 #enable php7.0 in apache2
sudo service apache2 restart

sudo systemctl stop apache2.service
sudo systemctl start apache2.service
sudo systemctl enable apache2.service
```

## install dokuwiki
```sh
stat -c '%G' /var/www/dokuwiki #check folder owner
sudo mkdir -p /var/www/dokuwiki #create a document root directory
sudo chown -R johndoe:johndoe /var/www/dokuwiki #change ownership of the directory to user
cd /var/www/dokuwiki
wget https://download.dokuwiki.org/src/dokuwiki/dokuwiki-stable.tgz #download newest stable release of DokuWiki

#Unpack the DokuWiki tarball.
tar xvf dokuwiki-stable.tgz
rm dokuwiki-stable.tgz
sudo mv dokuwiki/dokuwiki-*/ dokuwiki
rmdir dokuwiki-2018-04-22b/

#Change ownership of the /var/www/dokuwiki directory to www-data
sudo chown -R www-data:www-data /var/www/dokuwiki

#Change document root in Apache to point to /var/www/dokuwiki
sudo nano /etc/apache2/sites-enabled/000*.conf #Replace DocumentRoot /var/www/html with DocumentRoot /var/www/dokuwiki

#Change AllowOverrides setting in Apache2 to use .htaccess files for security
sudo vi /etc/apache2/apache2.conf #For directory /var/www/ replace AllowOverride None with AllowOverride All

#Restart php7.0-fpm.service
sudo systemctl restart php7.0-fpm.service

sudo rm /var/www/dokuwiki/install.php
```
