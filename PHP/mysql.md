# MySQL

In MySQL query returned results in PHP, every field will be a string OR NULL - be careful about the integer and float.

## run query

```php
$log = Logger::getLogger('MyLogger');
$db = SqlCnnFactory::getFactory()->getConnection();
  
$result = $db->query($qry);
if (!$result) {
    $log->fatal("SQL query error: " . mysqli_error($db));
    $log->info("SQL query error. Query: " . substr($qry, 0, min(1000, strlen($qry))));
}

class SqlCnnFactory {
    private static $factory;
    public static function getFactory() {
        if (!self::$factory)
            self::$factory = new SqlCnnFactory();
        return self::$factory;
    }

    private static $db;
    public function getConnection(?string $dbname = null) {
        if (!self::$db) {
            self::$db = mysqli_connect(DB_HOSTNAME, DB_USERNAME, DB_PASSWORD, $dbname, DB_PORT);
            if (mysqli_connect_errno()) {
                $log->fatal("Connect failed: " . mysqli_connect_error());
                exit;
            }
        }
        return self::$db;
    }
}
```
