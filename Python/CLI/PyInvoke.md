# PyInvoke

https://docs.pyinvoke.org/en/stable
```
from invoke import task
@task
def build(c):
    print("Building!")
```
in shell run 
```
invoke build
```

https://github.com/pyinvoke/invoke

a Python library for managing shell-oriented subprocesses and organizing executable Python code into CLI-invokable tasks. 

Invoke is a Python library used for automating and managing tasks. 
It provides a way to define and execute tasks, similar to build tools like Make, Ant, or Gradle, 
but it's specifically designed for Python projects and is often used in conjunction with other build and automation tools.

Here are some key features and use cases of Invoke:
- **Task Automation**: Invoke allows you to define and execute tasks in Python scripts. These tasks can be used to automate common development and deployment processes.
- **Command-Line Interface (CLI)**: It provides a command-line interface for running tasks, making it easy to integrate into your development workflow.
- **Configuration**: You can configure tasks using Python code, making it flexible and easy to adapt to your project's needs.
- **Dependency Management**: Tasks can have dependencies, so you can ensure that certain tasks run before others. This is useful for building complex automation workflows.
- **Parallel Execution**: Invoke supports parallel execution of tasks, which can significantly speed up the execution of tasks when appropriate.
- **Integration**: It can be used alongside other Python libraries and tools, such as virtual environments, testing frameworks, and more.
