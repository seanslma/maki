# Click

## return value using click
https://stackoverflow.com/questions/26246824/how-do-i-return-a-value-when-click-option-is-used-to-pass-a-command-line-argume

Use `standalone_mode=False`:
```
print(main(standalone_mode=False))
```

## Multiple Values from Environment Values
https://click.palletsprojects.com/en/7.x/options/

- The default implementation for all types is to split on `whitespace`
- The exceptions to this rule are the `File` and `Path` types: Unix systems `colon` (:), and Windows `semicolon` (;)

## functions
- `click.add_command` Registers another `class:Command` with this group
- `click.make_pass_decorator` Given an object type this creates a decorator with innermost context of type
- `click.argument` Attaches an argument to the command
- `click.option` Attaches an option to the command

## click.ParamType
Represents the type of a parameter.
Validates and converts values from the command line or Python into the correct type.

## subcommands
organize the commands as subcommands within the task group, providing a more modular and structured CLI application.

main.py
```py
import click
from task import task

@click.group()
def cli():
    """A simple todo application."""
    pass

# Add the 'task' subcommand group to the main CLI
cli.add_command(task)

if __name__ == '__main__':
    cli()
```

task.py
```py
import click
from functools import partial

# Add some parameters to click.option
click.option = partial(click.option, show_default=True)

@click.group()
def task():
    """Manage tasks."""
    pass

@task.command()
@click.argument('task')
def add(task):
    """Add a new task."""
    click.echo(f'Added task: {task}')

@task.command('list')
@click.option('--show/--no-show', default=True)
def list_tasks(show: bool):
    """List all tasks."""
    click.echo("List of tasks:")
    if show:
        click.echo('Number of tasks: ')
```

Here
- We create a subcommand group task using `@click.group()` in the `task.py` file.
- Inside the `task.py` file, we use `@task.command()` to define subcommands within the task group for add and list_tasks.
- In the `main.py` file, we add the task subcommand group to the main CLI using `cli.add_command(task)`.

Now, you can use the task subcommand group with its subcommands:
```
python main.py task add "Buy groceries"
python main.py task list --show=False
```
