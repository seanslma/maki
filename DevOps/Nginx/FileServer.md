# File server

## nginx.conf
```cfg
events {}
http {
    server {
        location / {
            autoindex on; # automatically generate a directory listing when a user requests a directory
            root /data;   # all file paths within the location / block will be relative to this root
        }
    }
}
```
