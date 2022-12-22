# curl

## get with header
```
curl 'https://my.api/hello?id=1&name=dev' -H 'Accept: text/csv'
curl 'https://my.api/hello?id=1&name=dev' -H 'Accept: text/csv' -o my.csv
curl `https://my.api/hello -H "X-Custom-Header: value" -H "Content-Type: application/json"
```

## post with header
```
curl -k -X POST https://dev.com/api/hello -H 'Content-Type: application/json' -d '{ "date": "2021-11-01", "value": 12 }' 
```
