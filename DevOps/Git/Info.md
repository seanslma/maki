# Info

## `git describe --long --always --dirty`
Provide detailed information about the current Git commit, including its tag, commit hash, and distance from the latest tag.
Indicates whether the working directory is dirty (i.e., has uncommitted changes).
- `--long`: Includes the commit hash, distance from the nearest tag, and the tag name in the output.
- `--always`: Ensures that a description is always provided, even if there are no tags in the repository.
- `--dirty`: Appends a -dirty suffix to the output if there are uncommitted changes in the working directory.

Output: `<tag_name>-<distance_from_tag>-g<commit_hash>`
- example: `v1.2.3-3-gabcdef1234567890-dirty`
- `<tag_name>`: The name of the nearest tag.
- `<distance_from_tag>`: The number of commits between the current commit and the nearest tag.
- `g<commit_hash>`: The commit hash of the current commit.
- `-dirty`: Appended if there are uncommitted changes.

## `git rev-parse HEAD`
Return the commit hash of the current branch head: `abcdef1234567890`.

## `git remote`
Display a list of all configured remote repositories: `origin`, `upstream`.

## `git ls-remote --get-url origin`
Retrieve the URL associated with the remote repository named `origin`.
