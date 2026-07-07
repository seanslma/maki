# Jekyll

## run locally
```sh
bundle exec jekyll serve
```

## include folder in site but exclude from jekyll processing
- https://talk.jekyllrb.com/t/include-all-files-in-a-specific-directory-even-if-the-filenames-start-with-underscores/5849/6


Solution:
- `include` does not work
- `exclude_files` does not work
- in workflows, add a step to copy the source folder to the `_site`
- if that folder is one of your repo, disable github pages in that repo. Otherwise the repo github page will overwrite your `user.github.io/repo_name` page
- also ensure that `.gitignore` not exclude any required folders, such as underscore folders
