# DateTime

## previous day
```php
$dt = date("Y-m-d H:i:s", strtotime("-1 day")); //$dt is a string
```

## shift date
```php
$tday = new DateTime('now');
echo "today is: {$tday->format('Y-m-d H:i:s')}\n";

$tday->sub(new DateInterval('P1D'));
echo "yestd is: {$tday->format('Y-m-d H:i:s')}\n";

$tday->add(new DateInterval('P2D'));
echo "tomrw is: {$tday->format('Y-m-d H:i:s')}\n";
```
