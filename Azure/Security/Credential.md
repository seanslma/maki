# Credential

## Azure ChainedTokenCredential Fails after Password Change
SharedTokenCacheCredential: Azure Active Directory error '(invalid_grant) AADSTS50173: 
The provided grant has expired due to it being revoked, a fresh auth token is needed. 
The user might have changed or reset their password.

Solution 1, delete the cache the credential uses
```
%LOCALAPPDATA%\.IdentityService\msal.cache
```

Solution 2, 
```
credential = DefaultAzureCredential(exclude_shared_token_cache_credential=True)
```

Solution 3, Clear Azure credential cache
- Install `Az-Cmdlets` for powershell
- Run `Clear-AzContext` to clear cached credentials in powershell

## Add credentials via client app's registration
Let container access the azure blob storage via `EnvironmentCredential`:
https://learn.microsoft.com/en-us/dotnet/api/azure.identity.environmentcredential?view=azure-dotnet

https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-configure-app-access-web-apis#add-credentials-to-your-web-application