# Issue

## markdown files in root folder
mkdocs does not allow markdown files in root folder.

solution:
- use `symlink`
- create a new folder
- link all root files and folders to that new folder
- this new folder should also be under git source control

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
