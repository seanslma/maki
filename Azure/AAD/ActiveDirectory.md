# Active directory

## Groups
Azure Active Directory (Azure AD) groups are used to manage users that all need the same access and permissions to resources.

## Activate an Azure AD role in PIM
https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/pim-how-to-activate-role

## grant has expired due to it being revoked
This will happen after password change
```
Azure Active Directory error '(invalid_grant) AADSTS50173: 
The provided grant has expired due to it being revoked, a fresh auth token is needed. 
The user might have changed or reset their password.
```
Solution: delete the cache the credential uses. When solution 3 does not work try this one.
```
%LOCALAPPDATA%\.IdentityService\msal.cache
```
