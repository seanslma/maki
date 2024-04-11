# SSL

## sslmode
https://www.postgresql.org/docs/current/libpq-ssl.html

## gssencmode
https://github.com/pgjdbc/pgjdbc/issues/1867

if we already set `sslmode=require` then a GSSAPI encrypted connection increases the latency for nothing.
```
gssencmode=disbale
```
