# State

## backend
Used to store the states remotely
- manage conflicts between team members by locking
- keep the states from accessing by other people

## manually update remote state
This is required when properties have been changed between versions

https://stackoverflow.com/questions/63427604/how-do-you-fix-terraform-unsupported-attribute-ses-smtp-password-after-upgradi
```
terraform state pull > state.json
#edit state.json and increment the serial attribute (ex "serial": 10, -> "serial": 11,)
terraform state push state.json
# run terraform plan
rm state.json #delete it
```
