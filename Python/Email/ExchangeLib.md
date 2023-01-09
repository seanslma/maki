# Exchangelib

https://www.activestate.com/resources/quick-reads/how-to-install-and-use-exchangelib-python/

Exchangelib is a Python client library (cross-platform) that provides an interface for accessing and working with Microsoft Exchange Web Services (EWS).

## test tls cert
Very helpful with lots of info related to ssl: \
https://github.com/ecederstrand/exchangelib/issues/798
```py
import requests
requests.post('https://owa.example.com/EWS/Exchange.asmx')
```

## supported tls version
```py
import requests
print(requests.get('https://www.howsmyssl.com/a/check', verify=True).json()['tls_version'])
```

## Custom TLS Validation
Supply a custom ‘requests’ transport adapter class, if custom TLS validation is needed.
```py
class CustomHTTPAdapter(requests.adapters.HTTPAdapter):
  def cert_verify(self, conn, url, verify, cert):
      cert_file = {
          'example.com': '/path/to/example.com.crt',
          'mail.internal': '/path/to/mail.internal.crt',
      }[urlparse(url).hostname]
      super(RootCAAdapter, self).cert_verify(conn=conn, url=url, verify=cert_file, cert=cert)
BaseProtocol.HTTP_ADAPTER_CLS = CustomHttpAdapter

class ProxyAdapter(requests.adapters.HTTPAdapter):
...
BaseProtocol.HTTP_ADAPTER_CLS = ProxyAdapter
```

## SSL error unsafe legacy renegotiation disabled
https://stackoverflow.com/questions/71603314/ssl-error-unsafe-legacy-renegotiation-disabled
- Import `ssl` and `urllib3`
  ```py
  import requests
  import urllib3
  import ssl
  ```
- Create a custom `HttpAdapter` which uses a custom ssl Context
  ```py
  class CustomHttpAdapter(requests.adapters.HTTPAdapter):
      """Transport adapter that allows us to use custom ssl_context."""

      def __init__(self, ssl_context=None, **kwargs):
          self.ssl_context = ssl_context
          super().__init__(**kwargs)

      def init_poolmanager(self, connections, maxsize, block=False):
          self.poolmanager = urllib3.poolmanager.PoolManager(
              num_pools=connections, 
              maxsize=maxsize,
              block=block, 
              ssl_context=self.ssl_context,
          )
  ```
- Set up an ssl context which enables `OP_LEGACY_SERVER_CONNECT`, and use it with the custom adapter.
  ```py
  def get_legacy_session():
      ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
      ctx.options |= 0x4  # OP_LEGACY_SERVER_CONNECT
      session = requests.session()
      session.mount('https://', CustomHttpAdapter(ctx))
      return session  
  ```
  - Use it like
  ```py
  with get_legacy_session() as s: 
      response = s.get(url=url)
  ```
  
