# Issue

## dockerfile in subdirectory
Solution: 
- use `context: .` so docker knows where to start
- for azure, use `buildContext: .`

https://stackoverflow.com/questions/47785706/docker-using-copy-when-the-dockerfile-is-located-in-a-subdirectory
