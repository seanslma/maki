# setup

https://www.dokuwiki.org/devel:css?s%5B%5D=userstyle.css#user_styles

## disable update messages
in dokuwiki/doku.php, change $updateVersion to a value higher than the unique ID shown in square brackets of the update messages

## dokuwiki admin blank, how to open
http://YOUR_DOMAIN_PATH/doku.php?id=start&do=admin&page=extension
  
## change default page width
you need to put style.local.ini into "../Sites/wiki/lib/tpl/dokuwiki/style.local.ini" if you make use of the dokuwiki-template.
  _site_width__ = "100%"
  
## adjust space before list and headers
```css conf/userstyle.css
/* move list up */
p + ul {
  margin-top: -20px;
}

p + ol {
  margin-top: -20px;
}

/* h2,h3 bottom margin */
h2, h3 {
  margin-bottom: 4px;
}
```
