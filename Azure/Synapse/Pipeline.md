# Pipeline

## paralell limitation
we do need to specify the max parallel run number.
Cannot run all jobs in real paralell mode - need to limit the number of jobs and there is the timeout limit in the automation pipeline.

## parameter and variable
https://learn.microsoft.com/en-us/azure/data-factory/concepts-parameters-variables

parameters
- defined for the whole pipeline 
- constant during a pipeline run
- can read them during a pipeline run but unable to modify them
- access parameter value: `@pipeline().parameters.<parameter-name>`

variables
- can be set at the start of a pipeline, 
- read and modified during a pipeline run through a Set Variable activity
- not thread safe, e.g. accessed from within a parallel iteration activity
- access variable value: `@variables('<variable-name>')`

## activity user property
https://www.techtalkcorner.com/monitor-azure-data-factory-user-properties/
- Easily monitor pipelines, complements perfectly with Azure Data Factory annotations  
- Find errors faster so you can solve them 
- Enhance the governance of pipelines and datasets 

## execute pipeline
https://learn.microsoft.com/en-us/azure/data-factory/control-flow-execute-pipeline-activity

## execution and triggers
https://learn.microsoft.com/en-us/azure/data-factory/concepts-pipeline-execution-triggers

## ForLoop call different pipelines
https://www.purplefrogsystems.com/2022/04/how-to-parameterise-the-execute-pipeline-activity-in-azure-synapse-analytics/

Call different pipelines with different parameters
