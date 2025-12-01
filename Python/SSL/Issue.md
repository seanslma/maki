# Issue

## az login fails with "certificate verify failed: unable to get local issuer certificate"
Azure CLI uses python to connect to server:
- https://github.com/Azure/azure-cli/issues/19571
- The proxy intercepts Azure CLI's HTTPS traffic, decrypts and re-encrypts it with its own certificate, but the proxy can't return all intermediate and root CA certificates, leading to the failure.
- All intermediate and root CA certificates should be appended to the `cacert.pem` file and then set the env var `REQUESTS_CA_BUNDLE` to this file.

## python list trusted CA certificates path
Output the paths where Python is looking for trusted CA certificates:
```sh
python -c "import ssl; print(ssl.get_default_verify_paths())"
```

The output on windows may look like this:
```
DefaultVerifyPaths(
    cafile='C:\\Users\\x\\conda-envs\\env1\\Library\\ssl\\cacert.pem',
    capath='C:\\Users\\x\\conda-envs\\env1\\Library\\ssl\\certs',
    openssl_cafile_env='SSL_CERT_FILE',
    openssl_cafile='C:\\Program Files\\Common Files\\ssl\\cert.pem',
    openssl_capath_env='SSL_CERT_DIR',
    openssl_capath='C:\\Program Files\\Common Files\\ssl\\certs'
)
```

In this case, as we use conda env, the `REQUESTS_CA_BUNDLE` env var should point to the conda env file (configured for the packages we're using) not the system-wide certificate file.
