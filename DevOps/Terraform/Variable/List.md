# List

## list vs map
https://sokolovtech.com/terraform/94-lists-vs-maps-in-terraform-variables

## List of objects
```tf
variable "shops" {
  type = list(object({
    name      = string
    address   = optional(string)
  }))
  default = []
}

shops = [
  {
    name      = "flowers",
    address   = "Asia",
  }, {
    name      = "animals",
    address   = "Africa",
  },
]

optional_shops {
  dynamic "my_shop" {
    for_each = var.shops[*]
    iterator = shop
    content {
      name      = shop.value.name
      address   = shop.value.address
    }
  }
}
```
