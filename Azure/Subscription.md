# Subscription

## change subscription
If resource-group could not be found, change default subscription
```
az login
az account list --output table #list all subscriptions
az account set --subscription <subscription-id> #set default subscription
```

## Role assignment with VS Pro Subscription


## Associate subscription to another directory
https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-how-subscriptions-associated-directory

## Transfer subscription to another directory
https://docs.microsoft.com/en-us/azure/role-based-access-control/transfer-subscription
