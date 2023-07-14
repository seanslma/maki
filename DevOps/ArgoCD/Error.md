# Error

## rpc error: code = Unknown desc = authentication required
- add the user/pass for the helm chart repo to argocd
- or the user/pass(token) ia not correct

## argocd repositories connection status failed
https://levelup.gitconnected.com/connect-argocd-to-your-private-github-repository-493b1483c01e

## could not read Username for 'https://github.com': No such device or address
There are two ways to check out code from Github:
- with user name/password,
- authenticate with an SSH key

In argocd, the credentials template still use `https` not `git@` but the credentials are provided via a pair of ssh keys.

when change the url to `git@` the error became `authentication required`. Maybe the ssh key is not correct???
