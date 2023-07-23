# php

the NON Thread safe (nts) php does not support apache and you have to install thread safe versions

## install
php.ini-development to php.ini and change:
  display_errors = on
  log_errors = on
  error_log = c:\log\php_errors.log
  SMTP = mail.svr.com
  extension=curl
  extension=gd2
  extension=mbstring
  extension=pdo_mysql

**print_r**() displays information about a variable in a way that's readable by humans.

**var_dump**() displays structured information about one or more expressions that includes its type and value.

```php
//to error_log
error_log( print_r( $object, true ) );

function error_log_var_dump( $object=null ){
    ob_start();                    // start buffer capture
    var_dump( $object );           // dump the values
    $contents = ob_get_contents(); // put the buffer into a variable
    ob_end_clean();                // end capture
    error_log( $contents );        // log contents of the result of var_dump( $object )
}

error_log_var_dump( $object );
```

## install package
npm i --save puppeteer

install to folder: "C:\Program Files\nodejs\node_modules"
npm install --prefix "C:\Program Files\nodejs" puppeteer --save

get data from web js in php:\\
https://developers.google.com/web/tools/puppeteer/articles/ssr

puppeteer-and-chrome-headless:\\
https://medium.com/@e_mad_ehsan/getting-started-with-puppeteer-and-chrome-headless-for-web-scrapping-6bf5979dee3e

https://dev.to/alanmbarr/scraping-html-with-php-node-and-puppeteer-10m2

## debug in VS code
* download xdebug based on php version: https://xdebug.org/download
* copy the dll to: C:\php\ext
* update php.ini, add:
```ini
[XDebug]
zend_extension="C:\php\ext\php_xdebug-3.0.4-7.4-vc15-x86_64.dll"
;xdebug.remote_enable = 1      depreciated
;xdebug.remote_autostart = 1   depreciated
xdebug.mode=debug
xdebug.start_with_request=yes
```
* in VS code, install extension PHP Debug
* in VS code, debug -> add config file
* run in debug mode

## get previous day
$dt = date("Y-m-d H:i:s", strtotime("-1 day")); //$dt is a string

## set local log date
date_default_timezone_set('Australia/Brisbane');

## log4php.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<log4php:configuration xmlns:log4php="http://logging.apache.org/log4php/">
    <appender name="myConsoleAppender" class="LoggerAppenderConsole">
        <layout class="LoggerLayoutPattern">
            <param name="conversionPattern" value="%-5level - %message%n" />
        </layout>
    </appender>

    <appender name="myFileAppender" class="LoggerAppenderFile" threshold="WARN">
        <layout class="LoggerLayoutPattern">
            <param name="conversionPattern" value="%date{Y-m-d H:i:s} %-5level - Line: %-5line File: %file%n  %-25logger %message%n" />
        </layout>
        <param name="file" value="myphp.log" />
    </appender>

    <appender name="myDBAppender" class="LoggerAppenderPDO" threshold="WARN">
        <layout class="LoggerLayoutPattern">
            <param name="conversionPattern" value="%date{Y-m-d H:i:s.u},%logger,%level,%message,%pid,%file,%line" />
        </layout>
        <param name="dsn" value="mysql:host=localhost;dbname=mydb;port=3306"/>
        <param name="user" value="usr" />
        <param name="password" value="pwd" />
        <param name="table" value="log_warn" />
        <param name="insertPattern" value="%date{Y-m-d H:i:s.u},%logger,%level,%message,%pid,%file,%line" />
    </appender>

    <root>
        <level value="DEBUG" />
        <appender_ref ref="myFileAppender" />
        <appender_ref ref="myConsoleAppender" />
        <appender_ref ref="myDBAppender" />
    </root>
</log4php:configuration>
```

## zip
```php
function OpenCsvInZip($zipfilename) {
    $zip = new ZipArchive;
    if ($zip->open($zipfilename)) {
        if ($zip->numFiles > 0) {
            $filename = $zip->getNameIndex(0);
            $fp = $zip->getStream($filename);
            if ($fp) {
                return $fp;
            }
        }
    }
    return null;
}
```
