# .bashrc

## `.bashrc` vs `.bashenv`
Both `.bashrc` and `.bashenv` are configuration files used with the Bash shell, but they have distinct purposes in terms of when they are read.

### `.bashrc` - Interactive Non-Login Shells
- Executed whenever you start a new interactive shell that is **not** a login shell. 
- Interactive shells are those you typically use when working on your terminal.
- Login shells occur when you first log in to a system through SSH or the physical console.
- Commonly used for:
    - Aliases: Shortcuts for frequently used commands
    - Functions: Reusable blocks of commands
    - PS1 customization: Defining how your bash prompt looks
    - History settings: Controlling how Bash remembers past commands

### `.bashenv` (Less Common)
- Not as widely used as `.bashrc`.
- Executed whenever an interactive shell is started, regardless of login or non-login status. 
- Typically used for:
    - Environment variables: Settings that affect how programs behave (e.g., PATH for finding executables)
