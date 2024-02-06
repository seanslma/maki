# Loop

## count
A common issue with `count` is that once you delete any resource other than the last one, 
Terraform will try to force replace all resources that the index doesn't match.

Usually only used for enable/disable a resource.
```tf
variable "add_storage_account" {
  description = "boolean to determine whether to create a storage account or not"
  type        = bool
}

resource "azurerm_storage_account" "main" {
  count = var.add_storage_account ? 1 : 0

  resource_group_name      = "rg-st"
  location                 = "eastus"
  account_tier             = "Standard"
  account_replication_type = "LRS"

  name = "stspacelift${count.index}${local.rand_suffix}"
}
```

## for_each
`for_each` isn't sensitive to changes in the order of resources.
```tf
variable "bucket_names" {
  type    = list(string)
  default = ["bucket-1", "bucket-2"]
}

resource "aws_s3_bucket" "main" {
  for_each = toset(var.bucket_names)

  bucket = each.value
  acl    = "private"
  
  tags = {
    Name = each.value
  }
}
```

Use both key anf value
```tf
variable "bucket_info" {
  type = map(object({
    acl = string
  }))
  default = {
    "bucket-1" = {
      acl = "private"
    },
    "bucket-2" = {
      acl = "public-read"
    }
  }
}

resource "aws_s3_bucket" "main" {
  for_each = var.bucket_info

  bucket = each.key
  acl    = each.value.acl
}
```

Limitations:
- the keys in for_each map block must have a known value.
  - can't be generated on the fly by functions (like bcrypt or timestamp)
  - can't refer to resource-specific attributes that are provided by a cloud provider, like a cloud resource ID
- we can't use sensitive values as arguments for for_each.
- basically, when using for_each, you need to directly specify the values.
