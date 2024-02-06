# Dynamic blocks
https://developer.hashicorp.com/terraform/language/expressions/dynamic-blocks

## conditional dynamic blocks
https://stackoverflow.com/questions/66152036/terraform-conditional-argument-block
```tf
resource "azurerm_automation_schedule" "example" {
  name                    = var.aaname
  resource_group_name     = azurerm_resource_group.example.name
  automation_account_name = azurerm_automation_account.example.name

  dynamic "monthly_occurrence" {
    for_each = var.frequency == "Month" ? [1] : []
    content {
       day = monthly_occurrence.value.day
       occurrence = monthly_occurrence.value.occurrence
    }
  }
}
```
