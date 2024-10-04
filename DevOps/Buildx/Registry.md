# Registry

## push to acr from aks pod
https://github.com/Azure/acr/issues/582
```
error: failed to solve: failed to push my-acr.azurecr.io/dev/test:0.0.1: 
failed to authorize: failed to fetch anonymous token:
unexpected status: 401 Unauthorized
```
bug in buildkit?
- https://github.com/moby/buildkit/blob/ffe2301031c8f8bfb8d5fc5034e5e509c5624913/session/auth/authprovider/authprovider.go#L91

## buildkit + private registry
connect to private registry:
- https://medium.com/@aabeing/aks-as-azure-devops-agents-buildkit-5af8e5cd43d1
- If credentials are required, buildctl will attempt to read Docker configuration file $DOCKER_CONFIG/config.json.
- $DOCKER_CONFIG defaults to ~/.docker.
  ```json
  {
    "auths": {
        "docker.example.com": {
          "identitytoken": "xyz="
        }
    }
  }
  ```
script to create config.json
```sh
acr_name=my_acr
docker_config_file=~/.docker/config.json
# retrieve token
token_value=$(az acr login --name $acr_name --expose-token --output tsv --query accessToken)
# create a sample file if not exists
if [ ! -f $docker_config_file ]; then
    echo '{}' > $docker_config_file
fi
# save the token in required docker config file format
jq -n --arg token $token_value '{"auths":{"'$acr_name'.azurecr.io":{"identitytoken":$token}}}' > tmp && mv tmp $docker_config_file
```
