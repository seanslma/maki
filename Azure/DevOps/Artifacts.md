# Azure Artifacts

## List feeds and packages
```py
import json
import requests
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
token = credential.get_token(
    'https://app.vssps.visualstudio.com/.default'
).token
headers = {'Authorization': f'Bearer {token}'}

# list feed names
organization = '<organization>'
url = f'https://feeds.dev.azure.com/{organization}/_apis/packaging/feeds'

params = {'api-version': '7.1'}
r = requests.get(url, params=params, headers=headers)

print(r.status_code)
for feed in r.json()['value']:
    if 'project' in feed:
        print(f"{feed['project']['name']}/{feed['name']}")
    else:
        print(feed['name'])
    print(f" - id: {feed['id']}")

# list feed packages	
project = '<project>'
feed_id = '<feed-id>'
url = f'https://feeds.dev.azure.com/{organization}/{project}/_apis/packaging/feeds/{feed_id}/packages'

params = {
    'api-version': '7.1',
    'protocolType': 'PyPI',
    'includeAllVersions': 'true',
}
r = requests.get(url, params=params, headers=headers)

print(r.status_code)
for package in r.json()['value']:
    print(package['name'])
    for version in package['versions']:
        print(f" - {version['version']}")	

# list feeds in detail
url = f'https://feeds.dev.azure.com/{organization}/_apis/packaging/feeds'

params = {'api-version': '7.1'}
r = requests.get(url, params=params, headers=headers)

print(r.status_code)
print(json.dumps(r.json(), indent=2))
```
