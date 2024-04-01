# Loop

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

## for_each with condition
https://spacelift.io/blog/terraform-conditionals
```tf
resource "azuread_group_member" "main" {
  for_each = { for key, val in data.azuread_user.main :
  	key => val if val.user_type == "Member" }

  group_object_id  = azuread_group.main.id
  member_object_id = data.azuread_user.main[each.key].id
}
```
