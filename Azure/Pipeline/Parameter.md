# Azure Pipeline Parameters

## Purpose
Parameters are used to define values that are passed to the pipeline at runtime. They are typically used to make your pipelines more flexible and reusable by allowing you to pass in different values when triggering the pipeline.

## Types
1. **Pipeline Parameters**: Passed when the pipeline is manually triggered or via an API call.
2. **Template Parameters**: Used in pipeline templates to allow customization when templates are referenced.

## Scope
- **Pipeline-Level**: Accessible throughout the pipeline, including all jobs and steps.
- **Template-Level**: Scoped to the specific template where they are defined.

## Syntax
- **YAML**: `${{ parameters.parameterName }}`
- **Usage in Templates**: Can define default values and types for parameters.

## Example

```yaml
parameters:
  env: 'dev'

jobs:
- job: Deploy
  steps:
  - script: |
      echo Deploying to ${{ parameters.env }}
    displayName: 'Deploy to Environment'
    condition: eq('${{ parameters.env }}', 'prd')
```

## Key Characteristics
- Must be defined at the beginning of the YAML pipeline or template.
- Values are provided when the pipeline is triggered.
- Can be used to parameterize templates, making them reusable with different inputs.
- Values are typically static during the pipeline run but can be used to control the flow and behavior of the pipeline based on the input.

## Summary

**Variables**:
- **Usage**: Store and manage values that can be used across steps and jobs. Can be dynamic and changed during runtime.
- **Scope**: Pipeline, job, or step level.
- **Syntax**: `$(variableName)` in YAML and `$VARIABLE_NAME` in scripts.

**Parameters**:
- **Usage**: Pass values into the pipeline or templates at runtime. Make pipelines and templates flexible and reusable.
- **Scope**: Pipeline or template level.
- **Syntax**: `${{ parameters.parameterName }}` in YAML.
