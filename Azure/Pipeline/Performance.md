# Performance

## Only rebuild changed porjects
https://timdeschryver.dev/blog/how-to-make-your-azure-devops-ci-cd-pipeline-faster?#the-end-result

The solution to a faster CI/CD pipeline is to only build and deploy the projects that are affected in the last commit.
The most important thing is to determine what projects are modified within the last commit and to assign these modified projects to an environment variable.

## Dependency Caching in Python CI pipeline
https://stackoverflow.com/questions/69542082/dependency-caching-in-python-ci-pipeline-in-azure-devops

https://medium.com/@andre.gensler/guide-how-to-speed-up-your-python-continuous-integration-pipeline-in-azure-devops-using-dependency-916d9cd792a0

To also cache the installation rather just the wheels, we need to use virtual env and cache the entire environment.
