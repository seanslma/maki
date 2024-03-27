# azuread_application

Manages an application registration within Azure Active Directory.
https://registry.terraform.io/providers/hashicorp/azuread/latest/docs/resources/application

Lightweighted version:
https://registry.terraform.io/providers/hashicorp/azuread/latest/docs/resources/application_registration

```tf
data "azuread_client_config" "main" {}

# https://registry.terraform.io/providers/hashicorp/azuread/latest/docs/resources/application
resource "azuread_application" "main" {
  display_name     = var.display_name
  identifier_uris  = ["api://example-app"]
  logo_image       = filebase64("/path/to/logo.png")
  
  sign_in_audience = "AzureADMultipleOrgs"
  
  owners = [
    data.azuread_client_config.main.object_id,
    data.azuread_service_principal.main.id,
    data.azuread_user.tst.id,    
  ]

  api {
    mapped_claims_enabled          = true
    requested_access_token_version = 2

    known_client_applications = [
      azuread_application.known1.application_id,
      azuread_application.known2.application_id,
    ]

    oauth2_permission_scope {
      admin_consent_description  = "Allow the application '${var.display_name}' to act on behalf of the signed-in user."
      admin_consent_display_name = "Allow impersonation"
      enabled                    = true
      id                         = random_uuid.main.result
      type                       = "User"
      user_consent_description   = "Allow the application '${var.display_name}' to act on your behalf."
      user_consent_display_name  = "Pass-through credentials"
      value                      = "user_impersonation"
    }
  }
  
  web {
    homepage_url  = "https://app.example.net"
    logout_url    = "https://app.example.net/logout"
    redirect_uris = ["https://app.example.net/account"]

    implicit_grant {
      access_token_issuance_enabled = true
      id_token_issuance_enabled     = true
    }
  }  

  # resource_access_scopes = {
    # "ms_graph" = [
      # "email", "profile", "user.read",
    # ]
    # "azure_key_vault" = ["user_impersonate"]    
    # "azure_storage"   = ["user_impersonate"]
    # "azure_data_lake" = ["user_impersonate"]
    # "oss_database"    = ["user_impersonate"]
    # "sql_database"    = ["user_impersonate"]
  # }
  dynamic "required_resource_access" {
    for_each = var.resource_access_scopes
    iterator = permissions
    content {
      resource_app_id = lookup(local.resource_ids, permissions.key)
      dynamic "resource_access" {
        for_each = permissions.value
        content {
          type = "Scope"
          id   = lookup(
            lookup(local.permissions, permissions.key),
            resource_access.value
          )
        }
      }
    }
  }

  # variable "id_token_claims" {
    # type = list(object({
      # name      = string
      # essential = bool
      # source    = optional(string)
      # additional_properties = optional(list(string))
    # }))
    # default = []
  # }
  optional_claims {
    dynamic "id_token" {
      for_each = var.id_token_claims[*]
      iterator = claim
      content {
        name                  = claim.value.name
        essential             = claim.value.essential
        source                = claim.value.source
        additional_properties = claim.value.additional_properties
      }
    }
  }
}
```

## azuread_application_password
https://discuss.hashicorp.com/t/azuread-application-password-rotation/35141

https://registry.terraform.io/providers/hashicorp/azuread/latest/docs/resources/application_password.html

password rotation (create a second secret with a different rotation period to avoid interruption)
```tf
resource "time_rotating" "password_rotate" {
  rotation_days = 60
}

resource "azuread_application_password" "main" {
  application_object_id = azuread_application.application.object_id
  end_date_relative     = "2400h"
  rotate_when_changed = {
    rotation = time_rotating.password_rotate.id
  }
}
```

## service principal
```tf
# https://registry.terraform.io/providers/hashicorp/azuread/latest/docs/resources/service_principal
resource "azuread_service_principal" "main" {
    application_id               = module.main.client_id
    app_role_assignment_required = false
    owners                       = module.main.owners
    tags                         = ["apiConsumer", "webApp"]
}
```
