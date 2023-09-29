# Issue

## dockerfile in subdirectory
Solution:
- use `context: .` so docker knows where to start
- for azure devops pipeline, use `buildContext: .`
- for docker build, use `-f` pointing to the dockerfile

https://stackoverflow.com/questions/47785706/docker-using-copy-when-the-dockerfile-is-located-in-a-subdirectory
