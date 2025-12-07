# Setting

## mkdocs.yml
https://mkdocs.readthedocs.io/en/0.10/user-guide/configuration/

## mkdocs-material settings
https://squidfunk.github.io/mkdocs-material/customization/

https://squidfunk.github.io/mkdocs-material/setup/setting-up-navigation/#navigation-tabs
```yaml
- header.autohide        #hide header after scrolling a few lines
- navigation.tabs        #top level sections as tabs after the header
- navigation.tabs.sticky #navigation tabs will remain visible when scrolling down
- navigation.indexes     #attach documents to sections
- navigation.tracking    #url address automatically updated
- search.highlight       #all saerch occurance will be highlighted
- search.suggest         #search suggestions
```

## md files n root folder
solution: use `symlink`
```sh
mkdir _docs
ln -s ../README.md _docs/index.md
ln -s ../AI _docs/AI
ln -s ../AWS _docs/AWS
ln -s ../Azure _docs/Azure
ln -s ../Coding _docs/Coding
ln -s ../Cybersecurity _docs/Cybersecurity
ln -s ../Data _docs/Data
ln -s ../DevOps _docs/DevOps
ln -s ../Documentation _docs/Documentation
ln -s ../Energy _docs/Energy
ln -s ../Learn _docs/Learn
ln -s ../ML _docs/ML
ln -s ../Optimization _docs/Optimizaton
ln -s ../PowerBI _docs/PowerBI
ln -s ../Python _docs/Python
ln -s ../SQL _docs/SQL
ln -s ../System _docs/System
```
