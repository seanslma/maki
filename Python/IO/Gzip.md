# Gzip

## read csv in gzip
```py
import gzip

file = 'c:/test/archive.csv.gz'
# readonly text mode
with gzip.open(file, 'rt') as f:
    df = pd.read_csv(f)
```

## read csv in zip
```py
import io
import zipfile

file = 'c:/test/archive.csv.zip'
with zipfile.ZipFile(zip_file_path, 'r') as archive:
    for csv_filename in archive.namelist():
        with archive.open(csv_filename) as csv_file:
            text_data = io.TextIOWrapper(csv_file, encoding='utf-8') #convert binary to text
            df = pd.read_csv(text_data)
```
