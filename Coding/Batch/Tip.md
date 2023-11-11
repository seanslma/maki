# tip

## escape char
^(^), ^<^>

## variables in if/for block
Environment variables in batch files are expanded when a line is parsed. The whole blocks delimited by parentheses (such as if) counts as a "line" or command. So the variables defined in the if/for block are replaces by their values before the block is run.

To solve this we should enable delayed expansion:  *setlocal enabledelayedexpansion* and use !your_variable!
