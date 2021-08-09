# Start

{{cc.png|test}}

See [[wiki:syntax|syntax]] for Wiki syntax.

```
This is a
plain text example.
```

And a math ($x = ay^2 + b\sqrt{y} + c$) example:
$$x_{\rm mean} = \frac{1}{n}\sum_{i=1}^{n}x_i$$

```file txt file_example.txt
This is a
file example with export title.
```

```python
#python code example
import pandas as pd
df = new DataFrame()
df['id'] = ['a','b','c']
df['val'] = [1,2,3]
```

## Setup
  - Go to your Extension Manager page on the Admin screen and install some useful extensions
  - Create a page called “sidebar” in the root namespace with this code in it: %%{{indexmenu>..#1|js navbar nocookie id#random}}%%
  - Go to the the Configuration Settings page on the Admin screen and set the following options:
```
useslash = true
plugin → indexmenu → skip_index = /(^wiki$|^playground$)/
plugin → indexmenu → skip_file = /(^sidebar$)/
```

## Extensions
  * [[https://www.dokuwiki.org/plugin:indexmenu|IndexMenu]] for left side tree navigation with namespaces
  * [[https://www.dokuwiki.org/plugin:plaintext|PlainText]] for keeping newline in text
  * [[https://www.dokuwiki.org/plugin:mathjax|MathJax]] for LaTex style math input

## Change data/conf folder
  - move the two folders to a new directory
  - in conf/local.php add: $conf['savedir'] = 'C:/Users/usr/media/wiki/data';
  - dokuwiki/inc/preload.php add: define('DOKU_CONF', 'C:/Users/usr/media/wiki/conf/');
  - Note that the relative path does not work and the bat file should also be updated

## Change default font size
```css
/* create the file conf/userstyle.css */
body {
    font: normal 75%/1.4 Arial, sans-serif;
    /* default font size: 100% => 16px; 93.75% => 15px; 87.5% => 14px; 81.25% => 13px; 75% => 12px; 68.75% => 11px */
    -webkit-text-size-adjust: 100%;
}
```

## Set timezone
```php
// create the file config/local.protected.php
<?php
date_default_timezone_set("Australia/Brisbane");
?>
```

## Change Edit-Page height
```js conf/userscript.js
jQuery(function() {
    jQuery('#wiki__text').height('480px');
});
```

## Remove extra space between paragraph and list
```css conf/userstyle.css
.page p + ul {
    margin-top: -1.3em;
}
```

## page width
```css conf/userstyle.css
#dokuwiki__site {
    max-width: 90% !important;
}
```

## Move the wiki to another folder
**DokuWiki Setup Error**: The datadir ('pages') at /pages is not found, isn't accessible or writable. You should check your config and permission settings. Or maybe you want to run the installer?

Solution:
  * change savedir to the new data path in conf/local.php
  * change DOKU_CONF definition in dokuwiki/inc/preload.php to the conf path

**Dokuwiki warning**: "Unknown:" failed to open stream windows

Solution
  * the data path should not have spaces
