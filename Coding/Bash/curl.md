# curl

## download to current folder
`-O` keep remote filename
```
curl -O https://dev.com/api/hello.cpp
```

Sending a request with HEAD method (`-I`) to see the redirected url
```
curl -LI https://dev.com/api/hello.cpp
```

Sometimes downloadd file has 0 size. Need to tell `curl` to follow HTTP redirection by using `-L/--location`
```
curl -LO https://dev.com/api/hello.cpp
```

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
