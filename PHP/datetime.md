# DateTime

## shift date (I)
```php
$today = date("Y-m-d H:i:s", strtotime("now"));    //$today is a string
$yestd = date("Y-m-d H:i:s", strtotime("-1 day")); //$yestd is a string
$tomrw = date("Y-m-d H:i:s", strtotime("1 day"));  //$tomrw is a string
```

## shift date (II)
```php
$tday = new DateTime('now');
echo "today is: {$tday->format('Y-m-d H:i:s')}\n";

$tday->sub(new DateInterval('P1D'));
echo "yestd is: {$tday->format('Y-m-d H:i:s')}\n";

$tday->add(new DateInterval('P2D'));
echo "tomrw is: {$tday->format('Y-m-d H:i:s')}\n";
```
