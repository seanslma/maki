# IO

## read csv in zip file

**Disadvantages**: if the zip file is huge, the memory uage is also huge.

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
