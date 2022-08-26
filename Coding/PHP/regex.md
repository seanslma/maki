# Regular Expression

```php
	$myMatch = array();
	$myPattern = "/_[0-9]+/";
	preg_match($myPattern, $filename, $myMatch);
	if (count($myMatch) > 0) {
		$year = substr($myMatch[0], 1, 4);
    echo "Year: " . $year;
	}
```
