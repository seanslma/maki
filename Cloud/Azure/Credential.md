# Credential

## Azure ChainedTokenCredential Fails after Password Change
SharedTokenCacheCredential: Azure Active Directory error '(invalid_grant) AADSTS50173: 
The provided grant has expired due to it being revoked, a fresh auth token is needed. 
The user might have changed or reset their password.

Solution 1, delete the cache the credential uses: 
```
%LOCALAPPDATA%\.IdentityService\msal.cache
```

Solution 2, 
```
credential = DefaultAzureCredential(exclude_shared_token_cache_credential=True)
```
