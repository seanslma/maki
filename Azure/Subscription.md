# Subscription

## change subscription
If resource-group could not be found, change default subscription
```
az login
az account list --output table #list all subscriptions
az account set --subscription <subscription-id> #set default subscription
```
