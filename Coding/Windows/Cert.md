# Cert

## show all certs 
```powershell
Get-ChildItem -Path cert:\LocalMachine\Root
```

## add cert to windows cert store
```powershell
Import-Certificate -CertStoreLocation cert:\LocalMachine\Root -FilePath C:\Path\To\Your\Certificate.crt 
```
