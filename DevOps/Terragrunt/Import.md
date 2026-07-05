# Import

## Group member deleted then added in portal
In this case, need to import that member to the tf state:
- run init and plan on the top level
- cd into the actual terraform folder (not the top level)
- `terragrunt import "module.[module_name]-[group_name].azuread_group_member.members[\"member_object_id\"]" group_object_id/member/member_object_id`
