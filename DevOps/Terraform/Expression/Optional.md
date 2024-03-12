# Optional

## skip a property by setting its value to `null`
https://developer.hashicorp.com/terraform/language/expressions/types#null

a value that represents absence or omission. If you set an argument of a resource to null, Terraform behaves as though you had completely omitted it 

```tf
account_tier = var.env == "prod" ? var.account_tier : null
```
