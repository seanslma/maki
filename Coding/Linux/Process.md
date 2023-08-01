# Process

https://netflixtechblog.com/debugging-a-fuse-deadlock-in-the-linux-kernel-c75cd7989b6d

## ps
`ps` stands for `process status` and is a command used to view information about currently running processes on a Unix-based operating system. 
It allows you to see a list of processes along with their associated details, such as process IDs (PIDs), CPU and memory usage, execution status, parent process IDs (PPIDs), and more.

```sh
ps
ps aux    #user friendly format
ps awwfux #show the process tree
```
## show process stack
```sh
cat /proc/<pid>/stack
```

## list process threads (pids)
```sh
ls /proc/<pid>/task
```
