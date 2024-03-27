# Authorization
- https://learn.microsoft.com/en-us/entra/identity-platform/index-web-app?pivots=devlang-python&tabs=windows
- https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow
- https://intility.github.io/fastapi-azure-auth/usage-and-faq/calling_your_apis_from_python/

If someone wants to use your API, they should create their own app registration and their own secret.

## get token
```py
import requests
def get_token(
    auth_url, client_id, client_secret, scope, grant_type = 'client_credentials'
):
    """
    Return: tuple[status_code, access_token]
    (200, {
        'token_type': 'Bearer',
        'expires_in': 3599,
        'ext_expires_in': 3599,
        'access_token': 'xxxx'
     })
    """    
    data = { 
        'client_id': client_id,        
        'client_secret': client_secret,
        'scope': scope,
        'grant_type': grant_type,
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    resp = requests.post(url=auth_url, data=data, headers=headers)
    return  resp.status_code, resp.json()
```

## call api with token
```py
# test
tenant_id = '567f1234-c7de-4321-987a-dd4e54321c98'
client_id = '1234de76-54a3-21ae-97bc-6eba3456789e'
client_secret = 'xxx'
scope = f'{client_id}/.default'

auth_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
url = 'https://test.data.example.com'
access_token = get_token(auth_url, client_id, client_secret, scope)[1]['access_token']
headers = {'Authorization': f'Bearer {access_token}'}
api_resp = requests.get(url=url, headers=headers)
print(api_resp.json())
```
