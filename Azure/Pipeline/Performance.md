# Performance

## Only rebuild changed porjects
https://timdeschryver.dev/blog/how-to-make-your-azure-devops-ci-cd-pipeline-faster?#the-end-result

The solution to a faster CI/CD pipeline is to only build and deploy the projects that are affected in the last commit.
The most important thing is to determine what projects are modified within the last commit and to assign these modified projects to an environment variable.
