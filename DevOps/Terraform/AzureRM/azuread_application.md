# azuread_application

Manages an application registration within Azure Active Directory.
https://registry.terraform.io/providers/hashicorp/azuread/latest/docs/resources/application

Lightweighted version:
https://registry.terraform.io/providers/hashicorp/azuread/latest/docs/resources/application_registration

## azuread_application_password
https://discuss.hashicorp.com/t/azuread-application-password-rotation/35141

https://registry.terraform.io/providers/hashicorp/azuread/latest/docs/resources/application_password.html

password rotation (create a second secret with a different rotation period to avoid interruption)
```tf
resource "time_rotating" "password_rotate" {
  rotation_days = 60
}

resource "azuread_application_password" "password" {
  application_object_id = azuread_application.application.object_id
  end_date_relative     = "2400h"
  rotate_when_changed = {
    rotation = time_rotating.password_rotate.id
  }
}
```
