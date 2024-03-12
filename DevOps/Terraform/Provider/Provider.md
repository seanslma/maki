# Provider

https://developer.hashicorp.com/terraform/language/modules/develop/providers

Provider configurations can be defined only in a root Terraform module.

Providers can be passed down to descendent modules in two ways:
- either implicitly through inheritance, or
- explicitly via the providers argument within a module block.

A module intended to be called by one or more other modules must not contain any provider blocks.

## passing Providers Explicitly
When
- child modules each need a different configuration of a particular provider, or
- where the child module requires a different provider configuration than its parent,
you can use the providers argument within a module block to explicitly define which provider configurations are available to the child module.

Those with the alias argument set are never inherited automatically by child modules, and so must always be passed explicitly using the providers map.

## determine what version of a provider a resource was created with
https://www.reddit.com/r/Terraform/comments/17ujw6f/how_can_i_determine_what_version_of_a_provider_a/

if get error `Resource instance managed by newer provider version` we need to figure out the version of the provider used to create the resource.
- from state file we can only get the `schema_version` linked to that resource
- then we need to find which version of the provider uses the `schema_version`
