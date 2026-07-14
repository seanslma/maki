# Migration

## Azure data migration
Copy data from one container to another container.
```sh
azcopy login

azcopy copy \
"https://sourceaccount.blob.core.windows.net/sourcecontainer" \
"https://destinationaccount.blob.core.windows.net/destinationcontainer" \
--recursive=true
```

Copy data from one storage account to another account.
```sh
azcopy copy \
"https://sourceaccount.blob.core.windows.net?<SAS>" \
"https://destaccount.blob.core.windows.net?<SAS>" \
--recursive=true

azcopy sync \
"https://sourceaccount.blob.core.windows.net?<SAS>" \
"https://destaccount.blob.core.windows.net?<SAS>"
```
