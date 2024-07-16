# String

## default
```terraform
variable "string_value" {
  type    = string
  default = null
}

var.string_value == null ? 0 : 1
```
